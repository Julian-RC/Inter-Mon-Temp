# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 601)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(740, 40, 431, 513))
        self.frame_5.setStyleSheet("background-color: rgb(48, 176, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(100, 10, 261, 31))
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_5)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 401, 411))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Sans Serif\";")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stop = QtWidgets.QPushButton(self.frame_5)
        self.stop.setEnabled(False)
        self.stop.setGeometry(QtCore.QRect(340, 480, 71, 23))
        self.stop.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 11pt \"Sans Serif\";")
        self.stop.setObjectName("stop")
        self.start = QtWidgets.QPushButton(self.frame_5)
        self.start.setEnabled(False)
        self.start.setGeometry(QtCore.QRect(40, 480, 80, 23))
        self.start.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"font: 11pt \"Sans Serif\";")
        self.start.setObjectName("start")
        self.lastdata = QtWidgets.QPushButton(self.frame_5)
        self.lastdata.setEnabled(False)
        self.lastdata.setGeometry(QtCore.QRect(160, 480, 161, 23))
        self.lastdata.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.lastdata.setObjectName("lastdata")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(10, 270, 721, 291))
        self.frame_6.setToolTip("")
        self.frame_6.setStyleSheet("background-color: rgb(11, 93, 148);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(230, 0, 261, 31))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(10, 40, 341, 241))
        self.frame_7.setToolTip("")
        self.frame_7.setStyleSheet("background-color: rgb(121, 150, 255);\n"
"font: 12pt \"Sans Serif\";")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.setPoint_num_1 = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.setPoint_num_1.setEnabled(False)
        self.setPoint_num_1.setGeometry(QtCore.QRect(100, 30, 81, 24))
        self.setPoint_num_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setPoint_num_1.setObjectName("setPoint_num_1")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(190, 30, 81, 21))
        self.label_9.setObjectName("label_9")
        self.ramp_1 = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.ramp_1.setEnabled(False)
        self.ramp_1.setGeometry(QtCore.QRect(250, 30, 71, 24))
        self.ramp_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ramp_1.setObjectName("ramp_1")
        self.range_1 = QtWidgets.QComboBox(self.frame_7)
        self.range_1.setEnabled(False)
        self.range_1.setGeometry(QtCore.QRect(260, 60, 71, 23))
        self.range_1.setObjectName("range_1")
        self.range_1.addItem("")
        self.range_1.addItem("")
        self.range_1.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.label_10.setObjectName("label_10")
        self.seeStatus_1 = QtWidgets.QCheckBox(self.frame_7)
        self.seeStatus_1.setEnabled(False)
        self.seeStatus_1.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.seeStatus_1.setObjectName("seeStatus_1")
        self.status_1 = QtWidgets.QScrollArea(self.frame_7)
        self.status_1.setEnabled(False)
        self.status_1.setGeometry(QtCore.QRect(120, 90, 211, 101))
        self.status_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.status_1.setWidgetResizable(True)
        self.status_1.setObjectName("status_1")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 209, 99))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.status_1.setWidget(self.scrollAreaWidgetContents_2)
        self.update_1 = QtWidgets.QPushButton(self.frame_7)
        self.update_1.setEnabled(False)
        self.update_1.setGeometry(QtCore.QRect(200, 200, 80, 23))
        self.update_1.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.update_1.setObjectName("update_1")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setGeometry(QtCore.QRect(70, 60, 191, 21))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.range_manual_1 = QtWidgets.QRadioButton(self.frame_9)
        self.range_manual_1.setEnabled(False)
        self.range_manual_1.setGeometry(QtCore.QRect(110, 0, 91, 21))
        self.range_manual_1.setObjectName("range_manual_1")
        self.range_automatic_1 = QtWidgets.QRadioButton(self.frame_9)
        self.range_automatic_1.setEnabled(False)
        self.range_automatic_1.setGeometry(QtCore.QRect(0, 0, 111, 21))
        self.range_automatic_1.setChecked(True)
        self.range_automatic_1.setObjectName("range_automatic_1")
        self.range_automatic_1.raise_()
        self.range_manual_1.raise_()
        self.Off_1 = QtWidgets.QPushButton(self.frame_7)
        self.Off_1.setEnabled(False)
        self.Off_1.setGeometry(QtCore.QRect(60, 200, 80, 23))
        self.Off_1.setStyleSheet("background-color: rgb(162, 42, 44);")
        self.Off_1.setObjectName("Off_1")
        self.heater_1 = QtWidgets.QRadioButton(self.frame_7)
        self.heater_1.setEnabled(False)
        self.heater_1.setGeometry(QtCore.QRect(110, 0, 108, 27))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.heater_1.setFont(font)
        self.heater_1.setToolTip("")
        self.heater_1.setStyleSheet("font: 14pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.heater_1.setObjectName("heater_1")
        self.label_10.raise_()
        self.frame_9.raise_()
        self.setPoint_num_1.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.ramp_1.raise_()
        self.range_1.raise_()
        self.seeStatus_1.raise_()
        self.status_1.raise_()
        self.update_1.raise_()
        self.Off_1.raise_()
        self.heater_1.raise_()
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setGeometry(QtCore.QRect(370, 40, 341, 241))
        self.frame_8.setToolTip("")
        self.frame_8.setStyleSheet("font: 11pt \"Sans Serif\";\n"
"background-color: rgb(255, 59, 25);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.setPoint_num_2 = QtWidgets.QDoubleSpinBox(self.frame_8)
        self.setPoint_num_2.setEnabled(False)
        self.setPoint_num_2.setGeometry(QtCore.QRect(100, 30, 81, 24))
        self.setPoint_num_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setPoint_num_2.setObjectName("setPoint_num_2")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setGeometry(QtCore.QRect(190, 30, 81, 21))
        self.label_11.setObjectName("label_11")
        self.ramp_2 = QtWidgets.QDoubleSpinBox(self.frame_8)
        self.ramp_2.setEnabled(False)
        self.ramp_2.setGeometry(QtCore.QRect(250, 30, 51, 24))
        self.ramp_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ramp_2.setObjectName("ramp_2")
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.label_12.setObjectName("label_12")
        self.seeStatus_2 = QtWidgets.QCheckBox(self.frame_8)
        self.seeStatus_2.setEnabled(False)
        self.seeStatus_2.setGeometry(QtCore.QRect(10, 100, 99, 21))
        self.seeStatus_2.setObjectName("seeStatus_2")
        self.status_2 = QtWidgets.QScrollArea(self.frame_8)
        self.status_2.setEnabled(False)
        self.status_2.setGeometry(QtCore.QRect(110, 90, 221, 101))
        self.status_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.status_2.setWidgetResizable(True)
        self.status_2.setObjectName("status_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 219, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.status_2.setWidget(self.scrollAreaWidgetContents_3)
        self.update_2 = QtWidgets.QPushButton(self.frame_8)
        self.update_2.setEnabled(False)
        self.update_2.setGeometry(QtCore.QRect(220, 200, 80, 23))
        self.update_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.update_2.setObjectName("update_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setGeometry(QtCore.QRect(70, 60, 181, 21))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.range_manual_2 = QtWidgets.QRadioButton(self.frame_10)
        self.range_manual_2.setEnabled(False)
        self.range_manual_2.setGeometry(QtCore.QRect(100, 0, 81, 21))
        self.range_manual_2.setObjectName("range_manual_2")
        self.range_automatic_2 = QtWidgets.QRadioButton(self.frame_10)
        self.range_automatic_2.setEnabled(False)
        self.range_automatic_2.setGeometry(QtCore.QRect(0, 0, 101, 21))
        self.range_automatic_2.setChecked(True)
        self.range_automatic_2.setObjectName("range_automatic_2")
        self.Off_2 = QtWidgets.QPushButton(self.frame_8)
        self.Off_2.setEnabled(False)
        self.Off_2.setGeometry(QtCore.QRect(50, 200, 80, 23))
        self.Off_2.setStyleSheet("background-color: rgb(163, 0, 2);")
        self.Off_2.setObjectName("Off_2")
        self.range_2 = QtWidgets.QComboBox(self.frame_8)
        self.range_2.setEnabled(False)
        self.range_2.setGeometry(QtCore.QRect(250, 60, 71, 23))
        self.range_2.setObjectName("range_2")
        self.range_2.addItem("")
        self.range_2.addItem("")
        self.range_2.addItem("")
        self.heater_2 = QtWidgets.QRadioButton(self.frame_8)
        self.heater_2.setEnabled(False)
        self.heater_2.setGeometry(QtCore.QRect(130, 0, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.heater_2.setFont(font)
        self.heater_2.setStyleSheet("font: 16pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.heater_2.setObjectName("heater_2")
        self.label_12.raise_()
        self.frame_10.raise_()
        self.seeStatus_2.raise_()
        self.setPoint_num_2.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.ramp_2.raise_()
        self.status_2.raise_()
        self.update_2.raise_()
        self.Off_2.raise_()
        self.range_2.raise_()
        self.heater_2.raise_()
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 0, 841, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.linePatch = QtWidgets.QLineEdit(self.layoutWidget)
        self.linePatch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linePatch.setObjectName("linePatch")
        self.horizontalLayout.addWidget(self.linePatch)
        self.directorio = QtWidgets.QToolButton(self.layoutWidget)
        self.directorio.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.directorio.setObjectName("directorio")
        self.horizontalLayout.addWidget(self.directorio)
        self.SeeData = QtWidgets.QPushButton(self.layoutWidget)
        self.SeeData.setEnabled(False)
        self.SeeData.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 11pt \"Sans Serif\";")
        self.SeeData.setObjectName("SeeData")
        self.horizontalLayout.addWidget(self.SeeData)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 40, 721, 221))
        self.frame_4.setToolTip("")
        self.frame_4.setStyleSheet("\n"
"background-color: rgb(85, 85, 127);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setGeometry(QtCore.QRect(10, 10, 231, 103))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 11pt \"Sans Serif\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.grafica1 = QtWidgets.QRadioButton(self.frame)
        self.grafica1.setEnabled(False)
        self.grafica1.setChecked(False)
        self.grafica1.setObjectName("grafica1")
        self.verticalLayout.addWidget(self.grafica1)
        self.grafica2 = QtWidgets.QRadioButton(self.frame)
        self.grafica2.setEnabled(False)
        self.grafica2.setChecked(True)
        self.grafica2.setObjectName("grafica2")
        self.verticalLayout.addWidget(self.grafica2)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(270, 40, 261, 111))
        self.frame_2.setStyleSheet("background-color: rgb(128, 255, 171);\n"
"font: 11pt \"Sans Serif\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setGeometry(QtCore.QRect(110, 50, 71, 24))
        self.timeEdit.setObjectName("timeEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 80, 251, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.radioButton.setObjectName("radioButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 71, 31))
        self.label_2.setObjectName("label_2")
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.timeEdit.raise_()
        self.label_2.raise_()
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(330, 160, 131, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 11pt \"Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setGeometry(QtCore.QRect(560, 10, 141, 201))
        self.frame_3.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 11pt \"Sans Serif\";")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Todos = QtWidgets.QCheckBox(self.frame_3)
        self.Todos.setEnabled(False)
        self.Todos.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.Todos.setChecked(True)
        self.Todos.setObjectName("Todos")
        self.CA = QtWidgets.QCheckBox(self.frame_3)
        self.CA.setEnabled(False)
        self.CA.setGeometry(QtCore.QRect(40, 30, 91, 21))
        self.CA.setChecked(True)
        self.CA.setObjectName("CA")
        self.CB = QtWidgets.QCheckBox(self.frame_3)
        self.CB.setEnabled(False)
        self.CB.setGeometry(QtCore.QRect(40, 50, 91, 21))
        self.CB.setChecked(True)
        self.CB.setObjectName("CB")
        self.D1 = QtWidgets.QCheckBox(self.frame_3)
        self.D1.setEnabled(False)
        self.D1.setGeometry(QtCore.QRect(40, 70, 85, 21))
        self.D1.setChecked(True)
        self.D1.setObjectName("D1")
        self.D2 = QtWidgets.QCheckBox(self.frame_3)
        self.D2.setEnabled(False)
        self.D2.setGeometry(QtCore.QRect(40, 90, 85, 21))
        self.D2.setChecked(True)
        self.D2.setObjectName("D2")
        self.D3 = QtWidgets.QCheckBox(self.frame_3)
        self.D3.setEnabled(False)
        self.D3.setGeometry(QtCore.QRect(40, 110, 85, 21))
        self.D3.setChecked(True)
        self.D3.setObjectName("D3")
        self.D4 = QtWidgets.QCheckBox(self.frame_3)
        self.D4.setEnabled(False)
        self.D4.setGeometry(QtCore.QRect(40, 130, 85, 21))
        self.D4.setChecked(True)
        self.D4.setObjectName("D4")
        self.C5 = QtWidgets.QCheckBox(self.frame_3)
        self.C5.setEnabled(False)
        self.C5.setGeometry(QtCore.QRect(40, 150, 85, 21))
        self.C5.setChecked(True)
        self.C5.setObjectName("C5")
        self.C6 = QtWidgets.QCheckBox(self.frame_3)
        self.C6.setEnabled(False)
        self.C6.setGeometry(QtCore.QRect(40, 170, 85, 21))
        self.C6.setChecked(True)
        self.C6.setObjectName("C6")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 171, 31))
        self.label_4.setObjectName("label_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setGeometry(QtCore.QRect(10, 120, 230, 74))
        self.frame_11.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 11pt \"Sans Serif\";")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout.setObjectName("gridLayout")
        self.SetPoint1 = QtWidgets.QCheckBox(self.frame_11)
        self.SetPoint1.setEnabled(False)
        self.SetPoint1.setObjectName("SetPoint1")
        self.gridLayout.addWidget(self.SetPoint1, 0, 0, 1, 1)
        self.SetPoint2 = QtWidgets.QCheckBox(self.frame_11)
        self.SetPoint2.setEnabled(False)
        self.SetPoint2.setObjectName("SetPoint2")
        self.gridLayout.addWidget(self.SetPoint2, 0, 1, 1, 1)
        self.heater1 = QtWidgets.QCheckBox(self.frame_11)
        self.heater1.setEnabled(False)
        self.heater1.setObjectName("heater1")
        self.gridLayout.addWidget(self.heater1, 1, 0, 1, 1)
        self.heater2 = QtWidgets.QCheckBox(self.frame_11)
        self.heater2.setEnabled(False)
        self.heater2.setObjectName("heater2")
        self.gridLayout.addWidget(self.heater2, 1, 1, 1, 1)
        self.layoutWidget.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1178, 20))
        self.menubar.setObjectName("menubar")
        self.menupl = QtWidgets.QMenu(self.menubar)
        self.menupl.setObjectName("menupl")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.action218 = QtWidgets.QAction(MainWindow)
        self.action218.setObjectName("action218")
        self.action335 = QtWidgets.QAction(MainWindow)
        self.action335.setObjectName("action335")
        self.menupl.addAction(self.actionInfo)
        self.menuSettings.addAction(self.action218)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.action335)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menupl.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#00557f;\">Acquisition of Data</span></p></body></html>"))
        self.scrollArea.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Status</span></p></body></html>"))
        self.scrollArea.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Estado</p></body></html>"))
        self.stop.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Stop acquisition</span></p></body></html>"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.start.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Start acquisition</span></p></body></html>"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.lastdata.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">See last data</span></p></body></html>"))
        self.lastdata.setText(_translate("MainWindow", "See last data"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Control</span></p></body></html>"))
        self.frame_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Heater 1</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Set Point:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Ramp:</span></p><p><br/></p></body></html>"))
        self.range_1.setItemText(0, _translate("MainWindow", "Low"))
        self.range_1.setItemText(1, _translate("MainWindow", "Med"))
        self.range_1.setItemText(2, _translate("MainWindow", "High"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Range:</span></p></body></html>"))
        self.seeStatus_1.setText(_translate("MainWindow", "See Status"))
        self.status_1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Status Heater 1</span></p></body></html>"))
        self.update_1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Update Heater 1</span></p></body></html>"))
        self.update_1.setText(_translate("MainWindow", "Update"))
        self.range_manual_1.setText(_translate("MainWindow", "Manual "))
        self.range_automatic_1.setText(_translate("MainWindow", "Automatic "))
        self.Off_1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Off Heater 1</span></p></body></html>"))
        self.Off_1.setText(_translate("MainWindow", "Off"))
        self.heater_1.setText(_translate("MainWindow", "Heater 1"))
        self.frame_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Set Point:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Ramp:</span></p><p><br/></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Range:</span></p></body></html>"))
        self.seeStatus_2.setText(_translate("MainWindow", "See Status"))
        self.status_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Status Heater 2</span></p></body></html>"))
        self.update_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Update Heater 2</span></p></body></html>"))
        self.update_2.setText(_translate("MainWindow", "Update"))
        self.range_manual_2.setText(_translate("MainWindow", "Manual "))
        self.range_automatic_2.setText(_translate("MainWindow", "Automatic "))
        self.Off_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Off Heater 2</span></p></body></html>"))
        self.Off_2.setText(_translate("MainWindow", "Off"))
        self.range_2.setItemText(0, _translate("MainWindow", "Low"))
        self.range_2.setItemText(1, _translate("MainWindow", "Med"))
        self.range_2.setItemText(2, _translate("MainWindow", "High"))
        self.heater_2.setText(_translate("MainWindow", "Heater 2"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Address:</span></p></body></html>"))
        self.directorio.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Select folder</span></p></body></html>"))
        self.directorio.setText(_translate("MainWindow", "..."))
        self.SeeData.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">See data</span></p></body></html>"))
        self.SeeData.setText(_translate("MainWindow", "See Data"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Type</span></p></body></html>"))
        self.grafica1.setText(_translate("MainWindow", "Plot with refresh"))
        self.grafica2.setText(_translate("MainWindow", "Plot without refresh"))
        self.radioButton_2.setText(_translate("MainWindow", "Desde el inicio de los tiempos"))
        self.radioButton.setText(_translate("MainWindow", "Period:"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Time</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Plot</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Plot</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.frame_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Sensors</span></p></body></html>"))
        self.Todos.setText(_translate("MainWindow", "All sensors"))
        self.CA.setText(_translate("MainWindow", "Cernox A"))
        self.CB.setText(_translate("MainWindow", "Cernox B"))
        self.D1.setText(_translate("MainWindow", "Diodo 1"))
        self.D2.setText(_translate("MainWindow", "Diodo 2"))
        self.D3.setText(_translate("MainWindow", "Diodo 3"))
        self.D4.setText(_translate("MainWindow", "Diodo 4"))
        self.C5.setText(_translate("MainWindow", "Cernox 5"))
        self.C6.setText(_translate("MainWindow", "Cernox 6"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#aaffff;\">Plot of Data</span></p></body></html>"))
        self.frame_11.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Plot data of Heaters</span></p></body></html>"))
        self.SetPoint1.setText(_translate("MainWindow", "SetPoint 1"))
        self.SetPoint2.setText(_translate("MainWindow", "SetPoint 2"))
        self.heater1.setText(_translate("MainWindow", "Heater 1"))
        self.heater2.setText(_translate("MainWindow", "Heater 2"))
        self.menupl.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.action218.setText(_translate("MainWindow", "218"))
        self.action335.setText(_translate("MainWindow", "335"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

