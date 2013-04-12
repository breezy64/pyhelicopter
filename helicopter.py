import agentsim
class Helicopter:
    """
    Helicopter Class draws the helicopter to the screen and controls/monitors 
    the motion of the helicopter
    """
    def __init__(self,x_coord,y_coord,photo=None,canvas=None):
        self.canvas=canvas
        self.x_coord=x_coord
        self.y_coord=y_coord
        
        # Approximate height and width of helicopter
        self.width=139
        self.height=53
        # id is the canvas id. It only gets a value when helicopter is drawn onto the canvas
        self.id=None
        # Photo stores the current helicopter image 
        self.photo=photo
        self.button_press=0
        #self.box_id=None
    
    # button_pressed and button_released are used to tell
    # the class whether the left mouse button
    # is pressed or released
    def button_pressed(self):
        self.button_press=1
    def button_released(self):
        self.button_press=0
   
    def set_x_coord(self,x_coord):
        self.x_coord=x_coord
    def set_y_coord(self,y_coord):
        self.y_coord=y_coord
    
    # Accesors
    def get_x_coord(self):
        return self.x_coord
    def get_y_coord(self):
        return self.y_coord
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def create_helicopter(self,canvas,photo):
        """
        create_helicopter loads the canvas and image of the helicopter into
        the class and draws the helicopter to the screen
        """
        self.photo=photo
        self.canvas=canvas
        self._draw()
    def play(self,photo,dy=50):
        """
        The play function controls the motion of the helicopter
        and updates the image of the helicopter
        """
        self.photo=photo
        # If left mouse is pressed, go up
        if self.button_press:
            dy-=2*dy
        # erase and redraw the helicopter (so that displays the new helicopter image)
        self.canvas.delete(self.id)
        self.y_coord+=dy
        self._draw()
    def _draw(self):
        # Draw the helicopter
        x=self.x_coord
        y=self.y_coord
        try:
            self.id=self.canvas.create_image(x,y,image=self.photo)
        except:
            print("No canvas.")
