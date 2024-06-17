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
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from Classes import debugwindow
import mysql.connector
from PIL import Image, ImageDraw
from notebook import Notepad
from NewsFeed import GetArticle, fetch_and_print_articles
import requests
from bs4 import BeautifulSoup


global root
master = tk.Tk()
tk = master
#fastapi = FastAPI()
#app =FastAPI()
#read_root()

#root = Tk()
#root.themename='darkly'
master.background = 'lightgrey'
cyan = '#C6FFE2'
menu = Menu(master)
master.config(menu=menu, relief=RAISED)
master.title('Tk Plain system')
appheight = IntVar()
appwidth = IntVar()
appmidpoint = IntVar()
appheight = 500
appwidth = 700
appmidpoint = int(appwidth / 2)
#appmidpoint = appwidth / 2

master.geometry(f'{appwidth}x{appheight}')
master.minsize(appwidth-150, appheight - 200)
#frame=Frame(master, height=appheight, width=appwidth)
#frame.place(master,height = appheight, width = appwidth)
#frame.grid(row=3,  column=2)

#Notepad()
textctrl = ScrolledText(master,
                        width=100, bg='#F2EEDC',
                        font='comicsans,12',  #xscrollcommand = scrollbar.set(0,100),
                        height=75,  #font='comicsans,12',

                        relief=FLAT, padx=5, pady=1, highlightthickness=3)



GetArticle(textctrl)
textctrl1 = textctrl
textctrl2 = textctrl
textctrl3 = textctrl
textctrl4 = textctrl
textctrl5 = textctrl

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
lbox1 = Listbox(master, listvariable=choicesvar,height=3,
           font='comicsans, 12', fg='black', bg='cyan',
           highlightbackground='cyan', bd=2)

scrollY = Scrollbar(lbox1)
scrollY.pack(side=RIGHT, fill=BOTH)
# tie  the scrollbar to the listbox
lbox1['yscrollcommand'] = scrollY.set
lbox1.configure(yscrollcommand=scrollY.set)
# attach the scrollbar to the listbox
scrollY.configure(command=lbox1.yview)
scrollY.configure(width=17)

widgets = [
    (lbox1, 0, 0, 2),
    (textctrl1, 1, 0, 1),
    (textctrl1, 1, 1, 1),
    (textctrl2, 2, 0, 1),
    (textctrl3, 2, 1, 1),
    (textctrl4, 3, 0, 2)
]
for widget, row, column, colspan in widgets:
    widget.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5, sticky="nsew")

#for widget, row, column, colspan in widgets:
#    widget.grid(row=row, column=column, columnspan=colspan, padx=10, pady=10, sticky ='nsew')
# Configure the grid to make the cells resizable
for i in range(3):
    master.rowconfigure(i, weight=1)
for j in range(2):
    master.columnconfigure(j, weight=1)

#Notepad()
#article = GetArticle(textctrl1)
#frame.add(article)
#txtctrl2 = textctrl
'''

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("3x2 Grid Layout with Different Widgets")

# Define the widgets to be placed in each cell
label = tk.Label(root, text="This is a Label")
button = tk.Button(root, text="Click Me")
entry = tk.Entry(root)
checkbutton = tk.Checkbutton(root, text="Check Me")
radiobutton = tk.Radiobutton(root, text="Option 1")
listbox = tk.Listbox(root)

# Add some items to the listbox
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)

# Arrange the widgets in a 3x2 grid
widgets = [
    (label, 0, 0),
    (button, 0, 1),
    (entry, 1, 0),
    (checkbutton, 1, 1),
    (radiobutton, 2, 0),
    (listbox, 2, 1)
]

for widget, row, column in widgets:
    widget.grid(row=row, column=column, padx=10, pady=10)

# Run the application
root.mainloop()

'''


mainloop()
