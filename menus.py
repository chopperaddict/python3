import tkinter as tk
import json
import string
from Classes import *
from Classes import sliders
from Support import *
from PanedPanels2 import createPanedWindow, createContainerWindow
import winsound  # for sound
import time  # for sleep

#from fastapi import FastAPI
from tkinter.scrolledtext import ScrolledText

#Create an object of tkinter window or frame
import linecache
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from Classes import debugwindow
#from Classes import ObservableModel
#from menus import *
import mysql.connector
from PIL import Image, ImageDraw
from notebook import Notepad
#from Get_stock_data import *  #get_stock_data
from NewsFeed import GetArticle, fetch_and_print_articles
import requests
from bs4 import BeautifulSoup

###################################################################################

#import Image
'''
Test system that creates two menus, and then 
creates various 'bound' Fn's to handle mouse down/up etc
It demonstates the use of passing widget variables 
to bound Fn's to enhance output options
It uses a generic FN from Support.py named 
show_values(Feedbacklabel, msg, ctrl1, ctrl2) that is bound to a 
Button. This expects a lab el type widget for output, a msg string
that will be printer 1st, and then the names of up to two 
StringVar's that will optionally be printed as comma seperated value 
in the relevant widget + the copnsole 

It handles the parsing of all the arguments received
and outputs any/all received args data in the specified 'Label' Widget 
and also prints it to the console in a similar format
'''
###################################################################################
# Functions
###################################################################################

global textctrl

def getConfigureOpts():
    getscaleoptions(Canvas, "Canvas")
    getscaleoptions(Entry, "Entry")
    getscaleoptions(Frame, "Frame")
    getscaleoptions(Menu, "Menu")
    getscaleoptions(Listbox, "Listbox")
    getscaleoptions(Radiobutton, "Radiobutton")
    getscaleoptions(Checkbutton, "Checkbutton")
    getscaleoptions(Label, "Label")
    getscaleoptions(Scrollbar, "Scrollbar")
    getscaleoptions(Text, "Text")
    getscaleoptions(Toplevel, "Toplevel")
    getscaleoptions(Spinbox, "Spinbox")
    getscaleoptions(LabelFrame, "LabelFrame")
    getscaleoptions(PanedWindow, "PanedWindow")
    getscaleoptions(Message, "Message")
    getscaleoptions(Menubutton, "Menubutton")
    getscaleoptions(Scale, "Scale")
    getscaleoptions(Button, "Button")

def GetQuote():
    #pass
    ibmval = get_stock_data()
    statusoutput.set(f'Current Stock value: IBM: ${float(ibmval):5.2f}')

def showheadlines(parentctrl):
    ### news feed
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        S = f'{len(response.text):,}'
        parentctrl.insert(END, f'Data Length is : {S} bytes\n\n')
        tmp = response.text
        #print(response.text[0:5000])
        startpos = int()
        startpos = 0
        while True:
            if startpos == -1:
                break
            startpos = tmp.find('name="description" content=', startpos, len(response.text)) - startpos
            if startpos < 0:
                break
            endpos = tmp.find('"', startpos + 28, len(response.text) - startpos)
            str = tmp[startpos + 28:endpos]
            parentctrl.insert(END, f'{str}\n')
            startpos = endpos + 1
            tnp = tmp[startpos:]
    parentctrl.insert(END, f'\nEND OF BBC HEADLINES\n')

def cleartxt():
    textctrl.delete("1.0", END)

###################################################################################
## Use the API from NewsAPI to get data
###################################################################################
## returns ALL trhe configure options for the sdlider
def getscaleoptions(ctrl, name):
    buf = ''
    buff = ''
    print(f"\nAvailable parameters for {ctrl}")
    buf = f"\nAvailable parameters for {ctrl}\n"
    buff += buf
    opts = ctrl.configure(root)
    for opt in opts:
        buff += f"{opt}\n"
        print(opt)
    #pos = ctrl.search('>', '1.0', stopindex=END)
    fname = f"x:\\master documents\\my documents\\{name}_info.txt"
    f = open(fname, 'w')
    buffer = buff
    f.write(buffer)
    f.close()

def jprint(obj):
    ## dump data received - dumps() parses it out 1st
    data = json.dumps(obj, sort_keys=True, indent=4)

def addtxt(val):
    val = slide1value.get()
    textctrl.insert(END, f"\nSlider [1] set to [{val}]")

def NewFile():
    print("New File!")

def gotfocus():
    print(' got focus hit')

def OpenFile():
    name = askopenfilename()
    print(name)

def About():
    print("This is a simple example of a menu")

###################################################################################
## LOCAL FUNCTIONS ##
###################################################################################

def dowarnbeep():
    winsound.Beep(345, 180)
    winsound.Beep(190, 650)

def dosuccessbeep():
    return
    winsound.Beep(500, 150)
    #winsound.Beep(470, 100)
    #winsound.Beep(440, 200)
    winsound.Beep(450, 150)
    winsound.Beep(500, 150)
    winsound.Beep(385, 300)

# resets the slider value input field
# so we can ignore non numeric characters
def resetentry(val):
    try:
        if len(val) >= 1:
            valid = '0123456789'
            if len(self.char) < 1 or self.char.lower() in valid == False:
                return
            slide1val.set(val)
            varname.set(str(val))
    except:
        return

# Resets slider thumb value
def resetvalue(val):
    lbloutput.set("")
    try:
        slide1value.set(str(val))
        dosuccessbeep()
    except:
        print(f'Error setting "slide1value"')

global errortxt
global slide1val
global maxval

# function that is bound to a keypress (using bind())
# to reset the value of the slide1 SCALE control
def setoutputfield(self):
    valid = '0123456789'
    print(self.keycode)
    keyval = int(self.keycode)
    strval= str(slide1val.get())
    if keyval == 8: # backspace hit !!
        var1 = strval[0: len(strval)]
        slide1val.set("")
        slide1val.set(var1)
        errortxt.set(f"Error information\nSlider [1] set to [{var1}]")
        entry1.icursor(len(var1))
        entry1.focus()
        #entry1.mark.set('insert', '%d' % len(strval) - 1)   # reposition cursor to end of value
    elif keyval >= 48 and keyval <= 57:
        # its a valid numeric value
        var1 = str(slide1val.get())
        #kval = slideval.value()
        if int(var1) > maxval:

            var1 = var1[0: len(var1) - 1]
            slide1val.set("")
            slide1val.set(var1)
            errortxt.set(f"Error information\nKey ignored-value > \nMAX VALUE is {maxval}")
            entry1.icursor(len(str(slide1val)))
            entry1.focus()
            dowarnbeep()

        elif keyval >= 48 and keyval <= 57:
            if len(self.char) < 1:
                entry1.focus()
                dowarnbeep()
            print(f'key hit was {self.char}')
            val = self.char
            if len(val) > 0:
                fullval = int(slide1val.get())
                if fullval > maxval:
                    fullval = maxval
                    errortxt.set(f"Error information\nSlider [2] set to MAX VALUE")
                else:
                    errortxt.set(f"Error information\nSlider [2] set to [{fullval}]")
                    textctrl.insert(END, f"\nSlider [2] set to [{fullval}]")
                    resetvalue(str(fullval))
                entry1.focus()
            else:
                charvalid = 'abcdefghijklmnopqrstuvwxyz'
                newchar = self.char.lower()
                fullval = slide1val.get()
                fullval = fullval[0: len(fullval) - 1]
                #self.char=""
                slide1val.set("")
                slide1val.set(fullval)
                print(f"4eypress {self.char} - MUST be a numeric value !")
                kval = self.char.value()
                if kval != 8 : errortxt.set(f"Error information\nInvalid key [{self.char}] - NOT numeric !")
                # reposition caret at end of field
                entry1.icursor(len(fullval))
                if newchar in charvalid:
                    entry1.focus()
                    dowarnbeep()
                else:
                    # refresh the slider value as it has probably
                    # been modified by del/bspace keys
                   strval = str(slide1val.get())
                   if strval[: len(strval) - 1] in valid == True:
                        var1 = int(slide1val.get())
                        if var1 >= 0 and var1 <= maxval:
                            slide1val.set(str(var1))
                            entry1.icursor(len(str(slide1val)))
                            slide1value.set(int(var1))
                        else:
                            print('Grrrrr - Invalid keypress....')

                        #if kval != 8:
                        if len(strval) > 1:
                                badkey = strval[len(strval) - 1]
                                newstr = strval[0: len(strval) - 1]
                                slide1val.set(str(newstr))
                                entry1.icursor(len(str(slide1val)))
                                slide1value.set(int(newstr))
                                errortxt.set(f"Error information\nInvalid key [{badkey}] entered ....")
                                dowarnbeep()
                        else:
                            slide1val.set("")
                            if len(strval) > 1:
                                errortxt.set(f"Error information\nInvalid key[{strval[len(strval - 1):]}] entered ....")
                            else:
                                errortxt.set(f"Error information\nInvalid key[{strval}] entered ....")
                                dowarnbeep()
                entry1.focus()

    else:
        # invalid key entered
        fullval = slide1val.get()
        fullval = fullval[0: len(fullval) - 1]
        errortxt.set(f"Error information\nInvalid key[{strval[len(strval)-1:]}] entered ....")
        strval= str(fullval)
        slide1val.set("")
        slide1val.set(strval)
        entry1.icursor(len(strval))
        entry1.focus()
        dowarnbeep()

def getoutputfield(self):
    valid = '0123456789'
    val = self.char
    kval = self.char.value()
    if kval != 8 or val in valid:
        currvalue = str(slide1val.get())
        currvalue += val
        slide1val.set(currvalue)
    else:
        print(f"Invalid keypress {self.char} - MUST be a numeric value !")
        errortxt.set(f"Error information\nInvalid key [{self.char}] - NOT numeric !")
        self.char = ""
        return False

def resetzero():
    slide1value.set(0)

def resetmax():
    slide1value.set(maxval)

def resetmid():
    slide1value.set(abs(maxval / 2))

def createmenu(filemenu):
    #img = Image.open()
    new_file_img = PhotoImage(file="W:\\Ebay images\\HO Coaches\\stained coach roof.png")

    menubar = Menu(root, bg='#F6DAD1')
    filemenu = Menu(menubar, tearoff=False, activebackground='red', font='comicsans,12', fg='#005D00', bg='#F6DAD1')
    Menu.add_cascade(menubar,label="File", menu=filemenu, activebackground='red', font='comicsans,12')
    filemenu.add_command(label="New", command=NewFile, activebackground='red',
                         font='comicsans,12')  #', image=new_file_img, compound=tk_left)
    filemenu.add_command(label="Open...", command=OpenFile, activebackground='red', font='comicsans,12')
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit, activebackground='red', font='comicsans,12')

    editmenu = Menu(menu, tearoff=False, activebackground='red', font='comicsans,12', fg='#8F7E51', bg='#F6DAD1')
    menu.add_cascade(label="Edit", menu=editmenu)
    editmenu.add_command(label="Reset Slider1 > 0%", command=resetzero, activebackground='red', font='comicsans,12')
    editmenu.add_command(label="Reset Slider1 > 50%", command=resetmid, activebackground='red', font='comicsans,12')
    editmenu.add_command(label="Reset Slider1 > 100%", command=resetmax, activebackground='red', font='comicsans,12')

    helpmenu = Menu(menu, tearoff=False, activebackground='red', font='comicsans,12', fg='#2421D6', bg='#F6DAD1')
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About, activebackground='red', font='comicsans,12')

def showslide1key():
    intval = slide1.get()
    slider1output.set(f'Slider [2] set to [{intval}]')
    textctrl.insert(END, f"\nSlider [2] set to [{intval}]")

# show slider1 value in text field
def showkey(self):
    intval = slide2.get()
    slider2output.set(f'Slider [2] set to [{intval}]')
    txtctrl.insert(END, f"\nSlider [2] set to [{intval}]")

# show slider2 value in text field
def showslider1value():
    intval = slide1value.get()
    lbloutput.set(f'Slider2 value : [{intval}]')
    textctrl.insert(END, f"\nSlider [2] set to [{intval}]")

global app

#app=FastAPI()
#@app.get("/get-mssage")
#async def read_root():
#    return {"Message":"Congratulations Ian, this is your first API !"}

###################################################################################
## END - LOCAL FUNCTIONS ##
###################################################################################

###################################################################################
# window setup
###################################################################################
#def main():
global root
root = Tk()
tk = root
#fastapi = FastAPI()
#app =FastAPI()
#read_root()

#root = Tk()
#root.themename='darkly'
root.background = 'lightgrey'
menu = Menu(root)
root.config(menu=menu, bg='#C6FFE2',relief=RAISED)
root.title('Tk Test system')
appheight = IntVar()
appwidth = IntVar()
appmidpoint = IntVar()
appheight = 700
appwidth = 1000
appmidpoint = int((appwidth / 7) * 3) + 80
#appmidpoint = appwidth / 2

root.geometry(f'{appwidth}x{appheight}')
root.minsize(appwidth-300, appheight - 300)
@gettime
@uppercase_decorator
def sayhi(arg1):
    print(arg1)

print(sayhi("Hi there Ian, how's it hanging buddy\n...Not too shabby I guess ?"))
###############
# menu setup ##
###############
filemenu = Menu(menu)
createmenu(filemenu)

#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code)

###################################################################################
## create frames ##
## 1st frame ##
###################################################################################
frame1height = IntVar()
frame1width = IntVar()

###################################################################################
## setup LH frame 1 ##
###################################################################################
frame1width = int((appmidpoint)-170)
#frame1width = int((appmidpoint)-5)
frame1height = appheight - 660
args = (
    '#ff00dd',
    SUNKEN,
    1,
    frame1width,
    frame1height)

Frame1 = Frame_Class(root, args)
#Frame1.place(x=0, y=0, anchor='nw')

#Frame1.place(anchor='nw', x = 0, y = 0)
Frame1.place(anchor='nw', relheight = 0.94, x = 0, y = 0)

slide1val = StringVar()
maxval = IntVar()
maxval = 10000
entry1 = Entry(Frame1, width=4, textvariable=slide1val, background='red', fg='white', font='comicsans, 14')
entry1.place(x=130, y=90)

entrylabel = Label(Frame1, text="<<-Enter slider value", background='green',
                fg='white', font='segoeui, 14', width=18)
entrylabel.place(x=190, y=90)

##########################
## widgets in 1st frame ##
##########################
## Error message
# create a label to contain error messages
# for LH frame1
errortxt = StringVar()
errortxt.set('Error information')
errormsg = Label(Frame1, textvariable=errortxt, background='cyan', foreground='blue',
                font='comicsans, 14', width=23, height=4)
errormsg.place(x=135, y=140)
###################################################################################
## END = Frame 1 ##
###################################################################################
###################################################################################
## add widgets to LH frame 1 ##
###################################################################################
global lbloutput
lbloutput = StringVar()
lbloutput.set('Feedback ...')

btntext = StringVar()
btntext.set('Show')
btn1 = Button(Frame1, textvariable=btntext, font='FranklinGothic, 12', height=3,
            width=10, background='#6100E7', foreground='yellow',
            command=lambda: show_values(btn1, lbloutput,
                                        btntext, f"current value : {slide1value.get()}"))
btn1.place(x=10, y=100)

###################################################################################
## setup RH frame 2 ##
###################################################################################
frame2_xpos = frame1width + 5
frame2width = appwidth - int(frame1width-150)
frame2height = appheight - 365
args = (
    '#DAB700',
    RAISED,
    3,
    frame2width-160,
    frame2height)
f2height = frame2height
f2width = 0
#f2width = frame2width - 450
frame2 = Frame_Class(root, args)
frame2.place( anchor='nw', x=frame2_xpos, y=3,
            relwidth=0.8, relheight=0.95)
print(f'Frame2 W={f2width} x H={f2height}')
###################################################################################
## END = Frame 2 ##
###################################################################################

###################################################################################
## 3rd frame for close button etc at very bottom of screen ##
## WORKING JUST FINE 14 JUNE 24 ##
###################################################################################
frame3 = Frame(root, relief=RAISED, borderwidth=1, background='#C64CE2',  # purple
            name='frame 3', width=(appwidth), height=55)
frame3.place(relwidth = 1.0, x = 0, y = -55, rely=1.00)

###################################################################################
## END = Frame 3 ##
###################################################################################

## TEMP - call these for anny widget type to
# get a file written to MY DOCUMENTS
# listing ALL configure options
#getConfigureOpts()

########################################################################
#                       CREATE SLIDER 1 ##
# call class library - sliders() to get a ready to go slider control
# using the values in the args list above
# its current value is stored in StringVar of "slide1value"
#########################################################################
def createslider1(*args):
    slide1value = StringVar()  # value of the slider below
    global slider1width

    slider1width = int(args[0] )

    slide1 = Scale(Frame1,
            orient=VERTICAL,  #orientation= horizontal/vertical
            relief=SUNKEN,  # relief
            length=700,  #length if horizontal, else height
            width=slider1width,  #width of slider ctrl ITSELF (WHERE THE THUMB CTRL IS)
            bd=2,  # border - overall depth of the relief selected
            variable=slide1value,  # variable name
            from_=0,  #range From
            to=10000,  # range To
            font='segoeUI, 10',  # font
            highlightcolor='black',  # fg
            bg='lightgrey',  # bg
            activebackground='purple',  # btn activebackground
            troughcolor='#88aa00',  # troughcolor
            showvalue=True,  # showvalue   at side of control
            label='',  # label
            tickinterval=100,
            sliderlength=40)  # sliderlength

    slide1.place(x=5, y=10)
    slide1value.set('4500')
    return slide1
#########################################################################

########################################
#mb = #messagebox()
####################
## END# Slider 1 ###
##########################

###################################################################################
slider1width = IntVar()
#########################################################################
slide1 =createslider1(25)
#########################################################################

#########################################################################
# create another slider                      #
# (horizontal this time)in RH frame          #
#########################################################################
def createslider2(*args):
    slide2value = args[0]
    length = int(args[1])

    slide2 = Scale(frame2,
            orient=HORIZONTAL,
            relief=RAISED,
            #length=350+400,
            length=length,
            width=30,  #width of slider
            borderwidth=2,
            variable=slide2value,
            from_=0, to=200,
            font='FranklinGothic, 10',
            fg='black',
            bg='lightgrey',
            activebackground='red',
            troughcolor='cyan',
            showvalue=True,
            label='Volume ...',
            tickinterval=20,
            digits=4,
            sliderlength=20,
            cursor='arrow'
            #slider1width=20,
            )
    frame2length = (appwidth / 2) - 40
    #slide2.place(x=11, y=10)
    slide2.place(relwidth = 1.0, x = 5, y = 10, rely=0,anchor='nw')

    return slide2

slider2output = StringVar()
slider2output.set('Information')
slide2value = StringVar()
## Info Label
labelwidth = IntVar()
labelwidth = 32
#########################################################################
slide2 = createslider2(slide2value, frame2width-500)
#########################################################################

slider2value = Label(frame2, textvariable=slider2output, background='#7E2B2C',
                    foreground='white', font='ComicSans,12', width=labelwidth)
slider2value.place(x=11, y=130)

###################################################################################
## END Slider 2             ##
## END OF SLIDERS CREATION  ##
###################################################################################
## LH frame "RESET" button
btn2 = Button(Frame1, text='Reset', font='FranklinGothic, 12', height=1,
            width=6, background='lightgreen', command=lambda: resetvalue(0))
btn2.place(x=slider1width + 105, y=appheight - 115)

###################################################################################
## Get stock quote usaing API ##
###################################################################################
## bottom panel widgets

statusoutput = StringVar()
statusline = Label(frame3, textvariable=statusoutput, background='#6E1AD5',
                foreground='white', width=42, font="Helvetica 12")
statusline.place(x=10, y=18)
#font = tkFont.Font(family='Comic sans', size=13, weight='bold')
stkbtn = Button(frame3, text='Get Stock price', background='Purple', foreground='yellow',
                height=1, width=13, font='FranklinGothic, 12', command=GetQuote)
stkbtn.place(x=420, y=12)

## BOTTOM BUTTON
btn3 = Button(frame3, text='Close', background='red', foreground='yellow', width=8, font='FranklinGothic, 12',
            command=exit)
btn3.place(x=appwidth - 95, y=10)

###################################################################################
# General screen layout ##
###################################################################################
## left hand frame
Feedbacklabel = Label(Frame1, textvariable=lbloutput, background='yellow',
                    foreground='black', width=labelwidth, font='comicsans,12')
Feedbacklabel.place(x=135, y=12)

###################################################################################
# create a value entry field for setting LIVE the slide1 setting
# the slider will instantly update to the value in this field,
# or to low/Highest values as soon as each key is released
###################################################################################
'''
slide1val = StringVar()
maxval = IntVar()
maxval = 10000
entry1 = Entry(Frame1, width=4, textvariable=slide1val, background='red', fg='white', font='comicsans, 14')
entry1.place(x=135, y=90)

entrylabel = Label(Frame1, text="<<-Enter slider value", background='lightgrey', font='segoeui, 14', width=18)
entrylabel.place(x=190, y=90)
'''
innerwidth = ((appwidth / 2) - 10)
innerwidth = int(innerwidth)
innerheight = f2height

# top buttons panel
frame4width = frame2width -50
frame4height = f2height - 280

args1 = ('#958D94',  # darkish grey
        RAISED,
        1,
        int(frame4width - 15),  # width
        50)
#60)        #height

## RH frame top button row
frame40 = Frame_Class(frame2, args1)
#frame40.place(x=10, y=170)
frame40.place(width = frame2width, x = 10, y = 180,anchor='nw')#, relwidth=1.0,  x = 10, y = 170, anchor='nw')

print(f'Frame4 W={int(frame4width)} x H={frame4height}')
btn10 = Button(frame40, text='Clear', font='FranklinGothic, 12', height=1, width=12,
            background='green', fg='white', command=cleartxt)
btn10.place(x=405, y=10)

statusoutput.set('Loading data from BBC News Feed .....')
btn9 = Button(frame40, text='Get BBC News Headlines', font='FranklinGothic, 12', height=1, width=23,
            background='lightgreen', command=lambda: GetArticle(textctrl))
btn9.place(x=530, y=10)

statusoutput.set('')
###################################################################################
## END = Frame 4 ##
# ###################################################################################
## Create main PanedPanel and populate it ##
###################################################################################
pwheight = frame2height
pwwidth = frame2width
###############################################################################
# call Fn to create Paned windows to be
# parented inside others inb the design
## CREATE PANED WINDOWS INSIDE FRAME4                                        ##
###############################################################################
# create lists[] of heights and widths to pass to paned window creation function
maxcount = 1  # total paned windows to be created
frame4height += 45

## light cyan
pwwidth -= 195
panecontainerwin = createContainerWindow(frame2, pwwidth, pwheight-1200, 3, '#CDEFF0')
panecontainerwin.place(x=5, y = 240 ,relwidth=1.0, relheight=0.7)
## purple bg - TOP section of container frame
########################################################################
## NOW CRFEATE  3 PANEDWINDOW'S ** ALL GO INSIDE ** PANNECONTAINERWIN
########################################################################
## create the rows in the grid
if maxcount > 1:
    panedwin1 = createPanedWindow(panecontainerwin, pwwidth - 100, 0, 5, '#9540CD', maxcount)
    panedwin1.place(x=3, y=5, relwidth=0.5, relheight=0.5)
    textctrl1 = ScrolledText(panedwin1,
                        width=int(pwwidth - 15), bg='#F2EEDC',
                        font='comicsans,12',  #xscrollcommand = scrollbar.set(0,100),
                        height=int(pwheight*2),  #font='comicsans,12',

                        relief=FLAT, padx=5, pady=1, highlightthickness=3)

    textctrl1.place(x=2, y=0, relwidth=1.0, relheight=0.95)
    panedwin1.add(textctrl1)
#txtctrl2 = textctrl
## create the grid inside container window
#frame2.add(panedwin1)

#panedwin1.grid(row=0, column=0, sticky='NSEW')
#panecontainerwin.place(  relwidth = 1.0, relheight=0.7, x = 3, y = -(pwheight+45), rely=1.0,anchor='nw')
#p1frame = Frame(panedwin1, height=pwheight,  width = pwwidth)
#panedwin1.pack()
## paper white bg
if maxcount >=2 :
    panedwin2 = createPanedWindow(panecontainerwin, pwwidth - 100, int((pwheight / 3)) , 10, '#F2EEDC', maxcount)
    panedwin2.place(x=3, y=150, relwidth=1.0, relheight=0.95)
    textctrl2 = ScrolledText(panedwin2,
                        width=int(pwwidth - 15), bg='#F2EEDC',
                        font='comicsans,12',  #xscrollcommand = scrollbar.set(0,100),
                        height=int(pwheight*2),  #font='comicsans,12',
                        relief=FLAT, padx=5, pady=1, highlightthickness=3)

    textctrl2.place(x=2, y=0)
#txtctrl2 = textctrl
    panedwin2.add(textctrl2)
#panecontainerwin.add(panedwin2)
#panedwin2.grid(row=1, column=0, sticky='NSEW')
#panedwin2.pack()
## lightish grey bg
if maxcount >= 3:
    panedwin3 = createPanedWindow(panecontainerwin, pwwidth -100, int(pwheight / 3) , 15, '#7E8286', maxcount)
    panedwin3.place(x=3, y=int(pwheight / 3) * 2)
    #frame2.add(panedwin3)
    #panedwin3.grid(row=2, column=0, sticky='EW')
    #panedwin3.pack()


    #################################################################################################
    # create text control in pane TWO with scrollbar for bbc new feed data
    #lab1 = print(f"textctrl W={int(widths[0] - 30)} x H=20")

    # add scrollbar to top inner (purple) pane - WORKING 14 JUne 24
    pw1scroll3 = ScrolledText(panedwin1,
                        width=int(pwwidth - 15), bg='#9540CD', fg='white',
                        font='comicsans,12',  #xscrollcommand = scrollbar.set(0,100),
                        height=int(pwheight) / 2,  #font='comicsans,12',
                        relief=FLAT, padx=5, pady=1, highlightthickness=3)
    panedwin1.add(pw1scroll3)
    #showheadlines(pw1scroll)

    '''
pw1scroll2 = ScrolledText(panedwin2,
                        width=int(pwwidth - 15), bg='#9540CD', fg='white',
                        font='comicsans,12',  #xscrollcommand = scrollbar.set(0,100),
                        height=int(pwheight) / 2,  #font='comicsans,12',
                        relief=FLAT, padx=5, pady=1, highlightthickness=3)
panedwin2.add(pw1scroll2)
# get and set BBC News Headlines in TOP pane ONE
showheadlines(pw1scroll2)
# get and set BBC News Headlines in MIDDLE pane TWO
showheadlines(textctrl)
    '''
    #Add a listbox + scrollbar to bottom (THIRD) pane
    choicesvar = StringVar()
    choices = ["This is a string in the listbox",
        "This is a 2nd string in the listbox",
        "This is a 3rd string in the listbox",
        "This is a 4th string in the listbox",
        "This is a 5th string in the listbox",
        "This is a 6th string in the listbox",
        "This is a 7th string in the listbox",
        "This is a 8th string in the listbox",
        "This is a 9th string in the listbox",
        "This is a 10th string in the listbox",
        "This is a 11th string in the listbox",
        "This is a 12th string in the listbox",
        "This is a 13th string in the listbox",
        "This is a 14th string in the listbox"]
    choicesvar = StringVar(value=choices)
    # create a scrollbar
    scrollY = Scrollbar(panedwin3)
    scrollY.pack(side=RIGHT, fill=BOTH)

    # create the listbox
    lbox1 = Listbox(panedwin3, listvariable=choicesvar,
                width=int(pwwidth - 15), height=200,
                font='comicsans, 15', fg='black', bg='cyan',
                highlightbackground='cyan', bd=2)
    lbox1.pack(side=LEFT, fill=BOTH)

    # tie  the scrollbar to the listbox
    pw1scroll3['yscrollcommand'] = scrollY.set
    lbox1.configure(yscrollcommand=scrollY.set)
    scrollY.configure(command=lbox1.yview)
    scrollY.configure(width=17)
###################################################################################
## END of Listbox + scrollbar creation/initialization
###################################################################################

###################################################################################
## Global BINDINGS ##
###################################################################################
# bind ENTRY1 TO <KeyRelease> to capture keystrokes
# once the key is released, so that the control
# actually has the data value in it.
entry1.bind("<KeyRelease>", setoutputfield)
## LEFT BUTTON RELEASED IN SLIDERS
slide1.bind("<ButtonRelease-1>", addtxt)
slide2.bind("<ButtonRelease-1>", showkey)
slide2.bind("<ButtonRelease-3>", showkey)

###################################################################################
## setup additionbal widgets ##
###################################################################################

###################################################################################
## load dbug window ?? ##
###################################################################################
#dbwin = debugwindow(panedwin1)
#print(f'Debug window count = {dbwin.getCount()}')
#panedwin1.add(dbwin.dbgwin)

###################################################################################
mainloop()
###################################################################################
#   E.O.F
###################################################################################
#class Window_program(tkinter.Frame):
#    def __init__ (self, parent):
#        Tkinter.Frame.__init__(self, parent)

#class main (Tkinter.Tk):
#    ### app consdtructor ###
#    def __init__(self):
#        self.windowprogram = Window_program(self)

if __name__ == "__main__":
    print('in "if __'
          'name__ == __main__()')
#    args = sys.argv[1:]
#App()
    main()
