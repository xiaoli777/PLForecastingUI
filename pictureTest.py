#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程

在这个例子中，我们显示窗口上的图像。

作者：我的世界你曾经来过
博客：http://blog.csdn.net/weiaitaowang
最后编辑：2016年8月4日
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap('PLerrorhistory2005.png')

        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)

        hbox.addWidget(lb1)
        self.setLayout(hbox)

        self.move(300, 300)
        self.setWindowTitle('像素图控件')        
        self.show()

    def showDate(self, date):

        self.lb1.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
