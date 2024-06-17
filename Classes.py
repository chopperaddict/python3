#from tkinter import *
from Support import *
import tkinter as tk
from tkinter import ttk
#from tkinter import class
#import ttkbootstrap as ttk
import os
import sys
from functools import wraps

class debugwindow():
    #parent = parent
    #global count
    #count = 0

    def Update(self, arg):
        self.label1.text = str(arg)
        #self.label1.update()
        #count = 0

    def __init__(self,parent):
        self.count = 0
        self.label = Label()
        self.parent = parent
        self.dbgwin = self.createnew(parent)

    def createnew(self,parent):
        self.dbgwin = PanedWindow(parent, bd=5, sashpad=5, showhandle=True,
                           height=100, bg='#DAB700',
                           width=int(150), orient=VERTICAL,
                           sashrelief=RAISED, sashwidth=2, handlesize=2, handlepad=1,
                           relief=SUNKEN, borderwidth=1)
        self.count += 1
        return self.dbgwin

    def getCount(self):
        return self.count

    def getLabelText(self):
        return self.Label.text

class Frame_Class(tk.Frame):
    def __init__(self,parent, args):
        tk.Frame.__init__(self, parent,
                          background=args[0],
                          relief=args[1],
                          borderwidth=args[2],
                          width=args[3],
                          height=args[4])

'''
        VERTICAL,      #orientation= horizontal/vertical
        SUNKEN,        # relief
        70,             #length if horizontal, else height
        sliderwidth,     #width of slider ctrl ITSELF (WHERE THE THUMB CTRL IS)
        2,             # border - overall depth of the relief selected
        slide1value,       # variable name
        0,             #range From
        10000,         # range To
        'segoeUI, 10', # font
        'black',       # fg
        'lightgrey',   # bg
        'purple',      # btn activebackground
        '#88aa00',     # troughcolor
        True,          # showvalue   at side of control
       '',       # label
        100,              # tick interval
        20,
        100)

'''
class slider(object):
    def __init__(self,
                 parent):
        w1 = Scale(parent)

class sliders(Scale):
    def __init__(self,
                 parent,
                 orient,
                 sliderrelief,
                 length,
                 width,
                 bd,
                 variable,
                 from_,
                 to,
                 font,
                 fg,
                 bg,
                 activebackground,
                 troughcolor,
                 showvalue,
                 label,
                 tickinterval,
                 sliderlength,
                 posx,
                 posy):

        w1 = Scale(parent)

        w1.configure(orient = orient,
            sliderrelief=sliderrelief,
            length = length,
            width= width,
            bd = bd,
            variable =variable,
            from_= from_,
            to = to,
            font = font,
            fg = fg,
            bg = bg,
            activebackground = activebackground,
            #highlightcolor = highlightcolor,
            troughcolor = troughcolor,
            showvalue = showvalue,
            label = label,
            tickinterval = tickinterval,
            sliderlength = sliderlength)


        w1.place(x = posx, y=posy)



if __name__ == "__main__":
    print('in "if __name__ == __main__')
    args = sys.argv[1:]
    print(args)
