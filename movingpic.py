class mPicture():
    """
    The mPicture class cycles through a group of images in an attempt to create an animation
    """
    def __init__(self,counter=0,images=None):
        self.images=images
        self.length=None
        self._counter=counter
    def add_images(self,images):
        self.images=images
        self.length=len(images)
    def update_image(self):
        photo=self.images[self._counter]
        if self._counter%(self.length-1)==0 and self._counter!=0:
            self._counter=0
        else:
            self._counter+=1
        return photo