import sys
from tkinter import *
from tkinter import ttk as ttkj
import os
import ctypes
import screeninfo
from screeninfo import get_monitors
from mainclass import *
##==============================================
# for watchdog !
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# ====================MY FUNCTIONS ===========================
global dataglobal, dbwinclass

#class Application(object):
#    def __init__(self, master):
#        self.master = master

##==============================================
#
#class stripargsdata :
#    Activetkwindow      = Tk
#    stripwin            = Tk
#    resultswin          = Tk
#    dbgwin              = Tk
#    outwincount         = 0
#    owner               = "StripChars"
#    argv                = []
#    Proceed             = True
#    InputWin            = Tk
#    stringinput         = ""
#    stringoutput        = ""
#    stringoriginal      = ""
#    stringstripped      = ""
#    stripchars          = ""
#    inputsize           = []
#    outputsize          = []
#    stripmode           = 0
#    dbug                = 0
#    charsremoved        = 0
#    strippedenvnname    = ""
#    inputenvnname       = ""
#    minsize             = []
#    monitor1            = []
#    monitor2            = []
#    monitor3            = []
#    mon1name            = ""
#    mon1array           = []
#    mon1height          = 0
#    mon1width           = 0
#    mon1isprimary       = False
#    mon2array           = []
#    mon2name            = ""
#    mon2height          = 0
#    mon2width           = 0
#    mon2isprimary       = False
#    mon3array           = []
#    mon3name            = ""
#    mon3height          = 0
#    mon3width           = 0
#    mon3isprimary       = False
#
#    def __init__(self, owner="StripChars", input="", chars="", mode=1, dbug=1):
#        self.owner = owner
#        self.stripclass = self
#        self.stringinput = input
#        self.stringoriginal = input
#        self.stringstripped = ""
#        self.stringoutput = ""
#        self.stripchars = chars
#        self.stripmode = mode
#        self.dbug = dbug
#        DBUG = self.dbug
#        self.UseMonitor = 0
#        self.strippedenvnname = "STRIP_RESULT"
#        self.inputenvnname = "STRIP_INPUT"

def getClass(self):
    #global data
    data = MainClass()
    return data
#============== END OF CLASS ================

def listinputs(data, mode):
    if mode == 0:
        print1(f"String received (INPUT) was [{mainclass.stringinput}]")
        print1(f"Chars to be removed are [{mainclass.stripchars}]")
    else:
        print1(f"String received (INPUT) was [{mainclass.stringoriginal}]")
        print1(f"Chars to be removed were [{mainclass.stripchars}]")
    if mode == 1:
        print1(f"Stripped string (RESULT) is  [{mainclass.stringoutput}]")
    if mode == 1  and mainclass.charsremoved > 0 :
        print1 (f"A total of [{mainclass.charsremoved}] from the [{len(mainclass.stripchars)}] in the strip characters set [{mainclass.stripchars}] were found & removed\n")
    elif mode == 1:
        print1 (f"NO characters from the [{len(mainclass.stripchars)}] in the strip characters set of {mainclass.stripchars}] were found...\n")

# ======================================================
def substring(input, start, lenreq):
    output = ""
    for x in start, lenreq:
        output = input[x]
        return output

# ======================================================
def reversestring(input):
    new = ""
    if (input == ""):
        return (9)
    count = len(input)
    if count == 0:
        return (9)
    while count > 0:
        ch = input[count - 1]
        new += ch
        if count > 0:
            count -= 1
        else:
            break
    return (new)

# ======================================================

def print0(arg):
    #only print to console if dbug == 0
    data = GetClass()
    if mainclass.dbug == 0:
        print (arg)
# ======================================================

def  print1(arg):
    data = GetClass()
    #only print to console if dbug == 1
    if mainclass.dbug == 1:
        print (arg)
# ======================================================

def print2(arg):
    #only print to console if dbug == 2
    data = GetClass()
    if mainclass.dbug == 2:
        print (arg)
# ======================================================

def printdbg(arg):
    #only print to console if dbug == 2
    data = GetClass()
    mainclass.dbgwin.label1= arg
    dbwin = mainclass.dbgwin
    #dbwin.label1.update()
    #dbwin.update()
    #label1 = Label(mainclass.dbgwin, text=arg, font="Arial, 14", bg='lightgrey', fg='black')
    #label1.pack()

def handler():
    x = 1
def handle_focus(event):
    try:
        print(f"event - {event.widget.focus}")
        #if event.widget.widgetName == 'toplevel':
        #    print(f"{event.widget.widgetName}[toplevel] has gained the focus")
    except:
        print('event is not available')
# ======================================================

def stripembedded(data):
    inputline = mainclass.stringinput
    partline1=""
    partline2=""
    notfound = 0
    breakout = False
    removedcount = 0

    while True:
        if breakout:
            break
        for ch in mainclass.stripchars.lower():
            if notfound == len(mainclass.stripchars) :
                breakout = True
                break
            print1(f"trying [{ch}] in [{inputline}]")
            try:
                position = inputline.index(ch)
                partline1  = inputline[0: position]
                if position + 1 < len(inputline):
                    partline2 =inputline[position + 1:]
                    inputline = partline1 + partline2
                    print1(f"1-input = [{inputline}]")
                    removedcount += 1
                else:
                    inputline = partline1
                    print1(f"[{ch}] removed, inputline in try =[{inputline}]")
                    removedcount += 1
                    break;
            except:
                if position >= len(inputline):
                    print1(f"2-[{ch}] NOT found, checking next strip char")
                    notfound += 1
                    continue
                else:
                    if position == 0:
                        partline1 = inputline[0:position+1]
                    else:
                        partline1 = inputline[0:position]
                    inputline = partline1
                    removedcount += 1

                    if position + 1 < len(inputline):
                        partline2 = inputline[position:]
                        inputline = partline1 + partline2
                        print1(f"inputline in except =[{inputline}]")
                    else:
                        inputline = partline1

                print1(f"1-input = [{inputline}]")
                continue
            else:
                print1(f"Position of [{ch}] was [{position}] / [{len(inputline) - 1}]")

        print1(f"after [{ch}] from [{mainclass.stripchars}] inputline==[{inputline}]")
    print1 (f"Removed [{mainclass.stripchars}] from {mainclass.stringoriginal}, so output=[{inputline}], ")
    mainclass.stringinput = inputline
    mainclass.stringstripped = inputline
    mainclass.stringoutput = inputline
    mainclass.charsremoved = removedcount
    return inputline

# ======================================================

def StripLeadingChars(data):
    charsremoved = 0
    stringinput = mainclass.stringinput
    stringlen = len(stringinput)
    mainclass.stringoriginal = stringinput
    mainclass.charsremoved = 0
    #stringoutput = ""
    stripchars = mainclass.stripchars
    stripcharslen = len(stripchars)
    chindex =  0
    lastmatchcount = 0
    nomatchcount = 0
    exitflag = False
    ch_count = 0
    while not exitflag:
        # move start position
        if len(stringinput) == 0:
            # no more input string to check
            break

        # get first char in current input string
        if len(stringinput) == 0:
               break
        # parse inputstrnig checking initial char for matching stripchar
        while len(stringinput) > 0:
            if nomatchcount == stripcharslen:
                exitflag  =True
                break
            count = 0
            checkchar = stringinput[0: 1].lower()
            # loop thru all stripchars
            ch_count = 0
            for ch in stripchars.lower():
                ch_count += 1
                chindex = stripchars.index(ch)
                if chindex == stripcharslen:
                    break
                if nomatchcount == stripcharslen:
                    exitflag = True
                    break
                ch_count += 1
                # '4321'
                if checkchar == ch:
                    # matches, so bypass to ignore it
                    # got a match, so clear our non match counter
                    nomatchcount = 0
                    mainclass.charsremoved += 1
                    lastmatchcount += 1
                    if len(stringinput) > 1:
                        # remove current 1st char
                        stringinput = stringinput[1:]
                        checkchar = stringinput[0]

                        # check the next char in INPUT  STRING TO SEE IF THERE IS MORE THAN ONE
                        # IF SO remove it as well.,-
                        while len(stringinput) > 0:# and checkchar == ch:
                            if count == 0:
                                break

                            if checkchar == ch:
                                mainclass.charsremoved += 1
                                stringinput = stringinput[1:]
                                lastmatchcount += 1
                                if len(stringinput) > 1:
                                    stringinput = stringinput[1:]
                                    checkchar= stringinput[0]

                                    # new  break
                                    break
                            else:
                                break

                            chcount = 0
                            count = 0
                            for ch in stripchars.lower():
                                # inner loop
                                ch_count += 1
                                chindex = ch.index(stripchars)
                                if len(ch) == 0:
                                    break
                                count = 0
                                while True:
                                    # get first char in current input string
                                    if len(stringinput) == 0:
                                        break
                                    checkchar = stringinput[0: 1].lower()
                                    count = 0
                                    # INNER loop Checking next char for initial char matching
                                    while True:
                                        if checkchar == ch:
                                            # matches, so bypass to ignore it
                                            count += 1
                                            mainclass.charsremoved += 1
                                            lastmatchcount += 1
                                            nomatchcount = 0
                                            # remove 1st char
                                            stringinput = stringinput[1:]
                                            checkchar = stringinput[0]
                                            continue
                                        else:
                                            # no more matches to this strip char, get next strip char
                                            ch_count = stripargslen - 1
                                            if ch_count == stripargslen - 1:
                                                nomatchcount += 1
                                                break
                                        break   # break out of inner while loop
                                    break   # break kout of foreach stripchar
                            if count == 0:
                                break
                            chindex = ch.index(stripchars)
                            if (chindex) == stripcharslen - 1 and len(stringinput) >= 1:
                                break
                            break

                        nomatchcount += 1
                        if ch_count == stripcharslen - 1:
                            # been thru all strip chars - start again
                            break
                        if (chindex) == stripcharslen - 1:
                            break;
                        break

                    # exit to outer loop
                    break
                #end - if checkchar == ch:

                if (chindex) == stripcharslen - 1:
                    nomatchcount += 1
                    break;

            # end while len(stringinput) > 0:

        # end while not exitflag: WE ARE OUTTA HERE
        mainclass.stringoutput = stringinput
        mainclass.stringstripped = stringinput
        x = mainclass.charsremoved
        # ============= END Inner loop ==================
   # ============ END outer loop - EXITING =========================
    return stringinput

# ==================END STRIPLEADING()=====================

def StripTrailingChars(data):
    # THIS CHEATS BY SIMPLY REVERSING THE INPUT STRING AND THEN USING
    # THE PROVEN STRIPlEADINGCHARS() METHOD, AND FINALY REVERSE IT BACK
    # TO PROVIDE THE RESULT STRING
    new = ""
    stringinput = mainclass.stringinput
    original = stringinput
    mainclass.stringinput = reversestring(stringinput)
    revstring = StripLeadingChars(data)
    mainclass.stringoutput = reversestring(revstring)
    mainclass.stringinput = original
    mainclass.stringstripped = mainclass.stringoutput
    return (mainclass.stringoutput)

# ======================================================
def center_window(win, width=300, height=200):
    # get screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    return

#====================================================
def justify_window(win, width=300, height=200):
    # get screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # calculate position x and y coordinates
    x = screen_width + 1100 - (width + 100)
    y = (screen_height / 2) - (height / 2) - 500
    #win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    return

#====================================================
def Set_Display_Monitor(left, top):
    x = 0
    y = 0
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{left},{top}"
    return

#====================================================
def get_monitor_from_coord(x, y):
    # this works, and gets all 3 of my screen details, incl name
    monitors = screeninfo.get_monitors()
    return monitors
#=================================================

#-----------------------------------------------#####
# fn's to calculater all my screens widths      #####
# ----------------------------------------------#####
#====================================================
class RECT(ctypes.Structure):
    _fields_ = [
        ('left', ctypes.c_long),
        ('top', ctypes.c_long),
        ('right', ctypes.c_long),
        ('bottom', ctypes.c_long)
    ]

# -------------*---------------------------------------
class MONITORINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_ulong),
        ('rcMonitor', RECT),
        ('rcWork', RECT),
        ('dwFlags', ctypes.c_ulong)
    ]

# ----------------------------------------------------
def dump(self):
    return [int(val) for val in (self.left, self.top, self.right, self.bottom)]

# ----------------------------------------------------

def get_monitors():
    retval = []
    CBFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(RECT), ctypes.c_double)

    def cb(hMonitor, hdcMonitor, lprcMonitor, dwData):
        r = lprcMonitor.contents
        print("cb: %s %s %s %s %s %s %s %s" % (hMonitor, type(hMonitor), hdcMonitor, type(hdcMonitor), lprcMonitor, type(lprcMonitor), dwData, type(dwData)))
        data = [hMonitor]
        #mainclass.append(r.dump())
        retval.append(data)
        return 1
    cbfunc = CBFUNC(cb)
    user = ctypes.windll.user32
    temp = user.EnumDisplayMonitors(0, 0, cbfunc, 0)
    print(temp)
    return retval
# ----------------------------------------------------

def monitor_areas():
    retval = []
    monitors = get_monitors()
    for hMonitor, extents in monitors:
        data = [hMonitor]
        mi = MONITORINFO()
        mi.cbSize = ctypes.sizeof(MONITORINFO)
        mi.rcMonitor = RECT()
        mi.rcWork = RECT()
        user = ctypes.windll.user32
        res = user.GetMonitorInfoA(hMonitor, ctypes.byref(mi))
        data = mi.rcMonitor.dump()
        #    mainclass.append(mi.rcWork.dump())
        retval.append(data)
    return retval
#----------------------------------------------------
# ===================== end of get monitor stuff ===============================

# ====================================================
def GetData(self):
    datalist = (self.stringinput,self.strippedstring, self.stripchars,self.stripmode, self.dbug, self.inputenvname, self.strippedenvname)
    return

# ====================================================
def GetClass():
    mainclass = MainClass()
    return mainclass      #stripargsdata

# ====================================================
def Process_Cancel():
    if  mainclass.OutputWin != None:
        mainclass.OutputWin.destroy()
    if mainclass.stripdata != None:
        mainclass.stripdatadestroy
    sys.exit()

# ====================================================
def getargs(args, data):
    argcount = len(args)
    #  remove program name from argv
    argv = sys.argv[1:]
    mainclass.argv = sys.argv

    results = []
    if  argcount == 1 :
        mainclass.stringinput = argv[0]
        return argcount,argv[[0]]

    # update class with the args we DO HAVE
    if argcount == 5:
        mainclass.stringinput    = argv[0]
        mainclass.stripchars     = argv[1]
        mainclass.stripmode      = argv[2]
        mainclass.dbug           = argv[3]
        DBUG = mainclass.dbug
        mainclass.usemonitor     = int(argv[4])
        results = [argv[0], argv[1], argv[2], argv[3],argv[4]]
    elif argcount == 4:
        mainclass.stringinput    = argv[0]
        mainclass.stripchars     = argv[1]
        mainclass.stripmode      = argv[2]
        mainclass.dbug           = argv[3]
        DBUG = mainclass.dbug
        mainclass.usemonitor     = 1
        results=[argv[0], argv[1],argv[2],argv[3]]
    elif argcount == 3:
        mainclass.stringinput    = argv[0]
        mainclass.stripchars     = argv[1]
        mainclass.stripmode      = argv[2]
        mainclass.dbug           = 2
        DBUG = mainclass.dbug
        mainclass.usemonitor     = 1
        results = [argv[0], argv[1], argv[2]]
    elif argcount == 2:
        mainclass.stringinput    = argv[0]
        mainclass.stripchars     = argv[1]
        mainclass.dbug           = 2
        DBUG = mainclass.dbug
        mainclass.usemonitor     = 1
        results=[argv[0], argv[1]]
    elif argcount == 1:
        mainclass.stringinput    = argv[0]
        mainclass.dbug           = 2
        DBUG = mainclass.dbug
        mainclass.usemonitor     = 1
        results = [argv[0]]


    ## results has all the valid args in it,
    ## including default values here necessary
    print (f"Arguments: count=[{argcount}]{results}")
    return argcount, results

# ====================================================

'''
def GetMonitorInfo(StripInputApp, data):
    #this gets ALL data on current monitor + all monitors
    data =  GetClass()
    monitors = get_monitor_from_coord(
        StripInputApp,
        mainclass.Activetkwindow.winfo_x(mainclass.Activetkwindow),
        mainclass.Activetkwindow.winfo_y(mainclass.Activetkwindow))
    # sort out the window size and
    # position
    retval = justify_window(StripInputApp,440, 195)
    # move window towards the centre monitor
    Set_Display_Monitor(2560, 200)
    # save the monitor data to our class
    for m in monitors:
        sname = m.name.strip('\\\\\\\\.\\\\')
        if sname == 'DISPLAY1':
            mainclass.mon1array = m
        if sname =='DISPLAY2':
            mainclass.mon2array = m
        if sname == 'DISPLAY3':
            mainclass.mon3array = m
        #create corrected entries in our data class (monitor1,2,3 (as per the name received)
        tmp= m.name
        if m.is_primary == True : mainclass.monitor1 = [m.width, m.height]
        if m.is_primary == False :
            if 'DISPLAY2' in tmp: mainclass.monitor2 = [m.width, m.height]
            if 'DISPLAY3' in tmp: mainclass.monitor3 = [m.width, m.height]

    currentxpos = mainclass.mon1array.width
    currentypos = mainclass.mon1array.height
    return monitors
'''
# ========================E.O.F ========================
