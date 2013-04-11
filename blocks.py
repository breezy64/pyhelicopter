import agentsim
import random

class Block():
    _instances = {}

    @classmethod
    def get_all_instances(cls):
        return [v for v in Block._instances.values() if isinstance(v, cls)]

    @classmethod
    def del_instance_with_id(cls, id):
        if id in Block._instances:
            del(Block._instances[id])
    @classmethod
    def get_instance_with_id(cls, id):
        if id in Obstacle._instances:
            return (Obstacle._instances[id])


    @classmethod
    def del_instance(cls, obj):
        cls.del_instance_with_id(obj.get_id())

    def __init__(self,width=25):
        self.canvas=agentsim.gui.get_canvas()
        self._id=self.canvas.create_rectangle(10,20,30,40,tags="block")
        Block._instances[self._id] = self

    def move_by(self,dx=100):
        self._x = self._x - dx
        self.canvas.move(self._id,-1*dx,0)
        xr=self._x+self._width
        if xr<0:
            self.canvas.delete(self._id)
            self.del_instance_with_id(self._id)

    def get_id(self):
        return self._id

class Ceil(Block):
    def __init__(self,x,width=100,min_height=45,max_height=60):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        self._height = random.randint(min_height,max_height)
        self._width=width
        self._x=x
        self._y=y_min
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,tags="ceiling",fill="blue",outline="")
        Ceil._instances[self._id] = self

class Floor(Block):
    def __init__(self, x, width = 100, min_height = 45, max_height = 60):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        self._height = random.randint(min_height,max_height)
        self._width=width
        self._x=x
        self._y=y_max-self._height
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,tags="floor",fill="blue",outline="")
        Floor._instances[self._id] = self

class Obstacle(Block):
    def __init__(self,width=25,height=100):
        self.canvas=agentsim.gui.get_canvas()
        (x_min, y_min, x_max, y_max) = agentsim.gui.get_canvas_coords()
        (y_min,y_max) = (y_min+60,y_max-160)
        self._y = random.randint(y_min,y_max)
        self._x = x_max
        self._width=width
        self._height=height
        self._id=self.canvas.create_rectangle(self._x,self._y,self._x+self._width,self._y+self._height,fill="red",tags="obstacle",)
        Obstacle._instances[self._id] = self

class Timer():
    def __init__(self):
        self.timer = 0

    def inc(self):        
        self.timer+=1
    def get_time(self):
        return self.timer

class Score():
    def __init__(self,xpos,ypos,canvas=None):
        self.t = 0
        self.x = xpos
        self.y = ypos

    def inc(self,inc=100):
        self.t = self.t + inc
        #print("Highscore:",self.t)
        return self.t
    
    def add_canvas(self,canvas):
        self.canvas = agentsim.gui.get_canvas()

    def getcanvas(self):
        return self.canvas

    def drawtime(self):
        self.score = self.canvas.create_text(self.x,self.y,text=str(self.t),fill='white')
                                         
    def hide(self):
        self.coords = self.canvas.coords(self.score)
        self.canvas.move(self.score,-1000,-1000)

    def dispscore(self):
        self.canvas.create_text(650,20,text='Your Score:',fill='white')
        self.endscore = self.canvas.create_text(725,20,text=str(self.t),fill='white')
