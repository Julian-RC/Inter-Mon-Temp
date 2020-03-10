# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_file.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plot_file(object):
    def setupUi(self, plot_file):
        plot_file.setObjectName("plot_file")
        plot_file.resize(557, 166)
        self.buttonBox = QtWidgets.QDialogButtonBox(plot_file)
        self.buttonBox.setGeometry(QtCore.QRect(180, 130, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.monitor = QtWidgets.QLineEdit(plot_file)
        self.monitor.setGeometry(QtCore.QRect(260, 90, 281, 23))
        self.monitor.setStyleSheet("font: 13pt \"Sans Serif\";")
        self.monitor.setObjectName("monitor")
        self.label = QtWidgets.QLabel(plot_file)
        self.label.setGeometry(QtCore.QRect(10, 60, 251, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(plot_file)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 251, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(plot_file)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_3.setObjectName("label_3")
        self.title = QtWidgets.QLineEdit(plot_file)
        self.title.setGeometry(QtCore.QRect(60, 20, 481, 23))
        self.title.setStyleSheet("font: 13pt \"Sans Serif\";")
        self.title.setObjectName("title")
        self.control = QtWidgets.QLineEdit(plot_file)
        self.control.setGeometry(QtCore.QRect(260, 60, 281, 23))
        self.control.setStyleSheet("font: 13pt \"Sans Serif\";")
        self.control.setObjectName("control")

        self.retranslateUi(plot_file)
        self.buttonBox.accepted.connect(plot_file.accept)
        self.buttonBox.rejected.connect(plot_file.reject)
        QtCore.QMetaObject.connectSlotsByName(plot_file)

    def retranslateUi(self, plot_file):
        _translate = QtCore.QCoreApplication.translate
        plot_file.setWindowTitle(_translate("plot_file", "Dialog"))
        self.label.setText(_translate("plot_file", "<html><head/><body><p><span style=\" font-size:14pt;\">Temperature Control 335:</span></p></body></html>"))
        self.label_2.setText(_translate("plot_file", "<html><head/><body><p><span style=\" font-size:14pt;\">Temperature Monitor 218:</span></p></body></html>"))
        self.label_3.setText(_translate("plot_file", "<html><head/><body><p><span style=\" font-size:14pt;\">Title:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    plot_file = QtWidgets.QDialog()
    ui = Ui_plot_file()
    ui.setupUi(plot_file)
    plot_file.show()
    sys.exit(app.exec_())

