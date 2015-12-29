#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class SolarWindow(QtGui.QWidget):
    def __init__(self):
        super(SolarWindow, self).__init__()
        self.pen = QtGui.QPen(QtCore.Qt.SolidLine)
        self.qp = QtGui.QPainter(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Solar System')
        self.fullScreen()
        self.show()

    def fullScreen(self):
        fg = self.frameGeometry()
        self.rect = rect = QtGui.QDesktopWidget().availableGeometry()
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
        self.pen.setColor(QtCore.Qt.red)
        self.qp.setPen(self.pen)
        center = self.rect.center()
        width = 50
        height = 50
        self.qp.drawEllipse(center.x() - width/2, center.y() - height/2, width, height)

    def drawMercury(self):
        self.qp.setPen(self.pen)
        self.qp.drawEllipse(100, 100, 50, 50)

# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

def main():
    app = QtGui.QApplication(sys.argv)
    w = SolarWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()