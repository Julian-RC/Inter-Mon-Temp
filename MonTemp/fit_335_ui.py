# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fit_335.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fit_335(object):
    def setupUi(self, fit_335):
        fit_335.setObjectName("fit_335")
        fit_335.resize(756, 87)
        self.select = QtWidgets.QToolButton(fit_335)
        self.select.setGeometry(QtCore.QRect(720, 20, 28, 22))
        self.select.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.select.setObjectName("select")
        self.file = QtWidgets.QLineEdit(fit_335)
        self.file.setGeometry(QtCore.QRect(60, 20, 651, 23))
        self.file.setReadOnly(True)
        self.file.setObjectName("file")
        self.fit = QtWidgets.QPushButton(fit_335)
        self.fit.setGeometry(QtCore.QRect(370, 50, 80, 23))
        self.fit.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"font: 12pt \"Sans Serif\";")
        self.fit.setObjectName("fit")
        self.label = QtWidgets.QLabel(fit_335)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label.setObjectName("label")

        self.retranslateUi(fit_335)
        QtCore.QMetaObject.connectSlotsByName(fit_335)

    def retranslateUi(self, fit_335):
        _translate = QtCore.QCoreApplication.translate
        fit_335.setWindowTitle(_translate("fit_335", "Dialog"))
        self.select.setText(_translate("fit_335", "..."))
        self.fit.setText(_translate("fit_335", "Fit"))
        self.label.setText(_translate("fit_335", "<html><head/><body><p><span style=\" font-size:16pt;\">File:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fit_335 = QtWidgets.QDialog()
    ui = Ui_fit_335()
    ui.setupUi(fit_335)
    fit_335.show()
    sys.exit(app.exec_())

