#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    txt = 0

    def __init__(self):
        super(Example, self).__init__()

        self.initUi()

    def initUi(self):
        vbox = QtGui.QVBoxLayout()
        self.txt = QtGui.QTextBrowser()
        vbox.addWidget(self.txt)

        self.setLayout(vbox)
        self.setWindowTitle('reimplementing Event Hander')
        self.resize(400, 320)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        else:
            self.txt.setText(str(e.key()))


def main():
    app = QtGui.QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()