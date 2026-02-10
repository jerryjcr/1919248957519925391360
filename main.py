import tkinter as tk
from PIL import ImageTk, Image
from fractions import *

#window setup
root=tk.Tk(className="The Master Work")
root.geometry("1280x720")
root.resizable(False,False)

#image setup
bgphoto=Image.open("masterwork.png")
bg=ImageTk.PhotoImage(bgphoto.resize((960,720)))
canvas1 = tk.Canvas( root, width = 1280,height = 720)
canvas1.create_rectangle(960,0,1280,720,fill="black")
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#global variables
curr_zoom_level=5
zooms={5:(960,720), 4:(1120,840), 3:(1280,960), 2:(1440,1080), 1:(1600,1200), 0:(2400,1800)}
curr_zoom_corner=[0,0]



#helper functions
def get_zoom_in_x_padding(x):
    res=round(x-Fraction( zooms[curr_zoom_level][0],zooms[curr_zoom_level+1][0] )*(x-curr_zoom_corner[0]))
    if res>0:
        return 0
    if res+zooms[curr_zoom_level][0]<960:
        return 960
    return res
def get_zoom_in_y_padding(y):
    res=round(y-Fraction( zooms[curr_zoom_level][1],zooms[curr_zoom_level+1][1] )*(y-curr_zoom_corner[1]))
    if res>0:
        return 0
    if res+zooms[curr_zoom_level][1]<720:
        return 720
    return res

def get_zoom_out_x_padding(x):
    res=round(x-Fraction( zooms[curr_zoom_level][0],zooms[curr_zoom_level-1][0] )*(x-curr_zoom_corner[0]))
    if res>0:
        return 0
    if res+zooms[curr_zoom_level][0]<960:
        return 960
    return res

def get_zoom_out_y_padding(y):
    res=round(y-Fraction( zooms[curr_zoom_level][1],zooms[curr_zoom_level-1][1] )*(y-curr_zoom_corner[1]))
    if res>0:
        return 0
    if res+zooms[curr_zoom_level][1]<720:
        return 720
    return res



#event methods
def draw_side_bar():
    canvas1.create_rectangle(960,0,1280,720,fill="black")

def zoom(e):
    global new_bg,curr_zoom_level,curr_zoom_corner
    if (e.delta==1) and curr_zoom_level>0:
        curr_zoom_level-=1
        new_bg=ImageTk.PhotoImage(bgphoto.resize(zooms[curr_zoom_level]))

        canvas1.create_image(get_zoom_in_x_padding(e.x), get_zoom_in_y_padding(e.y), image = new_bg, anchor = "nw")
        curr_zoom_corner= [get_zoom_in_x_padding(e.x), get_zoom_in_y_padding(e.y)]

    elif (e.delta==-1) and curr_zoom_level<5:
        curr_zoom_level+=1
        new_bg=ImageTk.PhotoImage(bgphoto.resize(zooms[curr_zoom_level]))
        canvas1.create_image(get_zoom_out_x_padding(e.x), get_zoom_out_y_padding(e.y), image = new_bg, anchor = "nw")
        curr_zoom_corner= [get_zoom_out_x_padding(e.x), get_zoom_out_y_padding(e.y)]
    draw_side_bar()


#event bindings
canvas1.bind('<MouseWheel>', zoom)


#main loop
canvas1.place(x=0,y=0)
root.mainloop()