import  string
import tkinter as tk
import json
from Classes import *
from Classes import sliders
from Support import *
#from menus import *

def createContainerWindow(parent, parentwidth, parentheight, sw, bg):
    # mid yellow
    pwparent = PanedWindow(parent, bd=5, sashpad=5, showhandle=True,
                           height=int(parentheight+20), bg='#DAB700',
                           width=int(parentwidth + 25), orient=VERTICAL,
                           sashrelief=RAISED, sashwidth=sw, handlesize=sw, handlepad=1,
                           relief=RAISED, borderwidth=4)
    #pwparent.pack()
    #pwparent.place(x=3, y=225)
    lab00 = Label(pwparent,
        text=f'Creating VERTICAL main [pwparent]: Container PanedWindow() (windows holder) W = {int(parentwidth + 25)}, H = {int(parentheight)}',
        bg='#FF9B78', fg='white')
    lab00.place(height = 2, width = parentwidth)
    return pwparent

def createPanedWindow(frame2, parentwidth, parentheight, sw, bg, maxcount):
    ##################
    ## WRAPPED PANES ##
    ###################
    #TOP FRAME - #orange/red
    print(f'Creating VERTICAL PanedWindow() [newpane] \
            W = {int(parentwidth + 25)}, \
            H = {int(parentheight)} (Child Pane)')
    # paper white (off white)
    newpane = PanedWindow(frame2,
        height=int(parentheight/3),
        width=int(parentwidth + 20), bg=bg,#bg='#FF9B78',
        sashpad=2, showhandle=True, orient=VERTICAL,
        sashwidth=sw, handlesize=sw+2, handlepad=2,sashrelief=RAISED)
    #newpane.pack()
    #newpane.place(x=10, y=100)
    #l00 = Label(newpane, text="This is the YELLOW/RED main_panel !!",bg='#FF9B78', fg='white')
    #l00.place(x=150, y=parentwidth - 18)
    #main_panel.add(l00)
    #panedwindows = [ main_panel]
    #f maxcount == 1:
    return newpane
    '''
    # SECOND PANEL - light green
    if maxcount >=2:
        print(f'creating VERTICAL [pw01] W = { int(parentwidth - 120)/2} H = {int(parentheight)}')
        # SECOND PANEL - light green
        # LIGHT GREEN RH Panel
        pw01 = PanedWindow(newpane,
                      height=int(parentheight/3),
                      width=int(abs((parentwidth - 120)/2)), bg='#8DCF87',  # light green
                      sashpad=5, showhandle=True, orient=VERTICAL,
                      sashwidth=10, handlesize=15, handlepad=9,sashrelief=RAISED)
        #pw01.place(x=5, y=65)
        newpane.add(pw01)#,sticky='swse')
        l000 = Label(pw01, text="This is the [PW01] LIGHT GREEN PW01 panel !!",bg='#8DCF87',fg='red')
        l000.place(x=15, y=5)
        pw01.add(l000)
        panedwindows = [newpane,pw01]
        if maxcount ==2: return newpane, pw01

    if maxcount >= 3:  # DArk green
        print(f'creating VERTICAL [pw1] W = {int(parentwidth - 40) / 4} H = {int(parentheight)}')
        pw02 = PanedWindow(newpane,
                           height=int(parentheight/3),
                           width =int(abs((parentwidth - 40)/4)),
                           bg='#1D6748', # black
                           sashpad=5, showhandle=True, orient=VERTICAL,
                           sashwidth=10, handlesize=15, handlepad=14,sashrelief=SUNKEN)

        #main_panel.add(pw02)#, sticky='sesw')
        l01 = Label(pw02, text="This is [PW1] !!", bg='#4A4041', fg='white')
        l01.place(x=5, y=50)
        pw02.add(l01)
        panedwindows = [ newpane, pw01, pw02]
        if maxcount == 3: return newpane, pw01, pw02
        #print(f'CREATEPANEDWINDOW [pw1] W={int(parentwidth/2) - 10} x H={int(winheight[0]/1.4) + 20}')

    if maxcount >= 4:
        print(f'creating VERTICAL [pw1] W={int(parentwidth - 50)} H={int(parentheight)}')
        pw03 = PanedWindow(newpane,           ## BLACK
                           width = int(parent_width - 50),
                           height=int(parentheight/3),
                           bg='#4A4041', # black
                           sashpad=5, showhandle=True, orient=VERTICAL,
                           sashwidth=10, handlesize=15, handlepad=14,sashrelief=SUNKEN)
        main_panel.add(pw03)#, sticky='sesw')
        l01 = Label(pw1, text="This is [PW1] !!", bg='#4A4041', fg='white')
        l01.place(x=5, y=50)
        pw03.add(l01)
        panedwindows = [main_panel,pw01. pw02, pw03]
        if maxcount == 4:
            return newpane, pw01, pw02, pe03
'''
