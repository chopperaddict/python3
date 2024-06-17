import  string
import tkinter as tk
import json
from Classes import *
from Classes import sliders
from Support import *

def createPanedWindow(parent, parentwidth, parentheight, heightargs, widthargs, maxcount):
#def createPanedWindow(parentheight,  parentwidth):

    if maxcount == 0:
        return []

    winheight = (list(heightargs))
    winwidth = (list(widthargs))

    ######################
    ## MAIN CONTAINER ####
    ######################
    ##mid/dark yellow -cannot be seen on screen,
    # but is main container for all other panes
    print(f'Creating main window holder [pwparent] W = {int(parentwidth + 25)},H = {int(winheight[1])}')
    pwparent = PanedWindow(parent, bd=5, sashpad=5, showhandle=True,
                           height=int(winheight[1]), bg='#DAB700',
                           width=int(parentwidth + 25), orient=VERTICAL,
                           sashwidth=10, handlesize=15, handlepad=1,sashrelief=RAISED)
    pwparent.pack()
    pwparent.place(x=3, y=225)
    #panedwindows = [pwparent]

    # create main Panned Winow and position it
    #dummy pane to contain all others
    ###################
    ## WRAPPED PANES ##
    ###################
    #TOP FRAME - #orange/red
    print(f'Creating main panel window  [main_panel] W = {int(abs(parentwidth - 10)/2)}, H = {int(parentheight - 45)}')
    main_panel = PanedWindow(parent,
        height=int(parentheight - 45),
        width=int(abs(parentwidth - 10)/2), bg='#F2EEDC',#bg='#FF9B78',
        sashpad=5, showhandle=True, orient=VERTICAL,
        sashwidth=10, handlesize=15, handlepad=5,sashrelief=RAISED)
    pwparent.add(main_panel)
    l00 = Label(main_panel, text="This is the YELLOW/RED main_panel !!",bg='#FF9B78', fg='white')
    l00.place(x=15, y=60)
    main_panel.add(l00)
    panedwindows = [ main_panel]

    # SECOND PANEL - light green
    if maxcount >=2:
        print(f'creating VERTICAL [pw01] W = { int(parentwidth - 120)/2} H = {int(winheight[0] -500)}')
        # SECOND PANEL - light green
        # LIGHT GREEN RH Panel
        pw01 = PanedWindow(main_panel,
                      height=int(winheight[0] - 500),
                      width=int(abs((parentwidth - 120)/2)), bg='#8DCF87',  # light green
                      sashpad=5, showhandle=True, orient=VERTICAL,
                      sashwidth=10, handlesize=15, handlepad=9,sashrelief=RAISED)
        #pw01.place(x=5, y=65)
        main_panel.add(pw01)#,sticky='swse')
        l000 = Label(pw01, text="This is the [PW01] LIGHT GREEN PW01 panel !!",bg='#8DCF87',fg='red')
        l000.place(x=15, y=5)
        pw01.add(l000)
        panedwindows = [main_panel,pw01]
        if maxcount ==2: return panedwindows

    if maxcount >= 2:  # DArk green
        print(f'creating VERTICAL [pw1] W = {int(parentwidth - 40) / 4} H = {int(winheight[0] / 1.4) + 20}')
        pw02 = PanedWindow(main_panel,
                           height=int(winheight[0] / 1.4)+ 20,
                           width =int(abs((parentwidth - 40)/4)),
                           bg='#1D6748', # black
                           sashpad=5, showhandle=True, orient=VERTICAL,
                           sashwidth=10, handlesize=15, handlepad=14,sashrelief=SUNKEN)

        main_panel.add(pw02)#, sticky='sesw')
        l01 = Label(pw02, text="This is [PW1] !!", bg='#4A4041', fg='white')
        l01.place(x=5, y=50)
        pw02.add(l01)
        panedwindows = [ main_panel,pw01, pw02]
        if maxcount == 3: return panedwindows
        #print(f'CREATEPANEDWINDOW [pw1] W={int(parentwidth/2) - 10} x H={int(winheight[0]/1.4) + 20}')

    if maxcount >= 3:
        print(f'creating VERTICAL [pw1] W={int(parentwidth - 50)} H={int(winheight[0] / 1.4) + 20}')
        pw03 = PanedWindow(main_panel,           ## BLACK
                           width = int(parent_width - 50),
                           height = int(winheight[0] / 1.4) + 20,
                           bg='#4A4041', # black
                           sashpad=5, showhandle=True, orient=VERTICAL,
                           sashwidth=10, handlesize=15, handlepad=14,sashrelief=SUNKEN)
        main_panel.add(pw03)#, sticky='sesw')
        l01 = Label(pw1, text="This is [PW1] !!", bg='#4A4041', fg='white')
        l01.place(x=5, y=50)
        pw03.add(l01)
        panedwindows = [main_panel,pw01. pw02, pw03]
        if maxcount == 4:
            return panedwindows
