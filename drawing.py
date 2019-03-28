import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *



class Simple_drawing_window(QWidget):
    def __init__ (self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")



    def paintEvent(self, e):
        pass

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()


    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())