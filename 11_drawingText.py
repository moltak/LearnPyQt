#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Exmaple(QtGui.QWidget):
    def __init__(self):
        super(Exmaple, self).__init__()

        self.initUi()

    def initUi(self):
        self.text = u'파이큐티 꽤 재밌넹'
        self.setWindowTitle('Drawing Text')
        self.resize(400, 320)
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(e, qp)
        qp.end()

    def drawText(self, e, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative, 10'))
        qp.drawText(e.rect(), QtCore.Qt.AlignCenter, self.text)


def main():
    app = QtGui.QApplication(sys.argv)
    e = Exmaple()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()