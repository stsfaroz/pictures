# Pictures

![Play with images](https://github.com/stsfaroz/pictures/blob/master/pictures/img/pictures.png)


### To install
```
pip3 install pictures
```

## Image to Gif

### Dependencies

>  pillow

> Ipython

> pathlib

Example :
```
   >>from pictures import imgtogif
   >>imgtogif.convert(path="./",file_name="mine.gif")
 ```
#### Default parameters values:
```
convert (path="./",file_name="imgtogif.gif",to="./",
img_format="all",duration=400,loop=0,
number_sort="n",string_sort="n",
gif_width=510,gif_height=310 ) 
```
  ___  
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
        Height of the gif```

