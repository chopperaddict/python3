import sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton,\
                               QMenuBar, QToolBar, QStatusBar, QDockWidget, QToolBar,\
                                QSlider, QVBoxLayout
from P6Button import ButtonHolder
from PySide6.QtCore import Qt
from layoutTest import Layout1

# subcklass QMainWindow to cvustomise apps main window
App = QApplication(sys.argv)
#window = QMainWindow()
#window.show()
layout = Layout1()
layoutval = layout.geometry()
layout.show()

App.exec()
#App.destroyed
