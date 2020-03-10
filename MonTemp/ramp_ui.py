# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ramp.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ramp(object):
    def setupUi(self, ramp):
        ramp.setObjectName("ramp")
        ramp.resize(281, 261)
        self.widget = QtWidgets.QWidget(ramp)
        self.widget.setGeometry(QtCore.QRect(0, 10, 281, 251))
        self.widget.setObjectName("widget")

        self.retranslateUi(ramp)
        QtCore.QMetaObject.connectSlotsByName(ramp)

    def retranslateUi(self, ramp):
        _translate = QtCore.QCoreApplication.translate
        ramp.setWindowTitle(_translate("ramp", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ramp = QtWidgets.QDialog()
    ui = Ui_ramp()
    ui.setupUi(ramp)
    ramp.show()
    sys.exit(app.exec_())

