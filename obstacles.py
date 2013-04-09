import agentsim
import random

class Obstacle():
    _instances = {}

    @classmethod
    def get_all_instances(cls):
        return [v for v in Obstacle._instances.values() if isinstance(v, cls)]

    @classmethod
    def del_instance_with_id(cls, id):
        if id in Obstacle._instances:
            del(Obstacle._instances[id])

    @classmethod
    def del_instance(cls, obj):
        cls.del_instance_with_id(obj.get_id())

    def __init__(self,width=25):
        self.canvas=agentsim.gui.get_canvas
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        self._height=random.randint(50,80)
        self._y = random.randint(ymin,ymax-self._height)
        self._x = x_max
        self._width=width
        self._id=self.canvas.create_rectangle(x_max,self._y,x_max+self._width,self._y+self._height,tags="obstacle")
        obstacle._instaces[self._id] = self

    def move_by(self,dx=100):
        self._x = self._x - dx
        self.canvas.move(self._id,-1*dx,0)
        xr=self._x+self._width
        if xr<0:
            self.canvas.delete(self._id)
            self.del_instance_with_id(self._id)

    def get_id(self):
        return self._id

class ceil(Obstacle):
    def __init__(self,x,width=100,min_height=15,max_height=25):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        self._height = random.randint(min_height,max_height)
        self._width=width
        self._x=x
        self._y=y_min
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,tags="ceiling",fill="blue",outline="")
        ceil._instances[self._id] = self

class Floor(Obstacle):
    def __init__(self, x, width = 100, min_height = 15, max_height = 25):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        self._height = random.randint(min_height,max_height)
        self._width=width
        self._x=x
        self._y=y_max-self._height
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,tags="ceiling",fill="blue",outline="")
        ceil._instances[self._id] = self

   
  

    
