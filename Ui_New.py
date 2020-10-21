# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\Eric6Save\PLForecastingUI\New.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ChooseFile(object):
    def setupUi(self, Dialog_ChooseFile):
        Dialog_ChooseFile.setObjectName("Dialog_ChooseFile")
        Dialog_ChooseFile.resize(600, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("New.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_ChooseFile.setWindowIcon(icon)
        Dialog_ChooseFile.setSizeGripEnabled(True)
        self.Button_close = QtWidgets.QPushButton(Dialog_ChooseFile)
        self.Button_close.setGeometry(QtCore.QRect(470, 450, 100, 30))
        self.Button_close.setObjectName("Button_close")
        self.label_ProjectName = QtWidgets.QLabel(Dialog_ChooseFile)
        self.label_ProjectName.setGeometry(QtCore.QRect(50, 100, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_ProjectName.setFont(font)
        self.label_ProjectName.setObjectName("label_ProjectName")
        self.label_Title = QtWidgets.QLabel(Dialog_ChooseFile)
        self.label_Title.setGeometry(QtCore.QRect(175, 30, 261, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.lineEdit_ProjectName = QtWidgets.QLineEdit(Dialog_ChooseFile)
        self.lineEdit_ProjectName.setGeometry(QtCore.QRect(200, 100, 300, 31))
        self.lineEdit_ProjectName.setObjectName("lineEdit_ProjectName")
        self.label_Forecasting = QtWidgets.QLabel(Dialog_ChooseFile)
        self.label_Forecasting.setGeometry(QtCore.QRect(50, 160, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_Forecasting.setFont(font)
        self.label_Forecasting.setObjectName("label_Forecasting")
        self.comboBox_Forecasting = QtWidgets.QComboBox(Dialog_ChooseFile)
        self.comboBox_Forecasting.setGeometry(QtCore.QRect(280, 160, 150, 30))
        self.comboBox_Forecasting.setObjectName("comboBox_Forecasting")
        self.comboBox_Forecasting.addItem("")
        self.comboBox_Forecasting.addItem("")
        #self.comboBox_Forecasting.addItem("")
        self.label_DataSource = QtWidgets.QLabel(Dialog_ChooseFile)
        self.label_DataSource.setGeometry(QtCore.QRect(50, 220, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_DataSource.setFont(font)
        self.label_DataSource.setObjectName("label_DataSource")
        self.dateTimeEdit_Start = QtWidgets.QDateTimeEdit(Dialog_ChooseFile)
        self.dateTimeEdit_Start.setGeometry(QtCore.QRect(200, 285, 130, 20))
        self.dateTimeEdit_Start.setFrame(False)
        self.dateTimeEdit_Start.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit_Start.setDateTime(QtCore.QDateTime(QtCore.QDate(2005, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_Start.setDate(QtCore.QDate(2005, 1, 1))
        self.dateTimeEdit_Start.setTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit_Start.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_Start.setMaximumDate(QtCore.QDate(2007, 12, 31))
        self.dateTimeEdit_Start.setMinimumDate(QtCore.QDate(2005, 1, 1))
        self.dateTimeEdit_Start.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateTimeEdit_Start.setObjectName("dateTimeEdit_Start")
        self.label_TimeRange = QtWidgets.QLabel(Dialog_ChooseFile)
        self.label_TimeRange.setGeometry(QtCore.QRect(50, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_TimeRange.setFont(font)
        self.label_TimeRange.setObjectName("label_TimeRange")
        self.dateTimeEdit_End = QtWidgets.QDateTimeEdit(Dialog_ChooseFile)
        self.dateTimeEdit_End.setGeometry(QtCore.QRect(370, 285, 130, 20))
        self.dateTimeEdit_End.setFrame(False)
        self.dateTimeEdit_End.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit_End.setDateTime(QtCore.QDateTime(QtCore.QDate(2005, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_End.setDate(QtCore.QDate(2005, 1, 1))
        self.dateTimeEdit_End.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_End.setMaximumDate(QtCore.QDate(2007, 12, 31))
        self.dateTimeEdit_End.setMinimumDate(QtCore.QDate(2005, 1, 1))
        self.dateTimeEdit_End.setObjectName("dateTimeEdit_End")
        self.label_Paramter = QtWidgets.QLabel(Dialog_ChooseFile)
        self.label_Paramter.setGeometry(QtCore.QRect(50, 340, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_Paramter.setFont(font)
        self.label_Paramter.setObjectName("label_Paramter")
        self.checkBox_Weather = QtWidgets.QCheckBox(Dialog_ChooseFile)
        self.checkBox_Weather.setGeometry(QtCore.QRect(200, 345, 91, 19))
        self.checkBox_Weather.setChecked(True)
        self.checkBox_Weather.setObjectName("checkBox_Weather")
        self.checkBox_Holiday = QtWidgets.QCheckBox(Dialog_ChooseFile)
        self.checkBox_Holiday.setGeometry(QtCore.QRect(200, 390, 91, 19))
        self.checkBox_Holiday.setObjectName("checkBox_Holiday")
        self.checkBox_Season = QtWidgets.QCheckBox(Dialog_ChooseFile)
        self.checkBox_Season.setGeometry(QtCore.QRect(370, 345, 91, 19))
        self.checkBox_Season.setObjectName("checkBox_Season")
        self.comboBox_dateset = QtWidgets.QComboBox(Dialog_ChooseFile)
        self.comboBox_dateset.setGeometry(QtCore.QRect(280, 220, 150, 30))
        self.comboBox_dateset.setObjectName("comboBox_dateset")
        self.comboBox_dateset.addItem("")
        self.comboBox_dateset.addItem("")
        self.comboBox_dateset.addItem("")
        self.Button_ok = QtWidgets.QPushButton(Dialog_ChooseFile)
        self.Button_ok.setGeometry(QtCore.QRect(350, 450, 100, 30))
        self.Button_ok.setObjectName("Button_ok")

        self.retranslateUi(Dialog_ChooseFile)
        self.Button_close.clicked.connect(Dialog_ChooseFile.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ChooseFile)

    def retranslateUi(self, Dialog_ChooseFile):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ChooseFile.setWindowTitle(_translate("Dialog_ChooseFile", "新建"))
        self.Button_close.setText(_translate("Dialog_ChooseFile", "取消"))
        self.label_ProjectName.setText(_translate("Dialog_ChooseFile", "项   目   名："))
        self.label_Title.setText(_translate("Dialog_ChooseFile", "新建模拟数据"))
        self.label_Forecasting.setText(_translate("Dialog_ChooseFile", "机器学习："))
        self.comboBox_Forecasting.setItemText(0, _translate("Dialog_ChooseFile", "BP神经网络"))
        self.comboBox_Forecasting.setItemText(1, _translate("Dialog_ChooseFile", "遗传算法"))
        #self.comboBox_Forecasting.setItemText(2, _translate("Dialog_ChooseFile", "日日拓扑"))
        self.label_DataSource.setText(_translate("Dialog_ChooseFile", "数   据   源："))
        self.dateTimeEdit_Start.setDisplayFormat(_translate("Dialog_ChooseFile", "yyyy/M/d"))
        self.label_TimeRange.setText(_translate("Dialog_ChooseFile", "时间范围："))
        self.dateTimeEdit_End.setDisplayFormat(_translate("Dialog_ChooseFile", "yyyy/M/d"))
        self.label_Paramter.setText(_translate("Dialog_ChooseFile", "参数因子："))
        self.checkBox_Weather.setText(_translate("Dialog_ChooseFile", "天气"))
        self.checkBox_Holiday.setText(_translate("Dialog_ChooseFile", "节假日"))
        self.checkBox_Season.setText(_translate("Dialog_ChooseFile", "季节"))
        self.comboBox_dateset.setItemText(0, _translate("Dialog_ChooseFile", "DataSet2005"))
        self.comboBox_dateset.setItemText(1, _translate("Dialog_ChooseFile", "DataSet2006"))
        self.comboBox_dateset.setItemText(2, _translate("Dialog_ChooseFile", "DataSet2007"))
        self.comboBox_dateset.setItemText(3, _translate("Dialog_ChooseFile", "DataSet"))
        self.Button_ok.setText(_translate("Dialog_ChooseFile", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ChooseFile = QtWidgets.QDialog()
    ui = Ui_Dialog_ChooseFile()
    ui.setupUi(Dialog_ChooseFile)
    Dialog_ChooseFile.show()
    sys.exit(app.exec_())

