import tkinter as Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# this WORKS and shows a complex graphic !!! 3/6/24
class Model():

    def __init__(self):
        self.xpoint = 200
        self.ypoint = 200
        self.res = None

    def calculate(self):
        x, y = np.meshgrid(np.linspace(-5, 5, self.xpoint),
                           np.linspace(-5, 5, self.ypoint))
        z = np.cos(x ** 2 * y ** 3)
        self.res = {"x": x, "y": y, "z": z}


class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.fig = Figure(figsize=(7.5, 4), dpi=80)
        self.ax0 = self.fig.add_axes(
            (0.05, .05, .90, .90), facecolor=(.75, .75, .75), frameon=False)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel = SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.draw()


class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        #self.frame2.place(x=120, y = 20)
        self.plotBut = Tk.Button(self.frame2, text="Plot ", width = 13, bg='lightgreen', fg='black')
        #self.plotBut.pack(side="top", fill=Tk.BOTH)
        self.plotBut.place(x = 5, y = 20)
        self.clearButton = Tk.Button(self.frame2, text="Clear", width=13, bg='lightcyan', fg='black')
        # self.clearButton.pack(side="top", fill=Tk.BOTH)
        self.clearButton.place(x=5, y=50)
        self.closeButton = Tk.Button(self.frame2, text="Close", width = 13, bg='red', fg='white')
        #self.clearButton.pack(side="top", fill=Tk.BOTH)
        self.closeButton.place(x = 5, y = 80)


class Controller():
    def close(self, event):
        self.exit()

    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.sidepanel.plotBut.bind("<Button>", self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>", self.clear)
        self.view.sidepanel.closeButton.bind("<Button>", self.close)

    def run(self):
        self.root.title("Tkinter MVC graphing example")
        self.root.deiconify()
        self.root.mainloop()

    def clear(self, event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()


    def my_plot(self, event):
        self.model.calculate()
        self.view.ax0.clear()
        self.view.ax0.contourf(self.model.res["x"], self.model.res["y"], self.model.res["z"])
        self.view.fig.canvas.draw()


if __name__ == '__main__':
    c = Controller()
    c.run()
