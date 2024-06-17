
#Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
import StripMethods
import StripApp
from StripMethods import stripargsdata

#from StripApp import process_string
#class mygui():
#    def __init__(self, master, *args, **kwargs):
#        self.master = master
#        #tk.Frame.__init__(self, parent, *args, **kwargs)
#        self.master = master
#        StripInputApp = master
#        #<create the rest of your GUI here>
#        StripInputApp.title="Debug  window"
#        #print(set(parent.keys()))
#        #StripInputApp = root
#        StripInputApp.configure(bg='lightgrey')
#        StripInputApp.minsize(600, 700)
#        StripInputApp.maxsize(1200, 1000)
##### slaved code

def closeDown():
    StripInputApp.destroy()
    sys.exit(0)

def process_string():
    print1("\nProcessing results  ()\n")
    # ------- Validate strIp character(s) string entry --------------
    data.stringinput = instring_entry.get()
    data.stringoriginal = data.stringinput

    stripstring = stripstring_entry.get()
    if stripstring == "" :
        oahead = messagebox.showwarning("Input Error", f'NO STRIP characters have been provided !2\n\nTo proceed, please enter 1 or more characters in this field')
        data.stripchars = ""
        stripstring_entry.focus()
        return False
    else:
        data.stripchars = stripstring

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
        data.stripmode= stripchoice - 1

    #------ Validate Output mode -----------------
    dbg = si.get()
    if dbg == "1":            # just default to mode 2 (Full output window)
        data.dbug = 2
    else:
        data.dbug = 0
    DBUG = data.dbug

    # hide this window
    #StripInputApp.withdraw()
    #StripInputApp.lower()
    retval = data.stripwin.lower()
    # create and go to our output window
    ShowResults = Toplevel()
    root.withdraw()
    #ShowResults.bind("<FocusIn>", handle_focus)
    #ShowResults.protocol("WM_TAKE_FOCUS", handler)
    # this is actually set in the code where we create this output window
    data.resultswin = ShowResults
    print1 ("calling StripChars()")
    dbwinclass.dbprint(data.dbgwin, "yet another attempt to get output in my debug window!!")
    StripChars(data, ShowResults)

def populateWin(StripInputApp):
# Window Layout - create various labels (text strings) && input fields
# ===================================================================
# 1ST ROW - string to be stripp[ed
    StripInputApp.configure(Title="hello world")
    label1 = tk.Label(StripInputApp, text="Input string", font="Arial, 14", bg='lightgrey')#.grid(column=1, row=1, sticky=W)
    label1.place(x=10, y = 10)
    input = tk.StringVar(StripInputApp, name="input")
    data = stripargsdata
    StripInputApp.setvar(name="input", value=data.stringinput)
    instring_entry = tk.Entry(StripInputApp, width=30, insertborderwidth='5',  insertbackground='red',\
                textvariable = input, font="Arial, 14", bg='lightgrey')
    # Style() padding adds pixels inside the Button. The widget’s position is not changed.
    #'Style().configure("Entry", padding=5)

    #instring_entry.pack(padx=14, pady=20)
    instring_entry.place(x=200, y=10)

    # 2ND ROW - strip characters
    label2 = tk.Label(StripInputApp, text="Chars to be removed", font="Arial, 14", bg='lightgrey', fg='black')
    label2.place(x=10, y = 50)
    stripstring_entry = tk.Entry(StripInputApp, width=20, textvariable=data.stripchars, font="Arial, 14",\
                    bg='lightgrey', fg='red')
    stripstring_entry.insert(0, data.stripchars)
    stripstring_entry.place(x=200, y=50)

    # 3RD ROW - strip mode
    radiolabel = tk.Label(StripInputApp, text="  Click below on the type of 'Stripping' you want to perform...   ",\
                    font="Arial, 14", bg='#cc0050', fg='white', height = 1, pady=2)
    radiolabel.place(x=24, y=90)

    # handle mode radio button selections
    def modeclick(value):
        # set mode to value in range 0-2
        data.stripmode=value
        return

    # default to strip from LEADING, as it is the most common option
    bm1 = tk.StringVar(StripInputApp, "2")
    # set default to 2nd button (strip trailing)
    bm1.set(2)

    Font_tuple = tk.font.Font(family="Arial",
                                   size=13,
                                   weight="bold")
    # 4TH ROW - strip mode
    rb1 = tk.Radiobutton(StripInputApp, text="Strip from ANYWHERE in string ( Use with CARE! )", bg='lightgrey',\
                      fg='red', font=Font_tuple, selectcolor='lightgreen', activeforeground='red', \
                      activebackground='#E1BBBC', variable=bm1, indicator=0, value="1",width=57, height=2,\
                      command=lambda: modeclick(bm1.get()))
    rb1.place(x=20, y=130)

    # 5TH ROW - strip mode
    rb2 = tk.Radiobutton(StripInputApp, text="Strip from LEADING End of string ONLY", bg='lightgrey', font=Font_tuple, \
                      selectcolor='lightgreen', activeforeground='red',  activebackground='#E1BBBC',\
                      width=57, height=2,highlightcolor='purple',
                       variable=bm1,indicator=0, value="2", command=lambda: modeclick(bm1.get()))
    rb2.place(x=20, y=185)

    # 46 ROW - strip mode
    rb3 = tk.Radiobutton(StripInputApp, text="Strip from TRAILING End of string ONLY", bg='lightgrey', font=Font_tuple, \
                      selectcolor='lightgreen', activeforeground='red', activebackground='#E1BBBC',  variable=bm1,\
                      indicator=0, value="3",width=57,height=2,  command=lambda: modeclick(bm1.get()))
    rb3.place(x=20, y=240)

    # set the dbug flag to control output
    def Setshowresult(val):
        print (f"current dbug_entry = {si.get()}")
        if val == '0':
            # no output required
            data.dbug = 0
        elif val == '1':
            # set it to our full window output
            data.dbug = 2
        DBUG = data.dbug
        print (f"new dbug_entry = {data.dbug}")
        return

    si= tk.StringVar()
    Font_tuple = tk.font.Font(family="Arial",
                                   size=18,weight="bold")    # 477H ROW - results flag
    dbug_entry = tk.StringVar
    dbug_entry = tk.Checkbutton(StripInputApp, text="Show Results in window ? ", \
                bg='#CCCC00',fg='black', font='SegoUI, 14', selectcolor='cyan', activeforeground='white', \
                variable=si, activebackground='green', onvalue='1', offvalue='0', height=3, width=24,
            command=lambda: Setshowresult(si.get()))
    dbug_entry.deselect() # workarund  to get it to start up correctly
    dbug_entry.place(x=21, y=313)

    ## 8TH ROW = PROCESS BUTTON for OUR INPUT
    btn2 = tk.Button(StripInputApp, text="Process string", command=self.process_string, font='SegoUI, 16', bg='#009900',\
                  fg='black', activebackground='#E1BBBC',width=16, height=3, borderwidth='4')
    btn2.place(x=340, y=306)
    StripInputApp.focus()

    def closeDown():
        StripInputApp.destroy()
        sys.exit(0)

    Font_tuple = ("Comic Sans MS", 16, "bold")
    ## 9TH ROW = PROCESS BUTTON for OUR INPUT with purple background
    btn3 = tk.Button(StripInputApp, text="Show Monitors status", command=self.commandfunc, font=Font_tuple,
                  bg='#AA00DD', fg='white', activebackground='#E1BBBC',activeforeground='black',
                  width=22, height=2, borderwidth='4', highlightcolor='lightgrey')
    btn3.place(x=21, y=410)

    ## 8TH ROW = EXIT BUTTON for OUR INPUT
    btn2 = tk.Button(StripInputApp, text="    Exit   ", command=self.closeDown, font=Font_tuple, bg='#990000', fg='white',\
                  activebackground='#E1BBBC', activeforeground='black', width=15, height=2, borderwidth='4')
    btn2.place(x=340, y=410)
    #StripInputApp.focus()

#dumnmy stubs to pass data to external fn()
def commandfunc():
    Show_DisplayInfo(data, StripInputApp, 0, midxpos,wincolor)

if __name__ == "__main__":
    StripInputApp = tk.Tk()

    def populateWin(StripInputApp):
    # Window Layout - create various labels (text strings) && input fields
    # ===================================================================
    # 1ST ROW - string to be stripp[ed
        label1 = tk.Label(StripInputApp, text="Input string", font="Arial, 14", bg='lightgrey')#.grid(column=1, row=1, sticky=W)
        label1.place(x=10, y = 10)
        input = tk.StringVar(StripInputApp, name="input")
        data = stripargsdata
        StripInputApp.setvar(name="input", value=data.stringinput)
        instring_entry = tk.Entry(StripInputApp, width=30, insertborderwidth='5',  insertbackground='red',\
                    textvariable = input, font="Arial, 14", bg='lightgrey')
        # Style() padding adds pixels inside the Button. The widget’s position is not changed.
        #'Style().configure("Entry", padding=5)

        #instring_entry.pack(padx=14, pady=20)
        instring_entry.place(x=200, y=10)

        # 2ND ROW - strip characters
        label2 = tk.Label(StripInputApp, text="Chars to be removed", font="Arial, 14", bg='lightgrey', fg='black')
        label2.place(x=10, y = 50)
        stripstring_entry = tk.Entry(StripInputApp, width=20, textvariable=data.stripchars, font="Arial, 14",\
                        bg='lightgrey', fg='red')
        stripstring_entry.insert(0, data.stripchars)
        stripstring_entry.place(x=200, y=50)

        # 3RD ROW - strip mode
        radiolabel = tk.Label(StripInputApp, text="  Click below on the type of 'Stripping' you want to perform...   ",\
                        font="Arial, 14", bg='#cc0050', fg='white', height = 1, pady=2)
        radiolabel.place(x=24, y=90)

        # handle mode radio button selections
        def modeclick(value):
            # set mode to value in range 0-2
            data.stripmode=value
            return

        # default to strip from LEADING, as it is the most common option
        bm1 = tk.StringVar(StripInputApp, "2")
        # set default to 2nd button (strip trailing)
        bm1.set(2)

        Font_tuple = tk.font.Font(family="Arial",
                                       size=13,
                                       weight="bold")
        # 4TH ROW - strip mode
        rb1 = tk.Radiobutton(StripInputApp, text="Strip from ANYWHERE in string ( Use with CARE! )", bg='lightgrey',\
                          fg='red', font=Font_tuple, selectcolor='lightgreen', activeforeground='red', \
                          activebackground='#E1BBBC', variable=bm1, indicator=0, value="1",width=57, height=2,\
                          command=lambda: modeclick(bm1.get()))
        rb1.place(x=20, y=130)

        # 5TH ROW - strip mode
        rb2 = tk.Radiobutton(StripInputApp, text="Strip from LEADING End of string ONLY", bg='lightgrey', font=Font_tuple, \
                          selectcolor='lightgreen', activeforeground='red',  activebackground='#E1BBBC',\
                          width=57, height=2,highlightcolor='purple',
                           variable=bm1,indicator=0, value="2", command=lambda: modeclick(bm1.get()))
        rb2.place(x=20, y=185)

        # 46 ROW - strip mode
        rb3 = tk.Radiobutton(StripInputApp, text="Strip from TRAILING End of string ONLY", bg='lightgrey', font=Font_tuple, \
                          selectcolor='lightgreen', activeforeground='red', activebackground='#E1BBBC',  variable=bm1,\
                          indicator=0, value="3",width=57,height=2,  command=lambda: modeclick(bm1.get()))
        rb3.place(x=20, y=240)

        # set the dbug flag to control output
        def Setshowresult(val):
            print (f"current dbug_entry = {si.get()}")
            if val == '0':
                # no output required
                data.dbug = 0
            elif val == '1':
                # set it to our full window output
                data.dbug = 2
            DBUG = data.dbug
            print (f"new dbug_entry = {data.dbug}")
            return

        si= tk.StringVar()
        Font_tuple = tk.font.Font(family="Arial",
                                       size=18,weight="bold")    # 477H ROW - results flag
        dbug_entry = tk.StringVar
        dbug_entry = tk.Checkbutton(StripInputApp, text="Show Results in window ? ", \
                    bg='#CCCC00',fg='black', font='SegoUI, 14', selectcolor='cyan', activeforeground='white', \
                    variable=si, activebackground='green', onvalue='1', offvalue='0', height=3, width=24,
                command=lambda: Setshowresult(si.get()))
        dbug_entry.deselect() # workarund  to get it to start up correctly
        dbug_entry.place(x=21, y=313)

        ## 8TH ROW = PROCESS BUTTON for OUR INPUT
        btn2 = tk.Button(StripInputApp, text="Process string", command=process_string, font='SegoUI, 16', bg='#009900',\
                      fg='black', activebackground='#E1BBBC',width=16, height=3, borderwidth='4')
        btn2.place(x=340, y=306)
        StripInputApp.focus()

        def closeDown():
            StripInputApp.destroy()
            sys.exit(0)

        Font_tuple = ("Comic Sans MS", 16, "bold")
        ## 9TH ROW = PROCESS BUTTON for OUR INPUT with purple background
        btn3 = tk.Button(StripInputApp, text="Show Monitors status", command=commandfunc, font=Font_tuple,
                      bg='#AA00DD', fg='white', activebackground='#E1BBBC',activeforeground='black',
                      width=22, height=2, borderwidth='4', highlightcolor='lightgrey')
        btn3.place(x=21, y=410)

        ## 8TH ROW = EXIT BUTTON for OUR INPUT
        btn2 = tk.Button(StripInputApp, text="    Exit   ", command=closeDown, font=Font_tuple, bg='#990000', fg='white',\
                      activebackground='#E1BBBC', activeforeground='black', width=15, height=2, borderwidth='4')
        btn2.place(x=340, y=410)
        #StripInputApp.focus()

    def _():
        StripInputApp.destroy()
        sys.exit(0)

    StripInputApp.configure(bg='lightgrey')
    StripInputApp.minsize(600, 700)
    StripInputApp.maxsize(1200, 1000)
    StripInputApp.Title="Debug window"
    populateWin(StripInputApp)


    StripInputApp.mainloop()
