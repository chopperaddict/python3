import  string
import tkinter as tk
import json
from Classes import *
from Classes import sliders
from Support import *
from PanedPanels import createPanedWindow, createContainerWindow
import winsound         # for sound
import time             # for sleep

from fastapi import FastAPI

import linecache
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from Classes import debugwindow
#from Classes import ObservableModel
from menus import *
import mysql.connector
from PIL import Image, ImageDraw
from notebook import Notepad
from Get_stock_data import *#get_stock_data
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
    getscaleoptions(Scale,"Scale")
    getscaleoptions(Button, "Button")

def GetQuote():
    #pass
    ibmval = get_stock_data()
    statusoutput.set(f'Current Stock value: IBM: ${float(ibmval):5.2f}')

def showheadlines() :
    ### news feed
    url='https://www.bbc.com/news'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        S = f'{len(response.text):,}'
        textctrl.insert(tk.END, f'Data Length is : {S} bytes\n\n')
        tmp = response.text
        #print(response.text[0:5000])
        startpos = int()
        startpos = 0
        while True:
            if startpos == -1:
                break
            startpos = tmp.find('name="description" content=',startpos, len(response.text))-startpos
            if startpos < 0:
                break
            endpos = tmp.find('"',startpos+28, len(response.text)-startpos)
            str = tmp[startpos+28:endpos]
            textctrl.insert(tk.END, f'{str}\n')
            startpos = endpos + 1
            tnp = tmp[startpos:]
    textctrl.insert(tk.END, f'\nEND OF BBC HEADLINES\n')

def cleartxt():
    textctrl.delete("1.0", tk.END)

###################################################################################
## Use the API from NewsAPI to get data
###################################################################################
## returns ALL trhe configure options for the sdlider
def getscaleoptions(ctrl,  name):
    buf = ''
    buff= ''
    print(f"\nAvailable parameters for {ctrl}")
    buf = f"\nAvailable parameters for {ctrl}\n"
    buff += buf
    opts = ctrl.configure(root)
    for opt in opts:

        buff += f"{opt}\n"
        print (opt)
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
    textctrl.insert(tk.END, f"\nSlider [1] set to [{val}]")

def NewFile():
    print("New File!")

def gotfocus():
    print( ' got focus hit')

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

# function that is bound to a keypress (using bind())
# to reset the value of the slide1 SCALE control
def setoutputfield(self):
    valid='0123456789'
    print(self.keycode)
    keyval = int(self.keycode)
    if keyval >= 48 and keyval  <= 57:
        # its a valid nuymeric value
        var1 = str(slide1val.get())
        if int(var1) > maxval :

            var1 = var1[0: len(var1) - 1]
            slide1val.set("")
            slide1val.set(var1)
            errortxt.set(f"Key ignored-value > MAX VALUE of {maxval}")
            entry1.icursor(len(str(slide1val)))
            dowarnbeep()

        elif keyval >= 48 and keyval  <= 57:
            if len(self.char) < 1:
                dowarnbeep()
                return
            print (f'key hit was {self.char}')
            val = self.char
            if len(val) > 0:
                fullval = int(slide1val.get())
                if fullval > maxval:
                    fullval = maxval
                    errortxt.set(f"Slider [2] set to MAX VALUE")
                else:
                    errortxt.set(f"Slider [2] set to [{fullval}]")
                    textctrl.insert(tk.END, f"\nSlider [2] set to [{fullval}]")

                resetvalue(fullval)
        else:
            charvalid = 'abcdefghijklmnopqrstuvwxyz'
            newchar = self.char.lower()
            fullval = slide1val.get()
            fullval = fullval[0: len(fullval) - 1]
            #self.char=""
            slide1val.set("")
            slide1val.set(fullval)
            print(f"Invalid keypress {self.char} - MUST be a numeric value !")
            errortxt.set(f"Invalid key [{self.char}] - NOT numeric !")
            # reposition caret at end of field
            entry1.icursor(len(fullval))
            if newchar in charvalid :
                dowarnbeep()
                entry1.focus()
            #time.sleep(0.25)

    else:
        # refresh the slider value as it has probably
        # been modified by del/bspace keys
        strval = str(slide1val.get())
        if strval[: len(strval) -1] in valid == True:
            var1 = int(slide1val.get())
            if var1 >=0 and var1 <= maxval:
                slide1val.set(str(var1))
                entry1.icursor(len(str(slide1val)))
                slide1value.set(int(var1))
            else:
                pass
        else:
            print('Grrrrr - Invalid keypress....')
            if len(strval) > 1:
                badkey = strval[len(strval) - 1]
                newstr = strval[0: len(strval) - 1]
                slide1val.set(str(newstr))
                entry1.icursor(len(str(slide1val)))
                slide1value.set(int(newstr))
                errortxt.set(f'Invalid key [{badkey}] entered ....')
                dowarnbeep()
            else:
                slide1val.set("")
                if len(strval) > 1 :
                    errortxt.set(f'Invalid key[{strval[len(strval - 1):]}] entered ....')
                else:
                    errortxt.set(f'Invalid key[{strval}] entered ....')
                dowarnbeep()

def     getoutputfield(self):
        valid = '0123456789'
        val = self.char
        if val in valid :
            currvalue =  str(slide1val.get())
            currvalue += val
            slide1val.set(currvalue)
        else:
            print(f"Invalid keypress {self.char} - MUST be a numeric value !")
            errortxt.set(f"Invalid key [{self.char}] - NOT numeric !")
            self.char=""
            return False
def resetzero():
    slide1value.set(0)
def resetmax():
    slide1value.set(maxval)
def resetmid():
    slide1value.set(abs(maxval / 2))
def createmenu(filemenu):
    #img = Image.open()
    new_file_img = tk.PhotoImage(file="W:\\Ebay images\\HO Coaches\\stained coach roof.png")

    menubar = tk.Menu(root, bg='#F6DAD1')
    filemenu = Menu(menubar, tearoff=False,activebackground='red', font='comicsans,12',fg='#005D00',bg='#F6DAD1')
    menu.add_cascade(label="File", menu=filemenu,activebackground='red', font='comicsans,12')
    filemenu.add_command(label="New", command=NewFile,activebackground='red', font='comicsans,12')#', image=new_file_img, compound=tk_left)
    filemenu.add_command(label="Open...", command=OpenFile,activebackground='red', font='comicsans,12')
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit,activebackground='red', font='comicsans,12')

    editmenu = Menu(menu, tearoff=False,activebackground='red', font='comicsans,12',fg='#8F7E51',bg='#F6DAD1')
    menu.add_cascade(label="Edit", menu=editmenu)
    editmenu.add_command(label="Reset Slider1 > 0%", command=resetzero, activebackground='red', font='comicsans,12')
    editmenu.add_command(label="Reset Slider1 > 50%", command=resetmid,activebackground='red', font='comicsans,12')
    editmenu.add_command(label="Reset Slider1 > 100%", command=resetmax,activebackground='red', font='comicsans,12')

    helpmenu = Menu(menu, tearoff=False,activebackground='red', font='comicsans,12',fg='#2421D6',bg='#F6DAD1')
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About,activebackground='red', font='comicsans,12')

def showslide1key():
    intval = slide1.get()
    slider1output.set(f'Slider [2] set to [{intval}]')
    textctrl.insert(tk.END, f"\nSlider [2] set to [{intval}]")


# show slider1 value in text field
def showkey(self):
    intval = slide2.get()
    slider2output.set(f'Slider [2] set to [{intval}]')
    textctrl.insert(tk.END, f"\nSlider [2] set to [{intval}]")

# show slider2 value in text field
def showslider1value():
    intval = slide1value.get()
    lbloutput.set(f'Slider2 value : [{intval}]')
    textctrl.insert(tk.END, f"\nSlider [2] set to [{intval}]")


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
root = Tk()
#fastapi = FastAPI()
#app =FastAPI()
#read_root()

#root = Tk()
#root.themename='darkly'
root.background='lightgrey'
menu = Menu(root)
root.config(menu=menu, bg='#C6FFE2')
root.title('Tk Test system')
appheight = IntVar()
#style = ttk.Style(root)#
#style.configure(root, background='#C6FFE2')
appwidth = IntVar()
appmidpoint = IntVar()
appheight = 800
appwidth = 1220
appmidpoint = appwidth/2
root.geometry(f'{appwidth}x{appheight}')
root.minsize(appwidth, appheight)
root.minsize(appwidth, appheight)
root.minsize(appwidth, appheight)
#root.maxsize(appwidth, appheight)

@gettime
@uppercase_decorator
def sayhi(arg1):
     print (arg1)

#@gettime
#def sayhi(arg1):#
#    print(arg1)

print(sayhi("Hi there Ian, how's it hanging buddy\n...Not too shabby I guess ?"))


###############
# menu setup ##
###############
filemenu = Menu(menu)
createmenu(filemenu)

###################################################################################
## create frames ##
## 1st frame ##
###################################################################################
frame1height = IntVar()
frame1width = IntVar()

###################################################################################
## setup LH frame 1 ##
###################################################################################
frame1width = int((appmidpoint)-200)
#frame1width = int((appmidpoint)-5)
frame1height = appheight-50
args = (
    '#ff00dd',
    SUNKEN,
    1,
    frame1width,
    frame1height)

Frame1 = Frame_Class(root,args)
Frame1.place(x=0, y=0, anchor='nw')
###################################################################################
## END = Frame 1 ##
###################################################################################
###################################################################################
## add widgets to LH frame 1 ##
###################################################################################
frame2_xpos = frame1width + 10
global lbloutput
lbloutput=StringVar()
lbloutput.set('Feedback ...')

btntext = StringVar()
btntext.set('Show')
btn1 = Button(Frame1, textvariable=btntext, font='FranklinGothic, 12', height=3,
              width=10, background='#6100E7', foreground='yellow',
              command=lambda: show_values(btn1, lbloutput,
                                          btntext, f"current value : {slide1value.get()}"))
btn1.place(x =10, y=100)


###################################################################################
## setup RH frame 2 ##
###################################################################################
frame2width= appwidth - 420
frame2height = frame1height
args = (
        '#DAB700',
        SUNKEN,
        2,
        frame2width,
        frame2height)
f2height = frame2height
f2width = frame2width
frame2 = Frame_Class(root,args)
frame2.place(x=frame2_xpos, y=0, anchor='nw')
print (f'Frame2 W={f2width} x H={f2height}')
###################################################################################
## END = Frame 2 ##
###################################################################################

###################################################################################
## 3rd frame for close button etc at very bottom of screen ##
###################################################################################
frame3 = Frame(root, relief=RAISED, borderwidth=1, background='#C64CE2',    # purple
               name='frame 3', width= (appwidth ), height=55)
frame3.place(x = 0, y=frame2height+55, anchor='sw')
###################################################################################
## END = Frame 3 ##
###################################################################################

########################################################################
#                       CREATE SLIDER 1 ##
# call class library - sliders() to get a ready to go slider control
# using the values in the args list above
# its current value is stored in StringVar of "slide1value"
#########################################################################
slide1value=StringVar()     # value of the slider below
global slider1width
slider1width = IntVar()
slider1width = 25

slide1 = Scale(Frame1,
        orient = VERTICAL,      #orientation= horizontal/vertical
        relief =SUNKEN,        # relief
        length = 700,             #length if horizontal, else height
        width = slider1width,     #width of slider ctrl ITSELF (WHERE THE THUMB CTRL IS)
        bd = 2,             # border - overall depth of the relief selected
        variable = slide1value,       # variable name
        from_ = 0,             #range From
        to = 10000,         # range To
        font = 'segoeUI, 10', # font
        highlightcolor = 'black',       # fg
        bg = 'lightgrey',   # bg
        activebackground = 'purple',      # btn activebackground
        troughcolor = '#88aa00',     # troughcolor
        showvalue = True,          # showvalue   at side of control
        label = '',       # label
        tickinterval = 100,
        sliderlength = 40)         # sliderlength

slide1.place(x = 5,y= 10)
slide1value.set('4500')

###################################################################################
## TEMP - call these for anny widget type to
# get a file written to MY DOCUMENTS
# listing ALL configure options
#getConfigureOpts()

########################################
#mb = #messagebox()
####################
## END# Slider 1 ###
##########################

###################################################################################
#           CREATE SLIDER 2                  #
# create another slider                      #
# (horizontal this time)in RH frame          #
###################################################################################
slide2value=StringVar()
slide2 = Scale(frame2,
            orient=HORIZONTAL,
            relief=RAISED,
            #length=350+400,
            length = frame2width -30,
            width = 30,      #width of slider
            borderwidth=2,
            variable=slide2value,
            from_=0, to=200,
            font='FranklinGothic, 10',
            fg='black',
            bg = 'lightgrey',
            activebackground = 'red',
            troughcolor='cyan',
            showvalue=True,
            label='Volume ...',
            tickinterval=20,
            digits=4,
            sliderlength=20,
            cursor = 'arrow'
            #slider1width=20,
           )
frame2length = (appwidth/2) - 40
slide2.place(x =11, y=10)

slider2output = StringVar()
slider2output.set('Information')
###################################################################################
## END Slider 2             ##
## END OF SLIDERS CREATION  ##
###################################################################################
btn2 = Button(Frame1, text='Reset', font='FranklinGothic, 12', height = 1,
              width = 6, background = 'lightgreen', command=lambda: resetvalue(0))
btn2.place(x = slider1width+105, y=frame1height - 65)

## Info Label
labelwidth = IntVar()
labelwidth = 32

slider2value = Label(frame2, textvariable=slider2output, background='#7E2B2C',
                     foreground='white', font='ComicSans,12', width = labelwidth)
slider2value.place(x=11, y=130)

###################################################################################
## Get stock quote usaing API ##
###################################################################################
## bottom panel widgets
statusoutput = StringVar()
statusline = Label(frame3, textvariable=statusoutput, background='#6E1AD5',
                 foreground='white', width = 42,font="Helvetica 12")
statusline.place(x=10, y=18)
#font = tkFont.Font(family='Comic sans', size=13, weight='bold')
stkbtn = Button(frame3, text='Get Stock price', background='Purple', foreground='yellow',
                height=1, width=13, font='FranklinGothic, 12',  command=GetQuote)
stkbtn.place(x = 420, y = 12)

## BOTTOM BUTTON
btn3 = Button(frame3, text='Close', background='red', foreground='yellow', width=8, font='FranklinGothic, 12', command=exit)
btn3.place(x = appwidth - 95, y = 10)

###################################################################################
# General screen layout ##
###################################################################################
## left hand frame
Feedbacklabel = Label(Frame1, textvariable=lbloutput, background='yellow',
                 foreground='black', width = labelwidth, font='comicsans,12')
Feedbacklabel.place(x=135, y=12)


###################################################################################
# create a value entry field for setting LIVE the slide1 setting
# the slider will instantly update to the value in this field,
# or to low/Highest values as soon as each key is released
###################################################################################
global slide1val
global maxval
slide1val = StringVar()
maxval= IntVar()
maxval = 10000
entry1 = Entry(Frame1, width=4, textvariable=slide1val, background='red', fg = 'white', font='comicsans, 14')
entry1.place(x= 135, y=90)

entrylabel = Label(Frame1, text="<<-Enter slider value", background='lightgrey', font='segoeui, 14', width=16)
entrylabel.place(x= 190, y=90)

## Error message
global errortxt
errortxt= StringVar()
errortxt.set("Error information")
errormsg = Label(Frame1, textvariable=errortxt, background='cyan', foreground='blue',
                 font='comicsans, 14',  width=22 )
errormsg.place(x= 135, y=140)

###################################################################################
## Create Frame 4 ###
## inside frame2
# ###################################################################################

innerwidth=((appwidth/2)- 10)
innerwidth = int(innerwidth)

innerheight=f2height
#innerheight=(frame1height+300) / 2
'''
args = ('#93AD7B',
        SUNKEN,
        1,
        innerwidth+170,
        #innerwidth - 20,
        innerheight + 20)
'''

# top buttons panel
frame4width = frame2width - 10
frame4height = f2height-280

args1 = ('#958D94',      # darkish grey
        RAISED,
        1,
        int(frame4width-15),     # width
        50)
        #60)        #height

## RH frame top button row
frame40 = Frame_Class(frame2, args1)
frame40.place(x=10, y=170)
print (f'Frame4 W={int(frame4width)} x H={frame4height}')
btn10 = Button(frame40, text='Clear', font='FranklinGothic, 12', height = 1, width=12,
              background = 'green', fg='white', command=cleartxt)
btn10.place(x = 405 , y=10)

statusoutput.set('Loading data from BBC News Feed .....')
btn9 = Button(frame40, text='Get BBC News Headlines', font='FranklinGothic, 12', height = 1, width=23,
              background = 'lightgreen', command=lambda: GetArticle(textctrl))
btn9.place(x =530, y=10)

statusoutput.set('')
###################################################################################
## END = Frame 4 ##
# ###################################################################################
## Create main PanedPanel and populate it ##
###################################################################################
pwheight = frame4height
pwwidth = frame4width - 25
###############################################################################
# call Fn to create Paned windows to be
# parented inside others inb the design
## CREATE PANED WINDOWS INSIDE FRAME4                                        ##
###############################################################################
# create lists[] of heights and widths to pass to paned window creation function
maxcount=1 # total paned windows to be created
frame4height += 45
heights = [frame4height, frame4height, pwheight, pwheight, pwheight]
if maxcount == 1:
    widths = [(int(pwwidth)+150), 0, 0]
else:
    widths = [(int(pwwidth)+160), int(pwwidth/2)+160, int(pwwidth) - 360, int(pwwidth) - 350, int(pwwidth) - 350]
print('\nWidths passed are ')
for width in widths:
    print (f'{width}, ')
print('\nheights passed are ')
for height in heights:
    print (f'{height}, ')

#wintotal = 3
# returns a list[] of the paned panes that have been created
panedwin0 = createContainerWindow(frame2, pwwidth,pwheight, heights, widths, maxcount)

panedwin1 = createPanedWindow(panedwin0, pwwidth,pwheight, heights, widths, maxcount)
#containerwin= createPanedWindow( frame4height, int(pwwidth)+150)
#panedwin = createPanedWindow(frame4height, int(pwwidth)+150)#
#containerwin.add(panedwin)
# initialise test labels
if maxcount == 1:
    lab1= Label()
elif maxcount == 2:
    lab1 = lab2 =  Label()
elif maxcount == 3:
    lab1 = lab2 = lab3 = Label()
elif maxcount == 4:
    lab1 = lab2 = lab3 = lab4 = Label()
elif maxcount == 5:
    lab1 = lab2 = lab3 = lab4 = lab5 = Label()

# Always add text widget
if maxcount >= 1:
    textctrl = Text(panedwin1,
        width = int(widths[0]-50),bg='#F2EEDC',
        font='comicsans,12',
        height=int(heights[0]), #font='comicsans,12',
        relief=FLAT, padx=5, pady=5, highlightthickness=1)
    #panedwindows[0].height = 80
    textctrl.place(x = 2, y = 2)
    panedwind1.add(textctrl)
    lab1 = print(f"textctrl W={int(widths[0] - 30)} x H=20")
    showheadlines()
    '''
else:
    textctrl = Text(panedwindows[1],
                    width = int(widths[1]/2) -50,bg='#F2EEDC',
                    height=int(heights[1]-500), font='comicsans,12',
                    relief=RAISED, padx=5,  highlightthickness=1)
    panedwindows[1].height = 120
    textctrl.place(x = 10, y = 10)
    panedwindows[1].add(textctrl)
    lab0 = print(f"textctrl W={int(widths[0]-550)} x H={int(heights[0]-250)}")
'''
    if maxcount > 2:
        lab2= Label(panedwindows[1], text=f"Label1 in pw2 W={widths[0]} H={heights[0]}", height=1, width=25,
                    bg='cyan', fg='black', font='comicsans,12', relief=SUNKEN)
        lab2.pack(side=TOP)
        #panedwindows[1].add(lab1)
        #panedwindows[1].add(lab1)

    if maxcount == 3:
        lab32= Label(panedwindows[2], text="Label2 in pw?", relief=RAISED,
                    height = 1, width = len(text))
        lab3.pack(side=TOP)
        #panedwindows[2].add(lab2)

    if maxcount == 4:
        lab4 = Label(panedwindows[3], text="Label2 in pw?", relief=RAISED,
                     height=1, width=13)
        lab4.pack(side=TOP)
        # panedwindows[3].add(lab3)

    if maxcount == 5:
        lab4 = Label(panedwindows[3], text="Label2 in pw?", relief=RAISED,
                     height=1, width=len(text))
        lab4.pack(side=TOP)
        # panedwindows[3].add(lab3)

    ################################################################################
    '''
    if maxcount == 2:
        panedwindows[1].add(lab1)
        #panedwindows[0].add(textctrl)
    if maxcount == 3:
        panedwindows[1].add(lab2)
        #panedwindows[0].add(textctrl)
    if maxcount == 4:
        panedwindows[2].add(tlab)
        panedwindows[1].add(lab2)
        #panedwindows[0].add(textctrl)
    '''

###################################################################################
## END PANED WINDOWS CREATION
###################################################################################

 #headlines = soup.find('body').find_all('H3')
 #for x in headlines:
 #    linecache.getline(headlines, 4)
 #    print(x.text.strip())

#showheadlines()

def savetext():
    pass
   #Fact = textctrl.get('5',20)
   #f = open('output.txt', 'a')
   #f.write(Fact)
   #f.close()
###################################################################################
## END of processing API from NewsAPI ##
###################################################################################
##########################
## widgets in 4th frame ##
##########################

## Error message
errortxt= StringVar()
errortxt.set('Error information')
errormsg = Label(Frame1, textvariable=errortxt, background='cyan', foreground='blue',
                 font='comicsans, 14',  width=22 )
errormsg.place(x= 135, y=140)

###################################################################################
## BINDINGS ##
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
dbwin = debugwindow()
#entry1.focus()
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
