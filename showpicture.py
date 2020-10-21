import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from Ui_showpicture import Ui_Dialog

class showpicture(QDialog, Ui_Dialog):
    project = ""
    
    def __init__(self, project_name, parent=None):
        self.project = project_name
        super(showpicture, self).__init__(parent)
        self.setupUi(self, project_name)
    
    def on_bnt1_clicked(self):
        pixmap = QPixmap('Save\\' + self.project + ' PLerrorhistory.png')
        self.label.setPixmap(pixmap)
        self.setWindowTitle(self.project + '电力负荷历史误差')
    
    def on_bnt2_clicked(self):
        pixmap = QPixmap('Save\\' + self.project + ' PLsimulation.png')
        self.label.setPixmap(pixmap)
        self.setWindowTitle(self.project + '电力负荷预测分析')
    
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = showpicture("test_1")
    sp.show()
    sys.exit(app.exec_()) 
