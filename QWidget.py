from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.echoGroup = QGroupBox('Echo')
        self.echoLabel = QLabel('Mode:')
        self.echoComboBox = QComboBox()
        self.echoComboBox.addItem('Normal')
        self.echoComboBox.addItem('Password')
        self.echoComboBox.addItem('PasswordEchoOnEdit')
        self.echoComboBox.addItem('No Echo')
        self.echoLineEdit = QLineEdit()
        self.echoLineEdit.setPlaceholderText('Placeholder Text')
        self.echoLineEdit.setFocus()

        self.validatorGroup = QGroupBox('Validator')
        self.validatorLabel = QLabel('Type:')
        self.validatorComboBox = QComboBox()
        self.validatorComboBox.addItem('No validator')
        self.validatorComboBox.addItem('Integer validator')
        self.validatorComboBox.addItem('Double validator')
        self.validatorLineEdit = QLineEdit()
        self.validatorLineEdit.setPlaceholderText('Placeholder Text')

        self.alignmentGroup = QGroupBox('Alignment')
        self.alignmentLabel = QLabel('Type:')
        self.alignmentComboBox = QComboBox()
        self.alignmentComboBox.addItem('Left')
        self.alignmentComboBox.addItem('Centered')
        self.alignmentComboBox.addItem('Right')
        self.alignmentLineEdit = QLineEdit()
        self.alignmentLineEdit.setPlaceholderText('Placeholder Text')

        self.inputMaskGroup = QGroupBox('Input mask')
        self.inputMaskLabel = QLabel('Type:')
        self.inputMaskComboBox = QComboBox()
        self.inputMaskComboBox.addItem('No mask')
        self.inputMaskComboBox.addItem('Phone number')
        self.inputMaskComboBox.addItem('ISO date')
        self.inputMaskComboBox.addItem('License key')
        self.inputMaskLineEdit = QLineEdit()
        self.inputMaskLineEdit.setPlaceholderText('Placeholder Text')

        self.accessGroup = QGroupBox('Access')
        self.accessLabel = QLabel('Read-only:')
        self.accessComboBox = QComboBox()
        self.accessComboBox.addItem('False')
        self.accessComboBox.addItem('True')
        self.accessLineEdit = QLineEdit()
        self.accessLineEdit.setPlaceholderText('Placeholder Text')

        self.echoComboBox.activated.connect(self.echoChanged)
        self.validatorComboBox.activated.connect(self.validatorChanged)
        self.alignmentComboBox.activated.connect(self.alignmentChanged)
        self.inputMaskComboBox.activated.connect(self.inputMaskChanged)
        self.accessComboBox.activated.connect(self.accessChanged)

        self.echoLayout = QGridLayout()
        self.echoLayout.addWidget(self.echoLabel, 0, 0)
        self.echoLayout.addWidget(self.echoComboBox, 0, 1)
        self.echoLayout.addWidget(self.echoLineEdit, 1, 0, 1, 2)
        self.echoGroup.setLayout(self.echoLayout)

        self.validatorLayout = QGridLayout()
        self.validatorLayout.addWidget(self.validatorLabel, 0, 0)
        self.validatorLayout.addWidget(self.validatorComboBox, 0, 1)
        self.validatorLayout.addWidget(self.validatorLineEdit, 1, 0, 1, 2)
        self.validatorGroup.setLayout(self.validatorLayout)

        self.alignmentLayout = QGridLayout()
        self.alignmentLayout.addWidget(self.alignmentLabel, 0, 0)
        self.alignmentLayout.addWidget(self.alignmentComboBox, 0, 1)
        self.alignmentLayout.addWidget(self.alignmentLineEdit, 1, 0, 1, 2)
        self.alignmentGroup.setLayout(self.alignmentLayout)

        self.inputMaskLayout = QGridLayout()
        self.inputMaskLayout.addWidget(self.inputMaskLabel, 0, 0)
        self.inputMaskLayout.addWidget(self.inputMaskComboBox, 0, 1)
        self.inputMaskLayout.addWidget(self.inputMaskLineEdit, 1, 0, 1, 2)
        self.inputMaskGroup.setLayout(self.inputMaskLayout)

        self.accessLayout = QGridLayout()
        self.accessLayout.addWidget(self.accessLabel, 0, 0)
        self.accessLayout.addWidget(self.accessComboBox, 0, 1)
        self.accessLayout.addWidget(self.accessLineEdit, 1, 0, 1, 2)
        self.accessGroup.setLayout(self.accessLayout)

        self.Layout = QGridLayout()
        self.Layout.addWidget(self.echoGroup, 0, 0)
        self.Layout.addWidget(self.validatorGroup, 1, 0)
        self.Layout.addWidget(self.alignmentGroup, 2, 0)
        self.Layout.addWidget(self.inputMaskGroup, 0, 1)
        self.Layout.addWidget(self.accessGroup, 1, 1)
        self.setLayout(self.Layout)

        self.setWindowTitle('Line Edits')

    def echoChanged(self, index):
        if index == 0:
            self.echoLineEdit.setEchoMode(QLineEdit.Normal)
        elif index == 1:
            self.echoLineEdit.setEchoMode(QLineEdit.Password)
        elif index == 2:
            self.echoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        elif index == 3:
            self.echoLineEdit.setEchoMode(QLineEdit.NoEcho)

    def validatorChanged(self, index):
        if index == 0:
            self.validatorLineEdit.setValidator(0)
        elif index == 1:
            self.validatorLineEdit.setValidator(QIntValidator(self.validatorLineEdit))
        elif index == 2:
            self.validatorLineEdit.setValidator(QDoubleValidator(-999.0, 999.0, 2, self.validatorLineEdit))

        self.validatorLineEdit.clear()

    def alignmentChanged(self, index):
        if index == 0:
            self.alignmentLineEdit.setAlignment(Qt.AlignLeft)
        elif index == 1:
            self.alignmentLineEdit.setAlignment(Qt.AlignCenter)
        elif index == 2:
            self.alignmentLineEdit.setAlignment(Qt.AlignRight)

    def inputMaskChanged(self, index):
        if index == 0:
            self.inputMaskLineEdit.setInputMask('')
        elif index == 1:
            self.inputMaskLineEdit.setInputMask('+99 99 99 99 99;_')
        elif index == 2:
            self.inputMaskLineEdit.setInputMask('0000-00-00')
            self.inputMaskLineEdit.setText('00000000')
            self.inputMaskLineEdit.setCursorPosition(0)
        elif index == 3:
            self.inputMaskLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

    def accessChanged(self, index):
        if index == 0:
            self.accessLineEdit.setReadOnly(False)
        elif index == 1:
            self.accessLineEdit.setReadOnly(True)


app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()
