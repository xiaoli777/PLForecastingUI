import sys
import os
import new
import forecasting
import openpicture

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QDesktopWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.CreateFileMenu()
        self.CreateEditMenu()
        self.CreateToolMenu()

        self.setGeometry(300, 300, 450, 0) 
        self.center()
        self.setWindowTitle('电力负荷预测系统') 
        self.setWindowIcon(QIcon('Power.jpg'))
        self.show()

    def CreateFileMenu(self):
        NewAction = QAction(QIcon('New.jpg'), '&新建', self, triggered = self.newaction)
        NewAction.setShortcut('Ctrl+N')
        NewAction.setStatusTip('新建模拟图表')

        ForecastAction = QAction(QIcon('forecast.jpeg'), '&预测', self, triggered = self.forecastaction)
        ForecastAction.setShortcut('Ctrl+F')
        ForecastAction.setStatusTip('未来负荷预测')

        OpenAction = QAction(QIcon('Open.jpg'), '&打开', self, triggered = self.openaction)
        OpenAction.setShortcut('Ctrl+O')
        OpenAction.setStatusTip('打开数据图表')

        DataMiningAction = QAction(QIcon('DataMining.jpg'), '&数据挖掘', self)
        DataMiningAction.setShortcut('Ctrl+M')
        DataMiningAction.setStatusTip('挖掘隐藏信息')

        exitAction = QAction(QIcon('close.jpg'), '&退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(self.close)

        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(NewAction)
        fileMenu.addAction(ForecastAction)
        fileMenu.addAction(DataMiningAction)
        fileMenu.addAction(OpenAction)
        fileMenu.addAction(exitAction)
        
        self.toolbar = self.addToolBar('文件')
        self.toolbar.addAction(NewAction)
        self.toolbar.addAction(ForecastAction)
        self.toolbar.addAction(DataMiningAction)
        self.toolbar.addAction(OpenAction)
        self.toolbar.addAction(exitAction)

    def CreateEditMenu(self):
        CopyAction = QAction(QIcon('Copy.jpg'), '&复制', self, triggered = self.findaction)
        CopyAction.setShortcut('Ctrl+C')
        CopyAction.setStatusTip('复制数据图表')
        
        DeleteAction = QAction(QIcon('Delete.jpg'), '&清除', self, triggered = self.findaction)
        DeleteAction.setStatusTip('清除数据图表')
        
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&编辑')
        fileMenu.addAction(CopyAction)
        fileMenu.addAction(DeleteAction)
        
        self.toolbar = self.addToolBar('编辑')
        self.toolbar.addAction(CopyAction)
        self.toolbar.addAction(DeleteAction)
        
    def CreateToolMenu(self):
        BigAction = QAction(QIcon('big.jpg'), '&放大', self)
        BigAction.setStatusTip('放大图表')
        
        SmallAction = QAction(QIcon('small.jpg'), '&缩小', self)
        SmallAction.setStatusTip('缩小图表')
        
        FindAction = QAction(QIcon('Find.jpg'), '&查找', self, triggered = self.findaction)
        FindAction.setShortcut('Ctrl+F')
        FindAction.setStatusTip('查找数据图表')
        
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&工具')
        fileMenu.addAction(BigAction)
        fileMenu.addAction(SmallAction)
        fileMenu.addAction(FindAction)
        
        self.toolbar = self.addToolBar('工具')
        self.toolbar.addAction(BigAction)
        self.toolbar.addAction(SmallAction)
        self.toolbar.addAction(FindAction)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def newaction(self):
        newWindow = new.New()
        newWindow.show()
        newWindow.exec_()
    
    def forecastaction(self):
        foreWindow = forecasting.Forecasting()
        foreWindow.show()
        foreWindow.exec_()
    
    def openaction(self):
        filePosition, filetype = QFileDialog.getOpenFileName(self,  "打开文件",  "D:\\Work\\Eric6Save\\PLForecastingUI\\SAVE",  "PNG(*.png);;JPG(*.jpg);;TXT(*.txt)")   #设置文件扩展名过滤,注意用双分号间隔  
        SelectedFileType = ""
        if filePosition != "":
            i, j = 0, 0
            fileName = ""
            for c in filePosition:
                if c == "/":
                    fileName = filePosition[i + 1:]
                i = i + 1
            for c in fileName:
                if c == ".":
                    SelectedFileType = fileName[j+1:]
                j = j + 1
            openWindow = openpicture.Open(fileName,SelectedFileType)
            openWindow.show()
            #openWindow.exec_()
            print(filePosition, fileName, SelectedFileType)
    
    def findaction(self):
        start_directory="D:\\Work\\Eric6Save\\PLForecastingUI\\SAVE"
        os.system("explorer.exe %s" % start_directory)
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '信息', '确认退出吗？', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
