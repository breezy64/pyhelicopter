#enemies.py
import agentsim
import random

class Enemy():
      _instances = {}

      @classmethod
      def get_all_instances(cls):
            return [v for v in Enemy._instances.values() if isinstance(v, cls)]
      @classmethod
      def get_instance_with_id(cls, id):
        if id in Enemy._instances:
            return (Enemy._instances[id])
      @classmethod
      def del_instance_with_id(cls, id):
            if id in Enemy._instances:
                  del(Enemy._instances[id])
      @classmethod
      def del_instance(cls, obj):
            cls.del_instance_with_id(obj.get_id())
                        
      def __init__(self):
            self._canvas=agentsim.gui.get_canvas()
            self._id=self.canvas.create_circle(10,20,30,40,tags="enemy")
            Enemy._instances[self._id] = self
            
      def move_by(self,dx=35):
        self._x = self._x - dx
        self._canvas.move(self._id,-1*dx,0)
        xr=self._x+self._width
        if xr<0:
            self._canvas.delete(self._id)
            self.del_instance_with_id(self._id)
            
      def get_id(self):
            return self._id
      
class Rocket(Enemy):
      
      def __init__(self,heli_y, width = 20,height = 20):
            self._canvas=agentsim.gui.get_canvas()
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
            self._x = x_max
            self._y = heli_y
            self._width=width
            self._height=height
            self._id=self._canvas.create_oval(self._x,self._y,self._x+self._width,self._y+self._height,fill="red",tags="rocket")
            Rocket._instances[self._id] = self
            
class Missile(Enemy):
      def __init__(self,heli_y, size = 20):
            self._canvas=agentsim.gui.get_canvas()
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
            self._x = x_max
            self._y = heli_y
            self._size = size
            self._height=size
            self._width=size
            self._id=self._canvas.create_oval(self._x,self._y,self._x+self._size,self._y+self._size,fill = "green",tags="missile")
            Missile._instances[self._id] = self
            
      def move_by(self,heli_y,dx = 20,dy = 2):
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
            
      
class Laser(Enemy):
      def __init__(self):
            self._canvas=agentsim.gui.get_canvas()
            (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
            self._x = x_min
            self._y = y_max//2
            self._height=5
            self._width=x_max-self._x
            self._id=self._canvas.create_rectangle(self._x,self._y,x_max,self._y+self._height,fill = "green",tags="laser",outline="")
            Rocket._instances[self._id] = self
            
      def move_by(self, heli_y):
            if heli_y > self._y:
                  dy = 2
            else:
                  dy = -2
            self._y = self._y + dy
            self._canvas.move(self._id,0,dy)
            
                  
                  
