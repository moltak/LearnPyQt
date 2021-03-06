#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUi()

    def initUi(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.resize(400, 320)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()