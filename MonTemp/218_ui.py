# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '218.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Segunda(object):
    def setupUi(self, Segunda):
        Segunda.setObjectName("Segunda")
        Segunda.resize(480, 330)
        self.buttonBox = QtWidgets.QDialogButtonBox(Segunda)
        self.buttonBox.setGeometry(QtCore.QRect(10, 300, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Segunda)
        self.buttonBox.accepted.connect(Segunda.accept)
        self.buttonBox.rejected.connect(Segunda.reject)
        QtCore.QMetaObject.connectSlotsByName(Segunda)

    def retranslateUi(self, Segunda):
        _translate = QtCore.QCoreApplication.translate
        Segunda.setWindowTitle(_translate("Segunda", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Segunda = QtWidgets.QDialog()
    ui = Ui_Segunda()
    ui.setupUi(Segunda)
    Segunda.show()
    sys.exit(app.exec_())

