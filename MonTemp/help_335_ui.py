# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_335.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help_335(object):
    def setupUi(self, help_335):
        help_335.setObjectName("help_335")
        help_335.resize(480, 538)
        self.textEdit = QtWidgets.QTextEdit(help_335)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 461, 521))
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(help_335)
        QtCore.QMetaObject.connectSlotsByName(help_335)

    def retranslateUi(self, help_335):
        _translate = QtCore.QCoreApplication.translate
        help_335.setWindowTitle(_translate("help_335", "Dialog"))
        self.textEdit.setHtml(_translate("help_335", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Lakeshore</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Temperature Controller 335</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The Model 335 offers two standard sensor inputs that are compatible with diode and RTD temperature sensors.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Providing a total of 75 W of heater power, the Model 335 is the most powerful half rack temperature controller available. Designed to deliver very clean heater power, precise temperature control is ensured throughout your full scale temperature range for excellent measurement reliability, efficiency and throughput. Two independent PID control outputs can be configured to supply 50 W and 25 W or 75 W and 1 W of heater power. Precise control output is calculated based on your temperature setpoint and feedback from the control sensor. Wide tuning parameters accommodate most cryogenic cooling systems and many high-temperature ovens commonly used in laboratories.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">For more info go:</span><span style=\" font-size:12pt;\"> </span><a href=\"https://www.lakeshore.com/products/categories/overview/temperature-products/cryogenic-temperature-controllers/model-335-cryogenic-temperature-controller\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">https://www.lakeshore.com/products/categories/overview/temperature-products/cryogenic-temperature-controllers/model-335-cryogenic-temperature-controller</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_335 = QtWidgets.QDialog()
    ui = Ui_help_335()
    ui.setupUi(help_335)
    help_335.show()
    sys.exit(app.exec_())

