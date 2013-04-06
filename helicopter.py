
class Helicopter:
    def __init__(self,x_coord,y_coord,width,height,canvas=None,id=None):
        self.canvas=canvas
        self.x_coord=x_coord
        self.y_coord=y_coord
        self.width=width
        self.height=height
        self.id=id
        self.button_press=0
        if self.canvas is not None:
            self.canvas.create_rectangle(x_coord,y_coord,x_coord+width,y_coord+height,fill="red")
    def button_pressed(self):
        self.button_press=1
    def button_released(self):
        self.button_press=0
    def set_x_coord(self,x_coord):
        self.x_coord=x_coord
    def set_y_coord(self,y_coord):
        self.y_coord=y_coord
    def get_x_coord(self):
        return self.x_coord
    def get_y_coord(self):
        return self.y_coord
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def create_helicopter(self,canvas):
        self.canvas=canvas
        self._draw()
    def play(self,dx=0,dy=20):
        if self.button_press:
            dy-=2*dy
        self.canvas.move(self.id,dx,dy)
        self.y_coord+=dy
    def _draw(self):
        x=self.x_coord
        y=self.y_coord
        width=self.width
        height=self.height
        try:
            self.id=self.canvas.create_rectangle(x-(width/2),y-(height/2),x+(width/2),y+(height/2),fill="red")
        except:
            print("No canvas.")
