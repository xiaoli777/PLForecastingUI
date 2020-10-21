import sys
import showpicture
import BPpower2005
#import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog , QApplication, QMessageBox

from Ui_New import Ui_Dialog_ChooseFile

class New(QDialog, Ui_Dialog_ChooseFile):
    status = 1
    state = 1
    def __init__(self, parent=None):
        super(New, self).__init__(parent)
        self.setupUi(self)
    
    def on_Button_ok_clicked(self):
        while self.status:
            if self.state == 1:
                start = self.dateTimeEdit_Start.dateTime()
                end = self.dateTimeEdit_End.dateTime()
                project_name = self.lineEdit_ProjectName.text()
                forecastalgorithm = self.comboBox_Forecasting.currentText()
                dateset = self.comboBox_dateset.currentText()
                print(project_name, forecastalgorithm, dateset)
                print(int(start.toString("yyyy")),int(start.toString("MM")), int(start.toString("dd")))   #yyyy-MM-dd hh:mm:ss ddd
                startDate = [int(start.toString("yyyy")),int(start.toString("MM")), int(start.toString("dd"))]
                endDate = [int(end.toString("yyyy")),int(end.toString("MM")), int(end.toString("dd"))]
                startDays = self.CalDays(startDate)
                endDays = self.CalDays(endDate)
                startDay = start.toString("yyyy") + "-" + start.toString("MM") + "-" + start.toString("dd")
                endDay = end.toString("yyyy") + "-" + end.toString("MM") + "-" + end.toString("dd")
                print(startDays, endDays, endDay, startDay)
                i = 0
                if self.checkBox_Weather.isChecked():
                    i = i + 1
                if self.checkBox_Holiday.isChecked():
                    i = i + 2
                if self.checkBox_Season.isChecked():
                    i = i + 4
                print(i)
                if  project_name == "":
                    self.state = 0
                    self.showDialog("项目名不能为空！")
                    break
                if startDays - endDays >= 0:
                    self.state = 0
                    self.showDialog("日期间隔必须为大于1的正数！")
                    break
                if i % 2 == 0:
                    self.state = 0
                    self.showDialog("请选择天气参数")
                    break
                if i == 0:
                    self.state = 0
                    self.showDialog("请选择预测参数")
                    break
                self.close()
                bp = BPpower2005.BP(project_name, startDay, endDay, i)
                bp.BP_test()
                #_thread.start_new_thread(BPpower2005.func,(project_name, startDay, endDay, i))
                #thread_test = threading.Thread(target = BPpower2005.func, args = (project_name, startDay, endDay, i), name = 'thread' + str(i))
                #thread_test.start()
                #thread_test.join()
                sp = showpicture.showpicture(project_name)
                sp.show()
                sp.exec_()
                self.status = 0
            else:
                self.state = 1
                break
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    
    def CalDays(self, date):
        result = (date[0] - 2005) * 365
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if date[0] % 400 == 0 or date[0] % 4 == 0 and date[0] % 100 != 0:
            month[1] = 29
        for m in range(date[1]):
            result = result + month[m]
        result = result + date[2]
        return result
    
    def showDialog(self, str):
        QMessageBox.information(self,"警告", str, QMessageBox.Yes, QMessageBox.Yes) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    new = New()
    new.show()
    sys.exit(app.exec_())
