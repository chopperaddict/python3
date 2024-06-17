
import sys
from tkinter import *
from tkinter import ttk
from StripMethods import *
from StripApp import *

#global root
global inputstring
global stripchars
global StripInputApp
global DBUG
global data
global dbwinclass
# ====================My classes ===============================

# Window Functions only
# ==========END OF FUNCTIONS ===========================

## ======================================================
# ==========START OF MAIN CODE =========================
# ======================================================
#while True:

##==================END OF FILE ===========================

######################################
# END of MAIN PROCESSING FUNCTION
def StripChars(data, showresultshandle):
    # ===============
    # DISPLAY AN OUTPUT WINDOW
    # basically working 21/5/24 16:32 hrs zulu
    # our output window has laready been created in stripchars.py
    # ===============
    def CloseOutputWin():
        ## drop this window in the stack order ?
        data.resultswin = None
        data.outwincount -= 1
        ShowResults.destroy()

    def Show_Display(winbackground):
        Show_DisplayInfo(data, ShowResults, 1, midxpos, winbackground)

    data.outwincount += 1
    ## set output window to be the active window
    winbackground = "#C4DEDE"
    data.activetkwindow = showresultshandle
    #  makes the outout window a topmost window
    data.activetkwindow.wm_attributes("-topmost", 1)
    data.activetkwindow.wm_attributes("-topmost", 0)

    ShowResults = showresultshandle
    ShowResults.config(bg=winbackground)   # light grey
    outwinheight= 160
    outwinwidth = 650
    data.outputsize = outwinheight,outwinwidth
    ShowResults.title("My test Python/TkInter window")
    ShowResults.minsize(outwinwidth, outwinheight)
    ShowResults.maxsize(outwinwidth + 200, outwinheight + 150)
    ShowResults.title("String processor - Full Results")
    midxpos = 10
    if int(data.usemonitor) == 1:
        midxpos = 10
    if int(data.usemonitor) == 2:
        midxpos = data.mon2array.width + 10
    if int(data.usemonitor) == 3:
        midxpos = data.mon2array.width + data.mon3array.width  + 10

    ShowResults.update()
    #ShowResults.geometry(f'575x290+{midxpos}+100')
    # stack outputwindows prettily if > 1 open
    ShowResults.geometry(f'{outwinheight}x{outwinwidth}+{midxpos}+100')

    ShowResults.wm_attributes("-topmost", 1)
    ShowResults.wm_attributes("-topmost", 0)

    printdbg("creating output window")
    ## create a fonnt for general use - DOESNT WORK !!!!!!!
    Font_tuple = Tk.font.Font(family="SegoeUI",
                                   size=20,
                                   weight="normal")

    if data.dbug > 0:
       # show ther chosen parameters in termnal before we process it all
       print1()
       print1("Received Input string= [" + data.stringinput + "]", end='\n')
       print1("Received Removal chars= [" + data.stripchars + "]", end='\n')
       if int(data.stripmode)  == 0: print1(f"Processing [{data.stripmode }] using Strip from EVERYWHERE in string")
       if int(data.stripmode)  == 1: print1(f"Processing [{data.stripmode }] using Strip from START of string only")
       if int(data.stripmode)  == 2: print1(f"Processing [{data.stripmode }] using Strip from END of string only\n")

    data.stringoriginal = data.stringinput
    # make a call to relevant procesing method in StripMethods.py
    if int(data.stripmode) == 0:
        input = stripembedded(data)
        data.stringstripped = input
    if int(data.stripmode) == 1:
        input = StripLeadingChars(data)
        data.stringstripped = input
    if int(data.stripmode) == 2:
        input = StripTrailingChars(data)
        data.stringstripped = input
        data.stringoriginal = data.stringinput

          #==============================================
        #Show our processed results in the output wndow
        #==============================================
        #force window to top of z-order'
    prompt="Mode selected was " +str(data.stripmode)
    fontsize = 16
    if data.stripmode == 0:
        label1 = Label(ShowResults, text="Mode selected was - [Remove from EVERYWHERE]",\
                       font= f'SegoeUI, {fontsize}', bg='#C4DEDE')
        #.grid(column=2, row=1, sticky=W)
        label1.place(x=10, y=10)
        print1(f"Mode selected was - [Remove from EVERYWHERE]")
        label5 = Label(ShowResults,\
                text="Chars to be removed were [" + data.stripchars + "] from EVERYWHERE", font=f'SegoeUI,{fontsize}',
                   bg='#C4DEDE', fg='red')
    if data.stripmode == 1:
        label2 = Label(ShowResults, text="Mode selected was - [Remove from START of string ONLY]",\
                       font= 'SegoeUI, 14', bg='#C4DEDE')
        label2.place(x=10, y=10)
        print1(f"Mode selected was [{data.stripmode}] - [Remove from START of string ONLY]")
        label5 = Label(ShowResults, text="Chars to be removed were [" + data.stripchars + "] from START",\
                       font=f'SegoeUI, {fontsize}',
                   bg='#C4DEDE', fg='red')
    if data.stripmode == 2:
        label3 = Label(ShowResults, text="Mode selected was - [Remove from END of string ONLY]",\
                font= f'SegoeUI, {fontsize}4', bg='#C4DEDE')
        label3.place(x=10, y=10)
        print1(f"Mode selected was - [Remove from END of string ONLY]")
        label5 = Label(ShowResults, text="Chars to be removed were ["+ data.stripchars + "] from END",\
                       font= f'SegoeUI, {fontsize}', bg='#C4DEDE', fg='red')

    label5.place(x=10, y=50)

    label6 = Label(ShowResults, text="Original string received was ["+ data.stringoriginal + "]",\
                   font = f'SegoeUI, {fontsize}', bg='#C4DEDE')
    label6.place(x=10, y=90)
    if data.stripchars== "":
        data.stringoutput="String was stripped ENTIRELY..."
        label7 = Label(ShowResults, text="Stripped string (RESULT) ["+ data.stringstripped + "]",\
                       font= f'SegoeUI, {fontsize}', bg='red', fg='white')
    else:
        label7 = Label(ShowResults, text="Stripped string (RESULT) [" + data.stringstripped + "]",\
                       font=f'SegoeUI, {fontsize}', bg='#C4DEDE')
    label7.place(x=10, y=130)

    label8 = Label(ShowResults, text="Total # of characters removed was [" + str(data.charsremoved)\
                                   + "]" , font=f'SegoeUI, {fontsize}',\
                   bg='#C4DEDE')
    label8.place(x=10, y=170)

     # print to our console as well
    listinputs(data, 1)
    btn3 = Button(ShowResults, text="Show Monitors status", command=lambda: Show_Display(winbackground), font=f'SegoeUI, {fontsize}',
                  bg='#AA00DD', fg='white', width=26, height=2)
    btn3.place(x=15, y=215)

    # Click to close window AND App
    btn = Button(ShowResults, text="Close Window", command=CloseOutputWin,\
                 font= f'SegoeUI, {fontsize}',\
                 width=14, height = 2, bg='#009900')
    ## position button-must be 140 or so pixels wide
    btn.place(x = outwinwidth-195, y = 215)

    #How to write + read ENV variables
    os.environ["PyResult"] = data.stringstripped
    #read it back
    str1 = os.environ["PyResult"]
    ## set Environment variable
    os.environ["PyInput"] = (data.stringoriginal)
    #read it back
    str2 = os.environ["PyInput"]
    ShowResults.focus_set()
    print1(f"INPUT  - PyInput  from ENV is [{str2}]")
    print1(f"OUTPUT - PyResult from ENV is [{str1}]")
    print1("Processing completed successfully ...\n")

    # Bring our processed results in the output wndow    state = data.stripwin.state()

    if data.resultswin != None:
        print1 (f"Stripwin = {data.stripwin}, resultswin = [{data.resultswin}]")
    else:
        print1(f"Stripwin = {data.stripwin}, resultswin = None")

    # run the window up
    #m ==================
    ShowResults.mainloop()
    #m ==================
######################################

## *** EOF ***
   # fo=open("X:/bat files/welcome.py", "r")
    # for index in range(5):
    #   line = fo.readline()#

    # Close opened file
    # fo.close()


   ## RTF style text box ???
    #text=Text(ShowResults, width=300, height=200)
    #text.insert('1.0', 'here is my\ntext to insert')
