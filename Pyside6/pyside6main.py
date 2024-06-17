# NB the Qt options are very much Case Sensitive !!!!
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore, QtWidgets, QtGui
from Buttonholder import ButtonHolder
import random
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
"""
App = QApplication(sys.argv)
Mainwindow = QWidget()
window = ButtonHolder()
#mainwindow.show()
window.show()
print(PySide6.__version__)
print(PySide6.QtCore.__version__)
widget = MyWidget()
widget.resize(800, 600)
widget.show()
App.exec()
App.destroy()
"""
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
