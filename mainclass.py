# MAINCLASS.PY
# from tkinter import ttk
# from tkinter import ttkbootstrap
from StripApp import *
from StripMethods import *


# from    StripMethods import GetClass
# from    StripMethods import stripargsdata


class MainClass():

    def __init__(self, owner="StripChars", Activetkwindow=Tk, input="", mode=1, dbug=1):
        self.Activetkwindow = Activetkwindow
        self.owner = owner
        self.stripapp = None
        self.stripchars = None
        self.resultswin = None
        self.stringinput = input
        self.stringoriginal = input
        self.stringstripped = ""
        self.stringoutput = ""
        self.stripchars = ""
        self.stripmode = mode
        self.dbug = dbug
        DBUG = self.dbug
        self.UseMonitor = 0
        self.strippedenvnname = "STRIP_RESULT"
        self.inputenvnname = "STRIP_INPUT"
        self.minsize = []
        self.monitor1 = []
        self.monitor2 = []
        self.monitor3 = []
        self.mon1name = ""
        self.mon1array = []
        self.mon1height = 0
        self.mon1width = 0
        self.mon1isprimary = False
        self.mon2array = []
        self.mon2name = ""
        self.mon2height = 0
        self.mon2width = 0
        self.mon2isprimary = False
        self.mon3array = []
        self.mon3name = ""
        self.mon3height = 0
        self.mon3width = 0
        self.mon3isprimary = False
        # ============== END OF CLASS ================

    def getClass(self):
        # global data
        data = MainClass()
        return data

    # class stripargsdata():
    # Activetkwindow = Tk
    # stripwin = Tk
    # resultswin = Tk
    # dbgwin = Tk
    # outwincount = 0
    # owner = "StripChars"
    # argv = []
    # Proceed = True
    # InputWin = Tk
    # stringinput = ""
    # stringoutput = ""
    # stringoriginal = ""
    # stringstripped = ""
    # stripchars = ""
    # inputsize = []
    # outputsize = []
    # stripmode = 0
    # dbug = 0
    # charsremoved = 0
    # strippedenvnname = ""
    # inputenvnname = ""
    # minsize = []
    # monitor1 = []
    # monitor2 = []
    # monitor3 = []
    # mon1name = ""
    # mon1array = []
    # mon1height = 0
    # mon1width = 0
    # mon1isprimary = False
    # mon2array = []
    # mon2name = ""
    # mon2height = 0
    # mon2width = 0
    # mon2isprimary = False
    # mon3array = []
    # mon3name = ""
    # mon3height = 0
    # mon3width = 0
    # mon3isprimary = False


if __name__ == "__main__":
    print('in "if __'
          'name__ == __main__()')
    args = sys.argv[1:]
    mainclass = MainClass.getClass(MainClass)
    print(mainclass.Activetkwindow)
    stripinapp(MainClass, len(args), args)
