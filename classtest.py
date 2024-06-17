import tkinter as tk
from tkinter import ttk, Label, Button, Frame
#==================================================================#

def PopulateScreen(self ):
    mainframe = Frame()
    master = self
    master.title("A simple GUI")
    master.minsize(400, 190)
    master.configure(bg='yellow')
    self.label = Label(master, text="This is our first GUI!", bg='yellow')
    self.label.pack()

    self.greet_button = Button(master, text="Greet", command=self.greet, width = 10, height=1, bg='lightgreen')
    self.greet_button.place(x=180, y=30)

    self.close_button = Button(master, text="Close", command=master.quit, width = 10, height=1, bg='#dd0000', fg='white')
    self.close_button.place(x=180, y=70)

    self.messagelabel = Label(master, text='Hit "Greet"', bg='green', fg='white', width=50)
    self.messagelabel.place(x=20,y=110 )
#==================================================================#
#==========================================#
###   MAIN ENTRY POINT FOR CLASSTEST.PY
#==========================================#
class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.master = master
        PopulateScreen(self)

    def greet(self):
        self.master.messagelabel.text="Greetings!"
#==========================================#
###   MAIN ENTRY POINT FOR CLASSTEST.PY
#==========================================#

#root = tk()
# get instance of the 1 & only class
#gui = windows()
print(windows)
self.mainloop()
