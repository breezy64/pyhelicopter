#    CMPUT 297/115 - Helicopter Game - agentsim.py - Due 2013-04-12
#                                                                                  
#    Version 3.0 2013-04-13                                            
#                                                                      
#    By: Byron Maroney                                                 
#        Edrick de Guzman
#        Navjeet Dhaliwal                                              
#                                                                       
#                                                                      
#   This assignment has been done under the full collaboration model,  
#   and any extra resources are cited in the code below.

# agentsim.py is a stripped down version of agentsim.py
# from the zombiegame assignment    

"""
Simple Graphical User Interface module for 2D agent simulations

You can only have one of these active, because there is only one Tk instance
that is in charge of all the windows and event handling.

To setup the simulation framework do, once only:

    agentsim.init(init_fn=None, step_fn=None, title="Simulation")

    init_fn() - is a function that is called on simulation start that
        sets up the initial conditions for the simulation.  

    step_fn() - is a function that is called on each time step of the
        simulation.  

    title is the text displayed on the top of the window

The simulation does not begin until you invoke, once only,

     agentsim.start()

The simulation environment consists of a resizable graphics area on which
visualizations of the agents are drawn and manipulated, and some controls
to start, pause, run, or single-step the simulation, along with a rate 
slider that controls the spped of the simulation.

NOTE: typing a q key will cause the simulation to quit without confirmation!

The agents being simulated need access to the state of the simulation room
and maintained by the graphical user interface.  To access the gui singleton, 
you use this global property
    agentsim.gui

To get to the canvas in order to draw additional graphics use
        canvas = agentsim.gui.get_canvas()
which resturns the canvas object, so that, for example, you can 
add additional artifacts:

    agentsim.gui.get_canvas().create_oval(10, 20, 30, 40, fill='black')

To get the dimensions of the canvas use
    (x_size, y_size) = agentsim.gui.get_canvas_size():

To get the actual coordinate space of the canvas use
    (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords():

Two convenient clipping functions are provided to ensure that points
(x,y) will be clipped to be within the canvas coordinate space
        new_x = agentsim.gui.clip_x(x)
        new_y = agentsim.gui.clip_y(y)

To access the global debug flag, you use
    agentsim.debug
See the documentation for bitflag.  The framework debug flags are
    1 - agentsim related 
    2 - Person or subclass related
    4 - Shape or subclass related
    8 - reserved
   16 - (and above) user defined

BUG ALERT: It is not clear what happens when you resize the canvas during
a simulation.  The positions will eventually get clipped by a move_by, but
that may be after quite some time! 

"""

import random
from tkinter import *
#from bitflag import BitFlag


# Singleton GUI instance, only one allowed to be created, remember it for
# global access.
# These are module level variables, on the grounds that the module is the
# singleton instance, the GUI class is just something used to help implement
# the module.

gui = None
#debug = BitFlag()

class GUI():
    """

    Constructor:

    GUI(init_fn=None, step_fn=None, title="Simulation"):

    The GUI constructor  will raise an exception if you try to create 
    more than one instance.
    
    init_fn() - is a function that is called on simulation start that
        sets up the initial conditions for the simulation.  

    step_fn() - is a function that is called on each time step of the
        simulation.  

    title is the text displayed on the top of the window

    The simulation does not begin until you invoke agentsim.gui.start()

    To get to the canvas in order to draw additional graphics use
        canvas = agentsim.gui.get_canvas()
    which resturns the canvas object, so that, for example, you can 
    add additional artifacts:

    agentsim.gui.get_canvas().create_oval(10, 20, 30, 40, fill='black')

    To get the dimensions of the canvas use
        (x_size, y_size) = agentsim.gui.get_canvas_size():

    To get the actual coordinate space of the canvas use
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords():

    Two convenient clipping functions are provided to ensure that points
    (x,y) will be clipped to be within the canvas coordinate space
        new_x = agentsim.gui.clip_x(x)
        new_y = agentsim.gui.clip_y(y)

    """

    # there can only be one instance of this class
    num_instances = 0

    def __init__(self, init_fn=None, step_fn=None, stop_fn=None, title="Simulation"):
        if GUI.num_instances != 0:
            raise Exception("GUI: can only have one instance of a simulation")
        GUI.num_instances = 1

        self._canvas_x_size = 800
        self._canvas_y_size = 500

        # if canvas is resized, the corners will change
        self._canvas_x_min = 0
        self._canvas_y_min = 0
        self._canvas_x_max = self._canvas_x_size
        self._canvas_y_max = self._canvas_y_size

        # simulation function hooks
        self._init_fn = init_fn
        self._step_fn = step_fn
        self._stop_fn = stop_fn

        # simulation state
        self._running = 0

        self._title = title

        self._root = Tk()

        self._root.wm_title(title)
        self._root.wm_geometry("+100+80")
        self._root.bind("<Key-q>", self._do_shutdown)
        self._root.bind("<Button-3>", self._do_run)
        self._root.resizable(FALSE,FALSE)

        self._canvas = Canvas(
            width=self._canvas_x_size,
            height=self._canvas_y_size,
            scrollregion=(0, 0, self._canvas_x_size, self._canvas_y_size),
            highlightthickness=0,
            borderwidth=0,
            )

        self._canvas.grid(column=0, row=0, sticky='nwes')

    # public method to start the simulation
    def start(self):
        if self._init_fn != None: 
            self._init_fn()
        self._root.mainloop()

    # actions attached to buttons are prefixed with _do_
    def do_shutdown(self):
        self._do_shutdown(None)
    def _cancel_next_simulation(self):
        """ 
        remove next simulation events from the queue
        """

        data = self._root.tk.call('after', 'info')
        scripts = self._root.tk.splitlist(data)
        # In Tk 8.3, splitlist returns: (script, type)
        # In Tk 8.4, splitlist may return (script, type) or (script,)
        for id in scripts:
            self._root.after_cancel(id)
        return    
    def _do_pause(self):
        self._running = 0
        self._cancel_next_simulation()

    def _do_shutdown(self, ev):
        print("Game Over")
        quit()

    def _do_run(self,ev):
        if not self._running:
            self._speed = 120
            self._running = 1
            self._run()
    def _do_reset(self,ev):
        self._running = 0
        self._cancel_next_simulation()
        if self._init_fn != None:
            self._init_fn()

    # needs to be own function, not part of _do_run, 
    # because it reschedules itself
    def _run(self):
        if self._running:
            if self._step_fn != None:
                self._step_fn()
                # queue a new event to be executed after some time
                if self._speed > 0:
                    id = self._root.after(150 - self._speed, self._run)
                else:
                    id = self._root.after(1, self._run)

    def get_canvas(self):
        return self._canvas

    def get_canvas_size(self):
        return (self._canvas_x_size, self._canvas_y_size)

    def get_canvas_coords(self):
        return (self._canvas_x_min, self._canvas_y_min,
                self._canvas_x_max, self._canvas_y_max)

    def clip_x(self, x):
        return max(self._canvas_x_min, min(self._canvas_x_max, x))

    def clip_y(self, y):
        return max(self._canvas_y_min, min(self._canvas_y_max, y))

# Agent simulation main methods
def init(init_fn=None, step_fn=None, stop_fn=None, title="Simulation"):
    # let us modify the value of the global gui variable
    global gui
    gui = GUI(init_fn=init_fn, step_fn=step_fn, stop_fn=stop_fn, title=title)

def start():
    gui.start()

def stop():
    gui.stop()

#def rgb_to_color(r, g, b):
#    """
#    Utility to generate a Tk color rgb string from  integer r, g, b, 
#    where 0 <= r, g, b <= 1

#    Use as in
#        agentsim.gui.get_canvas().create_oval(10, 20, 30, 40, 
#            fill=agentsim.rgb_to_color(.8, .8, 0) )
#    """

#    return '#{0:02x}{1:02x}{2:02x}'.format(
#        int((r * 255) % 256), int((g * 255) % 256), int((b * 255) % 256), )

def main():
    """
    process the command line arguments
    """
    # instantiate the framework
    agentsim.init(title="Empty Canvas", init_fn=None, step_fn=None)

    agentsim.start()


if __name__ == "__main__":
    # if we don't have this conditional main body code, then pydoc3 gets
    # really cofused trying to partially run the code to extract out the
    # methods etc.

    # only bring in all the tk stuff when really running
    import agentsim

    # bind to the move enhanced class

    main()
