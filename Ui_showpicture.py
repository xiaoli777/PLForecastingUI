# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\Eric6Save\PLForecastingUI\showpicture.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, project_name):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 750)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Power.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.bnt1 = QtWidgets.QPushButton(Dialog)
        self.bnt1.setGeometry(QtCore.QRect(200, 30, 200, 60))
        self.bnt1.setObjectName("bnt1")
        self.bnt2 = QtWidgets.QPushButton(Dialog)
        self.bnt2.setGeometry(QtCore.QRect(500, 30, 200, 60))
        self.bnt2.setObjectName("bnt2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 120, 800, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "结果分析"))
        self.bnt1.setText(_translate("Dialog", "误差趋势图"))
        self.bnt2.setText(_translate("Dialog", "预测结果图"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, "big.jpg")
    Dialog.show()
    sys.exit(app.exec_())

