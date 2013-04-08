import agentsim
class Helicopter:
    def __init__(self,x_coord,y_coord,width,height,photo=None,canvas=None):
        self.canvas=canvas
        self.x_coord=x_coord
        self.y_coord=y_coord
        self.width=width
        self.height=height
        self.id=None
        self.photo=photo
        self.button_press=0
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
    def create_helicopter(self,canvas,photo):
        self.photo=photo
        self.canvas=canvas
        self._draw()
    def play(self,dy=50):
        if self.button_press:
            dy-=2*dy
        self.canvas.move(self.id,0,dy)
        self.y_coord+=dy
    def _draw(self):
        x=self.x_coord
        y=self.y_coord
        try:
            self.id=self.canvas.create_image(x,y,image=self.photo)
        except:
            print("No canvas.")
