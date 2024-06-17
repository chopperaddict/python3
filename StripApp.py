# Processing for a Tkinter based input window
# called from stripchars.py
import os
import sys
import getopts
import getopt
from mainclass import *
from tkinter import *
import tkinter as TK
#from tkinter import ttk
#from tkinter import ttkbootstrap
#from StripMethods import GetMonitorInfo
#from    StripMethods import GetClass
#from    StripMethods import stripargsdata

from mainclass import *
from screeninfo import get_monitors
from tkinter import messagebox
import tkinter.font
import json # just to experiment
#import Stripchars
from Stripchars import *
#from StripMethods import *
#from Stripchars import data

# declare globals externally (for neatness)
global stripdb
global chkbox


# ================= FUNCTIONS =====================================

def Check_StripMode(input):
    if input.isdigit():
        print(input + " is a digit")
        return True
    if input == "":
        print(input + " is a  char")
        return True

        return False

def hide_moni_tors(tkwindow, type, data):
    if type == 0:
        siheight = mainclass.inputsize[0] - 10
        siwidth = mainclass.inputsize[1]
        #tkwindow..geometry(f'560x490+{midxpos}+100')
    else:
        siheight = mainclass.outputsize[0]
        siwidth = mainclass.outputsize[1]
        #window..geometry(f'560x490+{midxpos}+100')

    tkwindow.update()
    tkwindow.minsize(siwidth, siheight)
    tkwindow.maxsize(siwidth + 100, siheight)
    tkwindow.update()

def Show_DisplayInfo(mainclass,tkwin,type,midxpos, bcolor):
    #Show nfo on the monitors we have
    if type == 0:
        siheight = 720
        siwidth = 560
    else:
        siheight = mainclass.outputsize[0] + 200
        siwidth =  mainclass.outputsize[1]

    def hide_mons():
        #mainclass.Activetkwindow.update()
        #Activetkwindow.get(btn3)
        #mainclass.activetkwindow.btn3.configure(bg="purple")
        #mainclass.activetkwindow.update()
        hide_monitors(mainclass.activetkwindow, 1, mainclass)

    def hide_stripmons():
        hide_monitors(mainclass.activetkwindow, 0, mainclass)

    tkwin.minsize(siwidth, siheight)
    tkwin.maxsize(siwidth + 100, siheight + 100)
    # StripInputApp.geometry(f'560x490+{midxpos}+100')
    tkwin.update()

    for x in range(1,4):
        if x == 1: mon=mainclass.mon1array
        if x == 2: mon=mainclass.mon2array
        if x == 3: mon=mainclass.mon3array

        name = mon.name
        if type == 0:
            #strip selection window
            print ("Showing display stats for stripchars()" )
            label0 = Label(tkwin, text="Monitor(s) Information",
                           font="SegoeUI, 16", bg=bcolor, fg='blue')
            label0.place(x=140, y=530)
            rb1 = Button(tkwin, text="Hide", bg='lightgreen',\
                    fg='black', font="SegoeUI, 15", \
                    activeforeground='blue', activebackground='cyan',\
                    width=8, height=1, command=hide_stripmons)
            rb1.place(x=450, y=648)

            if(mon.is_primary):
                label1 = Label(tkwin, text=f"{name[4:]:}, Width = {mon.width}, Height={mon.height} (Default)",
                font="SegoeUI, 16", bg=bcolor, fg='black')
            else:
                label1 = Label(tkwin, text=f"{name[4:]}, Width = {mon.width}, Height = {mon.height}",
                font="SegoeUI, 16", bg=bcolor, fg='black')

            if x == 1:
                label1.place(x=40, y=570)
            if x == 2:
                label1.place(x=40, y=610)
            if x == 3:
                label1.place(x=40, y=650)


        if type == 1:
            #strip output window
            print("Showing display stats for stripapp()")
            label0 = Label(tkwin, text="Monitor(s) Information",
                           font="SegoeUI, 16", bg=bcolor, fg='blue')
            label0.place(x=140, y=290)

            rb1 = Button(tkwin, text="Hide", bg='lightgreen', \
                         fg='black', font="SegoeUI, 15", \
                         activeforeground='blue', activebackground='cyan', \
                         width=8, height=1, command=hide_mons)
            rb1.place(x=460, y=410)

            if (mon.is_primary):
                label1 = Label(tkwin, text=f"{name[4:]:}, Width = {mon.width}, Height={mon.height} (Default)", \
                               font="SegoeUI, 16", bg=bcolor, fg='black')
            else:
                label1 = Label(tkwin, text=f"{name[4:]}, Width = {mon.width}, Height = {mon.height}",
                               font="SegoeUI, 16", bg=bcolor, fg='black')
            if x == 1:
                label1.place(x=40, y=330)
            if x == 2:
                label1.place(x=40, y=370)
            if x == 3:
                label1.place(x=40, y=410)

    return
'''
def createdbugwin(data):
    # handle Tk Object stuff
    # create the Tk object - debug window
    # and save a pointer (dbgwin) to
    # it in our stripargsdata class
    # which is declared as a global ??
    debugwin = Toplevel()
    mainclass.dbgwin = debugwin
    debugwin.minsize(600, 500)
    debugwin.maxsize(2500, 1000)
    debugwin.update()
    debugwin.config(bg='lightgrey')
    global dbwinclass
    #handle CLASS
    # save a pointer to debug ** CLASS *
    dbwinclass = debugwindow()

    dbwinclass.dbprint("hi there")
    #debugwin.maxsize(siwidth + 100, siheight + 100)
    dbwinclass.config(bg='lightgrey')
    dbwinclass.title("DEBUG window")
    dbwinclass.minsize(500, 500)
    dbwinclass.maxsize(1200, 900)
    #debugwin.label1.configure(relief='sunken')

    # save a pointer to debug ** CLASS *
    dbwinclass = debugwindow()
    dbwinclass.update()

    # return tk object
    return debugwin, dbwinclass
'''

def get_monitor_from_coord(x, y):
    # this works, and gets all 3 of my screen details, incl name
    monitors = screeninfo.get_monitors()
    return monitors

def GetMonitorInfo(mainclass, StripInputApp, data):
    # this gets ALL data on current monitor + all monitors

    monitors = get_monitor_from_coord(
        mainclass.Activetkwindow.winfo_x(mainclass.Activetkwindow),
        mainclass.Activetkwindow.winfo_y(StripInputApp))
    # sort out the window size and
    # position
    retval = justify_window(StripInputApp, 440, 195)
    # move window towards the centre monitor
    Set_Display_Monitor(2560, 200)
    # save the monitor data to our class
    for m in monitors:
        sname = m.name.strip('\\\\\\\\.\\\\')
        if sname == 'DISPLAY1':
            mainclass.mon1array = m
        if sname == 'DISPLAY2':
            mainclass.mon2array = m
        if sname == 'DISPLAY3':
            mainclass.mon3array = m
        # create corrected entries in our data class (monitor1,2,3 (as per the name received)
        tmp = m.name
        if m.is_primary == True: mainclass.monitor1 = [m.width, m.height]
        if m.is_primary == False:
            if 'DISPLAY2' in tmp: mainclass.monitor2 = [m.width, m.height]
            if 'DISPLAY3' in tmp: mainclass.monitor3 = [m.width, m.height]

    currentxpos = mainclass.mon1array.width
    currentypos = mainclass.mon1array.height
    return monitors
########################################################

### =============== END OF FUNCTIONS ================###
########################################################

################################################################################
# ------------------  START OF MAIN INPUT WINDOW PROCESSING LOOP----------------
################################################################################
def stripinapp (mainclass, args, argv):
    # we receive a pointer to the class data
    #root.withdraw()
    #dbugwin, dbclass = createdbugwin(data)
    #mainclass.dbgwin = dbugwin
    #arg = "Hello world!!"
    #printdbg( arg)

    #wincolor = 'lightgrey'
    #dbugwin.bg = wincolor
    print("Entering stripinapp() on startup")

    #dumnmy stubs to pass data to external fn()
    def commandfunc():
        Show_DisplayInfo(mainclass, StripInputApp, 0, midxpos,wincolor)

    # ---------FN() to VALIOATE ALL OF THE ENTRIES FROM THE INPUT WINDOW ------------------

    def process_string():
        print1("\nProcessing results  ()\n")
        # ------- Validate strIp character(s) string entry --------------
        mainclass.stringinput = instring_entry.get()
        mainclass.stringoriginal = mainclass.stringinput

        stripstring = stripstring_entry.get()
        if stripstring == "" :
            oahead = messagebox.showwarning("Input Error", f'NO STRIP characters have been provided !2\n\nTo proceed, please enter 1 or more characters in this field')
            mainclass.stripchars = ""
            stripstring_entry.focus()
            return False
        else:
            mainclass.stripchars = stripstring

        # ------- Validate stripmode hoice  --------------
        stripchoice = int(bm1.get())
        if stripchoice < 1 or stripchoice > 3:
            messagebox.showwarning("Input's Error", \
                                             f'Invalid strip mode value of {stripchoice- 1} entered is outside valid range 0f 0-2\n\nTo proceed, please enter a value in the range 0-2 ONLY')
            # set initial focus to input string entry field
            mode_entry.focus()
            return False
        else:
            ## convert to zero based index
            mainclass.stripmode= stripchoice - 1

        #------ Validate Output mode -----------------
        dbg = si.get()
        if dbg == "1":            # just default to mode 2 (Full output window)
            mainclass.dbug = 2
        else:
            mainclass.dbug = 0
        DBUG = mainclass.dbug

        # hide this window
        #StripInputApp.withdraw()
        #StripInputApp.lower()
        retval = mainclass.stripwin.lower()
        ######################################
        # create and go to our output window
        ShowResults = Toplevel()
        ######################################
        #root.withdraw()
        #ShowResults.bind("<FocusIn>", handle_focus)
        #ShowResults.protocol("WM_TAKE_FOCUS", handler)
        # this is actually set in the code where we create this output window
        mainclass.resultswin = ShowResults
        print1 ("calling StripChars()")
        #dbwinclass.dbprint(mainclass.dbgwin, "yet another attempt to get output in my debug window!!")
        StripChars(mainclass, ShowResults)
        #mainclass.stripwin.destroy()
        #print("Returned from results")



    # ---------------START OF MAIN LOOP CODE------------
    # # -------------VALIDATE THE ARGS RECEIVED --------
    # handle arguments received
    argcount = args

    goahead='yes'
    # if we got em all, argcount = 4
    '''
    if args == 0:
        messagebox.goahead = messagebox.askquestion("Input's Error", 'No arguments have been provided\nDo you want to enter the needed details now ?\n\nIf not, select No and the program will exit....... ')
        if goahead == 'no':
            sys.exit(9)
    elif args < 3:
        goahead = messagebox.askyesno("Input's Error",
                                      'One or more required arguments have NOT been provided\nDo you want to enter theme now ?\n\nIf not, select No and the program will exit....... ')
        if goahead == False:
            sys.exit(9)

    if args == 2:
        # got strip chars , but no strip type option received,
        mainclass.stripchars = argv[1]
        emsg = f'No operating mode has been provided\nDo you want to select it now ?\n\nIf not, the program will defsult to \
                removing the character(s) [{mainclass.stripchars}] from ANYWHERE in the string !....... '
        goahead = messagebox.askyesno("Missing optiond Error",emsg)
        if goahead == False:
            sys.exit(9)
        else :
            # default to strip frm anywhere
            mainclass.stripmode = 1

    elif args == 1:
        # only the input string argument received
        mainclass.stringinput = argv[0]
        mainclass.dbug = 2
        DBUG = mainclass.dbug
        goahead = messagebox.askyesno("Input's Error",
                                      '3 required options have NOT been provided\nIf not, select No and the program will exit....... ')
        if goahead == False:
            sys.exit(9)

    elif args >= 5:
        mainclass.stringinput = argv[0]
        mainclass.stringoriginal = mainclass.stringinput
        mainclass.stripchars = argv[1]
        if type(argv[2]) is not int:
            mainclass.stripmode = int(argv[2])
        else:
            mainclass.stripmode = argv[2]
        if type(argv[3]) is not int:
            mainclass.dbug = int(argv[3])
        else:
            mainclass.dbug = argv[3]
        if type(argv[4]) is not int:
            mainclass.usemonitor = int(argv[4])
        else:
            mainclass.usemonitor = argv[4]
        DBUG = mainclass.dbug
    elif args >= 4:
        # no monitor arg received
        mainclass.stringinput = argv[0]
        mainclass.stringoriginal = mainclass.stringinput
        mainclass.stripchars = argv[1]
        if type(argv[2]) is not int:
            mainclass.stripmode = int(argv[2])
        else:
            mainclass.stripmode = argv[2]
        if type(argv[3]) is not int:
            mainclass.dbug = int(argv[3])
        else:
            mainclass.dbug = argv[3]

        mainclass.usemonitor = 1
        DBUG = mainclass.dbug


    elif args >= 3:
        mainclass.stringinput = argv[0]
        mainclass.stringoriginal = mainclass.stringinput
        mainclass.stripchars = argv[1]
        if type(argv[2]) is not int:
            mainclass.stripmode = int(argv[2])
        else:
            mainclass.stripmode = argv[2]

        mainclass.usemonitor = 1
        mainclass.dbug = 0
        DBUG = mainclass.dbug
    '''
    #############################################################################################
    #------------------------ END OF ARGS VALIDATION CODE----------------------------------------
    #############################################################################################

    # Create StripInputApp - the window that will get user input for  Stripchars.py to process
    # create and position the window the size we want it to be,,, and save pointers to class
    #---------------------------------------------------------------------------
    #root.withdraw()

    # root.destroy()
    #StripInputAp("<Enter>", handle_focus)
    #StripInputApp.protocol("WM_ACTIVATE", handler)
    #global mainclass
    from mainclass import MainClass
    mainclass = MainClass()
    #monitors = GetMonitorInfo(MainClass.Activetkwindow)
    StripInputApp= mainclass.stripapp
    mainclass.stripwin = StripInputApp
    mainclass.InputWin = StripInputApp
    #datta.activetkwindow = StripInputApp
    #create dictionary of key:monitor name, value:monitors index 1[-3]
    '''
    monitors = GetMonitorInfo(mainclass, StripInputApp, mainclass)
    midxpos = 10
    #if int(mainclass.usemonitor) == 1 : midxpos = 10
    #if int(mainclass.usemonitor) == 2 : midxpos = 2560 + 10
    #if int(mainclass.usemonitor) == 3 : midxpos = 2560 + 2560 + 10
    looper = 0
    # create dictionary
    for mon in monitors:
        entry = mon.name.split("\\\\.\\")
        print2(f"name = [{entry[1]}, status = [{mon.is_primary}]")
        looper += 1

    ## set our height and width into vars for ease of use
    midxpos =  10
    if int(mainclass.usemonitor) == 1:
        midxpos = 10
    if int(mainclass.usemonitor) == 2:
        midxpos = 2560 + 10
    if int(mainclass.usemonitor) == 3:
    
        midxpos = 2560 + 2560 + 10
    '''
    ######################################
    StripInputApp = mainclass.resultswin
    ######################################
    # -------------- set size,color & Title of window ------------------------------------
    siheight = 540
    siwidth = 560
    mainclass.inputsize = siheight, siwidth
    StripInputApp.minsize(siwidth, siheight)
    StripInputApp.maxsize(siwidth + 100, siheight + 100)
    StripInputApp.config(bg='lightgrey')
    StripInputApp.title("My test Python/TkInter window")

    ## position our input window on top left'ish of  screen
    #root.update()
    #root.geometry(f'560x{siheight}+{midxpos}+100')
    #root.update()
    StripInputApp.update()
    #root.geometry(f'560x{siheight}+{midxpos}+100')
    StripInputApp.geometry(f'{siwidth}x{siheight}+{midxpos}+100')

    # finally bring Input window to TOP of Z-Order
    StripInputApp.lift()
    StripInputApp.attributes('-topmost', True)
    StripInputApp.attributes('-topmost', False)

    #------------------END OF WIINDOW SEUP--------------------------------

    # Window Layout - create various labels (text strings) && input fields
    # ===================================================================
    # 1ST ROW - string to be stripp[ed
    label1 = Label(StripInputApp, text="Input string", font="Arial, 14", bg='lightgrey')#.grid(column=1, row=1, sticky=W)
    label1.place(x=10, y = 10)
    input = StringVar(StripInputApp, name="input")

    StripInputApp.setvar(name="input", value=mainclass.stringinput)
    instring_entry = Entry(StripInputApp, width=30, insertborderwidth='5',  insertbackground='red',\
                textvariable = input, font="Arial, 14", bg='lightgrey')
    # Style() padding adds pixels inside the Button. The widget’s position is not changed.
    #'Style().configure("Entry", padding=5)

    #instring_entry.pack(padx=14, pady=20)
    instring_entry.place(x=200, y=10)

    # 2ND ROW - strip characters
    label2 = Label(StripInputApp, text="Chars to be removed", font="Arial, 14", bg='lightgrey', fg='black')
    label2.place(x=10, y = 50)
    stripstring_entry = Entry(StripInputApp, width=20, textvariable=mainclass.stripchars, font="Arial, 14",\
                    bg='lightgrey', fg='red')
    stripstring_entry.insert(END, mainclass.stripchars)
    stripstring_entry.place(x=200, y=50)

    # 3RD ROW - strip mode
    radiolabel = Label(StripInputApp, text="  Click below on the type of 'Stripping' you want to perform...   ",\
                    font="Arial, 14", bg='#cc0050', fg='white', height = 1, pady=2)
    radiolabel.place(x=24, y=90)

    # handle mode radio button selections
    def modeclick(value):
        # set mode to value in range 0-2
        mainclass.stripmode=value
        return

    # default to strip from LEADING, as it is the most common option
    bm1 = StringVar(StripInputApp, "2")
    # set default to 2nd button (strip trailing)
    bm1.set(2)

    Font_tuple = Tk.font.Font(family="Arial",
                                   size=13,
                                   weight="bold")
    # 4TH ROW - strip mode
    rb1 = Radiobutton(StripInputApp, text="Strip from ANYWHERE in string ( Use with CARE! )", bg='lightgrey',\
                      fg='red', font=Font_tuple, selectcolor='lightgreen', activeforeground='red', \
                      activebackground='#E1BBBC', variable=bm1, indicator=0, value="1",width=57, height=2,\
                      command=lambda: modeclick(bm1.get()))
    rb1.place(x=20, y=130)

    # 5TH ROW - strip mode
    rb2 = Radiobutton(StripInputApp, text="Strip from LEADING End of string ONLY", bg='lightgrey', font=Font_tuple, \
                      selectcolor='lightgreen', activeforeground='red',  activebackground='#E1BBBC',\
                      width=57, height=2,highlightcolor='purple',
                       variable=bm1,indicator=0, value="2", command=lambda: modeclick(bm1.get()))
    rb2.place(x=20, y=185)

    # 46 ROW - strip mode
    rb3 = Radiobutton(StripInputApp, text="Strip from TRAILING End of string ONLY", bg='lightgrey', font=Font_tuple, \
                      selectcolor='lightgreen', activeforeground='red', activebackground='#E1BBBC',  variable=bm1,\
                      indicator=0, value="3",width=57,height=2,  command=lambda: modeclick(bm1.get()))
    rb3.place(x=20, y=240)

    # set the dbug flag to control output
    def Setshowresult(val):
        print (f"current dbug_entry = {si.get()}")
        if val == '0':
            # no output required
            mainclass.dbug = 0
        elif val == '1':
            # set it to our full window output
            mainclass.dbug = 2
        DBUG = mainclass.dbug
        print (f"new dbug_entry = {mainclass.dbug}")
        return

    si= StringVar()
    Font_tuple = Tk.font.Font(family="Arial",
                                   size=18,weight="bold")    # 477H ROW - results flag
    dbug_entry = StringVar
    dbug_entry = Checkbutton(StripInputApp, text="Show Results in window ? ", \
                bg='#CCCC00',fg='black', font='SegoUI, 14', selectcolor='cyan', activeforeground='white', \
                variable=si, activebackground='green', onvalue='1', offvalue='0', height=3, width=24,
            command=lambda: Setshowresult(si.get()))
    dbug_entry.deselect() # workarund  to get it to start up correctly
    dbug_entry.place(x=21, y=313)

    ## 8TH ROW = PROCESS BUTTON for OUR INPUT
    btn2 = Button(StripInputApp, text="Process string", command=process_string, font='SegoUI, 16', bg='#009900',\
                  fg='black', activebackground='#E1BBBC',width=16, height=3, borderwidth='4')
    btn2.place(x=340, y=306)
    StripInputApp.focus()

    def closedown():
        StripInputApp.destroy()
        sys.exit(0)

    Font_tuple = ("Comic Sans MS", 16, "bold")
    ## 9TH ROW = PROCESS BUTTON for OUR INPUT with purple background
    btn3 = Button(StripInputApp, text="Show Monitors status",  font=Font_tuple,
                  bg='#AA00DD', fg='white', activebackground='#E1BBBC',activeforeground='black',
                  width=22, height=2, borderwidth='4', highlightcolor='lightgrey')
    #btn3 = Button(StripInputApp, text="Show Monitors status", command=commandfunc, font=Font_tuple,
    #              bg='#AA00DD', fg='white', activebackground='#E1BBBC',activeforeground='black',
    #              width=22, height=2, borderwidth='4', highlightcolor='lightgrey')
    btn3.place(x=21, y=410)

    ## 8TH ROW = EXIT BUTTON for OUR INPUT
    btn2 = Button(StripInputApp, text="    Exit   ", command=closedown, font=Font_tuple, bg='#990000', fg='white',\
                  activebackground='#E1BBBC', activeforeground='black', width=15, height=2, borderwidth='4')
    btn2.place(x=340, y=410)
    StripInputApp.focus()

    def launchDrvwatch() :
        #exec("X:\\python files\drivewatch\\drivewatch.py" "X:\\master documents\\")
        return
    # ---- eNd of window setup ----------
    #force widow to top of z-order'
    StripInputApp.lift()
    StripInputApp.attributes('-topmost', True)
    StripInputApp.attributes('-topmost', False)
    StripInputApp.focus_set()

    # set initial focus to first empty entry field
    if len(mainclass.stringinput) == 0:
        instring_entry.focus()
    elif len(mainclass.stripchars) == 0:
        stripstring_entry.focus()
    else:
        rb2.focus()

    print()
    mainclass.stringoriginal = mainclass.stringinput
    #show inputs in console
    listinputs(mainclass, 0)

    #######################
    ## run the tkinter loop
    #######################
    StripInputApp.mainloop()

#########################################################################################
##                      END OF STRIPCHARS.PY PROCESSING                               ###
#########################################################################################

def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    # get a pointer to our Class
    #Application(self)
    mainclass = MainClass()

    getargs(args, mainclass)
    for opt, args in opts:
        if opt == '-h':
            print
            'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = args
        elif opt in ("-o", "--ofile"):
            outputfile = args

    if len(args) ==0 and mainclass.dbug !=  0:
        mainclass = MainClass()
        #data = stripargsdata()
        if mainclass.dbug == 1:
            if len(mainclass.stringinput ) == 0:
                print("No arguments were received, system is aborting ...")
                args=""
                argv=[""]
                stripinapp(mainclass, args, argv)
                sys.exit(9)
                return

            print()  # mainclass.stringinput = input
            # store input into originalstring
            mainclass.stringoriginal = mainclass.stringinput
        else:
            #root.withdraw()
            stripinapp(mainclass,len(args), args)
    else:
        #root.withdraw()
        stripinapp(mainclass, len(args), args)

if __name__ == "__main__":
 
    print('in "if __'
          'name__ == __main__()')
    args = sys.argv[1:]
    maiknclass = MainClass()
    stripinapp(mainclass, len(args), args)

# ===================== E.O.F =================================
