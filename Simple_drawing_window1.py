import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__ (self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        p.setBrush(Qt.white)
        p.drawRect(e.rect())
        # for circle make the ellipse radii match
        radx = 100
        rady = 100
        # draw red circles
        p.setPen(Qt.red)
        for k in range(125, 220, 10):
            center = QPoint(k, k)
            # optionally fill each circle yellow
            p.setBrush(Qt.yellow)
            p.drawEllipse(center, radx, rady)
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

