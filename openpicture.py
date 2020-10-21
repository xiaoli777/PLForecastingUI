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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  
from PyQt5.QtCore import * 
from PyQt5 import QtCore
import matplotlib.pyplot as plt

class Open(QDialog):
    def __init__(self, fileName, FileType):
        super().__init__()
        self.initUI(fileName, FileType)
        self.ctrlPressed=False

    def initUI(self, fileName, FileType):
        if FileType.lower() == "txt" :
            date = []
            dateselected = []
            sampleout = []
            networkout = []
            f=open("SAVE\\" + fileName,"r")
            for line in f.readlines():
                lineArr = line.strip().split('\t')
                date.append(str(lineArr[0]))
                sampleout.append(float(lineArr[1]))
                networkout.append(float(lineArr[2]))
            index = 0
            #对日期进行缩减
            for pl in date:
                if len(date) >= 10:
                    if index % 3 == 0:
                        pl = pl[5:]
                    else:
                        pl = ""
                    index = index + 1
                else:
                    pl = pl[5:]
                dateselected.append(pl) 
            f.close()
            #print(dateselected,sampleout, networkout)
            self.ShowDiagram(dateselected,sampleout, networkout)
        else:
            hbox = QHBoxLayout(self)
            self.imageLabel=QLabel()  
            self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)   
            self.imageLabel.setScaledContents(True)  
          
            #self.setCentralWidget(self.imageLabel)  
            self.image=QImage()  
            if self.image.load("SAVE\\" + fileName):
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
                self.resize(self.image.width(),self.image.height())          
            hbox.addWidget(self.imageLabel)
            self.setLayout(hbox)

            self.move(0, 0)
            self.setWindowTitle(fileName)
            self.setWindowIcon(QIcon('open.jpg'))        
            self.show()
            self.exec_()

    def ShowDiagram(self, ds, spout, nwout):
        plt.figure('电力负荷预测分析')
        ax=plt.gca()
        line1, = ax.plot(nwout,'k',marker = u'$\circ$')
        line2, = ax.plot(spout,'r',markeredgecolor='b',marker = u'$\star$',markersize=9)

        ax.legend((line1,line2),('simulation output','real output'),loc = 'upper left')

        yticks = range(0, 10000, 1000)
        ytickslabel = range(0, 10000, 1000)
        ax.set_yticks(yticks)
        ax.set_yticklabels(ytickslabel)
        ax.set_ylabel(u'Power Load')

        xticks = range(0,len(ds),1)
        xtickslabel = ds
        ax.set_xticks(xticks)
        ax.set_xticklabels(xtickslabel)
        ax.set_xlabel(u'Date')
        ax.set_title('Power Load Simulation')

        plt.ion()
        plt.title('PLsimulation')
        plt.grid(True)
        plt.show()
    
    def wheelEvent(self, event):
        if self.ctrlPressed:
            delta=event.angleDelta()
            oriention= delta.y()/8
            self.zoomsize=0
            if oriention>0:
                self.zoomsize+=1
                if self.image.isNull():  
                    return  
                martix = QTransform()  
                martix.scale(2,2)  
                self.image=self.image.transformed(martix);  
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
                self.resize(self.image.width(),self.image.height())   
            else:
                self.zoomsize-=1
                if self.image.isNull():  
                    return  
                martix = QTransform()   
                martix.scale(0.5,0.5)  
                self.image=self.image.transformed(martix);  
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
                self.resize(self.image.width(),self.image.height()) 
            print(self.zoomsize)
        else: 
          return super().wheelEvent(event)

    def keyReleaseEvent(self, QKeyEvent):
        if QKeyEvent.key()==QtCore.Qt.Key_Control:
            self.ctrlPressed=False
        return super().keyReleaseEvent(QKeyEvent)
        
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()
        if QKeyEvent.key()==QtCore.Qt.Key_Control:
            self.ctrlPressed=True
            print("The ctrl key is holding down")
        return super().keyPressEvent(QKeyEvent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    open = Open("big.jpg")
    open.show()
    sys.exit(app.exec_())
