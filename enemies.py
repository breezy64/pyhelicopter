#    CMPUT 297/115 - Helicopter Game - enemies.py - Due 2013-04-12
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


#most basic enemy class includes class methods for getting and deleting instances of enemy
class Enemy():
      """
      Enemy class includes Rockets, Missiles, and Lasers
      
      Rocket:
      most basic class, takes in helicopters y coordinate to spawn infront of helicopter on right side of screen
      move class only moves object left then delets when object is off screen
      
      Missile: Missiles are a little bit more complex then rockets, spawns at random y coordinate and on the right side of the screen
      move class moves it left constantly and up or down depending on location of helicopter then deletes it when missile if off screen
      
      Laser: Laser spawns middle y coordinate of whole screen and is as wide as the entire screen 
      move class moves laser up or down based on helicopters location and deletes function after certain number of calls
    
      """      
      _instances = {}
      # taken from zombiegame assignment, self explanatory 
      @classmethod
      def get_all_instances(cls):
            return [v for v in Enemy._instances.values() if isinstance(v, cls)]
      # based on del_instance_with_id
      @classmethod
      def get_instance_with_id(cls, id):
        if id in Enemy._instances:
            return (Enemy._instances[id])
      #from zombiegame assignment
      @classmethod
      def del_instance_with_id(cls, id):
            if id in Enemy._instances:
                  del(Enemy._instances[id])
      # taken from zombiegame, self explanatory 
      @classmethod
      def del_instance(cls, obj):
            cls.del_instance_with_id(obj.get_id())
      # simple init function, never actually used creates circle and id for instance
      def __init__(self):
            self._canvas=agentsim.gui.get_canvas()
            self._id=self.canvas.create_circle(10,20,30,40,tags="enemy")
            Enemy._instances[self._id] = self     
      def move_by(self,dx=25):
        """
         move_by moves enemy across the canvas, and then deletes it when
         it is off the screen
        """
        self._x = self._x - dx
        self._canvas.move(self._id,-1*dx,0)
        xr=self._x+self._width
        if xr<0:
            self._canvas.delete(self._id)
            self.del_instance_with_id(self._id)
            
      def get_id(self):
            return self._id
      
# rocket inherits from Enemy     
class Rocket(Enemy):
      """
      Rocket Class spawns rocket (moving circle) on the same y coordinate as helicopter
      
      Constructor:
      heli_y: The current y coordinate of helicopter
      height, width: The height and width bounding box that encloses the circle
      """
      def __init__(self,heli_y, width = 20,height = 20):
            self._canvas=agentsim.gui.get_canvas()
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
            self._x = x_max
            self._y = heli_y
            self._width=width
            self._height=height
            self._id=self._canvas.create_oval(self._x,self._y,self._x+self._width,self._y+self._height,fill="red",tags="rocket")
            Rocket._instances[self._id] = self
            
# missile inherits from Enemy
class Missile(Enemy):
      """
      The Missile class  creates a moving obstacle that is initialized off the screen and
      and at the current y coordinate of helicopter. The moving obstacle moves towards the obstacle
      in the y direction

      Constructor: 
    
      Missile(heli_y,size = 20)
	  
	  heli_y: The current y coordinate of the helicopter
      size: The size of the moving obstacle   
      """
      # init spawns missile at random y coordinate and on the right said of the screen
      def __init__(self,heli_y, size = 20):
            self._canvas=agentsim.gui.get_canvas()
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
            self._x = x_max
            self._y = heli_y
            self._size = size
            self._id=self._canvas.create_oval(self._x,self._y,self._x+self._size,self._y+self._size,fill = "green",tags="missile")
            Missile._instances[self._id] = self
        
      def move_by(self,heli_y,dx = 20,dy = 2):
            """
            move_by takes in helicopters y coordinate and moves toward it 
            vertically but moves left constantly
            """
            if heli_y > self._y:
                  dy = 2
            else:
                  dy = -2
            self._x = self._x - dx
            self._y = self._y + dy
            self._canvas.move(self._id,-1*dx,dy)
            
            xr=self._x+self._size
            if xr<0:
                  self._canvas.delete(self._id)
                  self.del_instance_with_id(self._id)
            
#laser inherits from Enemy 
class Laser(Enemy):
      """
      The Laser Class creates a laser (a thin rectangle that is as long as the canvas).
      The laser moves towards the helicopter in attempt to cause a collision
      """
      def __init__(self):
            self._canvas=agentsim.gui.get_canvas()
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
            self._x = x_min
            self._y = y_max//2
            self._height=5
            self._width=x_max-self._x
            self._id=self._canvas.create_rectangle(self._x,self._y,x_max,self._y+self._height,fill = "green",tags="laser",outline="")
            Rocket._instances[self._id] = self
            self.timer = 0
    
      def move_by(self, heli_y):
            """
            move_by moves laser up or down depending on whether helicopter is above or below
            deletes laser after certain number of moves
            """
            if heli_y > self._y:
                  dy = 2
            else:
                  dy = -2
            self._y = self._y + dy
            self._canvas.move(self._id,0,dy)
            self.timer += 1
            if self.timer > 30:
                  self._canvas.delete(self._id)
                  self.del_instance_with_id(self._id)
            
                  
                  
