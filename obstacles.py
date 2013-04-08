import agentsim
import random

class Obstacle():
    _instances = {}

    @classmethod
    def get_all_instances(cls):
        return [v for v in obstacle._instances.values() if isinstance(v, cls)]

    @classmethod
    def del_instance_with_id(cls, id):
        if id in obstacle._instances:
            obstacle._instances[id].hide()
            del(obstacle._instances[id])

    @classmethod
    def del_instance(cls, obj):
        cls.del_instance_with_id(obj.get_id())

    def __init__(self,width=25):
        self.canvas=agentsim.gui.get_canvas
        (xmin, ymin, xmax, ymax) = agentsim.gui.get_canvas_coords()
        self._y = random.randint(ymin,ymax)
        self._x = xmax
        self._width=width
        self._height=random.randint(50,80)
        self._id=self.canvas.create_rectangle(xmax,self._y,xmax+self.width,self._y+self_height,tags="obstacle")
        obstacle._instaces[self._id] = self

    def move_by(self,dx=100):
        self._x = self._x - dx
        self.canvas.move(self._id,dx,0)

    def get_id(self):
        return self._id

class ceil(Obstacle):

    def __init__(self):
        (xmin, ymin, xmax, ymax) = agentsim.gui.get_canvas_coords()
        self._y = random.randint(ymin+20,(ymax/2)-50)
        self._x = xmax
        self._id = ceil._nextId
        ceil._nextId += 1
        ceil._instaces[self._id] = self

    def move_by(self):
        self._x = self._x - 50

    def get_id(self):
        return self._id

    def drawceil(self,x_min,y_min,x_max,y_max):
        agentsim.gui.get_canvas().create_rectangle(x_min,y_min,x_max,y_max, fill='blue')

class floor():
    _nextId = 1
    _instances = {}

    @classmethod
    def get_all_instances(cls):
        return [v for v in obstacle._instances.values() if isinstance(v, cls)]

    @classmethod
    def del_instance_with_id(cls, id):
        if id in floor._instances:
            floor._instances[id].hide()
            del(floor._instances[id])

    @classmethod
    def del_instance(cls, obj):
        cls.del_instance_with_id(obj.get_id())

    def __init__(self):
        (xmin, ymin, xmax, ymax) = agentsim.gui.get_canvas_coords()
        self._y = random.randint(ymin+325,ymax-20)
        self._x = xmax
        self._id = floor._nextId
        floor._nextId += 1
        floor._instances[self._id] = self

    def move_by(self):
        self._x = self._x - 50

    def get_id(self):
        return self._id

    def drawfloor(x_min,y_min,x_max,y_max):
        agentsim.gui.get_canvas().create_rectangle(x_min,y_min,x_max,y_max, fill='blue')
