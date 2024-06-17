import tkinter as tk
import string
from PIL import Image, ImageTk
'''
This script creates a windoiw containing 4 rows and 
    3 columns with a mix of widget controls, where the 
    listbox using 2 RH volumns in bottom row.
All cells  resize roughly equally witrh window resizing
'''
# Create the main window
master = tk.Tk()
master.title("4x3 Grid Layout with mixed & Different Widgets")

master.geometry(f'200x400')
master.minsize(500, 300)
master.configure(bg='lightgrey')

#======================================================================
#Add a listbox + scrollbar to bottom (fourth) row, right hand 2 columns
#======================================================================
choicesvar = tk.StringVar()
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
choicesvar = tk.StringVar(value=choices)
# create a scrollbar
scrollY = tk.Scrollbar(master)
# create the listbox
lbox1 = tk.Listbox(master, listvariable=choicesvar,height=10,
           width=5, font='comicsans, 12', fg='black', bg='cyan',
           highlightbackground='cyan', bd=2)

# tie  the scrollbar to the listbox
lbox1['yscrollcommand'] = scrollY.set
lbox1.configure(yscrollcommand=scrollY.set)
# attach the scrollbar to the listbox
scrollY.configure(command=lbox1.yview)
scrollY.configure(width=17)

#=======================================================
# Define the widgets to be placed in each of the cells
#=======================================================
masterlabel = tk.Label(master, text="This is the master row\n it goes on\nand on.........\nand on.........\nand on.........\nand on.........\n",height=8)
label = tk.Label(master, text="This is a Label", height=2, padx=3, pady=3)
label1 = tk.Label(master, text="This is a Label 1", height=1, width=3, padx=3, pady=3)
label2 = tk.Label(master, text="This is a Label 2", height=1, width=3, padx=3, pady=3)
button = tk.Button(master, text="Click Me", height=3, padx=3, pady=3, bg='yellow')
button2 = tk.Button(master, text="Button2", height=3, padx=3, pady=3, bg='yellow')
button3 = tk.Button(master, text="Button 3", height=3, padx=3, pady=3, bg='lightblue')
mbutton1 = tk.Button(master, text="menu 1", height=13, width=15, bg='green', font='comicsans, 14')
mbutton2 = tk.Button(master, text="menu 2", height=13, width=15, bg='purple', fg='white', font='comicsans, 14')
mbutton3 = tk.Button(master, text="menu 3", height=13, width=15, bg='red', fg='white', font='comicsans, 14')
mbutton4 = tk.Button(master, text="menu 4", height=13, width=15, bg='orange', fg='black', font='comicsans, 14')
entry = tk.Entry()
checkbutton = tk.Checkbutton(master, text="Check Me", height=3, padx=3, pady=3)
radiobutton = tk.Radiobutton(master, text="Option 1", height=3, padx=3, pady=3)
radiobutton2 = tk.Radiobutton(master, text="Option 2", height=3, padx=3, pady=3)
# create the listbox
lbox1 = tk.Listbox(master, listvariable=choicesvar,
        font='comicsans, 11', fg='black', bg='cyan',
        highlightbackground='cyan', bd=2,height=5, width=10)
#frame1= tk.Frame(lbox1, height=10, width=30, padx=3, pady=3)

#=======================================================
widgets =  [
    #row 0      row,col,cspan,rspan'''
    (mbutton1,      0, 0, 1, 1),
    (label1,        0, 1, 1, 1),      # label widget in the seondc column
    (button2,       0, 2, 1, 1),      # label widget in the second and  third ccolumns
    # row 1
    (mbutton2,      1, 0, 1, 1),
    (checkbutton,   1, 1, 1, 1),      # label widget in the seondc column
    (label2,        1, 2, 1, 1),      # label widget in the second and  third ccolumns
    #row 2
    (mbutton3,      2, 0, 1, 1),      # bbutton widget in the second row, second column & Spans 2 columns
    (masterlabel,   2, 1, 1, 1),      # label widget in the seconf ond row, second column & Spans 2 columns
    (label,         2, 2, 1, 1),      # label widget in the seconf ond row, second column & Spans 2 columns
    # row 3
    (mbutton4,      3, 0, 1, 1),
    (lbox1,         3, 1, 2, 1)       # listbox spans col 2 & 3
#    (lbox1,         3, 2, 1, 1)      # label widget in the seconf ond row, second column & Spans 2 columns
]
# Add some items for the listbox
#=======================================================
''' row,col,colspan,rowspan
buttons = [
        (mbutton1, 1, 0),
        (mbutton2, 2, 0),
        (mbutton3, 3, 1),
        (mbutton4, 4, 1)
]
'''
#==================================================================
# Arrange the widgets in a grid with three rows, with row1 being fixed width
# Place widgets in the grid with the specified columnspan
#==================================================================
for widget, row, column, colspan, rowspan in widgets:
    if column == 0:
        widget.grid(row=row, column=column, columnspan=colspan, padx=2, pady=2, sticky="nsew")
    else:
        widget.grid(row=row, column=column, columnspan=colspan,  padx=2, pady=2, sticky="nsew")

# Configure the grid to make the cells resizable
for i in range(4):
    if i == 3:
        master.rowconfigure(i, weight=2)
    else:
        master.rowconfigure(i, weight=6)
    for j in range(0,3):
        if j == 0:
            master.columnconfigure(j, weight=0)
        else:
            master.columnconfigure(j, weight=1)

#for button, row, column, colspan, rowspan in widgets:
#    widget.grid(row=row, column=column, columnspan=colspan, rowspan=rowspan, padx=2, pady=2,sticky="nsw")

#=======================================================
# Run the application
#=======================================================
if __name__ == '__main__':
    master.mainloop()
