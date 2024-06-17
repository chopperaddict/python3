import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from Support import *

import tkinter.font

#border_effects = {
#    "sunken": tk.SUNKEN,
#    "raised": tk.RAISED,
#    "groove": tk.GROOVE,
#    "ridge": tk.RIDGE,
#    "flat": tk.FLAT
#}
# create an array of 20 border types so that
# if   the requirement is for mixed types, we can handle up to 20 rows
reliefstyle = [
    tk.SUNKEN,
    tk.RIDGE,
    tk.RAISED,
    tk.GROOVE,
    tk.FLAT,
    tk.SUNKEN,
    tk.RIDGE,
    tk.RAISED,
    tk.GROOVE,
    tk.FLAT,
    tk.SUNKEN,
    tk.RIDGE,
    tk.RAISED,
    tk.GROOVE,
    tk.FLAT,
    tk.SUNKEN,
    tk.RIDGE,
    tk.RAISED,
    tk.GROOVE,
    tk.FLAT
]

def printdata(label, str):
    # this works, but the label does **NOT** show it, despite the update()
    label.text=str
    label.update()
    print("data placed in bottomn label !!")
    print(str)

def closewin(win):
    win.destroy()

# method to automate the creatrion of multiple Rows/Columns
# including applying different types of visual styles and
# setting column "Weight" to control which columns expand/contract
def create_frames(owner,        # parent window
                rowcount,       # total rows to be created
                colcount,       # total cols to be created
                row_minheight,  # list of minimum height of one or more rows
                col_minwidth,   # list of minimum widths of each column
                bordersize,     # list of borderwidths
                reliefset,      # list of >= 1  indices into frame styles structure to be used
                resizable,      # list of one or more 'relief' values for each frame  ('nsew' & similar)
                pad_x,          # list of padx values, used by all
                pad_y)    :     # list of pady values, used by all

    reliefsetting=[]

    if len(reliefset)== 1:
        # create a set of frame styles matching single selection provided, all the same for each column specified
        intval = int(reliefset[0])
        reliefopts = [reliefstyle[intval]]
        for x in range (colcount):
            reliefsetting.append(reliefopts)
    elif len(reliefset) < colcount:
        # not enough args for # of cols, and we MUST receive a matching # of args to our column count
        # as different columns may well use different styles eg a flat label in col  0 & and sunken entry() field in col 1
        return -3
    else:
        # gew a set of framestyle to match the # of columns we are going to create
        for j in range(colcount):
            intval = reliefset[j]
            reliefopts = reliefstyle[int(intval)]
            reliefsetting .append(reliefopts)

    if len(bordersize) < rowcount:
        return -2

    bwidth = 0
    for i in range(rowcount):
        if colcount > 1:
            if len(bordersize) > 1: bwidth = int(bordersize[i])
            else:                   bwidth = int(bordersize[0])

            for j in range(colcount):
                frame = ttk.LabelFrame(
                    master=owner,
                    borderwidth= bordersize[j],
                    height=row_minheight,
                    relief=reliefstyle[j] )
                print(f"relief is {reliefstyle[j]}, height={bordersize}")
                frame.grid(row=i, column=j, padx=pad_x, pady=pad_y, sticky='nw')
                # add to list array so we can access them later
                frames.append(frame)
                window.columnconfigure(j, weight=resize[j], minsize=col_minwidth)
        else:
            # single column only
            if len(bordersize) > 1:
                bwidth = bordersize[i]
            else:
                print(f"Rows/Cols={rowcount}/{colcount}, bordersize={bordersize}, relief={reliefsetting[0]}, padding={pad_x}/{pad_y}")
                bwidth = bordersize
                frame = ttk.Frame(
                    master=owner,
                    borderwidth = int(bordersize[0]),
                    height=row_minheight,
                    relief=reliefsetting[0]    #on;y nered one arg in thiis case, so take forst one anyway
                )
                frame.grid(row=i, column=0, padx=pad_x, pady=pad_y, sticky='nw')
                # add to list array so we can access them later
                frames.append(frame)

    print(f"frame creation  done...total frames = {len(frames)}")
################### END OF FMODULE UNCTIONS ###########################
'''
def RunFramesApp1():
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
#    b2 = ttk.Button(frame2, textvariable=tomtext, width=30, +borderwidth=4, background=tombground, anchor='w',\
#                font='segoeUI,14', command=lambda:showtomatomsg(appletext, tomtext, infotext, b2))
    b2.grid(row=0, column=2, padx=50, pady=0, sticky='w')   # pad adds space around button so the frame container gets larger, NOT the button itself
    #dummy padding frame at right side of window
    frame3 = Frame(frame0, padx=15, pady=15, relief=FLAT, borderwidth=1)
    frame3.grid(row=0, column=2, padx=20, pady=20)
    frames.append(frame3)

    #Row 1 frame at bottom of window
    frameb = Frame(frame0, padx=5, pady=5, width=200, relief=SUNKEN, borderwidth=3)
    frameb.grid(row=1, column=0,  columnspan=3, padx=0, pady=0, sticky='w')
    frames.append(frameb)

    infotext = StringVar()    #setup tkinter variables so we can update these labels
    infotext.set('Watch this space...')    #initialise variables value (can be done anywhere)
    labelb = Label(frameb, textvariable=infotext, width=60, background='green', foreground='white', font='segoeUI,14')
    labelb.grid(row=1, column=0 , sticky='ne')

    window.columnconfigure(0, weight=0, minsize=150)
    window.columnconfigure(1, weight=8, minsize=150)
    window.columnconfigure(2, weight=8, minsize=75)
    window.columnconfigure(3, weight=0, minsize=25)
    print(frame0.children)
'''
############################
# CREATE OUR WINDOW WIDGETS
############################
app = Tk()
# Give a title to your app
app.title("My test window")

window = app
window.minsize(620, 160)
window.maxsize(1000, 400)
window.configure(background='lightgrey')
window.update()

'''
#SUPPORTING METHODS FOR THE RunFramesApp1()
# method to handle updating the apples label
# also reset the tomato button to original prompt
# TGHESE AL USE THE LAMBDA METHOD TO CALL THEM
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
'''
RunFramesApp1(window)

window.mainloop()
##################### END OF WINDOW SETUP #####################
'''
# CREATE A BUNCH OF FRAMES IN OUR WINDOW - THE EASIER WAY !!
resize = [1,0,0,1,1]        #   CONTROL COLUMN EXPANSION
reliefstyles = 0,2,1,4,6,3,2      #   FRAME STYLES TO BE USED / COLUMN
result = create_frames(window,
                8,
                5,
                80,
                80,
                '8,3,7,12,5',
                reliefstyles, # LIST OF INDICES into frame style array
                resize,
          2,    # SPACE BETWEEN COLUMNS
          2)    # VERTICAL ROW SPACING

print(f"row creation returned {result}")
if result != None and result < 0:
    if(result == -2):
        oahead = messagebox.showwarning("Error -2, the list of frame styles is  not long enough")
else:
    print(f"Frames created successfully")
###########################################################
# This code create a matrix of 5 rows & 2 columns where
# the left column alone resizes horizontally,
# #but all rows expand equally vertically,
# but the height of the content does NOT change
###########################################################
'''

'''
window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=0, minsize=75)
for i in range(5):
   # create 5 rows
    print(borders[i])
    window.rowconfigure(i, weight=1, minsize=75)
    # create 2 columns
    for j in range(2):
        frame = tk.Frame(
                master=window,
                borderwidth=6,
                relief=borders[i]
        )
        frame.grid(row=i, column=j, padx=5, pady=5, sticky='new')
        label = tk.Label(master=frame, text=f"Row {i}\nColumn 0",  height=2)
        label.grid(row=i, column=j, padx=5, pady=5, sticky='e')

window.mainloop()
'''
'''
window.columnconfigure(0, weight=1, minsize=650)
rowpos = 0
for i in range(3):
    window.rowconfigure(i, weight=1, minsize=70)

    if i == 1:
        print(f'rowpos1={rowpos} ENTRY')
        frame1= tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
        frame1.grid(row = i + rowpos, column=0, sticky='nw')
        greeting = tk.Label(master=frame1, text="Hello, Tkinter")
        greeting.grid(row=0, column=0, sticky='nw')
        frame11 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
        frame11.grid(row=rowpos, column=0, sticky='nw')
        print(f'rowpos11={rowpos} FILLER ROW')
        #rowpos = rowpos + 1
        #rowpos = rowpos + 1

    if i == 2:
        print(f'rowpos2={rowpos} ENTRY')
        frame2 = tk.Frame(master=window,relief=tk.RAISED,borderwidth=3)
        frame2.grid(row=i + rowpos, column=0, sticky='w')
        label1 = tk.Label(master=frame2, text="Enter your Name below ...")
        label1.grid(row=0, column=0, sticky='w')
        frame23 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
        frame23.grid(row=rowpos, column=0)
        print(f'rowpos22={rowpos} FILLER ROW')
        #rowpos = rowpos + 1
    if i == 3:
        frame24 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
        frame24.grid(row=rowpos, column=0)
    if i == 4:
        frame25 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
        frame25.grid(row=rowpos, column=0)
    if i == 5:
        frame26 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
        frame26.grid(row=rowpos, column=0)
    if i == 6:
        frame27 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
        frame27.grid(row=rowpos, column=0)
        '''
    #    print(f'rowpos3={rowpos} ENTRY')
    #    rowpos += 1
    #    frame3 = tk.Frame(master=window,relief=tk.RIDGE,borderwidth=8)
    #    frame3.grid(row=rowpos, column=0)
    #    entry = tk.Entry(master=frame3, fg="yellow", background="cyan", foreground='black', width=50)
    #    entry.grid(row=0, column=0, sticky='w')
    #    rowpos = rowpos + 1
    #    print(f'rowpos31={i + rowpos} MIDDLE')
    #    frame63 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
    #    frame63.grid(row=0, column=0)
    #    rowpos = rowpos + 1
    #    print(f'rowpos33={i + rowpos} EXITING')
    #if i == 4:
    #    print(f'rowpos4={rowpos} FRAME')
    #    rowpos += 1
    #    frame4 = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=8)
    #    frame4.grid(row=0, column=0)
    #    print(f'rowpos4={i + rowpos} FRAME')
    #    button = tk.Button(master=frame4, text="Click me!", width=8, height=1, bg="blue", fg="yellow", \
    #        font='SegoeUI, 16', command=lambda: printdata(label1, entry.get()))
    #    button.grid(row=i + rowpos, column=0, sticky='w')
    #    rowpos = rowpos + 1
    #    print(f'rowpos44={i + rowpos} MIDDLE')
    #    frame64 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
    #    frame64.grid(row=0, column=0)
    #    rowpos = rowpos + 1
    #    print(f'rowpos444={i + rowpos} EXITING')
    #if i == 5:
    #    rowpos += 1
    #    frame5 = tk.Frame(master=window,relief=tk.GROOVE,borderwidth=8)
    #    frame5.grid(row=0, column=0)
    #    print(f'rowpos5={i + rowpos} FRAME')
    #    label2 = tk.Label(master=frame5, text="", width=32, background='black', foreground='white', font='SegoeUI, 15')
    #    label2.grid(row=i + rowpos, column=0, sticky='w')
    #    rowpos = i + 1
    #    print(f'rowpos55={i + rowpos} MIDDLE')
    #    frame65 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
    #    frame65.grid(row=0, column=0)
    #    rowpos = rowpos + 1
    #    print(f'rowpos555={i + rowpos} EXITING')
    #if i == 6:
    #    rowpos += 1
    #    frame6 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=8)
    #    frame6.grid(row=0, column=0)
    #    print(f'rowpos6={i + rowpos} FRAME')
    #    button2 = tk.Button(master=frame6, text="Close !", width=8, height=1, bg="red", fg="white", \
    #                    font='SegoeUI, 16', command=lambda: closewin(window))
    #    button2.grid(row=i + rowpos, column=0, sticky='e')
    #    rowpos = rowpos + 1
    #    print(f'rowpos66={i + rowpos} MIDDLE')
    #    frame66 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=3)
    #    frame66.grid(row=0, column=0)
    #    rowpos = rowpos + 1
    #    print(f'rowpos666={i + rowpos} EXITING')

    #rowpos += 1

#name = entry.get()
#print (name)
#offset=15
#entry.focus()

#window.mainloop()
