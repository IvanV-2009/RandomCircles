from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import QPointF
from random import randint, randrange
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.draw_flag = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.button = QPushButton('Нарисовать', self)
        self.button.move(20, 20)
        self.button.resize(80, 20)
        self.button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if self.draw_flag:
            painter = QPainter(self)
            painter.begin(self)
            painter.setBrush(QColor('yellow'))
            r = randint(20, 100)
            x, y = randrange(100, 500), randrange(100, 500)
            painter.drawEllipse(QPointF(x, y), r, r)
            painter.end()
            self.draw_flag = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
