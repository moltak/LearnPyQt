#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class SolarWindow(QtGui.QWidget):
    def __init__(self):
        super(SolarWindow, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Solar System')
        self.fullScreen()
        self.show()

    def fullScreen(self):
        fg = self.frameGeometry()
        rect = QtGui.QDesktopWidget().availableGeometry()
        center = rect.center()
        fg.moveCenter(center)
        self.move(fg.topLeft())
        self.resize(rect.width(), rect.height())

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        qp.begin(self)
        brush = QtGui.QBrush()
        self.drawSun(qp, brush)
        qp.end()

    def drawSun(self, qp, brush):
        brush.setStyle(QtCore.Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawArc(240, 250, 100, 100, 0, 0)

    def drawMercury(self, qp, brush):
        brush.setStyle(QtCore.Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawArc(500, 500, 100, 100, 0, 0)

# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

def main():
    app = QtGui.QApplication(sys.argv)
    w = SolarWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()