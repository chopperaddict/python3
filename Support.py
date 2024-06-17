
import functools
import re
import os
import sys
import getopts
import getopt
from tkinter import *
import tkinter as TK
from tkinter import ttk
from screeninfo import get_monitors
from tkinter import messagebox
import tkinter.font
import json # just to experiment
import random
import time

# FILE CONTAINING ONLY SUPPORTING METHODS

######################
## DUNDER FUNCTIONS ##
######################
def upperfunc(arg):
    return arg.upper()

def uppercase_decorator(function):
    #@gettime
    def wrapper(arg1):
        func = function
        return arg1.upper()
    return wrapper

def toupper(arg):
    return arg

def gettime(function):
    def wrapper(arg1):
        start=time.time()
        print("executing gettime()Dunder method")
        print(f'Starting at {start}')
        func = function(arg1)
        print("Comnpleted gettime()Dunder method")
        ending=time.time()
        print(f'Ending at {ending }, duration = {ending - start}')

    return wrapper


class ObjectCreationTime(object):
    def __init__(self, objName):
            self._created = time.time()
            self._objName = objName

    def __lt__(self, other):
        print('Creation Time:\n'
                  '% s:% f\n % s:% f' % (self._objName, self._created,
                                         other._objName, other._created))
        return self._created < other._created

    def __gt__(self, other):
        print('Creation Time:\n'
                  '% s:% f\n % s:% f' % (self._objName, self._created,
                                         other._objName, other._created))
        return self._created > other._created

#############################################
########## AUTO FRAME CREATION ##############
#############################################
def RunFramesApp1(window):
    frames = []
    s = ttk.Style()
    s.configure('TFrame', background='#B5B1AF', foreground='white', borderwidth=2, relief='raised', font='SegoeUI, 15')

    #dummy padding frame that encloses ALL otgher controls
    frame0 = ttk.Frame(window, style='TFrame', height=160)
    frame0.grid(row=0, column=0,padx=0, pady=0 )
    frames.append(frame0)

    # Constructing the first INNER frame, frame1
    frame1 = LabelFrame(frame0, text="Apples-SALE", bg="green", fg="white", font='segoeUI,14', padx=1, pady=3, relief=SUNKEN, borderwidth=3)
    frame1.grid(row=0, column=0, padx=5, pady=3)
    frames.append(frame1)
    appletext = StringVar()
    appletext.set('Juicy apples for sale')
    b1 = Button(frame1, textvariable=appletext, width=20, pady=10, font='segoeUI,14', command=lambda: showapplemsg(appletext, tomtext, infotext, b1))
    b1.grid(padx=15, pady=15)

    frame2 = LabelFrame(frame0, text="RIPE Red Tom's", bg="red",  font='segoeUI, 14', foreground='white', padx=15, pady=15, relief=RAISED, borderwidth=3)
    frame2.grid(row=0, column=1, padx=12, pady=25, )  # pad adds space around OUTSIDE of frame, NOT the inside (pad it's content to do this)
    frames.append(frame2)

    tomtext= StringVar()    #setup tkinter variables so we can update these labels
    tomtext .set('Succulent Tomatoes here ...')    #initialise varfiables value (can be done anywhere)
    tombground = StringVar()
    tombground.set('lightgreen')
    b2 = ttk.Button(frame2, textvariable=tomtext, width=30,  \
                command=lambda:showtomatomsg(appletext, tomtext, infotext, b2))
    b2.grid(row=0, column=2, padx=50, pady=0, sticky='w')   # pad adds space around button so the frame container gets larger, NOT the button itself
    #dummy padding frame at right side of window
    frame3 = Frame(frame0, padx=15, pady=15, relief=FLAT, borderwidth=1)
    frame3.grid(row=0, column=2, padx=20, pady=20)
    frames.append(frame3)

    #Row 1 frame at bottom of window
    frameb = Frame(frame0, padx=5, pady=5, width=200, relief=SUNKEN, borderwidth=3)
    frameb.grid(row=1, column=0,  columnspan=3, padx=0, pady=0, sticky='we')
    frames.append(frameb)

    infotext = StringVar()    #setup tkinter variables so we can update these labels
    infotext.set('Watch this space...')    #initialise variables value (can be done anywhere)
    labelb = Label(frameb, textvariable=infotext, width=60, background='green', foreground='white', font='segoeUI,14')
    labelb.grid(row=1, column=0, columnspan=4, sticky='we')

    window.columnconfigure(0, weight=0, minsize=150)
    window.columnconfigure(1, weight=8, minsize=150)
    window.columnconfigure(2, weight=8, minsize=75)
    window.columnconfigure(3, weight=0, minsize=25)
    print(frame0.children)

def showapplemsg(appletext,tomtext, infotext, bg):
    appletext.set("BUY SOME NOW !!")
    infotext.set("Get your Apples before they all go .....")
    tomtext.set('Succulent Tomatoes here...')
    bg.background='orange'

# method to handle updating the tomato label
# also reset the apple button to original prompt
def showtomatomsg(appletext,tomtext, infotext, bg):
    infotext.set("These tomatoes are amazing, get yours NOW !")
    tomtext.set("How many do you want?")
    appletext.set('Juicy apples for sale')
    bg.update()

########## END OF AUTO FRAME CREATION SUPPORT ##############

def show_values(btn, outlabel, btntext, msg):
    out=""
    if outlabel.get() != "":
        outlabel.set(msg)
        return

    if outlabel== None: return -9

    #if btn.text == 'show':
    if msg == None: msg=""
    try:
        if msg=="":
            print("show_values() error-NO TEXT VALUE received")
            return -3
        else:
            outlabel.set(msg)
            print (f"DEBUG : Show_values() updated {outlabel} with : {outlabel}")

    except Exception as inst:
        print(f'Error encountered in Show_Values(): {inst.args}')

    #   print (msg=msg, ctrl1=ctrl1.get(), ctgrl2=ctrl2.get())

def get_random_color():
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    return bg_colour

def LButton():
    print(f'Left button hit @ ') #{event.x}:{event.y} ...')
    #outputlabel.set

if __name__ == "__main__":
    print('in "if __'
          'name__ == __main__()')
    args = sys.argv[1:]
