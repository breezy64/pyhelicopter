#    CMPUT 297/115 - Helicopter Game - movingpic.py - Due 2013-04-12
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

class mPicture():
    """
    The mPicture class cycles through a group of images in an attempt to create an animation/
    
    Constructor: 
    
    mPicture(counter,images=None)
    
    counter: The  starting index in the list of images 
    
    images: list of gif images to cycle through   
    """
    def __init__(self,counter=0,images=None):
        self.images=images
        self.length=None
        self._counter=counter
    def add_images(self,images):
        """
        add_images loads the list of images into mPicture object        
        """        
        self.images=images
        self.length=len(images)
    def update_image(self):
        """
        update_image returns the image at the current index and increments the counter        
        """        
        photo=self.images[self._counter]
        if self._counter%(self.length-1)==0 and self._counter!=0:
            self._counter=0
        else:
            self._counter+=1
        return photo
