# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'icon.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Icon(object):
    def setupUi(self, Icon):
        Icon.setObjectName("Icon")
        Icon.resize(436, 117)
        self.buttonBox = QtWidgets.QDialogButtonBox(Icon)
        self.buttonBox.setGeometry(QtCore.QRect(10, 80, 411, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.passwo = QtWidgets.QLineEdit(Icon)
        self.passwo.setGeometry(QtCore.QRect(10, 50, 411, 23))
        self.passwo.setReadOnly(False)
        self.passwo.setObjectName("passwo")
        self.label = QtWidgets.QLabel(Icon)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 21))
        self.label.setObjectName("label")
        self.buttonBox.raise_()
        self.label.raise_()
        self.passwo.raise_()

        self.retranslateUi(Icon)
        self.buttonBox.accepted.connect(Icon.accept)
        self.buttonBox.rejected.connect(Icon.reject)
        QtCore.QMetaObject.connectSlotsByName(Icon)

    def retranslateUi(self, Icon):
        _translate = QtCore.QCoreApplication.translate
        Icon.setWindowTitle(_translate("Icon", "Dialog"))
        self.label.setText(_translate("Icon", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Please enter the password sudo to create the icon</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Icon = QtWidgets.QDialog()
    ui = Ui_Icon()
    ui.setupUi(Icon)
    Icon.show()
    sys.exit(app.exec_())

