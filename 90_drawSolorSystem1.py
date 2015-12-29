#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class SolarWindow(QWidget):
    def __init__(self):
        super(SolarWindow, self).__init__()
        self.pen = QPen(Qt.SolidLine)
        self.qp = QPainter(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Solar System')
        self.fullScreen()
        self.show()

    def fullScreen(self):
        fg = self.frameGeometry()
        self.rect = rect = QDesktopWidget().availableGeometry()
        center = rect.center()
        fg.moveCenter(center)
        self.move(fg.topLeft())
        self.resize(rect.width(), rect.height())

    def paintEvent(self, e):
        self.qp.begin(self)
        self.drawSun()
        self.drawMercury()
        self.qp.end()

    def drawSun(self):
        b = QImage("./solorSystemPlanet/sun.png")
        center = self.rect.center()
        self.qp.drawImage(center.x() - b.width() / 2, center.y() - b.height() / 2, b)

    def drawMercury(self):
        self.qp.setPen(self.pen)
        center = self.rect.center()
        self.qp.drawEllipse(center.x() - 100, center.y() - 100, 200, 200)


# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

def main():
    app = QApplication(sys.argv)
    w = SolarWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
