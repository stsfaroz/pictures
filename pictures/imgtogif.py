import os
from PIL import Image
import re
import glob
from pathlib import Path

from IPython.display import Image as show_gif


class ImageFormat(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
class ImagePath(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
class PathError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
        


def convert(path="./",file_name="imgtogif.gif",to="./",img_format="all",duration=400,loop=0,number_sort="n",string_sort="n", gif_width = 510 ,gif_height=310 ):
    owd = os.getcwd()
    """
    convert (path="./",file_name="imgtogif.gif",to="./",
    img_format="all",duration=400,loop=0,
    number_sort="n",string_sort="n",
    gif_width=510,gif_height=310 )

    Parameters:

    path:
    Path to the source of the image files
    file_name:
    File name for the gif to be saved 
    to:
    Destination of the gif file
    img_format:
    In which format of images are need to be converted to gif
    Formats are : png , jpg , jpeg or all
    duration:
    Duration of the gif
    loop:
    0 for gif to play again and again
    1 for play 1 time
    number_sort:
    [Sorting image files numerically]
    Example:
    images=[2.png,34.png,1.png]
    if number sort is yes means:
    this will be sorted as [1.png,2.png,34.png]
    and gif will be created
    string_sort:
    [sorting image files alphabetically]
    Example:
    images=[c.png,b.png,a.png]
    if string sort is yes means:
    this will be sorted as [a.png,b.png,c.png]
    and gif will be created
    gif_width:
    width of the gif
    gif_height:
    Height of the gif

    """
    imgfiles = []
    
    path=r'%s' % path
    path = Path(path)
    retval = os.getcwd()


  
    to= r'%s' % to
    dest = Path(to)
    

    try:
        if os.path.exists(path):
            pass
        else:
            raise PathError("Source Path does not Exist","PathError")
        
        if os.path.exists(dest):
            pass
        else:
            raise PathError("Destination Path does not Exist","PathError")
        

        os.chdir(path)
        if img_format=="png":
            for file in glob.glob("*.png"):
                imgfiles.append(file)
        elif img_format=="jpg":
            for file in glob.glob("*.jpg"):
                imgfiles.append(file)
        elif img_format=="jpeg":
            for file in glob.glob("*.jpeg"):
                imgfiles.append(file)
        elif img_format=="all" or img_format=="All":
            for file in glob.glob("*.png"):
                imgfiles.append(file)
            for file in glob.glob("*.jpg"):
                imgfiles.append(file)
            for file in glob.glob("*.jpeg"):
                imgfiles.append(file)
        else:
            raise ImageFormat("Image format is not correct","ImageError")


        filelist=[]    
        files=[]
        if str(path)==".":
            for i in imgfiles:
                files.append(i)
            
        else:
            for i in imgfiles:
                files.append(i.replace(str(path),""))
    

        if number_sort=="y" or number_sort=="yes":
            try:
                files= sorted(files,key=lambda x: int(os.path.splitext(x)[0]))
            except:
                raise ImageFormat("Image name has Alphabet - Number sort ","ImageNameError")
        elif string_sort=="y" or string_sort=="yes" :
            files.sort()
        else:
            pass
        


        new_im=[]
        for file in files:
            new_frame = Image.open(file)
            img = new_frame.resize((gif_width, gif_height), Image.ANTIALIAS)
            new_im.append(img)
            
        if new_im==[]:
            raise ImagePath("No images in the path","ImageError")
        else:
            pass

        os.chdir(to)
        
        new_im[0].save(file_name, format='GIF',append_images=new_im[:],save_all=True,duration=duration, loop=loop)
    finally:
        os.chdir(owd)
