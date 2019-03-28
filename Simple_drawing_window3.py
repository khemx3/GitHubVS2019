import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window3(QWidget):
    def __init__ (self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")


    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        

        p.setPen(QColor(127, 127, 0))
        p.setBrush(QColor(150, 127, 127))
        p.drawLine(20, 240, 180, 250)
        p.drawLine(20,240,120,50)
        p.drawLine(120,50,180,250)
        p.drawRect(20, 240, 155, 250)
        #p.fillRect(20,240,160,100, qRed)

        

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        #p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        
        
        

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

