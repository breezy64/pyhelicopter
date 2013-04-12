#    CMPUT 297/115 - Helicopter Game - blocks.py - Due 2013-04-12
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
    
import agentsim
import random


class Block():
    _instances = {}

    # taken from zombiegame assignment, self explanatory
    @classmethod
    def get_all_instances(cls):
        return [v for v in Block._instances.values() if isinstance(v, cls)]
    # taken from zombiegame assignment, self explanatory
    @classmethod
    def del_instance_with_id(cls, id):
        if id in Block._instances:
            del(Block._instances[id])
    # based on del_instance_with_id 
    @classmethod
    def get_instance_with_id(cls, id):
        if id in Obstacle._instances:
            return (Obstacle._instances[id])

	# taken from zombiegame assignment, self explanatory
    @classmethod
    def del_instance(cls, obj):
        cls.del_instance_with_id(obj.get_id())

    def __init__(self,width=25):
        self.canvas=agentsim.gui.get_canvas()
        self._id=self.canvas.create_rectangle(10,20,30,40,tags="block")
        Block._instances[self._id] = self

    def move_by(self,dx=100):
       	"""
         move_by moves block across the canvas, and then deletes it when
         it is off the screen
        """
        self._x = self._x - dx
        self.canvas.move(self._id,-1*dx,0)
        xr=self._x+self._width
        if xr<0:
            self.canvas.delete(self._id)
            self.del_instance_with_id(self._id)

    def get_id(self):
        return self._id

class Ceil(Block):
    """
    Ceil class creates recatngles (of random height) that move along the bottom of screen
    
    Constructor:
    
    Ceil(x, width = 100, min_height = 45, max_height = 60)
    
    x: starting x position of floor block
    width: width of floor block
    min_height, max_height: constraints for the height of block 
    """      
    def __init__(self,x,width=100,min_height=45,max_height=60):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        # randomly generated height of floor block         
        self._height = random.randint(min_height,max_height)
        self._width=width
        self._x=x
        self._y=y_min
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,tags="ceiling",fill="blue",outline="")
        Ceil._instances[self._id] = self

class Floor(Block):
    """
    Floor class creates recatngles (of random height) that move along the bottom of screen
    
    Constructor:
    
    Floor(x, width = 100, min_height = 45, max_height = 60)
    
    x: starting x position of floor block
    width: width of floor block
    min_height, max_height: constraints for the height of block 
    """    
    def __init__(self, x, width = 100, min_height = 45, max_height = 60):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        # randomly generated height of floor block         
        self._height = random.randint(min_height,max_height)
        self._width=width
        self._x=x
        # y position of block        
        self._y=y_max-self._height
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,tags="floor",fill="blue",outline="")
        Floor._instances[self._id] = self

class Obstacle(Block):
    """
    Obstacle class creates a thin long rectangle that moves across the screen. It is drawn at
    a relatively random y coordinate

    Constructor:
    
    Obstacle(width=25,height=100)
    
    width: width of obstacle
    height: height of obstacle     
    """    
    def __init__(self,width=25,height=100):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        # adjust y_min, y_max to accomdate the ceiling and floor objects        
        (y_min,y_max) = (y_min+60,y_max-160)
        # obstacle block has random generated y position without having to,
        # collide with the floor and the ceiling
        self._y = random.randint(y_min,y_max)
        self._x = x_max
        self._width=width
        self._height=height
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,fill="red",tags="obstacle",)
        Obstacle._instances[self._id] = self

class Timer():
    """
    Timer is a loop counter    
    """    
    def __init__(self):
        self.timer = 0

    def inc(self):        
        self.timer+=1
    def get_time(self):
        # return counter for use
        return self.timer

class Score():
    """
    The Score class is used for the scoring system in helicopter_game
    
    Constructor:
    
    Score(xpos,ypos,canvas=None)
    
    xpos,ypos: x and postion of high score text on the canvas
    canvas: the canvas object on which the score is displayed     
    """
    def __init__(self,xpos,ypos,canvas=None):
        self.t = 0
        self.x = xpos # displays in x position
        self.y = ypos # displays in y position

    def inc(self,inc=100):
        # main counter for score
        self.t = self.t + inc
        # print("Highscore:",self.t)
        return self.t
    
    def add_canvas(self,canvas):
        # calls canvas for use in class
        self.canvas = agentsim.gui.get_canvas()

    def getcanvas(self):
        # retrieve canvas from class
        return self.canvas

    def drawtime(self):
        # draw the time in the canvas in given coordinates
        self.score = self.canvas.create_text(self.x,self.y,text=str(self.t),fill='white')
                                         
    def hide(self):
        # this method is used to draw and redraw on the canvas without,
        # drawing over the displayed score
        self.coords = self.canvas.coords(self.score)
        self.canvas.move(self.score,-1000,-1000)

    def dispscore(self):
        # this display the final score during end game
        self.canvas.create_text(650,20,text='Your Score:',fill='white')
        self.endscore = self.canvas.create_text(725,20,text=str(self.t),fill='white')
