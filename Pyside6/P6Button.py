from PySide6.QtWidgets import  QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button holder App")
        button = QPushButton("Press me")
        ## set our button as central widget
        self.setCentralWidget(button)
