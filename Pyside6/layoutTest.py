import sys
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, \
    QMenuBar, QToolBar, QStatusBar, QDockWidget, QToolBar, \
    QSlider, QVBoxLayout, QHBoxLayout
from P6Button import ButtonHolder
from PySide6.QtCore import Qt

def btn_clicked(arg):
    print('Button  was clicked')

def slider_response(data):
    print (f"Slider set to {data}", data)

class Layout1(QWidget):
    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.setWindowTitle("Ians #1 window test")
        self.button1 = QPushButton("Press me")
        self.button2 = QPushButton("and press me")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(slider_response)
        #slider.show()
        self.slider.setMinimum(0)
        self.slider.setMaximum(200)
        self.slider.setValue(65)

        self.button1.clicked.connect(btn_clicked)
        #QWidget.height = 10
        self.widgetLayout = QVBoxLayout()
        self.widgetLayout.addWidget(self.button1)
        self.widgetLayout.addWidget(self.button2)
        self.widgetLayout.addWidget(self.slider)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)
        #self.layout.width = 600


if __name__ == "__main__":
    print('in "if __'
          'name__ == __main__()')
    args = sys.argv[1:]
    #layout= Layout1()
