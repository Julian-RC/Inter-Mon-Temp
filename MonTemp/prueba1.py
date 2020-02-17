import os, serial, sys, time, datetime, subprocess, pickle
sudoPassword = 'rakshasadebian'
command = 'sudo apt upgrade'
#os.system('echo %s|sudo -S %s' % (sudoPassword, command))
os.system("xrdb " +os.path.realpath(__file__).strip('prueba1.py') + "cfg/terminal.cfg")
#os.system('cd '+os.path.realpath(__file__).strip('prueba1.py')+'cfg && sudo chmod 777 /dev/ttyUSB*')
#print(os.system('which Temperature'))
from MonTemp.prueba1_ui import Ui_MainWindow
from MonTemp.info_ui import Ui_Dialog
from MonTemp.segunda_ui import Ui_Segunda
from MonTemp.tercera_ui import Ui_Tercera
from MonTemp.help_218_ui import Ui_help_218
from MonTemp.help_335_ui import Ui_help_335
from MonTemp.plot_file import Ui_plot_file
from MonTemp.fit_218_ui import Ui_fit_218
from MonTemp.fit import Ui_fit
from MonTemp.fit_335_ui import Ui_fit_335
from PyQt5 import QtWidgets,QtGui,QtCore
import pyqtgraph as pg
from numpy import append
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg \
  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg \
  import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class Plot_File(QtWidgets.QDialog,Ui_plot_file):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Plot File")
        except KeyboardInterrupt as KBI:
            pass

class Fit_of_data(QtWidgets.QDialog,Ui_fit):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Fit of Data")
            self.CA.setDecimals(4)
            self.CB.setDecimals(4)
            self.C5.setDecimals(4)
            self.C6.setDecimals(4)
            self.D1.setDecimals(4)
            self.D2.setDecimals(4)
            self.D3.setDecimals(4)
            self.D4.setDecimals(4)
        except KeyboardInterrupt as KBI:
            pass

class D218_Data(QtWidgets.QDialog,Ui_fit_218):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Fit Data Temperature Monitor 218")
        except KeyboardInterrupt as KBI:
            pass

class D335_Data(QtWidgets.QDialog,Ui_fit_335):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Fit Data Temperature Control 335")
        except KeyboardInterrupt as KBI:
            pass

class Help_218(QtWidgets.QDialog,Ui_help_218):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Help Temperature Monitor 218")
        except KeyboardInterrupt as KBI:
            pass

class Help_335(QtWidgets.QDialog,Ui_help_335):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Help Temperature Monitor 335")
        except KeyboardInterrupt as KBI:
            pass

class Dialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        try:
            global textDict
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("About Temperature")
        except KeyboardInterrupt as KBI:
            pass

class Segunda(QtWidgets.QDialog,Ui_Segunda):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.timeOut.setRange(0.1,99.9)
            self.timeOut.setDecimals(1)
            self.savedata.setRange(10,1000)
            self.samplinperiod.setDecimals(1)
            self.samplinperiod.setRange(0,100)
            self.average.setRange(10,1000)
            self.curve1.setRange(0,28)
            self.curve2.setRange(0,28)
            self.curve3.setRange(0,28)
            self.curve4.setRange(0,28)
            self.curve5.setRange(0,28)
            self.curve6.setRange(0,28)
            self.curve7.setRange(0,28)
            self.curve8.setRange(0,28)
            self.setWindowTitle("218 TemperatureMonitor")
            self.name.setText(textDict.ConfigDict['Name'])
            self.nameaverage.setText(textDict.ConfigDict['NameAverage'])
            self.model.setText(textDict.ConfigDict['Model'])
            if textDict.ConfigDict['Sensor Status 1']=='1':
                self.sensor1.setText(textDict.ConfigDict['Sensor Type'][0])
                self.sensor1_on.setChecked(True)
                self.curve1.setValue(int(textDict.ConfigDict['CP1']))
            if textDict.ConfigDict['Sensor Status 2']=='1':
                self.sensor2.setText(textDict.ConfigDict['Sensor Type'][1])
                self.sensor2_on.setChecked(True)
                self.curve2.setValue(int(textDict.ConfigDict['CP2']))
            if textDict.ConfigDict['Sensor Status 3']=='1':
                self.sensor3.setText(textDict.ConfigDict['Sensor Type'][2])
                self.sensor3_on.setChecked(True)
                self.curve3.setValue(int(textDict.ConfigDict['CP3']))
            if textDict.ConfigDict['Sensor Status 4']=='1':
                self.sensor4.setText(textDict.ConfigDict['Sensor Type'][3])
                self.sensor4_on.setChecked(True)
                self.curve4.setValue(int(textDict.ConfigDict['CP4']))
            if textDict.ConfigDict['Sensor Status 5']=='1':
                self.sensor5.setText(textDict.ConfigDict['Sensor Type'][4])
                self.sensor5_on.setChecked(True)
                self.curve5.setValue(int(textDict.ConfigDict['CP5']))
            if textDict.ConfigDict['Sensor Status 6']=='1':
                self.sensor6.setText(textDict.ConfigDict['Sensor Type'][5])
                self.sensor6_on.setChecked(True)
                self.curve6.setValue(int(textDict.ConfigDict['CP6']))
            if textDict.ConfigDict['Sensor Status 7']=='1':
                self.sensor7.setText(textDict.ConfigDict['Sensor Type'][6])
                self.sensor7_on.setChecked(True)
                self.curve7.setValue(int(textDict.ConfigDict['CP7']))
            if textDict.ConfigDict['Sensor Status 8']=='1':
                self.sensor8.setText(textDict.ConfigDict['Sensor Type'][7])
                self.sensor8_on.setChecked(True)
                self.curve8.setValue(int(textDict.ConfigDict['CP8']))
            self.sensor1_on.toggled.connect(self.desbloquear_sensor1)
            self.sensor2_on.toggled.connect(self.desbloquear_sensor2)
            self.sensor3_on.toggled.connect(self.desbloquear_sensor3)
            self.sensor4_on.toggled.connect(self.desbloquear_sensor4)
            self.sensor5_on.toggled.connect(self.desbloquear_sensor5)
            self.sensor6_on.toggled.connect(self.desbloquear_sensor6)
            self.sensor7_on.toggled.connect(self.desbloquear_sensor7)
            self.sensor8_on.toggled.connect(self.desbloquear_sensor8)
            self.port.setText(textDict.ConfigDict['Port'])
            self.savedata.setValue(int(textDict.ConfigDict['SaveData']))
            self.average.setValue(int(textDict.ConfigDict['Average']))
            self.samplinperiod.setValue(float(textDict.ConfigDict['SamplingPeriod']))
            self.timeOut.setValue(float(textDict.ConfigDict['TimeOut']))
            #self.buttonBox.accepted.connect(self.accept)
        except KeyboardInterrupt as KBI:
            pass

    def desbloquear_sensor1(self):
        if self.sensor1_on.isChecked():
            self.sensor1.setEnabled(True)
            self.curve1.setEnabled(True)
        else:
            self.sensor1.setEnabled(False)
            self.surve1.setEnabled(False)

    def desbloquear_sensor2(self):
        if self.sensor2_on.isChecked():
            self.sensor2.setEnabled(True)
            self.curve2.setEnabled(True)
        else:
            self.sensor2.setEnabled(False)
            self.curve2.setEnabled(False)

    def desbloquear_sensor3(self):
        if self.sensor3_on.isChecked():
            self.sensor3.setEnabled(True)
            self.curve3.setEnabled(True)
        else:
            self.sensor3.setEnabled(False)
            self.curve3.setEnabled(False)

    def desbloquear_sensor4(self):
        if self.sensor4_on.isChecked():
            self.sensor4.setEnabled(True)
            self.curve4.setEnabled(True)
        else:
            self.sensor4.setEnabled(False)
            self.curve4.setEnabled(False)

    def desbloquear_sensor5(self):
        if self.sensor5_on.isChecked():
            self.sensor5.setEnabled(True)
            self.curve5.setEnabled(True)
        else:
            self.sensor5.setEnabled(False)
            self.curve5.setEnabled(False)

    def desbloquear_sensor6(self):
        if self.sensor6_on.isChecked():
            self.sensor6.setEnabled(True)
            self.curve6.setEnabled(True)
        else:
            self.sensor6.setEnabled(False)
            self.curve6.setEnabled(False)

    def desbloquear_sensor7(self):
        if self.sensor7_on.isChecked():
            self.sensor7.setEnabled(True)
            self.curve7.setEnabled(True)
        else:
            self.sensor7.setEnabled(False)
            self.curve7.setEnabled(False)

    def desbloquear_sensor8(self):
        if self.sensor8_on.isChecked():
            self.sensor8.setEnabled(True)
            self.curve8.setEnabled(True)
        else:
            self.sensor8.setEnabled(False)
            self.curve8.setEnabled(False)

    def accept(self):
        if 9<self.curve1.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 1",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve2.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 2",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve3.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 3",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve4.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 4",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve5.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 5",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve6.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 6",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve7.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 7",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif 9<self.curve8.value()<21:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Curve Sensor 8",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.name.text() or self.name.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Name",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.nameaverage.text() or self.nameaverage.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Name Average",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.model.text() or self.model.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Model",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.port.text() or self.port.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Port",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor1.text() or self.sensor1.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensor1",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor2.text() or self.sensor2.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors2",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor3.text() or self.sensor3.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensor3",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor4.text() or self.sensor4.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors4",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor5.text() or self.sensor5.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors5",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor6.text() or self.sensor6.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors6",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor7.text() or self.sensor7.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors7",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor8.text() or self.sensor8.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors8",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()

class Terminal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        try:
            super(Terminal, self).__init__(parent)
            self.process = QtCore.QProcess(self)
            self.terminal = QtWidgets.QWidget(self)
            layout = QtWidgets.QVBoxLayout(self)
            layout.addWidget(self.terminal)
            self.process.start('urxvt',['-embed', str(int(self.winId()))])
            self.setFixedSize(1300, 273)
            pg.QtGui.QApplication.processEvents()
        except KeyboardInterrupt as KBI:
            pass

class Tercera(QtWidgets.QDialog,Ui_Tercera):
    def __init__(self, *args, **kwargs):
        try:
            global textDict2
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.timeOut.setRange(0.1,99.9)
            self.timeOut.setDecimals(1)
            self.savedata.setRange(10,1000)
            self.samplinperiod.setDecimals(1)
            self.samplinperiod.setRange(0,100)
            self.average.setRange(10,1000)
            self.setWindowTitle("335 TemperatureController")
            self.name.setText(textDict2.ConfigDict['Name'])
            self.nameAverage.setText(textDict2.ConfigDict['NameAverage'])
            self.model.setText(textDict2.ConfigDict['Model'])
            if len(textDict2.ConfigDict['Channels'])==2:
                self.sensor1.setText(textDict2.ConfigDict['Sensor Type'][0])
                self.sensor2.setText(textDict2.ConfigDict['Sensor Type'][1])
                self.sensor1_on.setChecked(True)
                self.sensor2_on.setChecked(True)
            elif textDict2.ConfigDict['Channels']=='A':
                self.sensor1.setText(textDict2.ConfigDict['Sensor Type'])
                self.sensor1_on.setChecked(True)
            elif textDict2.ConfigDict['Channels']=='B':
                self.sensor2.setText(textDict2.ConfigDict['Sensor Type'])
                self.sensor2_on.setChecked(True)
            self.sensor1_on.toggled.connect(self.desbloquear_sensor1)
            self.sensor2_on.toggled.connect(self.desbloquear_sensor2)
            self.port.setText(textDict2.ConfigDict['Port'])
            self.savedata.setValue(int(textDict2.ConfigDict['SaveData']))
            self.average.setValue(int(textDict2.ConfigDict['Average']))
            self.samplinperiod.setValue(float(textDict2.ConfigDict['SamplingPeriod']))
            self.timeOut.setValue(float(textDict2.ConfigDict['TimeOut']))

        except KeyboardInterrupt as KBI:
            pass
    def desbloquear_sensor1(self):
        if self.sensor1_on.isChecked():
            self.sensor1.setEnabled(True)
        else:
            self.sensor1.setEnabled(False)

    def desbloquear_sensor2(self):
        if self.sensor2_on.isChecked():
            self.sensor2.setEnabled(True)
        else:
            self.sensor2.setEnabled(False)
    def accept(self):
        if not self.name.text() or self.name.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Name",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.nameAverage.text() or self.nameAverage.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Name Average",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.model.text() or self.model.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Model",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.port.text() or self.port.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido Port",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor1.text() or self.sensor1.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensor1",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        elif not self.sensor2.text() or self.sensor2.text().isspace():
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Valor inválido TypeSensors2",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None,*args, **kwargs):
        super(MainWindow, self).__init__()
       # QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        global label_scroll, textDict, textDict2, patch,textDict_color
        patch = os.path.realpath(__file__).strip('prueba1.py')
        filename = patch + "cfg/file_218.cfg"
        filename2 = patch + "cfg/file_335.cfg"
        filename_color = patch + "cfg/color.cfg"
        filename_fit = patch + "cfg/sensores_fit.cfg"
        textDict = ConfigModule(filename,0,0)
        textDict2 = ConfigModule(filename2,0,0)
        textDict_color = ConfigModule(filename_color,0,0)
        for a in textDict_color.ConfigDict:
            textDict_color.ConfigDict[a]=textDict_color.ConfigDict[a].split(',')
        textDict_fit = ConfigModule(filename_fit,0,0)
        for a in textDict_fit.ConfigDict:
            textDict_fit.ConfigDict[a]=textDict_fit.ConfigDict[a].split(',')
        DataTemp = TempClass(textDict.ConfigDict)
        DataTemp2 = TempClass(textDict2.ConfigDict,DataTemp.InitTime)
        self.setupUi(self)
        self.setWindowTitle("Temperature Module")
        self.setWindowIcon(QtGui.QIcon(os.path.realpath(__file__).strip('prueba1.py')+'Temperature.png'))
        self.pushButton.clicked.connect(self.graficar)
        self.radioButton.toggled.connect(self.desbloquear_radioButton)
        self.radioButton_2.toggled.connect(self.desbloquear_radioButton_2)
        self.Todos.toggled.connect(self.desbloquear_Todos)
        self.heater_1.toggled.connect(self.desbloquear_heater_1)
        self.heater_2.toggled.connect(self.desbloquear_heater_2)
        self.range_manual_1.toggled.connect(self.desbloquear_range_manual_1)
        self.range_automatic_1.toggled.connect(self.desbloquear_range_automatic_1)
        self.range_manual_2.toggled.connect(self.desbloquear_range_manual_2)
        self.range_automatic_2.toggled.connect(self.desbloquear_range_automatic_2)
        self.seeStatus_1.toggled.connect(self.desbloquear_seeStatus_1)
        self.seeStatus_2.toggled.connect(self.desbloquear_seeStatus_2)
        self.grafica2.toggled.connect(self.desbloquear_grafica2)
        self.grafica1.toggled.connect(self.desbloquear_grafica1)
        self.CA.toggled.connect(self.desbloquear_sensores_CA)
        self.CB.toggled.connect(self.desbloquear_sensores_CB)
        self.C5.toggled.connect(self.desbloquear_sensores_C5)
        self.C6.toggled.connect(self.desbloquear_sensores_C6)
        self.D1.toggled.connect(self.desbloquear_sensores_D1)
        self.D2.toggled.connect(self.desbloquear_sensores_D2)
        self.D3.toggled.connect(self.desbloquear_sensores_D3)
        self.D4.toggled.connect(self.desbloquear_sensores_D4)
        self.heater1.toggled.connect(self.desbloquear_heater1)
        self.heater2.toggled.connect(self.desbloquear_heater2)
        self.SetPoint1.toggled.connect(self.desbloquear_SetPoint1)
        self.SetPoint2.toggled.connect(self.desbloquear_SetPoint2)

        self.directorio.clicked.connect(self.buscarDirectorio)
        self.start.clicked.connect(self.start_adquisition)
        self.stop.clicked.connect(self.stop_adquisition)
        self.see_ramp.clicked.connect(self.rampa)

        self.actionInfo.triggered.connect(self.show_dialog)
        self.action218.triggered.connect(self.show_218)
        self.action335.triggered.connect(self.show_335)
        self.actionAbout_Temperature_Monitor_218.triggered.connect(self.show_help_218)
        self.actionAbout_Temperature_Control_335.triggered.connect(self.show_help_335)
        self.action218_Data.triggered.connect(self.show_218_Data)
        self.action335_Data.triggered.connect(self.show_335_Data)
        self.actionFit_of_data.triggered.connect(self.show_Fit_of_data)
        self.actionPlot_File.triggered.connect(self.show_Plot_File)

        self.setPoint_num_1.setRange(50,300)
        self.setPoint_num_2.setRange(50,300)

        self.ramp_1.setDecimals(1)
        self.ramp_2.setDecimals(1)
        self.ramp_1.setRange(0,5)
        self.ramp_2.setRange(0,5)
        self.ss.setRange(0,59)
        self.mm.setRange(0,59)

        self.update_1.clicked.connect(self.Update_1)
        self.update_2.clicked.connect(self.Update_2)
        self.Off_1.clicked.connect(self.off_heater_1)
        self.Off_2.clicked.connect(self.off_heater_2)
        self.SeeData.clicked.connect(self.see_data)
        self.lastdata.clicked.connect(self.last)
        self.color_H1.clicked.connect(self.change_color_H1)
        self.color_H2.clicked.connect(self.change_color_H2)
        self.color_S1.clicked.connect(self.change_color_S1)
        self.color_S2.clicked.connect(self.change_color_S2)
        self.color_D1.clicked.connect(self.change_color_D1)
        self.color_D2.clicked.connect(self.change_color_D2)
        self.color_D3.clicked.connect(self.change_color_D3)
        self.color_D4.clicked.connect(self.change_color_D4)
        self.color_C5.clicked.connect(self.change_color_C5)
        self.color_C6.clicked.connect(self.change_color_C6)
        self.color_CA.clicked.connect(self.change_color_CA)
        self.color_CB.clicked.connect(self.change_color_CB)
        self.update_graph.clicked.connect(self.update_plot)



        label_scroll='-------------------------------------------------------------------------\n'+\
                     '               Welcome, Temperature has begun\n                          '+\
                     '{:%d-%m-%Y %H:%M:%S}\n'.format(datetime.datetime.now())+\
                     '-------------------------------------------------------------------------\n '+\
                     '                   Please select a folder to start\n'\
                     '-------------------------------------------------------------------------\n'
        self.Update_label()
        self.tabWidget.clear()
        self.tabWidget.addTab(Terminal(),"Terminal")
        pg.QtGui.QApplication.processEvents()
    def Update_label(self):
        self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        pg.QtGui.QApplication.processEvents()
    def change_color_H1(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['H1']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['H1']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_H1.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_S1(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['S1']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['S1']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_S1.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_H2(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['H2']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['H2']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_H2.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_S2(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['S2']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['S2']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_S2.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_CA(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['CA']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['CA']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_CA.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_CB(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['CB']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['CB']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_CB.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_D1(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['D1']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['D1']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_D1.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_D2(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['D2']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['D2']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_D2.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_D3(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['D3']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['D3']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_D3.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_D4(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['D4']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['D4']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_D4.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_C5(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['C5']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['C5']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_C5.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    def change_color_C6(self):
        global textDict_color
        color_rgb = textDict_color.ConfigDict['C6']
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            textDict_color.ConfigDict['C6']=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_C6.setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
    
    def rampa(self):
        global ramp_stat,rampa_true
        ramp_stat = True
        rampa_true = Ramp()

    def last(self):
        global label_scroll
        label_scroll +='                              See Last Data\n                           '+\
                       '{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+\
                       '\n-------------------------------------------------------------------------\n'
        self.Update_label()
        label_scroll +='               ' + 'Sensor'+'           '+'Time[s]'+ '        ' +'Data[K]\n'
        for Obj in [DataTemp2,DataTemp]:
               label_scroll += Obj.PrintValue()
        self.Update_label()

    def see_data(self):

        global label_scroll
        try:
            for Obj in [DataTemp,DataTemp2]:
                Obj.__str__()
        except:
           label_scroll += '   ERROR: Text file cannot be shown.\n'
        self.Update_label()

    def off_heater_1(self):

        self.On_335_1()
        time.sleep(0.05)
        self.Update_1()

    def off_heater_2(self):

        self.On_335_2()
        time.sleep(0.05)
        self.Update_2()

    def On_335_1(self):
        global SP_1
        Ramp_1 = str(DataTemp2.Read_335('RAMP?','1')[2:7])
        self.ramp_1.setValue(float(Ramp_1))
        SetP_1 = str(DataTemp2.Read_335('SETP?','1'))
        SP_1 = float(SetP_1)
        self.setPoint_num_1.setValue(SP_1)

    def On_335_2(self):
        global SP_2
        Ramp_2 = str(DataTemp2.Read_335('RAMP?','2')[2:7])

        self.ramp_2.setValue(float(Ramp_2))
        SetP_2 = DataTemp2.Read_335('SETP?','2')
        SP_2 = float(SetP_2)
        self.setPoint_num_2.setValue(SP_2)
    def Update_1(self):
        global RANGE_1,SP_1,label_scroll
        Ramp_1 = str(self.ramp_1.value())
        DataTemp2.Update_335('RAMP','1','1,'+Ramp_1)
        time.sleep(0.05)
        SetP_1 = str(self.setPoint_num_1.value())
        SP_1 = float(SetP_1)
        DataTemp2.Update_335('SETP','1',SetP_1)
        if self.range_manual_1.isChecked():
            time.sleep(0.05)
            RANGE_1 = False
            Range = str(self.range_1.currentIndex()+1)
            DataTemp2.Update_335('RANGE','1',Range)
            if Range == '1':
                Range_print='Low'
            elif Range == '2':
                Range_print='Med'
            elif Range == '3':
                Range_print='High'
            elif Range == '0' :
                Range_print='Off'
        else:
            RANGE_1 = True
            Range = 'Auto'

        label_scroll +='                            Update Heater 1\n                          '+\
                        '{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'\n'+\
                        '-------------------------------------------------------------------------\n'
        label_scroll +='Ramp= '+Ramp_1+' k/min SetPoint= '+SetP_1+' k  Range= '+ Range +\
                        '\n-------------------------------------------------------------------------\n'
        self.Update_label()
    def Update_2(self):
        global RANGE_2
        DataTemp2.Update_335('RANGE','2','1')
        time.sleep(0.05)
        Ramp_2 = str(self.ramp_2.value())
        DataTemp2.Update_335('RAMP','2','1,'+Ramp_2)
        time.sleep(0.05)
        SetP_2 = str(self.setPoint_num_2.value())
        SP_2 = float(SetP_2)
        DataTemp2.Update_335('SETP','2',SetP_2)
        if self.range_manual_2.isChecked():
            time.sleep(0.05)
            RANGE_2 = False
            Range = str(self.range_2.currentIndex()+1)
            DataTemp2.Update_335('RANGE','2',Range)
        else:
            RANGE_2 = True
    def start_adquisition(self):
        global Start,actual, filename, label_scroll,status_heater_1,label_heater_1,ramp_stat
        Start,actual,bt = True,False, True
        self.pushButton.setEnabled(True)
        DataTemp.Start()
        DataTemp2.Start()
        label_scroll+='                          Aquisition has begun\n'\
                        '                          '+'{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'\n'\
                        '-------------------------------------------------------------------------\n'
        self.Update_label()
        DataTemp2.Read_335('SETP?','1')
        DataTemp2.Read_335('SETP?','2')
        DataTemp2.Read_335('RAMP?','1')
        DataTemp2.Read_335('RAMP?','2')
        DataTemp2.Read_335('RANGE?','1')
        DataTemp2.Read_335('RANGE?','2')
        self.grafica1.setEnabled(True)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self.directorio.setEnabled(False)
        self.heater_1.setEnabled(True)
        self.heater_2.setEnabled(True)
        self.lastdata.setEnabled(True)

        while Start:
            try:
                    DataTemp.GetData()
                    pg.QtGui.QApplication.processEvents()
                    pg.QtGui.QApplication.processEvents()
                    if DataTemp.InitTime != 0: DataTemp2.InitTime = DataTemp.InitTime
                    DataTemp2.GetData()
                    pg.QtGui.QApplication.processEvents()
            except:
                    label_scroll += '                             Error en la adquisición\n'
                    label_scroll+='-------------------------------------------------------------------------\n'
                    self.Update_label()
            if actual:
                          global plt_mgr, close_plot,rampa_true
                          Data_2 = []
                          for Obj in [DataTemp2,DataTemp]:
                              a=Obj.Last_data()
                              if a==[]:
                                  pass
                              else:
                                  for algo in a:
                                      Data_2.append(algo)
                                      pg.QtGui.QApplication.processEvents()
                              pg.QtGui.QApplication.processEvents()
                          if Data_2 == []:
                              pass
                          else:
                              plt_mgr.add(Data_2)
                              plt_mgr.update()
                              pg.QtGui.QApplication.processEvents()
                          close_plot = True
                          pg.QtGui.QApplication.processEvents()
            elif close_plot:

                              plt_mgr.close()
                              if ramp_stat:
                                  rampa_true.close()
                                  ramp_stat = False
                              close_plot = False
            if ramp_stat:
                rampa_true.plot()
            if status_heater_1:
                            Ramp_1 = str(DataTemp2.Read_335('HTR?','1'))
                            time.sleep(0.05)
                            label_heater_1 +=str(Ramp_1)+'%'
                            SetP_1 = str(DataTemp2.Read_335('SETP?','1'))
                            time.sleep(0.05)
                            label_heater_1 +='   '+str(SetP_1)+'K'
                            Ran_1 = str(DataTemp2.Read_335('RANGE?','1'))
                            time.sleep(0.05)
                            Range = ''
                            if int(Ran_1)==0:
                                Range = 'Off'
                            elif int(Ran_1)==1:
                                Range = 'Low'
                            elif int(Ran_1)==2:
                                Range = 'Med'
                            elif int(Ran_1)==3:
                                Range = 'High'
                            label_heater_1 += '   '+Range+'\n'
                            label_heater_1 += '--------------------------------------\n'
                            self.status_1.setWidget(QtWidgets.QLabel(label_heater_1))
                            self.status_1.verticalScrollBar().setValue(self.status_1.verticalScrollBar().maximum())
    def stop_adquisition(self):
        global Start,label_scroll
        Start = False
        global actual,plt_mgr
        self.box = QtWidgets.QMessageBox()
        reply = self.box.question(self,
                                 'Stop',
                                 "¿Realmente desea detener la adquision?",
                                  self.box.Yes | self.box.No, self.box.No)
        if reply == self.box.Yes:
                reply = self.box.question(self,
                                 'Stop',
                                 "¿Está seguro?",
                                  self.box.Yes | self.box.No, self.box.No)
                if reply == self.box.Yes:
                                    if actual:
                                        plt_mgr.close()
                                        actual = False
                                    self.grafica2.setChecked(True)
                                    self.grafica1.setChecked(False)
                                    self.grafica1.setEnabled(False)
                                    self.start.setEnabled(True)
                                    self.stop.setEnabled(False)
                                    #self.linePatch.setEnabled(True)
                                    self.directorio.setEnabled(True)
                                    self.heater_1.setEnabled(False)
                                    self.heater_2.setEnabled(False)
                                    self.range_automatic_1.setChecked(True)
                                    self.range_manual_1.setChecked(False)
                                    self.seeStatus_1.setChecked(False)
                                    self.range_automatic_2.setChecked(True)
                                    self.range_manual_2.setChecked(False)
                                    self.seeStatus_2.setChecked(False)
                                    self.heater_1.setChecked(False)
                                    self.heater_2.setChecked(False)
                                    self.off_heater_1()
                                   # self.off_heater_2()
                                    label_scroll+='                        Acquisition has stopped\n'
                                    label_scroll+='                          '+'{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'\n'
                                    label_scroll+='-------------------------------------------------------------------------\n'
                                    self.Update_label()
    def closeEvent(self, event):
        try:
            global actual,Start,plt_mgr,bt,patch
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Exit',
                                    "¿Realmente desea cerrar la aplicacion?",
                                    self.box.Yes | self.box.No, self.box.No)
            pg.QtGui.QApplication.processEvents()
            if reply == self.box.Yes:
                    if Start == True:
                        reply = self.box.question(self,
                                    'Stop',
                                    "Hay una adquisición en proceso, ¿Desea detenerla?",
                                    self.box.Yes | self.box.No, self.box.No)
                        if reply == self.box.Yes:
                                Start = False
                                if actual:
                                            plt_mgr.close()
                                            actual = False
                                #self.off_heater_1()
                                #self.off_heater_2()
                        else:
                                event.ignore()
                    if bt == True:
                        reply = self.box.question(self,
                                                        'Bitácora',
                                                        "¿Desea guardar la bitácora?\n(Se guardará en:  "+patch+")",
                                                        self.box.Yes | self.box.No, self.box.Yes)
                        if reply == self.box.Yes:
                            global label_scroll
                            f = open (patch+'/Temperature.bt','a')
                            f.write(label_scroll)
                            f.close()
            else:
                    event.ignore()
        except KeyboardInterrupt as KBI:
            pass
    def show_dialog(self):
        dialog_1 = Dialog(self)  # self hace referencia al padre
        dialog_1.show()
    def show_218(self):
        dialog_2 = Segunda(self)  # self hace referencia al padre
        dialog_2.show()
    def show_335(self):
        dialog_3 = Tercera(self)  # self hace referencia al padre
        dialog_3.show()
    def show_help_218(self):
        dialog_4 = Help_218(self)  # self hace referencia al padre
        dialog_4.show()
    def show_help_335(self):
        dialog_5 = Help_335(self)  # self hace referencia al padre
        dialog_5.show()
    def show_218_Data(self):
        dialog_6 = D218_Data(self)  # self hace referencia al padre
        dialog_6.show()
    def show_335_Data(self):
        dialog_7 = D335_Data(self)  # self hace referencia al padre
        dialog_7.show()
    def show_Fit_of_data(self):
        dialog_8 = Fit_of_data(self)  # self hace referencia al padre
        dialog_8.show()
    def show_Plot_File(self):
        dialog_9 = Plot_File(self)  # self hace referencia al padre
        dialog_9.show()
    def buscarDirectorio(self):
        global patch,label_scroll,filename,filename2
        label_scroll+='                           Wait a moment Please\n'
        label_scroll+='-------------------------------------------------------------------------\n'
        self.Update_label()
        self.buscarDirectorio_2()
        if patch:
            global textDict,textDict2,DataTemp,DataTemp2
            ls = subprocess.getoutput("cd && cd " +patch+ "&&ls")
           # print(ls.strip('\n'))
            if len(ls)<150:
                label_scroll+='                               Selected folder\n'
                label_scroll+='-------------------------------------------------------------------------\n'
                self.Update_label()
                path = os.path.realpath(__file__).strip('prueba1.py')
                config_filename = path + "cfg/file_218.cfg"
                config_filename2 = path + "cfg/file_335.cfg"
                os.system('cp '+ config_filename +' '+ patch)
                os.system('cp '+ config_filename2 +' '+ patch)
                os.system('cd && cd '+patch+' && chmod 777 file_218.cfg')
                os.system('cd && cd '+patch+' && chmod 777 file_335.cfg')
                filename = patch + '/file_218.cfg'
                filename2 = patch + '/file_335.cfg'
                try:
                    textDict = ConfigModule(filename,1,1)
                    self.Update_label()
                    pg.QtGui.QApplication.processEvents()
                    textDict2 = ConfigModule(filename2,0,1)
                    pg.QtGui.QApplication.processEvents()
                    DataTemp = TempClass(textDict.ConfigDict)
                    pg.QtGui.QApplication.processEvents()
                    self.Update_label()
                    DataTemp2 = TempClass(textDict2.ConfigDict,DataTemp.InitTime)
                    pg.QtGui.QApplication.processEvents()
                    self.Update_label()
                    label_scroll+='                               Config File Ok\n'
                    self.start.setEnabled(True)
                    self.SeeData.setEnabled(True)
                    self.grafica2.setEnabled(True)
                    self.grafica2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                    self.radioButton_2.setEnabled(True)
                    self.radioButton_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                    self.Todos.setEnabled(True)
                    self.Todos.setChecked(True)
                    label_scroll+='               Push "Start" for begin adquisition\n'
                    label_scroll+='-------------------------------------------------------------------------\n'
                    self.linePatch.setText(patch)
                    self.Update_label()
                    self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    pg.QtGui.QApplication.processEvents()
                    self.ramp_la.setStyleSheet("color:rgb(255,255,255);")
                    self.graph_sensor.setStyleSheet("color:rgb(255,255,255);")
                    self.color_sensor.setStyleSheet("color:rgb(255,255,255);")
                except:
                    label_scroll += '       Error al cargar la configuración de los modulos\n'
                    label_scroll+='-------------------------------------------------------------------------\n'
                    self.Update_label()
                    self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                    self.start.setEnabled(False)
                    self.SeeData.setEnabled(False)
                    self.grafica2.setEnabled(False)
                    self.grafica2.setStyleSheet("background-color: a(0);")
                    self.radioButton_2.setEnabled(False)
                    self.radioButton_2.setStyleSheet("background-color: a(0);")
                    self.Todos.setEnabled(False)
                    self.Todos.setChecked(False)
                    self.Todos.setStyleSheet("background-color: a(0);")
                    self.D1.setEnabled(False)
                    self.D1.setChecked(False)
                    self.D1.setStyleSheet("background-color: a(0);")
                    self.D2.setEnabled(False)
                    self.D2.setChecked(False)
                    self.D2.setStyleSheet("background-color: a(0);")
                    self.D3.setEnabled(False)
                    self.D3.setChecked(False)
                    self.D3.setStyleSheet("background-color: a(0);")
                    self.D4.setEnabled(False)
                    self.D4.setChecked(False)
                    self.D4.setStyleSheet("background-color: a(0);")
                    self.C5.setEnabled(False)
                    self.C5.setChecked(False)
                    self.C5.setStyleSheet("background-color: a(0);")
                    self.C6.setEnabled(False)
                    self.C6.setChecked(False)
                    self.C6.setStyleSheet("background-color: a(0);")
                    self.CA.setEnabled(False)
                    self.CA.setChecked(False)
                    self.CA.setStyleSheet("background-color: a(0);")
                    self.CB.setEnabled(False)
                    self.CB.setChecked(False)
                    self.CB.setStyleSheet("background-color: a(0);")
                    self.Time.setStyleSheet(" ")
                    self.Type.setStyleSheet(" ")
                    self.ramp_la.setStyleSheet(" ")
                    self.graph_sensor.setStyleSheet(" ")
                    self.color_sensor.setStyleSheet(" ")
                    self.pushButton.setEnabled(False)
                    self.ramp.setEnabled(False)
            else:
                label_scroll += '                         The folder contains files\n'
                label_scroll+='-------------------------------------------------------------------------\n'
                self.linePatch.setText(patch)
                self.Update_label()
                self.start.setEnabled(False)
                self.SeeData.setEnabled(True)
                self.Time.setStyleSheet("color:rgb(255,255,255);border: 0px solid black;background-color: a( 0);")
                self.grafica2.setEnabled(True)
                self.grafica2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                self.Type.setStyleSheet("color:rgb(255,255,255);border: 0px solid black;background-color: a( 0);")
                self.radioButton_2.setEnabled(True)
                self.radioButton_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                self.color_sensor.setStyleSheet("color:rgb(255,255,255);")
                self.pushButton.setEnabled(True)
                self.Todos.setEnabled(True)
                self.Todos.setChecked(True)
                self.ramp.setEnabled(True)
                self.ramp_la.setStyleSheet("color:rgb(255,255,255);")
                self.graph_sensor.setStyleSheet("color:rgb(255,255,255);")
                path = os.path.realpath(__file__).strip('prueba1.py')
                filename = path + "cfg/file_218.cfg"
                filename2 = path + "cfg/file_335.cfg"
                textDict = ConfigModule(filename,0,0)
                textDict2 = ConfigModule(filename2,0,0)
                print(textDict.ConfigDict)
                print(textDict2.ConfigDict)
                DataTemp = TempClass(textDict.ConfigDict)
                DataTemp2 = TempClass(textDict2.ConfigDict,DataTemp.InitTime)
                self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        else:
            label_scroll+='                               No selected folder\n'
            label_scroll+='-------------------------------------------------------------------------\n'
            self.Update_label()
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    def buscarDirectorio_2(self):
        global patch
        patch = QtWidgets.QFileDialog.getExistingDirectory(self, 'Search folder', QtCore.QDir.homePath())
        self.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        pg.QtGui.QApplication.processEvents()
    def desbloquear_grafica2(self):
        if self.grafica2.isChecked():
                self.grafica2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                self.radioButton.setEnabled(False)
                self.radioButton.setStyleSheet("background-color: a(0);")
                self.SetPoint1.setEnabled(False)
                self.heater1.setEnabled(False)
                self.SetPoint1.setChecked(False)
                self.heater1.setChecked(False)
                self.SetPoint2.setEnabled(False)
                self.heater2.setEnabled(False)
                self.SetPoint2.setChecked(False)
                self.heater2.setChecked(False)
                self.graph_heater_la.setStyleSheet(" ")
                self.color_heater.setStyleSheet(" ")
                self.SetPoint1.setStyleSheet("background-color: a(0);")
                self.SetPoint2.setStyleSheet("background-color: a(0);")
                self.heater1.setStyleSheet("background-color: a(0);")
                self.heater2.setStyleSheet("background-color: a(0);")
                self.see_ramp.setEnabled(True)
                self.ramp.setEnabled(False)
                self.update_graph.setEnabled(True)
        else:
            self.grafica2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.radioButton.setEnabled(True)
            self.radioButton.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            if self.heater_1.isChecked():
                self.SetPoint1.setEnabled(True)
                self.heater1.setEnabled(True)
                self.graph_heater_la.setStyleSheet("color:rgb(255,255,255);")
                self.color_heater.setStyleSheet("color:rgb(255,255,255);")
                self.SetPoint1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
                self.heater1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            if self.heater_2.isChecked():
                self.SetPoint2.setEnabled(True)
                self.heater2.setEnabled(True)
                self.graph_heater_la.setStyleSheet("color:rgb(255,255,255);")
                self.color_heater.setStyleSheet("color:rgb(255,255,255);")
                self.SetPoint2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
                self.heater2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.see_ramp.setEnabled(False)
            self.ramp.setEnabled(True)
            self.update_graph.setEnabled(False)
    def desbloquear_grafica1(self):
        if self.grafica1.isChecked():
            self.grafica1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
        else:
            self.grafica1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
    def desbloquear_radioButton(self):
        if self.radioButton.isChecked():
            self.radioButton.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.hh.setEnabled(True)
            self.mm.setEnabled(True)
            self.ss.setEnabled(True)
        else:
            self.radioButton.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.hh.setEnabled(False)
            self.mm.setEnabled(False)
            self.ss.setEnabled(False)
    def desbloquear_radioButton_2(self):
        if self.radioButton_2.isChecked():
            self.radioButton_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
        else:
            self.radioButton_2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
    def desbloquear_Todos(self):

        if self.Todos.isChecked():
            self.Todos.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.CA.setEnabled(False)
            self.CB.setEnabled(False)
            self.C5.setEnabled(False)
            self.C6.setEnabled(False)
            self.D1.setEnabled(False)
            self.D2.setEnabled(False)
            self.D3.setEnabled(False)
            self.D4.setEnabled(False)
            self.CA.setChecked(True)
            self.CB.setChecked(True)
            self.C5.setChecked(True)
            self.C6.setChecked(True)
            self.D1.setChecked(True)
            self.D2.setChecked(True)
            self.D3.setChecked(True)
            self.D4.setChecked(True)
            self.CA.setStyleSheet("background-color: a(0);")
            self.CB.setStyleSheet("background-color: a(0);")
            self.C5.setStyleSheet("background-color: a(0);")
            self.C6.setStyleSheet("background-color: a(0);")
            self.D1.setStyleSheet("background-color: a(0);")
            self.D2.setStyleSheet("background-color: a(0);")
            self.D3.setStyleSheet("background-color: a(0);")
            self.D4.setStyleSheet("background-color: a(0);")
        else:
            self.Todos.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.CA.setEnabled(True)
            self.CB.setEnabled(True)
            self.C5.setEnabled(True)
            self.C6.setEnabled(True)
            self.D1.setEnabled(True)
            self.D2.setEnabled(True)
            self.D3.setEnabled(True)
            self.D4.setEnabled(True)
            self.CA.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.CB.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.C5.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.C6.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.D1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.D2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.D3.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.D4.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
    def desbloquear_heater_1(self):
        global label_scroll
        if self.heater_1.isChecked():
            try:
                #self.On_335_1()
                self.heater_1.setStyleSheet("background-color: a(0);color: rgb(255, 240, 23);font: 15pt 'Sans Serif';")
                self.label_7.setStyleSheet("background-color: a(0);color: rgb(255, 255, 255);")
                self.label_13.setStyleSheet("background-color: a(0);color: rgb(255, 255, 255);")
                self.setPoint_num_1.setEnabled(True)
                self.label_9.setStyleSheet("background-color: a(0);color: rgb(255, 255, 255);")
                self.label.setStyleSheet("background-color: a(0);color: rgb(255, 255, 255);")
                self.ramp_1.setEnabled(True)
                self.label_10.setStyleSheet("background-color: a(0);color: rgb(255, 255, 255);")
                self.range_automatic_1.setEnabled(True)
                self.range_automatic_1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                self.range_manual_1.setEnabled(True)
                self.range_manual_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
                self.seeStatus_1.setEnabled(True)
                self.seeStatus_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);font: 12pt 'Sans Serif';")
                self.update_1.setEnabled(True)
                self.Off_1.setEnabled(True)
                if self.grafica2.isChecked():
                    self.SetPoint1.setEnabled(False)
                    self.heater1.setEnabled(False)
                    self.SetPoint1.setChecked(False)
                    self.heater1.setChecked(False)
                    self.graph_heater_la.setStyleSheet(" ")
                    self.color_heater.setStyleSheet(" ")
                    self.SetPoint1.setStyleSheet("background-color: a(0);")
                    self.heater1.setStyleSheet("background-color: a(0);")
                else:
                    self.SetPoint1.setEnabled(True)
                    self.heater1.setEnabled(True)
                    self.graph_heater_la.setStyleSheet("color:rgb(255,255,255);")
                    self.color_heater.setStyleSheet("color:rgb(255,255,255);")
                    self.SetPoint1.setStyleSheet("background-color: a(0);color:rgb(88, 160, 255);")
                    self.heater1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            except:
                label_scroll += '                     Error al cargar Heater 1'
                self.heater_1.setStyleSheet("background-color: a(0);color: rgb(0,255, 0);font: 15pt 'Sans Serif';")
                self.Update_label()
                self.label_13.setStyleSheet("background-color: a(0);")
                self.label_7.setStyleSheet("background-color: a(0);")
                self.setPoint_num_1.setEnabled(False)
                self.label_9.setStyleSheet("background-color: a(0);")
                self.label.setStyleSheet("background-color: a(0);")
                self.ramp_1.setEnabled(False)
                self.label_10.setStyleSheet("background-color: a(0);")
                self.range_automatic_1.setChecked(True)
                self.range_automatic_1.setEnabled(False)
                self.range_automatic_1.setStyleSheet("background-color: a(0);")
                self.range_manual_1.setEnabled(False)
                self.range_manual_1.setStyleSheet("background-color: a(0);")
                self.seeStatus_1.setEnabled(False)
                self.seeStatus_1.setStyleSheet("background-color: a(0);font: 12pt 'Sans Serif';")
                self.seeStatus_1.setChecked(False)
                self.update_1.setEnabled(False)
                self.Off_1.setEnabled(False)
                self.SetPoint1.setEnabled(False)
                self.heater1.setEnabled(False)
                self.SetPoint1.setChecked(False)
                self.heater1.setChecked(False)
                self.graph_heater_la.setStyleSheet(" ")
                self.color_heater.setStyleSheet(" ")
                self.SetPoint1.setStyleSheet("background-color: a(0);")
                self.heater1.setStyleSheet("background-color: a(0);")
            
        else:
            self.heater_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);font: 15pt 'Sans Serif';")
            self.label_13.setStyleSheet("background-color: a(0);")
            self.label_7.setStyleSheet("background-color: a(0);")
            self.setPoint_num_1.setEnabled(False)
            self.label_9.setStyleSheet("background-color: a(0);")
            self.label.setStyleSheet("background-color: a(0);")
            self.ramp_1.setEnabled(False)
            self.label_10.setStyleSheet("background-color: a(0);")
            self.range_automatic_1.setChecked(True)
            self.range_automatic_1.setEnabled(False)
            self.range_automatic_1.setStyleSheet("background-color: a(0);")
            self.range_manual_1.setEnabled(False)
            self.range_manual_1.setStyleSheet("background-color: a(0);")
            self.seeStatus_1.setEnabled(False)
            self.seeStatus_1.setChecked(False)
            self.seeStatus_1.setStyleSheet("background-color: a(0);font: 12pt 'Sans Serif';")
            self.update_1.setEnabled(False)
            self.Off_1.setEnabled(False)
            self.SetPoint1.setEnabled(False)
            self.heater1.setEnabled(False)
            self.SetPoint1.setChecked(False)
            self.heater1.setChecked(False)
            self.graph_heater_la.setStyleSheet(" ")
            self.color_heater.setStyleSheet(" ")
            self.SetPoint1.setStyleSheet("background-color: a(0);")
            self.heater1.setStyleSheet("background-color: a(0);")
            #self.off_heater_1()
    def desbloquear_heater_2(self):
        global label_scroll
        if self.heater_2.isChecked():
            try:
                self.On_335_2()
            except:
                label_scroll += '                                   Error al cargar Heater 2'
                self.Update_label()
            self.setPoint_num_2.setEnabled(True)
            self.ramp_2.setEnabled(True)
            self.range_automatic_2.setEnabled(True)
            self.range_manual_2.setEnabled(True)
            self.seeStatus_2.setEnabled(True)
            self.update_2.setEnabled(True)
            self.Off_2.setEnabled(True)
            if self.grafica2.isChecked():
                self.SetPoint2.setEnabled(False)
                self.heater2.setEnabled(False)
                self.SetPoint2.setChecked(False)
                self.heater2.setChecked(False)
            else:
                self.SetPoint2.setEnabled(True)
                self.heater2.setEnabled(True)

        else:
            self.setPoint_num_2.setEnabled(False)
            self.ramp_2.setEnabled(False)
            self.range_automatic_2.setEnabled(False)
            self.range_manual_2.setEnabled(False)
            self.seeStatus_2.setEnabled(False)
            self.update_2.setEnabled(False)
            self.Off_2.setEnabled(False)
            self.SetPoint2.setEnabled(False)
            self.heater2.setEnabled(False)
    def desbloquear_range_manual_1(self):
        if self.range_manual_1.isChecked():
            self.range_manual_1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.range_1.setEnabled(True)
        else:
            self.range_manual_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.range_1.setEnabled(False)
    def desbloquear_range_automatic_1(self):
        if self.range_automatic_1.isChecked():
            self.range_automatic_1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
        else:
            self.range_automatic_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
    def desbloquear_range_manual_2(self):
        if self.range_manual_2.isChecked():
            self.range_manual_2.setStyleSheet("background-color: a(0);color: rgb(0, 255,0);")
            self.range_2.setEnabled(True)
        else:
            self.range_manual_2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.range_2.setEnabled(False)
    def desbloquear_range_automatic_2(self):
        if self.range_automatic_2.isChecked():
            self.range_automatic_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
        else:
            self.range_automatic_2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
    def desbloquear_seeStatus_1(self):
        if self.seeStatus_1.isChecked():
            self.seeStatus_1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);font: 12pt 'Sans Serif';")
            self.status_1.setEnabled(True)
            global heater_1_estatus, status_heater_1,label_heater_1
            status_heater_1 = True
            if heater_1_estatus:
                label_heater_1 += '--------------------------------------\n'
                label_heater_1 += '       Status Heater 1      \n'
                label_heater_1 += '--------------------------------------\n'
                heater_1_estatus = False
            self.status_1.setWidget(QtWidgets.QLabel(label_heater_1))
        else:
            self.seeStatus_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);font: 12pt 'Sans Serif';")
            status_heater_1 = False
            self.status_1.verticalScrollBar().setValue(self.status_1.verticalScrollBar().maximum())
    def desbloquear_seeStatus_2(self):
        if self.seeStatus_2.isChecked():
            self.seeStatus_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.status_2.setEnabled(True)
        else:
            self.seeStatus_2.setStyleSheet("background-color: a(0);rgb(88, 160, 255);")
    def desbloquear_sensores_CA(self):
        global textDict_color
        if self.CA.isChecked():
            self.CA.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_CA.setEnabled(True)
            self.ramp_CA.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['CA']
            self.color_CA.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.CA.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_CA.setEnabled(False)
            self.ramp_CA.setEnabled(False)
            self.ramp_CA.setChecked(False)
            self.color_CA.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_CB(self):
        global textDict_color
        if self.CB.isChecked():
            self.CB.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_CB.setEnabled(True)
            self.ramp_CB.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['CB']
            self.color_CB.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.CB.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_CB.setEnabled(False)
            self.ramp_CB.setEnabled(False)
            self.ramp_CB.setChecked(False)
            self.color_CB.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_C5(self):
        global textDict_color
        if self.C5.isChecked():
            self.C5.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_C5.setEnabled(True)
            self.ramp_C5.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['C5']
            self.color_C5.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.C5.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_C5.setEnabled(False)
            self.ramp_C5.setEnabled(False)
            self.ramp_C5.setChecked(False)
            self.color_C5.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_C6(self):
        global textDict_color
        if self.C6.isChecked():
            self.C6.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_C6.setEnabled(True)
            self.ramp_C6.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['C6']
            self.color_C6.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.C6.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_C6.setEnabled(False)
            self.ramp_C6.setEnabled(False)
            self.ramp_C6.setChecked(False)
            self.color_C6.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_D1(self):
        global textDict_color
        if self.D1.isChecked():
            self.D1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_D1.setEnabled(True)
            self.ramp_D1.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['D1']
            self.color_D1.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.D1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_D1.setEnabled(False)
            self.ramp_D1.setEnabled(False)
            self.ramp_D1.setChecked(False)
            self.color_D1.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_D2(self):
        global textDict_color
        if self.D2.isChecked():
            self.D2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_D2.setEnabled(True)
            self.ramp_D2.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['D2']
            self.color_D2.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.D2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_D2.setEnabled(False)
            self.ramp_D2.setEnabled(False)
            self.color_D2.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_D3(self):
        global textDict_color
        if self.D3.isChecked():
            self.D3.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_D3.setEnabled(True)
            self.ramp_D3.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['D3']
            self.color_D3.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.D3.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_D3.setEnabled(False)
            self.ramp_D3.setEnabled(False)
            self.ramp_D3.setChecked(False)
            self.color_D3.setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_D4(self):
        global textDict_color
        if self.D4.isChecked():
            self.D4.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_D4.setEnabled(True)
            self.ramp_D4.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['D4']
            self.color_D4.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.D4.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_D4.setEnabled(False)
            self.ramp_D4.setEnabled(False)
            self.ramp_D4.setChecked(False)
            self.color_D4.setStyleSheet("background-color: a(0);")
    def desbloquear_heater1(self):
        global textDict_color
        if self.heater1.isChecked():
            self.heater1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_H1.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['H1']
            self.color_H1.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.heater1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_H1.setEnabled(False)
            self.color_H1.setStyleSheet("background-color: a(0);")
    def desbloquear_heater2(self):
        global textDict_color
        if self.heater2.isChecked():
            self.heater2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_H2.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['H2']
            self.color_H2.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.heater2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_H2.setEnabled(False)
            self.color_H2.setStyleSheet("background-color: a(0);")
    def desbloquear_SetPoint1(self):
        global textDict_color
        if self.SetPoint1.isChecked():
            self.SetPoint1.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_S1.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['S1']
            self.color_S1.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.SetPoint1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_S1.setEnabled(False)
            self.color_S1.setStyleSheet("background-color: a(0);")
    def desbloquear_SetPoint2(self):
        global textDict_color
        if self.SetPoint2.isChecked():
            self.SetPoint2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_S2.setEnabled(True)
            color_rgb = textDict_color.ConfigDict['S2']
            self.color_S2.setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.SetPoint2.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_S2.setEnabled(False)
            self.color_S2.setStyleSheet("background-color: a(0);")
    def update_plot(self):
        global curvas, curvas_last, plt_mgr, textDict_color, color_last
        if self.radioButton.isChecked():
            horas = self.hh.value()
            minutos = self.mm.value()
            segundos = self.ss.value()
            Time_graph = horas*3600 + minutos*60 + segundos
        else:
            Time_graph = float('inf')
        if curvas == curvas_last:
            if textDict_color == color_last:
                pass
            else:
                color_last = textDict_color.ConfigDict
                plt_mgr.update_curvas()  
        else:
            curvas_last = curvas
            if self.Todos.isChecked():
                    curvas[0] = 1
            else:
                    if self.CA.isChecked():
                        curvas[1] = 1
                        self.see_ramp.setEnabled(True)
                    if self.CB.isChecked():
                        curvas[2] = 1
                    if self.D1.isChecked():
                        curvas[3] = 1
                    if self.D2.isChecked():
                        curvas[4] = 1
                    if self.D3.isChecked():
                        curvas[5] = 1
                    if self.D4.isChecked():
                        curvas[6] = 1
                    if self.C5.isChecked():
                        curvas[7] = 1
                    if self.C6.isChecked():
                        curvas[8] = 1
            if self.SetPoint1.isChecked():
                    curvas[9] = 1
            if self.heater1.isChecked():
                    curvas[10] = 1
            if self.SetPoint2.isChecked():
                    curvas[11] = 1
            if self.heater2.isChecked():
                    curvas[12] = 1
            if textDict_color == color_last:
                color_last = textDict_color.ConfigDict
            plt_mgr.update_curvas()
    def graficar(self):
        global actual,close_plot,DataTemp, DataTemp2, curvas, curvas_last, textDict_color,color_last
        curvas = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        if self.Todos.isChecked():
                curvas[0] = 1
        else:
                if self.CA.isChecked():
                    curvas[1] = 1
                    self.see_ramp.setEnabled(True)
                if self.CB.isChecked():
                    curvas[2] = 1
                if self.D1.isChecked():
                    curvas[3] = 1
                if self.D2.isChecked():
                    curvas[4] = 1
                if self.D3.isChecked():
                    curvas[5] = 1
                if self.D4.isChecked():
                    curvas[6] = 1
                if self.C5.isChecked():
                    curvas[7] = 1
                if self.C6.isChecked():
                    curvas[8] = 1
        if self.SetPoint1.isChecked():
                curvas[9] = 1
        if self.heater1.isChecked():
                curvas[10] = 1
        if self.SetPoint2.isChecked():
                curvas[11] = 1
        if self.heater2.isChecked():
                curvas[12] = 1

           #     print(b)
        if self.grafica1.isChecked():
            global plt_mgr,Time_graph
            actual, close_plot = True, False
            plt_mgr = LivePlotter()
            curvas_last = curvas
            color_last = textDict_color.ConfigDict
        else:
            actual = False
            self.matplotlib()
        if self.radioButton.isChecked():
            horas = self.hh.value()
            minutos = self.mm.value()
            segundos = self.ss.value()
            Time_graph = horas*3600 + minutos*60 + segundos
        else:
            Time_graph = float('inf')
    def matplotlib(self):
        mpl = Lienzo()
        mpl.show()

class LivePlotter(object):

    global curvas, textDict_color

    def __init__(self):
        self.win = pg.GraphicsWindow(title='Data')
        self.p = self.win.addPlot(title='Sensores')
        self.p.setLabel('left', 'Temperature ',units= 'K')
        self.p.setLabel('bottom', 'Time ',units='s')
        self.p.showGrid(x=False,y=True,alpha=0.3)
        self.p.addLegend()
        if curvas[0] == 1:
            self.curva1=self.p.plot(pen=(int(textDict_color.ConfigDict['CA'][0]),\
                                         int(textDict_color.ConfigDict['CA'][1]),\
                                         int(textDict_color.ConfigDict['CA'][2])),\
                                         name='CernoxA')
            self.curva2=self.p.plot(pen=(int(textDict_color.ConfigDict['CB'][0]),\
                                        int(textDict_color.ConfigDict['CB'][1]),\
                                        int(textDict_color.ConfigDict['CB'][2])),\
                                        name='CernoxB')
            self.curva3=self.p.plot(pen=(int(textDict_color.ConfigDict['D1'][0]),\
                                        int(textDict_color.ConfigDict['D1'][1]),\
                                        int(textDict_color.ConfigDict['D1'][2])),\
                                        name='Diodo1')
            self.curva4=self.p.plot(pen=(int(textDict_color.ConfigDict['D2'][0]),\
                                        int(textDict_color.ConfigDict['D2'][1]),\
                                        int(textDict_color.ConfigDict['D2'][2])),\
                                        name='Diodo2')
            self.curva5=self.p.plot(pen=(int(textDict_color.ConfigDict['D3'][0]),\
                                        int(textDict_color.ConfigDict['D3'][1]),\
                                        int(textDict_color.ConfigDict['D3'][2])),\
                                        name='Diodo3')
            self.curva6=self.p.plot(pen=(int(textDict_color.ConfigDict['D4'][0]),\
                                        int(textDict_color.ConfigDict['D4'][1]),\
                                        int(textDict_color.ConfigDict['D4'][2])),\
                                        name='Diodo4')
            self.curva7=self.p.plot(pen=(int(textDict_color.ConfigDict['C5'][0]),\
                                        int(textDict_color.ConfigDict['C5'][1]),\
                                        int(textDict_color.ConfigDict['C5'][2])),\
                                        name='Cernox5')
            self.curva8=self.p.plot(pen=(int(textDict_color.ConfigDict['C6'][0]),\
                                        int(textDict_color.ConfigDict['C6'][1]),\
                                        int(textDict_color.ConfigDict['C6'][2])),\
                                        name='Cernox6')
            self.Data_curva1,self.Time_curva1=[],[]
            self.Data_curva2,self.Time_curva2=[],[]
            self.Data_curva3,self.Time_curva3=[],[]
            self.Data_curva4,self.Time_curva4=[],[]
            self.Data_curva5,self.Time_curva5=[],[]
            self.Data_curva6,self.Time_curva6=[],[]
            self.Data_curva7,self.Time_curva7=[],[]
            self.Data_curva8,self.Time_curva8=[],[]
        else:
            if curvas[1] == 1:
                self.curva1=self.p.plot(pen=(int(textDict_color.ConfigDict['CA'][0]),\
                                            int(textDict_color.ConfigDict['CA'][1]),\
                                            int(textDict_color.ConfigDict['CA'][2])),\
                                            name='CernoxA')
                self.Data_curva1,self.Time_curva1=[],[]
            if curvas[2] == 1:
                self.curva2=self.p.plot(pen=(int(textDict_color.ConfigDict['CB'][0]),\
                                            int(textDict_color.ConfigDict['CB'][1]),\
                                            int(textDict_color.ConfigDict['CB'][2])),\
                                            name='CernoxB')
                self.Data_curva2,self.Time_curva2=[],[]
            if curvas[3] == 1:
                self.curva3=self.p.plot(pen=(int(textDict_color.ConfigDict['D1'][0]),\
                                            int(textDict_color.ConfigDict['D1'][1]),\
                                            int(textDict_color.ConfigDict['D1'][2])),\
                                            name='Diodo1')
                self.Data_curva3,self.Time_curva3=[],[]
            if curvas[4] == 1:
                self.curva4=self.p.plot(pen=(int(textDict_color.ConfigDict['D2'][0]),\
                                            int(textDict_color.ConfigDict['D2'][1]),\
                                            int(textDict_color.ConfigDict['D2'][2])),\
                                            name='Diodo2')
                self.Data_curva4,self.Time_curva4=[],[]
            if curvas[5] == 1:
                self.curva5=self.p.plot(pen=(int(textDict_color.ConfigDict['D3'][0]),\
                                            int(textDict_color.ConfigDict['D3'][1]),\
                                            int(textDict_color.ConfigDict['D3'][2])),\
                                            name='Diodo3')
                self.Data_curva5,self.Time_curva5=[],[]
            if curvas[6] == 1:
                self.curva6=self.p.plot(pen=(int(textDict_color.ConfigDict['D4'][0]),\
                                            int(textDict_color.ConfigDict['D4'][1]),\
                                            int(textDict_color.ConfigDict['D4'][2])),\
                                            name='Diodo4')
                self.Data_curva6,self.Time_curva6=[],[]
            if curvas[7] == 1:
                self.curva7=self.p.plot(pen=(int(textDict_color.ConfigDict['C5'][0]),\
                                            int(textDict_color.ConfigDict['C5'][1]),\
                                            int(textDict_color.ConfigDict['C5'][2])),\
                                            name='Cernox5')
                self.Data_curva7,self.Time_curva7=[],[]
            if curvas[8] == 1:
                self.curva8=self.p.plot(pen=(int(textDict_color.ConfigDict['C6'][0]),\
                                            int(textDict_color.ConfigDict['C6'][1]),\
                                            int(textDict_color.ConfigDict['C6'][2])),\
                                            name='Cernox6')
                self.Data_curva8,self.Time_curva8=[],[]
        if curvas[9] == 1:
            self.curva9 = self.p.plot(pen=(int(textDict_color.ConfigDict['S1'][0]),\
                                            int(textDict_color.ConfigDict['S1'][1]),\
                                            int(textDict_color.ConfigDict['S1'][2])),\
                                            name='SetPoint-1')
            self.Data_curva9,self.Time_curva9=[],[]
        if curvas[10] == 1:
            self.curva10 = self.p.plot(pen=(int(textDict_color.ConfigDict['H1'][0]),\
                                            int(textDict_color.ConfigDict['H1'][1]),\
                                            int(textDict_color.ConfigDict['H1'][2])), \
                                            name = 'Heater-1')
            self.Data_curva10,self.Time_curva10=[],[]
        if curvas[11] == 1:
            self.curva11 = self.p.plot(pen=(int(textDict_color.ConfigDict['S2'][0]),\
                                            int(textDict_color.ConfigDict['S2'][1]),\
                                            int(textDict_color.ConfigDict['S2'][2])),\
                                            name = 'SetPoint-2')
            self.Data_curva11,self.Time_curva11=[],[]
        if curvas[12] == 1:
            self.curva12 = self.p.plot(pen=(int(textDict_color.ConfigDict['H2'][0]),\
                                            int(textDict_color.ConfigDict['H2'][1]),\
                                            int(textDict_color.ConfigDict['H2'][2])),\
                                            name = 'Heater-2')
            self.Data_curva12,self.Time_curva12=[],[]
        self.p.setRange(yRange=[50, 300])
    def update_curvas(self):
            if curvas[1] == 1:
                self.curva1=self.p.plot(pen=(int(textDict_color.ConfigDict['CA'][0]),\
                                            int(textDict_color.ConfigDict['CA'][1]),\
                                            int(textDict_color.ConfigDict['CA'][2])),\
                                            name='CernoxA')
            else:
                self.Data_curva1,self.Time_curva1=[],[]
            if curvas[2] == 1:
                self.curva2=self.p.plot(pen=(int(textDict_color.ConfigDict['CB'][0]),\
                                            int(textDict_color.ConfigDict['CB'][1]),\
                                            int(textDict_color.ConfigDict['CB'][2])),\
                                            name='CernoxB')
            else:
                self.Data_curva2,self.Time_curva2=[],[]
            if curvas[3] == 1:
                self.curva3=self.p.plot(pen=(int(textDict_color.ConfigDict['D1'][0]),\
                                            int(textDict_color.ConfigDict['D1'][1]),\
                                            int(textDict_color.ConfigDict['D1'][2])),\
                                            name='Diodo1')
            else:
                self.Data_curva3,self.Time_curva3=[],[]
            if curvas[4] == 1:
                self.curva4=self.p.plot(pen=(int(textDict_color.ConfigDict['D2'][0]),\
                                            int(textDict_color.ConfigDict['D2'][1]),\
                                            int(textDict_color.ConfigDict['D2'][2])),\
                                            name='Diodo2')
            else:
                self.Data_curva4,self.Time_curva4=[],[]
            if curvas[5] == 1:
                self.curva5=self.p.plot(pen=(int(textDict_color.ConfigDict['D3'][0]),\
                                            int(textDict_color.ConfigDict['D3'][1]),\
                                            int(textDict_color.ConfigDict['D3'][2])),\
                                            name='Diodo3')
            else:
                self.Data_curva5,self.Time_curva5=[],[]
            if curvas[6] == 1:
                self.curva6=self.p.plot(pen=(int(textDict_color.ConfigDict['D4'][0]),\
                                            int(textDict_color.ConfigDict['D4'][1]),\
                                            int(textDict_color.ConfigDict['D4'][2])),\
                                            name='Diodo4')
            else:
                self.Data_curva6,self.Time_curva6=[],[]
            if curvas[7] == 1:
                self.curva7=self.p.plot(pen=(int(textDict_color.ConfigDict['C5'][0]),\
                                            int(textDict_color.ConfigDict['C5'][1]),\
                                            int(textDict_color.ConfigDict['C5'][2])),\
                                            name='Cernox5')
            else:
                self.Data_curva7,self.Time_curva7=[],[]
            if curvas[8] == 1:
                self.curva8=self.p.plot(pen=(int(textDict_color.ConfigDict['C6'][0]),\
                                            int(textDict_color.ConfigDict['C6'][1]),\
                                            int(textDict_color.ConfigDict['C6'][2])),\
                                            name='Cernox6')
            else:
                self.Data_curva8,self.Time_curva8=[],[]
            if curvas[9] == 1:
                self.curva9 = self.p.plot(pen=(int(textDict_color.ConfigDict['S1'][0]),\
                                                int(textDict_color.ConfigDict['S1'][1]),\
                                                int(textDict_color.ConfigDict['S1'][2])),\
                                                name='SetPoint-1')
            else:
                self.Data_curva9,self.Time_curva9=[],[]
            if curvas[10] == 1:
                self.curva10 = self.p.plot(pen=(int(textDict_color.ConfigDict['H1'][0]),\
                                                int(textDict_color.ConfigDict['H1'][1]),\
                                                int(textDict_color.ConfigDict['H1'][2])), \
                                                name = 'Heater-1')
            else:
                self.Data_curva10,self.Time_curva10=[],[]
            if curvas[11] == 1:
                self.curva11 = self.p.plot(pen=(int(textDict_color.ConfigDict['S2'][0]),\
                                                int(textDict_color.ConfigDict['S2'][1]),\
                                                int(textDict_color.ConfigDict['S2'][2])),\
                                                name = 'SetPoint-2')
            else:
                self.Data_curva11,self.Time_curva11=[],[]
            if curvas[12] == 1:
                self.curva12 = self.p.plot(pen=(int(textDict_color.ConfigDict['H2'][0]),\
                                                int(textDict_color.ConfigDict['H2'][1]),\
                                                int(textDict_color.ConfigDict['H2'][2])),\
                                                name = 'Heater-2')
            else:
                self.Data_curva12,self.Time_curva12=[],[]
    def return_data(self):
        return self.Data_curva1,self.Time_curva1

    def add(self, x):
            global Time_graph
            if curvas[0] == 1:
                self.Data_curva1,self.Time_curva1 = self.Curvas_add(self.Data_curva1,\
                                                    self.Time_curva1,float(x[0][2]),x[0][1])
                self.Data_curva2,self.Time_curva2 = self.Curvas_add(self.Data_curva2, \
                                                    self.Time_curva2,float(x[1][2]),x[1][1])
                self.Data_curva3,self.Time_curva3 = self.Curvas_add(self.Data_curva3, \
                                                    self.Time_curva3,float(x[2][2]),x[2][1])
                self.Data_curva4,self.Time_curva4 = self.Curvas_add(self.Data_curva4, \
                                                    self.Time_curva4,float(x[3][2]),x[3][1])
                self.Data_curva5,self.Time_curva5 = self.Curvas_add(self.Data_curva5, \
                                                    self.Time_curva5,float(x[4][2]),x[4][1])
                self.Data_curva6,self.Time_curva6 = self.Curvas_add(self.Data_curva6, \
                                                    self.Time_curva6,float(x[5][2]),x[5][1])
                self.Data_curva7,self.Time_curva7 = self.Curvas_add(self.Data_curva7, \
                                                    self.Time_curva7,float(x[6][2])*1.0257-2.1852,x[6][1])
                self.Data_curva8,self.Time_curva8 = self.Curvas_add(self.Data_curva8, \
                                                    self.Time_curva8,float(x[7][2])*1.0151-0.7786,x[7][1])
            else:
                if curvas[1] == 1:
                    self.Data_curva1,self.Time_curva1 = self.Curvas_add(self.Data_curva1,\
                                                        self.Time_curva1,float(x[0][2]),x[0][1])
                if curvas[2] == 1:
                    self.Data_curva2,self.Time_curva2 = self.Curvas_add(self.Data_curva2,\
                                                        self.Time_curva2,float(x[1][2]),x[1][1])
                if curvas[3] == 1:
                    self.Data_curva3,self.Time_curva3 = self.Curvas_add(self.Data_curva3,\
                                                        self.Time_curva3,float(x[2][2]),x[2][1])
                if curvas[4] == 1:
                    self.Data_curva4,self.Time_curva4 = self.Curvas_add(self.Data_curva4, \
                                                        self.Time_curva4,float(x[3][2]),x[3][1])
                if curvas[5] == 1:
                    self.Data_curva5,self.Time_curva5 = self.Curvas_add(self.Data_curva5, \
                                                        self.Time_curva5,float(x[4][2]),x[4][1])
                if curvas[6] == 1:
                    self.Data_curva6,self.Time_curva6 = self.Curvas_add(self.Data_curva6, \
                                                        self.Time_curva6,float(x[5][2]),x[5][1])
                if curvas[7] == 1:
                    self.Data_curva7,self.Time_curva7 = self.Curvas_add(self.Data_curva7, \
                                                        self.Time_curva7,float(x[6][2])*1.0257-2.1852,x[6][1])

                if curvas[8] == 1:
                    self.Data_curva8,self.Time_curva8 = self.Curvas_add(self.Data_curva8, \
                                                        self.Time_curva8,float(x[7][2])*1.0151-0.7786,x[7][1])

            if curvas[9] == 1:
                self.Data_curva9,self.Time_curva9 = self.Curvas_add(self.Data_curva9, \
                                                    self.Time_curva9,SP_1,x[7][1])

            if curvas[10] == 1:
                HTR_1 = float(DataTemp2.Read_335('SETP?','1'))
                self.Data_curva10,self.Time_curva10 = self.Curvas_add(self.Data_curva10, \
                                                      self.Time_curva10,HTR_1,x[7][1])
                time.sleep(0.05)

            if curvas[11] == 1:
                self.Data_curva11,self.Time_curva11 = self.Curvas_add(self.Data_curva11, \
                                                      self.Time_curva11,SP_2,x[7][1])

            if curvas[12] == 1:
                HTR_2 = float(DataTemp2.Read_335('SETP?','2'))
                self.Data_curva12,self.Time_curva12 = self.Curvas_add(self.Data_curva12,\
                                                      self.Time_curva12,HTR_2,x[7][1])
                time.sleep(0.05)

            global actual
           # actual = False
            pg.QtGui.QApplication.processEvents()

    def Curvas_add(self,Datos_curvas,Tiempo_curvas,datos,tiempos):
        Datos_curvas.append(datos)
        Tiempo_curvas.append(tiempos)
        for i in range(len(Tiempo_curvas)):
            if Tiempo_curvas[-1]-Tiempo_curvas[0] > Time_graph:
                Datos_curvas,Tiempo_curvas = self.Quitar_datos(Datos_curvas,Tiempo_curvas)
            else:
                break
            pg.QtGui.QApplication.processEvents()
        return Datos_curvas,Tiempo_curvas


    def Quitar_datos(self, Arreglo_curvas,Arreglo_tiempo):
        Arreglo_curvas = Arreglo_curvas[-(len(Arreglo_curvas)-1):]
        Arreglo_tiempo = Arreglo_tiempo[-(len(Arreglo_tiempo)-1):]
        return Arreglo_curvas,Arreglo_tiempo


    def update(self):
        #try:
            if curvas[0] == 1:
                self.curva1.setData(self.Time_curva1,self.Data_curva1)
                self.curva2.setData(self.Time_curva2,self.Data_curva2)
                self.curva3.setData(self.Time_curva3,self.Data_curva3)
                self.curva4.setData(self.Time_curva4,self.Data_curva4)
                self.curva5.setData(self.Time_curva5,self.Data_curva5)
                self.curva6.setData(self.Time_curva6,self.Data_curva6)
                self.curva7.setData(self.Time_curva7,self.Data_curva7)
                self.curva8.setData(self.Time_curva8,self.Data_curva8)
            else:
                if curvas[1] == 1:
                    self.curva1.setData(self.Time_curva1,self.Data_curva1)
                if curvas[2] == 1:
                    self.curva2.setData(self.Time_curva2,self.Data_curva2)
                if curvas[3] == 1:
                    self.curva3.setData(self.Time_curva3,self.Data_curva3)
                if curvas[4] == 1:
                    self.curva4.setData(self.Time_curva4,self.Data_curva4)
                if curvas[5] == 1:
                    self.curva5.setData(self.Time_curva5,self.Data_curva5)
                if curvas[6] == 1:
                    self.curva6.setData(self.Time_curva6,self.Data_curva6)
                if curvas[7] == 1:
                    self.curva7.setData(self.Time_curva7,self.Data_curva7)
                if curvas[8] == 1:
                    self.curva8.setData(self.Time_curva8,self.Data_curva8)
            if curvas[9] == 1:
                self.curva9.setData(self.Time_curva9,self.Data_curva9)
            if curvas[10] == 1:
                self.curva10.setData(self.Time_curva10,self.Data_curva10)
            if curvas[11] == 1:
                self.curva11.setData(self.Time_curva11,self.Data_curva11)
            if curvas[12] == 1:
                self.curva12.setData(self.Time_curva12,self.Data_curva12)
     #   except Exception as e:

      #pass

    def close(self):
        try:
            self.win.close()
        except Exception as e:
            pass

class Ramp(object):
    def __init__(self):
        self.win = pg.GraphicsWindow(title='Data')
        self.p = self.win.addPlot(title='RAMP')
        self.p.setLabel('left', 'RAMP ',units= 'K/min')
        self.p.setLabel('bottom', 'Time ',units='s')
        self.p.showGrid(x=False,y=True,alpha=0.3)
        self.p.addLegend()
        self.curva1=self.p.plot(pen=(255,255,255),width=10,name='Rampa-CernoxB')


    def deriv_h4_no_uniforme(self,f,x):
        f_prima = [0]*len(f)  #definimos la longitud de la funcion f
        for i in range(2,len(f)-2): #tomamos un intervalo despreciando el primero, segundo, penúltimo y último término
            hi_2,hi_1,hi1, hi2 = x[i]-x[i-2],x[i]-x[i-1],x[i+1]-x[i],x[i+2]-x[i] # definimos las h utilizadas
            a,b,c,d=hi_2*hi1,hi2*hi_1,hi_1*hi1,hi2*hi_2 #definimos terminos que aparecen constantemente en la formula
            #implementamos la derivada
            f_prima[i] = ((1/(a)+1/(b)-1/(c)-1/(d))**-1)\
                       *(f[i] \
                       *((hi2-hi_1)/((b)**2) \
                       +(hi1-hi_2)/((a)**2)\
                       -(hi1-hi_1)/((c)**2)\
                       -(hi2-hi_2)/((d)**2))\
                       -(hi_1**2*f[i+1]-hi1**2*f[i-1])/((hi_1+hi1)*(c)**2)\
                       -(hi_2**2*f[i+2]-hi2**2*f[i-2])/((hi_2+hi2)*(d)**2)\
                       +(hi_1**2*f[i+2]-hi2**2*f[i-1])/((hi_1+hi2)*(b)**2)\
                       +(hi_2**2*f[i+1]-hi1**2*f[i-2])/((hi_2+hi1)*(a)**2))
            pg.QtGui.QApplication.processEvents()
        return f_prima


    def plot(self):
        global plt_mgr
        plot_data,plot_time = plt_mgr.return_data()
        data_plot = self.deriv_h4_no_uniforme(plot_data,plot_time)
        for i in range(len(data_plot)):
            data_plot[i] = data_plot[i]*60
        self.curva1.setData(plot_time,data_plot)


    def close(self):
        try:
            self.win.close()
        except Exception as e:
            pass

class Lienzo(FigureCanvas):

    def __init__(self):
        global DataTemp,DataTemp2
        self.figura = Figure()
        self.figura_2 = Figure()
        self.ejes = self.figura.add_subplot(111)
        b = []
        for name in [DataTemp2,DataTemp]:
            a = name.Plot_inter()
            for c in a:
                b.append(c)
        if curvas[0] == 1:
            self.ejes.plot(b[0][0], b[0][1],label='Cernox A',color=[int(textDict_color.ConfigDict['CA'][0])/255,\
                                                                    int(textDict_color.ConfigDict['CA'][1])/255,\
                                                                    int(textDict_color.ConfigDict['CA'][2])/255])
            self.ejes.plot(b[1][0], b[1][1],label='Cernox B',color=[int(textDict_color.ConfigDict['CB'][0])/255,\
                                                                    int(textDict_color.ConfigDict['CB'][1])/255,\
                                                                    int(textDict_color.ConfigDict['CB'][2])/255])
            self.ejes.plot(b[2][0],  b[2][1],label='Diodo 1',color=[int(textDict_color.ConfigDict['D1'][0])/255,\
                                                                    int(textDict_color.ConfigDict['D1'][1])/255,\
                                                                    int(textDict_color.ConfigDict['D1'][2])/255])
            self.ejes.plot(b[3][0],  b[3][1],label='Diodo 2',color=[int(textDict_color.ConfigDict['D2'][0])/255,\
                                                                    int(textDict_color.ConfigDict['D2'][1])/255,\
                                                                    int(textDict_color.ConfigDict['D2'][2])/255])
            self.ejes.plot(b[4][0],  b[4][1],label='Diodo 3',color=[int(textDict_color.ConfigDict['D3'][0])/255,\
                                                                    int(textDict_color.ConfigDict['D3'][1])/255,\
                                                                    int(textDict_color.ConfigDict['D3'][2])/255])
            self.ejes.plot(b[5][0],  b[5][1],label='Diodo 4',color=[int(textDict_color.ConfigDict['D4'][0])/255,\
                                                                    int(textDict_color.ConfigDict['D4'][1])/255,\
                                                                    int(textDict_color.ConfigDict['D4'][2])/255])
            self.ejes.plot(b[6][0], b[6][1],label='Cernox 5',color=[int(textDict_color.ConfigDict['C5'][0])/255,\
                                                                    int(textDict_color.ConfigDict['C5'][1])/255,\
                                                                    int(textDict_color.ConfigDict['C5'][2])/255])
            self.ejes.plot(b[7][0], b[7][1],label='Cernox 6',color=[int(textDict_color.ConfigDict['C6'][0])/255,\
                                                                    int(textDict_color.ConfigDict['C6'][1])/255,\
                                                                    int(textDict_color.ConfigDict['C6'][2])/255])

        else:
            if curvas[1] == 1:
                self.ejes.plot(b[0][0], b[0][1],label='Cernox A',color=[int(textDict_color.ConfigDict['CA'][0])/255,\
                                                                        int(textDict_color.ConfigDict['CA'][1])/255,
                                                                        int(textDict_color.ConfigDict['CA'][2])/255])
            if curvas[2] == 1:
                self.ejes.plot(b[1][0], b[1][1],label='Cernox B',color=[int(textDict_color.ConfigDict['CB'][0])/255,\
                                                                        int(textDict_color.ConfigDict['CB'][1])/255,\
                                                                        int(textDict_color.ConfigDict['CB'][2])/255])
            if curvas[3] == 1:
                self.ejes.plot(b[2][0],  b[2][1],label='Diodo 1',color=[int(textDict_color.ConfigDict['D1'][0])/255,\
                                                                        int(textDict_color.ConfigDict['D1'][1])/255,\
                                                                        int(textDict_color.ConfigDict['D1'][2])/255])
            if curvas[4] == 1:
                self.ejes.plot(b[3][0],  b[3][1],label='Diodo 2',color=[int(textDict_color.ConfigDict['D2'][0])/255,\
                                                                        int(textDict_color.ConfigDict['D2'][1])/255,\
                                                                        int(textDict_color.ConfigDict['D2'][2])/255])
            if curvas[5] == 1:
                self.ejes.plot(b[4][0],  b[4][1],label='Diodo 3',color=[int(textDict_color.ConfigDict['D3'][0])/255,\
                                                                        int(textDict_color.ConfigDict['D3'][1])/255,\
                                                                        int(textDict_color.ConfigDict['D3'][2])/255])
            if curvas[6] == 1:
                self.ejes.plot(b[5][0],  b[5][1],label='Diodo 4',color=[int(textDict_color.ConfigDict['D4'][0])/255,\
                                                                        int(textDict_color.ConfigDict['D4'][1])/255,\
                                                                        int(textDict_color.ConfigDict['D4'][2])/255])
            if curvas[7] == 1:
                self.ejes.plot(b[6][0], b[6][1],label='Cernox 5',color=[int(textDict_color.ConfigDict['C5'][0])/255,\
                                                                        int(textDict_color.ConfigDict['C5'][1])/255,\
                                                                        int(textDict_color.ConfigDict['C5'][2])/255])
            if curvas[8] == 1:
                self.ejes.plot(b[7][0], b[7][1],label='Cernox 6',color=[int(textDict_color.ConfigDict['C6'][0])/255,\
                                                                        int(textDict_color.ConfigDict['C6'][1])/255,\
                                                                        int(textDict_color.ConfigDict['C6'][2])/255])
        self.ejes.title.set_text("Plot of Data")
        self.ejes.set_xlabel("t [s]")
        self.ejes.set_ylabel("T [K]")
        self.ejes.grid(),self.ejes.legend()
        FigureCanvas.__init__(self,self.figura_2)
        self.canvas = FigureCanvas(self.figura)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)

#################################################################################################################



#----------------------------------------------------------
#Esta función remueve las listas vacías con caracteres ''
#----------------------------------------------------------

def FilterEmptyStrings(Data):
    DataF = list(filter(None,Data))
    return DataF

#----------------------------------------------------------
#Esta función se encarga de Remover el Header de los
#de texto para recuperar la cadena con los datos de las
#mediciones.
#----------------------------------------------------------

def RemoveHeaderFunction(root,name):
    StringData = ''
    for line in open(root + name):
            if line[0] == "#" :

                continue
            elif line[0] == "\n" :

                continue
            else:
                StringData += line + '\n'

    return StringData
#----------------------------------------------------------
#Esta función escribe encuentra el comando que fue
# seleccionado.
#----------------------------------------------------------
'''
def MenuCommandFunction(Command,ObjArray):
    if Command == 'help':
        print('\n------------------------------------------------------------\n')
        print('This program makes the data aquisition of a LakeShore modules\n')
        print('------------------------------------------------------------\n')
        print('------------------------------------------------------------')
        print('The options of this program are the next:\n')
        print('\t\t\t exit -- Saves and terminates the data aquisition')
        print('\t\t\t help -- Displays help information')
        print('\t\t\t str  -- Open .txt file')
        print('\t\t\t plot -- Plots the aquaried data')
        print('\t\t\t info -- Gives additional information of the program')
        print('\t\t\t config -- Allows to configure plotting to show all or only last acquired points')
        print('\t\t\t value -- Print the last values of temperature acquaried, if there is any')
        print('------------------------------------------------------------\n')
        print('Press any key + Enter to return to the data aquisition\n')
        input('')
        print('\n------------------------------------------------------------')
        print('The aquisition is in process again.')
        print('------------------------------------------------------------\n')

    elif Command == 'exit':
        try:
            TerminateFunction(ObjArray)

        except SystemExit:
            print('\n------------------------------------------------------------')
            print('The aquisition is over. You can find your data in:')
            for Obj in ObjArray:
                print(Obj.FileAddress)
            print('------------------------------------------------------------\n')
            sys.exit(0)
            return
        except:
            print('\nERROR: Error of unknown origin. Please terminate the process manually.')
            print('Warning: Manual termination could make some data be lost.')

    elif Command == 'plot':
        #try:
            for Obj in ObjArray:
                Obj.Plot(Obj.DataSerie)
        #except:
        #    print('\nERROR: Data cannot be plotted.')

    elif Command == 'str':
        try:
            for Obj in ObjArray:
                Obj.__str__()
        except:
            print('\nERROR: Text file cannot be shown.')

    elif Command == 'info':
        try:
            print('\n------------------------------------------------------------')
            print('This program was developed by: Jaime Octavio Guerra Pulido and Mauricio Martínez Montero')
            print('Version: 2.0')
            print('Date of last update: October 2019')
            print('This program is a modification of the original one to make it able to read two modules at the same time.')
            print('------------------------------------------------------------\n')
        except:
            print('\nERROR: Additional information cannot be shown.')
    elif Command == 'config':
        try:
            for Obj in ObjArray:
                print('\n------------------------------------------------------------')
                print('Plot starting from the begining (yes) or plot only last point (no)')
                print('Plot Configuration for ' + Obj.Brand +': '+ Obj.Device )
                print('\n------------------------------------------------------------')
                Obj.ConfigurePlotMethod()
        except:
            print('ERROR: Configuration cannot be done.')
    elif Command == 'value':
        try:
            for Obj in ObjArray:
                Obj.PrintValue()
            pass
        except:
            print('ERROR: Values cannot be printed.')

    else:
        return 1
    return 0

'''
#----------------------------------------------------------
#Esta función escribe datos en el archivo de texto de salida
#----------------------------------------------------------

def WriteToFile(root,name,Text):
    try:
        File = open(root + name, 'a', encoding='utf-8')
        File.writelines(Text)
        File.close()
        return Text
    except:
        print('ERROR: Cannot write in '+ root + name + ' file.')

#----------------------------------------------------------
#Esta función adjunta datos a archivos pickle
#----------------------------------------------------------

def AppendToPickleFile(root,name,Data):

    FilePickle = open(root + name,'ba')
    pickle.dump(Data,FilePickle)
    FilePickle.close()

#----------------------------------------------------------
#Esta función crea un archivo de texto donde se guardarán
#los datos obtenidos de las mediciones.
#----------------------------------------------------------

def FileHeader(root,name,textDict,MeasureType):
    HeaderText = "#--------------------------------------------------------------------\n"
    HeaderText += "#Temperature Measurments using a {} {} {}\n".format(textDict['Brand'],\
                    textDict['Device'],textDict['Model'])
    HeaderText += "#Type of file: " + MeasureType +"\n"
    HeaderText += "#Sensors: "
    #HeaderText += "Sensors: {} \n".format(textDict['Sensor type'])
    ListaSensores = textDict['Sensors']
    TipoSensores = textDict['Sensor Type']

    for Num, String in enumerate(TipoSensores):
        HeaderText += ListaSensores[Num] + ' -- ' + String + '  '

    HeaderText += "\n#Date: {:%d-%m-%Y %H:%M:%S}\n".format(datetime.datetime.now())
    HeaderText += "#--------------------------------------------------------------------\n"
    HeaderText = WriteToFile(root,name,HeaderText)
    return HeaderText

#----------------------------------------------------------
#Esta función escribe los valores de la primera columna
#----------------------------------------------------------

def ColumnText(ListaSensores):
    try:
        ColumnText = "\n# Time\t"

        for String in ListaSensores:
            ColumnText += String+"\t"

        ColumnText += "\n"
    except:
        print('ERROR: El encabezado no pudo ser escrito.')

    return ColumnText

#----------------------------------------------------------
#Esta función escribe los valores de la primera columna
#----------------------------------------------------------

def ColumnNames(root,name,ColumnNames):

    ColumnNames = WriteToFile(root,name,ColumnNames)
    #return ColumnNames

#----------------------------------------------------------
#Esta función guarda los datos obtenidos de las mediciones
#----------------------------------------------------------

def SaveData(root,name,nameAvg,Data,DataSerie,DataAverage,DataAverageText):

    WriteToFile(root,name,DataSerie)
    WriteToFile(root,nameAvg,DataAverageText)
    namepck = name.split('.')
    nameAvgpck = nameAvg.split('.')
    AppendToPickleFile(root,namepck[0]+'.pck',Data)
    AppendToPickleFile(root,nameAvgpck[0]+'.pck',DataAverage)

#----------------------------------------------------------
#Esta función grafica los datos obtenidos de las mediciones
#----------------------------------------------------------
'''
def PlotData(Data):
    PlotData = Data.split('\n')
    PlotData = FilterEmptyStrings(PlotData)
    Tiempo = []
    Temperaturas = []
    plt.figure(0)
    for Num in range(len(PlotData)):
        VectAux = (PlotData[Num].split('\t'))
        Tiempo.append(float(VectAux[0]))
        TemperaturasVect = []
        for Num2 in range(1,len(VectAux)):
            TemperaturasVect.append(float(VectAux[Num2]))

        Temperaturas.append(TemperaturasVect)

    for Num in range(len(TemperaturasVect)):
        TempCol = []
        for Num2 in range(len(Temperaturas)):
            TempCol.append(Temperaturas[Num2][Num])

        plt.plot(Tiempo, TempCol)
    plt.xlabel('Time/s')
    plt.ylabel('Temperature/K')
    plt.show()
'''
def PlotData_Interface(Data):
    PlotData = Data.split('\n')
    PlotData = FilterEmptyStrings(PlotData)
    Tiempo = []
    Temperaturas = []
    Data_plot = []
    for Num in range(len(PlotData)):
        VectAux = (PlotData[Num].split('\t'))
        Tiempo.append(float(VectAux[0]))
        TemperaturasVect = []
        for Num2 in range(1,len(VectAux)):
            TemperaturasVect.append(float(VectAux[Num2]))

        Temperaturas.append(TemperaturasVect)

    for Num in range(len(TemperaturasVect)):
        TempCol = []
        for Num2 in range(len(Temperaturas)):
            TempCol.append(Temperaturas[Num2][Num])

        Data_plot.append([Tiempo, TempCol])
    return Data_plot

#----------------------------------------------------------
#Esta función se encarga de leer los datos del monitor
#----------------------------------------------------------

def GetDataFunction(port,Channels,InitialTime):
    datos,tiempo,ReadTime,ps,flag,= [] ,[], [],0,1




    for Channel in Channels:

        while flag == 1:
            str2port = 'KRDG? ' +str(Channel)+'\r\n'
            port.write(str2port.encode())
            BinData = port.read(79)
            if (len(BinData) == 9) or (len(BinData) == 65):
                flag = 0
                pg.QtGui.QApplication.processEvents()
            pg.QtGui.QApplication.processEvents()

        tiempo.append(time.time())
        StrData = BinData.decode()
        ReadTime.append(tiempo[ps] - InitialTime)
        if (len(BinData) == 9):
            datos.append(StrData.rstrip('\r\n'))
            pg.QtGui.QApplication.processEvents()
        elif (len(BinData) == 65):
            datos = StrData.rstrip('\r\n').split(',')
            break
            pg.QtGui.QApplication.processEvents()

        ps += 1
        flag = 1
        pg.QtGui.QApplication.processEvents()
    AvgTime = sum(ReadTime)/len(ReadTime)
    datosFormatted = '{:10.2f}'.format(AvgTime)
    pg.QtGui.QApplication.processEvents()
    for dato in datos:
        datosFormatted += '\t' + dato
        pg.QtGui.QApplication.processEvents()

    datosFormatted += '\n'
    pg.QtGui.QApplication.processEvents()
    return datos, ReadTime, datosFormatted

#----------------------------------------------------------
#Esta función se encarga de hacer el promedio de cierto número de datos
#----------------------------------------------------------

def AverageFunction(Data,AverageStr,Sensors):

    AvgDataStr = ''
    LenSens = len(Sensors)
    AvgData = ['Average']
    TProm = 0
    AverageInt = int(AverageStr)
    DataLen = len(Data)
    for Num in range(LenSens):
        AvgData.append([0] * LenSens)
        pg.QtGui.QApplication.processEvents()
    try:

        for Num2 in range(LenSens):
            for Num in range(DataLen-AverageInt,DataLen):
                AvgData[Num2+1][0] += Data[Num][Num2][1]
                AvgData[Num2+1][1] += float(Data[Num][Num2][2])
                pg.QtGui.QApplication.processEvents()

            AvgData[Num2+1][0] /= AverageInt
            AvgData[Num2+1][1] /= AverageInt
            TProm += AvgData[Num2+1][0] / LenSens
            pg.QtGui.QApplication.processEvents()

        AvgDataStr += str(TProm) + '\t'
        for Num2 in range(LenSens):
            AvgDataStr += '{}'.format(float(AvgData[Num2+1][1])) + '\t'
            pg.QtGui.QApplication.processEvents()
        AvgDataStr += '\n'
        pg.QtGui.QApplication.processEvents()

    except:
        print('ERROR: "Average" of the configuration file must be an integer.')
        pg.QtGui.QApplication.processEvents()

    return AvgData, AvgDataStr

#----------------------------------------------------------
#Esta función se encarga de imprimir los datos
#----------------------------------------------------------

def StrFunction(Data,Address):
    try:
        subprocess.Popen(['gedit', Address])

    except:
        print('El editor de texto "gedit" no se encuentra en sus sistema. /rInstalelo para habilitar esta función')
        #print(Data)

#----------------------------------------------------------
#Esta función se encarga de terminar con la ejecución
#del programa
#----------------------------------------------------------

def TerminateFunction(ObjArray):

    print('\n------------------------------------------------------------')
    print('Are you sure you want to end the data aquisition?')
    print('------------------------------------------------------------\n')
    ValidChar = False
    MenuKey = YesOrNo(ValidChar)
    ValidChar == False
    if MenuKey == 'y':
        for Obj in ObjArray:
            Obj.Save()
            print('\n------------------------------------------------------------')
            print('Do you want to open the txt file of ' + Obj.name +'?')
            print('------------------------------------------------------------\n')
            StrKey = YesOrNo(ValidChar)
            if StrKey == 'y':
                Obj.__str__()

        for Obj in ObjArray:
            print('\n------------------------------------------------------------')
            print('Do you want to plot the data of ' + Obj.name +'?')
            print('------------------------------------------------------------\n')
            PlotKey = YesOrNo(ValidChar)
            if PlotKey == 'y':
                Obj.Plot(Obj.DataSerieOld)

        sys.exit()

    elif MenuKey == 'n':
        print('\n------------------------------------------------------------')
        print('The aquisition is in process again.')
        print('------------------------------------------------------------\n')

#----------------------------------------------------------
#Esta función se encarga de recibir una "y" para yes o "n"
#para no y devuelve el resultado
#----------------------------------------------------------
'''
def YesOrNo(ValidChar):
    while ValidChar == False:
        MenuKey = input('Press "y" (yes) or "n" (no): ')
        if MenuKey == 'y' or MenuKey == 'n':
            ValidChar = True
    return MenuKey
'''
#----------------------------------------------------------
#Esta clase contendrá toda la información de las mediciones
#y los procedimientos para guardarlos y procesarlos.
#----------------------------------------------------------
'''
class CommandLine:

    def __init__(self):
        self.InputString = ""
        self.IsCommand = False
        self.MenuDict = {'Prompt':'>> ','Help':'help','Plot':'plot','Exit':'exit','Str':'str','Info':'info','ConfigurePlot':'config','Value':'value'}
        self.Pointer = self.MenuDict['Prompt']

    def Input(self,Obj):
        print('\n------------------------------------------------\nWARNING: The data aquisition has been stopped until any key be pressed.\n------------------------------------------------\n')
        self.InputString = input(self.Pointer)
        self.IsCommand = self.InputString in self.MenuDict.values()
        if self.IsCommand:
            self.MenuCommand(Obj)

    def MenuCommand(self,Obj):
        MenuCommandFunction(self.InputString,Obj)
'''
#----------------------------------------------------------
#Esta clase contendrá toda la información de las mediciones
#y los procedimientos para guardarlos y procesarlos.
#----------------------------------------------------------

class TempClass:
    global patch
    def __init__(self,textDict,TimeStamp=0):
        self.textDict = textDict #Diccionario que incluye información sobre la medición que se realizará
        self.root = patch + '/'#Raiz del archivo en el que se guardarán los datos
        self.name = textDict['Name'] #Nombre del archivo en el que se guardarán los datos
        self.nameAvg = textDict['NameAverage']
        self.Sensors = textDict['Sensors'].split(',') #Esta variable guarda el nombre de los sensores que se usan
        self.textDict['Sensors'] = self.Sensors
        self.textDict['Sensor Type'] = textDict['Sensor Type'].split(',')
        self.Average = float(textDict['Average']) #Esta variable guarda como cadena cúantas muestras se estaŕan promediando
        self.textDict['Average'] = self.Average
        self.SamplingPeriod = float(textDict['SamplingPeriod'])
        self.FileAddress = self.root + self.name #Dirección completa del archivo


        try:
            self.Channels = [int(i) for i in textDict['Channels'].split(',')]
        except ValueError:
            self.Channels = [i for i in textDict['Channels'].split(',')]

        self.textDict['Channels'] = self.Channels
        self.Brand = self.textDict['Brand']
        self.Device = self.textDict['Device']
        self.Data = [] #En esta variable se almacenan TODOS los datos de la medición como listas de tuplas
        self.DataSerie = '' #En esta variable se almacenan N datos de la medición en formato cadena para despúes vaciarlos al archivo de texto
        self.DataAverage = [] #En esta variable se almacena el promedio de M lecturas
        self.DataAverageText = '' #En esta variable se guardan los datos del promedio en formato cadena

        self.InitTime = 0 #Esta variable almacena el tiempo en el cual se inició la medición
        self.Cont = 0   #Esta variable almacena el valor de muestras que se han guardado y que no han sido guardadas
        self.Tiempo = ''
        self.DataRecovered = ''
        self.ConfigPlot = 1
        self.DataSerieOld = ''


    def Start(self):
        self.Header = FileHeader(self.root,self.name,self.textDict,'Complete Data')
        self.HeaderAvg = FileHeader(self.root,self.nameAvg,self.textDict,'Averaged')
        self.ColumnText = ColumnText(self.Sensors)
        ColumnNames(self.root,self.name,self.ColumnText)
        ColumnNames(self.root,self.nameAvg,self.ColumnText)
        self.port = serial.Serial(self.textDict['Port'], self.textDict['BaudRate'], timeout=\
                    float(self.textDict['TimeOut']), bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, \
                    stopbits=serial.STOPBITS_ONE)
        global label_scroll
        label_scroll += '-------------------------------------------------------------------------\n'
        label_scroll += '      The aquisition of the temperature with\n ' +'    '+ self.Brand +' '+ \
                        self.Device + ' has begun.\n'
        label_scroll += '-------------------------------------------------------------------------\n'

    def __str__(self): #Función completamente implementada
        StrFunction(self.Data,self.FileAddress)

    def Save(self):
        SaveData(self.root,self.name,self.nameAvg,self.Data,self.DataSerie,self.DataAverage,self.DataAverageText)
        self.Data = []
        self.DataSerie = ''
        self.DataSerieOld = self.DataSerie
        self.DataAverage = []
        self.DataAverageText = ''
        self.Cont = 0

    def Plot(self,Data):
        pid = os.fork()
        #pid = 0

        time.sleep(0.05)
        if pid == 0:
            if self.ConfigPlot == 0:
                PlotData(Data)
            elif self.ConfigPlot == 1:
                self.RemoveHeader()
                PlotData(self.DataRecovered)
            sys.exit()

    def Plot_inter(self):
        self.RemoveHeader()
        var = PlotData_Interface(self.DataRecovered)
         # var.append(PlotData_Interface(Obj.DataSerie)) #header
        return var

    def GetData(self):
        ListTupla = []
        if self.InitTime == 0:
            self.InitTime = time.time()
            pg.QtGui.QApplication.processEvents()

        As,Bs,Cs = GetDataFunction(self.port,self.Channels,self.InitTime)

        if self.SamplingPeriod != 0:
            time.sleep(self.SamplingPeriod)
            pg.QtGui.QApplication.processEvents()

        self.DataSerie += Cs
        if (len(Bs) != len(As)):
            Bs *= len(As)
            pg.QtGui.QApplication.processEvents()


        for Num in range(len(As)):
            try:
                ListTupla.append([self.textDict['Sensor Type'][Num],Bs[Num],As[Num]])
                pg.QtGui.QApplication.processEvents()
            except IndexError:
                ListTupla.append([Num + 1,Bs[Num],As[Num]])
                pg.QtGui.QApplication.processEvents()
            pg.QtGui.QApplication.processEvents()


        self.Data.append(ListTupla)
        self.Cont += 1

        if self.Cont % float(self.Average) == 0:
            self.AverageCalc()
            pg.QtGui.QApplication.processEvents()
        pg.QtGui.QApplication.processEvents()

    def Update_335(self,Orden,Heater,Data,Otro=None):
        if Otro == None:
            Command = Orden+ ''+Heater+','+Data + '\r\n'
        else:
            Command = Orden+ ''+Heater+','+Data+Otro+'\r\n'
        self.port.write(Command.encode())
        return 0

    def Read_335(self,Orden,Heater):
        Command = Orden+' '+Heater+'\r\n'
        self.port.write(Command.encode())
        datos = self.port.read(69)
        datos = datos.decode().strip('\r\n')
        return datos

    def AverageCalc(self):
        As, Bs = AverageFunction(self.Data,self.Average,self.Sensors)
        self.DataAverage.append(As)
        self.DataAverageText += Bs

        if self.Cont >= int(self.textDict['SaveData']):
            self.Save()
            pg.QtGui.QApplication.processEvents()
        pg.QtGui.QApplication.processEvents()

    def RemoveHeader(self):
        self.DataRecovered = RemoveHeaderFunction(self.root,self.name)

    def ConfigurePlotMethod(self):
        ValidChar = False
        ConfigureKey = YesOrNo(ValidChar)
        if ConfigureKey == 'y':
            self.ConfigPlot = 1
        elif ConfigureKey == 'n':
            self.ConfigPlot == 0

    def PrintValue(self):
        a = ''
        if self.Data==[]:
            a += '-------------------------------------------------------------------------\n'
            a += 'Currently, buffer is empty of temperature data. \n         Please try again in a moment.\n'
            a += '-------------------------------------------------------------------------\n'
        else:
            a += '-------------------------------------------------------------------------\n'
            for Vect in self.Data[-1]:
                a +='              ' + Vect[0]+'         '+str(round(Vect[1],2))+ '         ' +Vect[2]+'\n'
            a += '-------------------------------------------------------------------------\n'
        return a

    def Last_data(self):
        Return = []
        if self.Data==[]:
            pass
        else:
            for Vect in self.Data[-1]:
                Return.append(Vect)
        return Return

    def Change_root(self,file,new,string_file):
        with open(file, "r") as f:
            lines = (line.rstrip() for line in f)
            altered_lines = [string_file+': '+new+'/' if line== string_file+':'+textDict[string_file] \
                            else line for line in lines]
        with open(file, "w") as f:
            f.write('\n'.join(altered_lines) + '\n')
#----------------------------------------------------------
#Esta clase contiene toda la información y métodos para
#crear los diccionarios y configurar el módulo de temperatura
#----------------------------------------------------------

class ConfigModule:

    def __init__(self,configFileName,setCurvesFlag,port):

        self.ConfigDict = {}
        self.configFileName = configFileName
        self.getDictFromConfigFile()
        if port == 1:
            self.Port = self.ConfigPort()
        self.Channel = ''
        if setCurvesFlag == 1:
            self.setCurves()
            self.setSensOn()


    def getDictFromConfigFile(self):

        for line in open(self.configFileName):
            if line[0] == "#" :
                #print("skipping comment")
                continue
            if line[0] == "\n" :
                #print("skipping comment")
                continue
            List=line.split(":")
            self.ConfigDict.setdefault(List[0],List[1].strip()) #strip() quita espacios
    #Simple data acquisition rutine, ask for all the channels and print the result

    def getData(self):

        str2port='KRDG? '+str(self.Channel)+'\r\n'
        self.Port.write(str2port.encode())
        datos=self.Port.read(79)
        datos=datos.decode()
        return datos

    #Define channel sensor status On/Off
    def setSensOn(self):
        global label_scroll
        Ch=1
        out={}
        for key in self.ConfigDict.keys():
            keySplit = key.split(' ')
            if keySplit[0]=='Sensor':  #Sensor
                if keySplit[1]=='Status':  #Status On/Off
                    #set On/Off
                    str2port='INPUT '+str(Ch)+','+str(self.ConfigDict.get(key))+'\r\n'
                    self.Port.write(str2port.encode())
                    time.sleep(.1)
                    #read status
                    str2port='INPUT? '+str(Ch)+'\r\n'
                    self.Port.write(str2port.encode())
                    out.setdefault('Sens '+str(Ch),self.Port.read(79).decode().strip()+'\n')
                    time.sleep(.1)
                    Ch=Ch+1
                continue
            continue
        label_scroll +='                                    Status\n'  #Print On/Iff Settings
        label_scroll+='-------------------------------------------------------------------------\n'
        i = 0
        for a in out:
            label_scroll +='      ' +a+':'+out[a].strip('\n')
            i += 1
            if i == 4:
                label_scroll += '\n'
                i = 0
        label_scroll+='-------------------------------------------------------------------------\n'
        #return 'Done\r\n'

    def setCurves(self):
        global label_scroll
        Ch=1
        out={}
        for key in self.ConfigDict:
            if key[0]=='C':   #Curve
                if key[1]=='P':  #Parameter
                    #Set curve in Ch channel
                    str2port='INCRV '+str(Ch)+','+ str(self.ConfigDict.get(key))+'\r\n'
                    self.Port.write(str2port.encode())
                    time.sleep(.1)
                    #read curve value
                    str2port='INCRV? '+str(Ch)+'\r\n'
                    self.Port.write(str2port.encode())
                    out.setdefault(key,self.Port.read(79).decode().strip())
                    time.sleep(.1)
                    Ch=Ch+1
                continue
            continue
        label_scroll += '                                    Curves\n' #Print Curve Settings
        label_scroll+='-------------------------------------------------------------------------\n'
        i = 0
        for a in out:
            label_scroll += '       '+a+' :'+out[a].strip('\n')
            i += 1
            if i == 4:
                label_scroll += '\n'
                i=0
        label_scroll+='-------------------------------------------------------------------------\n'
        #return   'Done\r\n'

    def ConfigPort(self):
        return serial.Serial(self.ConfigDict['Port'], self.ConfigDict['BaudRate'], serial.SEVENBITS,\
            serial.PARITY_ODD, serial.STOPBITS_ONE, float(self.ConfigDict['TimeOut']))


#----------------------------------------------------------
#Main code --- MAIN
#----------------------------------------------------------

global  label_scroll,Start,close_plot,status_heater_1,label_heater_1,SP_1,SP_2,ramp_stat,curvas_last,bt,cfg
label_scroll,Start,close_plot,status_heater_1,label_heater_1,heater_1_estatus,ramp_stat,curvas_last, bt,cfg\
    = '',     False, False,      False,          '',              True,         False,       []    ,False,False

def launch():
    try:
        app = QtWidgets.QApplication(['Temperature'])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt as KBI:
        pass

if __name__ == "__main__":
      launch()
