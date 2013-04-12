import agentsim
class Helicopter:
    def __init__(self,x_coord,y_coord,photo=None,canvas=None):
        self.canvas=canvas
        self.x_coord=x_coord
        self.y_coord=y_coord
        self.width=139
        self.height=53
        self.id=None
        self.photo=photo
        self.button_press=0
        #self.box_id=None
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
        #self.box_id=canvas.create_rectangle(self.x_coord-0.5*self.width,self.y_coord-0.5*self.height,self.x_coord+0.5*self.width,self.y_coord+0.5*self.height)
        self._draw()
    def play(self,photo,dy=50):
        self.photo=photo
        if self.button_press:
            dy-=2*dy
        #self.canvas.move(self.box_id,0,dy)
        self.canvas.delete(self.id)
        self.y_coord+=dy
        self._draw()
    def _draw(self):
        x=self.x_coord
        y=self.y_coord
        try:
            self.id=self.canvas.create_image(x,y,image=self.photo)
        except:
            print("No canvas.")
