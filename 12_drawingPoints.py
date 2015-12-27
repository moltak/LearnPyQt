#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('DrawingPoints')
        self.resize(400, 320)
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

def main():
    app = QtGui.QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()