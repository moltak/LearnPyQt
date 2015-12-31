#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
key doc -  Kepler's laws of planetary motion
https://ko.wikipedia.org/wiki/%EC%BC%80%ED%94%8C%EB%9F%AC%EC%9D%98_%ED%96%89%EC%84%B1%EC%9A%B4%EB%8F%99%EB%B2%95%EC%B9%99

key doc2 - pyqt4
http://zetcode.com/gui/pyqt4/
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import astropy

class SolarWindow(QWidget):
    def __init__(self):
        super(SolarWindow, self).__init__()
        self.pen = QPen(Qt.DashDotLine)
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
        print('paintEvent')
        self.qp.begin(self)
        self.drawSun()
        self.drawMercury()
        self.qp.end()

    def drawSun(self):
        b = QImage("./solorSystemPlanet/sun.png")
        center = self.rect.center()
        size = 40
        br = QRect(center.x() - size / 2, center.y() - size / 2, size, size)
        self.qp.drawImage(br, b)

    def drawMercury(self):
        self.pen.setColor(QColor.fromRgb(0xffb976))
        self.qp.setPen(self.pen)
        center = self.rect.center()
        # 중심점 찾기.(초점 이해하기)
        # 이심율 구하기 - width, height 만들기
        # drawEllipse 하기.
        self.qp.drawEllipse(center.x() - 100, center.y() - 100, 200, 200)


# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

def main():
    app = QApplication(sys.argv)
    w = SolarWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
