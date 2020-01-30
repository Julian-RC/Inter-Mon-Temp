import os
from MonTemp.prueba1_ui import *
from MonTemp.info_ui import *
from MonTemp.segunda_ui import *
from MonTemp.tercera_ui import *
from pyqtgraph import QtGui, QtCore
from PyQt5 import QtWidgets
import pyqtgraph as pg
from numpy import roll,append
import serial
import sys
import time
import collections
import numpy as np
# Se importa el objeto Figure de Matplotlib 
from matplotlib.figure import Figure
#Se importa QT4Agg como Canvas.
from matplotlib.backends.backend_qt5agg \
  import FigureCanvasQTAgg as FigureCanvas
import datetime
#import serial
import subprocess
import pickle
#import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')
#import os
import matplotlib.pyplot as plt

from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class QColorBox(QFrame):
 
    colorChanged = pyqtSignal()
 
    def __init__(self, parent=None, defaultColor=Qt.white):
        super(QColorBox,self).__init__(parent)
 
        self.setStyleSheet("border-color: rgba(0,0,0,0);")
        self.__color = None
        self.__defaultColor = QColor(defaultColor)
        self.setColor(self.__defaultColor)
        self.setFixedHeight(20)
        self.setFrameStyle(1)
 
    def setColor(self, color):
        if color != self.__color:
            self.__color = QColor(color)
            self.setStyleSheet("background-color: %s;" % self.__color.name())
            self.colorChanged.emit()
 
    def color(self):
        return self.__color
 
    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            color = QColorDialog.getColor(self.__color)
            if color.isValid():
                self.setColor(color)
                self.colorChanged.emit()
        elif e.button() == Qt.RightButton:
            self.setColor(self.__defaultColor)
 
#
# test


class Dialog(QDialog,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        try:
            QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("About Temperature Module")
        except KeyboardInterrupt as KBI:
            pass
        
class Segunda(QDialog,Ui_Segunda):
    def __init__(self, *args, **kwargs):
        try:
            QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("218 TemperatureMonitor")
        except KeyboardInterrupt as KBI:
            pass
            
class Tercera(QDialog,Ui_Tercera):
    def __init__(self, *args, **kwargs):
        try:
            QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("335 TemperatureController")
        except KeyboardInterrupt as KBI:
            pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        global label_scroll

        #self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.setupUi(self)
        self.setWindowTitle("Temperature Module")
        self.pushButton.clicked.connect(self.graficar)
        
        self.radioButton.toggled.connect(self.desbloquear_radioButton)
        self.Todos.toggled.connect(self.desbloquear_Todos)
        self.heater_1.toggled.connect(self.desbloquear_heater_1)
        self.heater_2.toggled.connect(self.desbloquear_heater_2)
        self.range_manual_1.toggled.connect(self.desbloquear_range_manual_1)
        self.range_manual_2.toggled.connect(self.desbloquear_range_manual_2)
        self.seeStatus_1.toggled.connect(self.desbloquear_seeStatus_1)
        self.seeStatus_2.toggled.connect(self.desbloquear_seeStatus_2)
        self.grafica2.toggled.connect(self.desbloquear_grafica2)
        
        self.directorio.clicked.connect(self.buscarDirectorio)
        self.start.clicked.connect(self.start_adquisition)
        self.stop.clicked.connect(self.stop_adquisition)
        self.see_ramp.clicked.connect(self.rampa)

        self.actionInfo.triggered.connect(self.show_dialog)
        self.action218.triggered.connect(self.show_218)
        self.action335.triggered.connect(self.show_335)
        
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
        
        
        label_scroll='-------------------------------------------------------------------------\n'
        label_scroll+=' Welcome, Interface TemperatureModule has begun\n'
        label_scroll+='                   Please select a folder to start\n'
        label_scroll+='-------------------------------------------------------------------------\n'
        self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
    def rampa(self):
        global ramp_stat,rampa_true
        ramp_stat = True
        rampa_true = Ramp()
        
    def last(self):
        global label_scroll
        for Obj in [DataTemp,DataTemp2]:
               label_scroll += Obj.PrintValue()
        self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def see_data(self):
        
        global label_scroll
        try:
            for Obj in [DataTemp,DataTemp2]:
                Obj.__str__()
        except:
           label_scroll += 'ERROR: Text file cannot be shown.\n'
        self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
     
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
        global RANGE_1,SP_1
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
        else:
            RANGE_1 = True
            
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
        Start,actual = True,False
        DataTemp2.Read_335('SETP?','1')
        DataTemp2.Read_335('SETP?','2')
        DataTemp2.Read_335('RAMP?','1')
        DataTemp2.Read_335('RAMP?','2')
        DataTemp2.Read_335('RANGE?','1')
        DataTemp2.Read_335('RANGE?','2')
        self.grafica1.setEnabled(True)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self.linePatch.setEnabled(False)
        self.directorio.setEnabled(False)
        self.heater_1.setEnabled(True)
        self.heater_2.setEnabled(True)
        self.lastdata.setEnabled(True)
        label_scroll+='                          Acquisition has begun\n'
        label_scroll+='-------------------------------------------------------------------------\n'
        self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        while Start:
            try:
                    DataTemp.GetData()
                    QtGui.QApplication.processEvents() 
                    QtGui.QApplication.processEvents()
                    if DataTemp.InitTime != 0: DataTemp2.InitTime = DataTemp.InitTime
                    DataTemp2.GetData()    
                    QtGui.QApplication.processEvents()
            except:
                    label_scroll += '                             Error en la adquisición'
                    self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
                    self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
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
                                      QtGui.QApplication.processEvents()
                              QtGui.QApplication.processEvents()
                          if Data_2 == []:
                              pass
                          else:
                              plt_mgr.add(Data_2)
                              plt_mgr.update()
                              QtGui.QApplication.processEvents()
                          close_plot = True
                          QtGui.QApplication.processEvents()
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
        reply = QMessageBox.question(self,
                                 'Stop',
                                 "¿Realmente desea detener la adquision?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
                reply = QMessageBox.question(self,
                                 'Stop',
                                 "¿Está seguro?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                                    if actual:
                                        plt_mgr.close()
                                        actual = False
                                    self.grafica2.setChecked(True)
                                    self.grafica1.setChecked(False)
                                    self.grafica1.setEnabled(False)
                                    self.start.setEnabled(True)
                                    self.stop.setEnabled(False)
                                    self.linePatch.setEnabled(True)
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
                                    self.off_heater_2()
                                    label_scroll+='                        Acquisition has stopped\n'
                                    label_scroll+='-------------------------------------------------------------------------\n'
                                    self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
                                    self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())


        
    def closeEvent(self, event):
        global actual,Start,plt_mgr
        reply = QMessageBox.question(self,
                                 'Exit',
                                 "¿Realmente desea cerrar la aplicacion?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        QtGui.QApplication.processEvents()
        if reply == QMessageBox.Yes:
                if Start == True:
                    reply = QMessageBox.question(self,
                                 'Stop',
                                 "Hay una adquisición en proceso, ¿Desea detenerla?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                            Start = False
                            if actual:
                                        plt_mgr.close()
                                        actual = False
                            #self.off_heater_1()
                            #self.off_heater_2()
                    else:
                            event.ignore()
                else:
                    event.accept()
        else:
                event.ignore()
        
        
    def show_dialog(self):
        dialog = Dialog(self)  # self hace referencia al padre
        dialog.show()
    
    def show_218(self):
        dialog = Segunda(self)  # self hace referencia al padre
        dialog.show()
    
    def show_335(self):
        dialog = Tercera(self)  # self hace referencia al padre
        dialog.show()
      
    def buscarDirectorio(self):
        global patch,label_scroll,filename,filename2
        self.buscarDirectorio_2()
        if patch:
            pg.QtGui.QApplication.processEvents()
            label_scroll+='                               Selected folder\n'
            label_scroll+='-------------------------------------------------------------------------\n'
            self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
            pg.QtGui.QApplication.processEvents()
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
                Update_Config()
                pg.QtGui.QApplication.processEvents()
                label_scroll+='                               Config File Ok\n'
                self.linePatch.setText(patch) 
                self.start.setEnabled(True)
                self.SeeData.setEnabled(True)
                self.grafica2.setEnabled(True)
                self.radioButton_2.setEnabled(True)
                self.pushButton.setEnabled(True)
                self.Todos.setEnabled(True)
                self.radioButton.setEnabled(True)
                label_scroll+='               Push "Start" for begin adquisition\n'
                label_scroll+='-------------------------------------------------------------------------\n'
                self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
                self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
                self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                pg.QtGui.QApplication.processEvents()
            except:
                label_scroll += ' Error al cargar la configuración de los modulos\n'
                label_scroll+='-------------------------------------------------------------------------\n'
                self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
                self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
                self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        else:
            label_scroll+='                               No selected folder\n'
            label_scroll+='-------------------------------------------------------------------------\n'
            self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        
    def buscarDirectorio_2(self):
        global patch
        label_scroll+='                           Wait a moment Please\n'
        label_scroll+='-------------------------------------------------------------------------\n'
        self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        patch = QtWidgets.QFileDialog.getExistingDirectory(self, 'Buscar Carpeta', QtCore.QDir.homePath())
        self.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        pg.QtGui.QApplication.processEvents()
        
        pg.QtGui.QApplication.processEvents()
            
    def desbloquear_grafica2(self):
        if self.grafica2.isChecked():
                self.SetPoint1.setEnabled(False)
                self.heater1.setEnabled(False)
                self.SetPoint1.setChecked(False)
                self.heater1.setChecked(False)
                self.SetPoint2.setEnabled(False)
                self.heater2.setEnabled(False)
                self.SetPoint2.setChecked(False)
                self.heater2.setChecked(False)
        else:
            if self.heater_1.isChecked():
                self.SetPoint1.setEnabled(True)
                self.heater1.setEnabled(True)
            if self.heater_2.isChecked():
                self.SetPoint2.setEnabled(True)
                self.heater2.setEnabled(True)
    
    def desbloquear_radioButton(self):
        if self.radioButton.isChecked():
            self.hh.setEnabled(True)
            self.mm.setEnabled(True)
            self.ss.setEnabled(True)
        else:
            self.hh.setEnabled(False)
            self.mm.setEnabled(False)
            self.ss.setEnabled(False)


    def desbloquear_Todos(self):
        if self.Todos.isChecked():
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
        else:
            self.CA.setEnabled(True)
            self.CB.setEnabled(True)
            self.C5.setEnabled(True)
            self.C6.setEnabled(True)
            self.D1.setEnabled(True)
            self.D2.setEnabled(True)
            self.D3.setEnabled(True)
            self.D4.setEnabled(True)
    def desbloquear_heater_1(self):
        global label_scroll 
        if self.heater_1.isChecked():
            try:
                self.On_335_1()
            except:
                label_scroll += '                     Error al cargar Heater 1'
                self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
                self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
            self.setPoint_num_1.setEnabled(True)
            self.ramp_1.setEnabled(True)
            self.range_automatic_1.setEnabled(True)
            self.range_manual_1.setEnabled(True)
            self.seeStatus_1.setEnabled(True)
            self.update_1.setEnabled(True)
            self.Off_1.setEnabled(True)
            if self.grafica2.isChecked():
                self.SetPoint1.setEnabled(False)
                self.heater1.setEnabled(False)
                self.SetPoint1.setChecked(False)
                self.heater1.setChecked(False)
            else:
                self.SetPoint1.setEnabled(True)
                self.heater1.setEnabled(True)
        else:
            self.setPoint_num_1.setEnabled(False)
            self.ramp_1.setEnabled(False)
            self.range_automatic_1.setEnabled(False)
            self.range_manual_1.setEnabled(False)
            self.seeStatus_1.setEnabled(False)
            self.update_1.setEnabled(False)
            self.Off_1.setEnabled(False)
            self.SetPoint1.setEnabled(False)
            self.heater1.setEnabled(False)

    
    def desbloquear_heater_2(self):
        global label_scroll
        if self.heater_2.isChecked():
            try:
                self.On_335_2()
            except:
                label_scroll += '                                   Error al cargar Heater 2'
                self.scrollArea.setWidget(QtWidgets.QLabel(label_scroll))
                self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
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
            self.range_1.setEnabled(True)
        else:
            self.range_1.setEnabled(False)
    def desbloquear_range_manual_2(self):
        if self.range_manual_2.isChecked():
            self.range_2.setEnabled(True)
        else:
            self.range_2.setEnabled(False)
    def desbloquear_seeStatus_1(self):
        if self.seeStatus_1.isChecked():
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
            status_heater_1 = False
            self.status_1.verticalScrollBar().setValue(self.status_1.verticalScrollBar().maximum())
    def desbloquear_seeStatus_2(self):
        if self.seeStatus_2.isChecked():
            self.status_2.setEnabled(True)
    def graficar(self):
        global actual,close_plot,DataTemp, DataTemp2, curvas, curvas_last
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
            if curvas_last==[]:
                pass
            if curvas_last==curvas:
                pass
            else:
                global plt_mgr,Time_graph
                actual, close_plot = True, False
                plt_mgr = LivePlotter()
                curvas_last = curvas
                
        else:
            actual = False
            self.see_ramp.setEnabled(False)
        if self.radioButton.isChecked():
            horas = self.hh.value()
            minutos = self.mm.value()
            segundos = self.ss.value()
            Time_graph = horas*3600 + minutos*60 + segundos
        else:
            Time_graph = float('inf')

        
    def matplotlib6(self):
    # Se crea el widget para matplotlib    
        mpl = Lienzo()
    # Se muestra el widget.
        mpl.show()

                
class LivePlotter(object):
    
    global curvas
    
    def __init__(self):
        self.win = pg.GraphicsWindow(title='Data')
        self.p = self.win.addPlot(title='Sensores')
        self.p.setLabel('left', 'Temperature ',units= 'K')
        self.p.setLabel('bottom', 'Time ',units='s')
        self.p.showGrid(x=False,y=True,alpha=0.3)
        self.p.addLegend()
        if curvas[0] == 1:
            self.curva1=self.p.plot(pen=(255,255,255),width=10,name='CernoxA')
            self.curva2=self.p.plot(pen=(0,226,250),name='CernoxB')
            self.curva3=self.p.plot(pen=(255,255,0),name='Diodo1')
            self.curva4=self.p.plot(pen=(255,85,150),name='Diodo2')
            self.curva5=self.p.plot(pen=(0,255,0),name='Diodo3')
            self.curva6=self.p.plot(pen=(0,0,255),name='Diodo4')
            self.curva7=self.p.plot(pen=(255,0,0),name='Cernox5')
            self.curva8=self.p.plot(pen=(84,100,214),name='Cernox6')
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
                self.curva1=self.p.plot(pen=(255,255,255),name='CernoxA')
                self.Data_curva1,self.Time_curva1=[],[]
            if curvas[2] == 1:
                self.curva2=self.p.plot(pen=(0,226,250),name='CernoxB')
                self.Data_curva2,self.Time_curva2=[],[]
            if curvas[3] == 1:
                self.curva3=self.p.plot(pen=(255,255,0),name='Diodo1')
                self.Data_curva3,self.Time_curva3=[],[]
            if curvas[4] == 1:
                self.curva4=self.p.plot(pen=(255,85,150),name='Diodo2')
                self.Data_curva4,self.Time_curva4=[],[]
            if curvas[5] == 1:
                self.curva5=self.p.plot(pen=(0,255,0),name='Diodo3')
                self.Data_curva5,self.Time_curva5=[],[]
            if curvas[6] == 1:
                self.curva6=self.p.plot(pen=(0,0,255),name='Diodo4')
                self.Data_curva6,self.Time_curva6=[],[]
            if curvas[7] == 1:
                self.curva7=self.p.plot(pen=(255,0,0),name='Cernox5')
                self.Data_curva7,self.Time_curva7=[],[]
            if curvas[8] == 1:
                self.curva8=self.p.plot(pen=(178,155,214),name='Cernox6')
                self.Data_curva8,self.Time_curva8=[],[]
        if curvas[9] == 1:
            self.curva9 = self.p.plot(pen=(214,103,29),name='SetPoint-1')
            self.Data_curva9,self.Time_curva9=[],[]
        if curvas[10] == 1:
            self.curva10 = self.p.plot(pen=(255,192,33), name = 'Heater-1')
            self.Data_curva10,self.Time_curva10=[],[]
        if curvas[11] == 1:
            self.curva11 = self.p.plot(pen=(214,140,162),name = 'SetPoint-2')
            self.Data_curva11,self.Time_curva11=[],[]
        if curvas[12] == 1:
            self.curva12 = self.p.plot(pen=(200,148,214),name = 'Heater-2')
            self.Data_curva12,self.Time_curva12=[],[]
        self.p.setRange(yRange=[50, 300])
    
    def return_data(self):
        return self.Data_curva1,self.Time_curva1

    def add(self, x):
            global Time_graph
            if curvas[0] == 1:
                self.Data_curva1,self.Time_curva1 = self.Curvas_add(self.Data_curva1, self.Time_curva1,float(x[0][2]),x[0][1])
                self.Data_curva2,self.Time_curva2 = self.Curvas_add(self.Data_curva2, self.Time_curva2,float(x[1][2]),x[1][1])
                self.Data_curva3,self.Time_curva3 = self.Curvas_add(self.Data_curva3, self.Time_curva3,float(x[2][2]),x[2][1])
                self.Data_curva4,self.Time_curva4 = self.Curvas_add(self.Data_curva4, self.Time_curva4,float(x[3][2]),x[3][1])
                self.Data_curva5,self.Time_curva5 = self.Curvas_add(self.Data_curva5, self.Time_curva5,float(x[4][2]),x[4][1])
                self.Data_curva6,self.Time_curva6 = self.Curvas_add(self.Data_curva6, self.Time_curva6,float(x[5][2]),x[5][1])
                self.Data_curva7,self.Time_curva7 = self.Curvas_add(self.Data_curva7, self.Time_curva7,float(x[6][2])*1.0257-2.1852,x[6][1])
                self.Data_curva8,self.Time_curva8 = self.Curvas_add(self.Data_curva8, self.Time_curva8,float(x[7][2])*1.0151-0.7786,x[7][1])
            else:
                if curvas[1] == 1:
                    self.Data_curva1,self.Time_curva1 = self.Curvas_add(self.Data_curva1, self.Time_curva1,float(x[0][2]),x[0][1])
                if curvas[2] == 1:
                    self.Data_curva2,self.Time_curva2 = self.Curvas_add(self.Data_curva2, self.Time_curva2,float(x[1][2]),x[1][1])
                if curvas[3] == 1:
                    self.Data_curva3,self.Time_curva3 = self.Curvas_add(self.Data_curva3, self.Time_curva3,float(x[2][2]),x[2][1])
                if curvas[4] == 1:
                    self.Data_curva4,self.Time_curva4 = self.Curvas_add(self.Data_curva4, self.Time_curva4,float(x[3][2]),x[3][1])
                if curvas[5] == 1:
                    self.Data_curva5,self.Time_curva5 = self.Curvas_add(self.Data_curva5, self.Time_curva5,float(x[4][2]),x[4][1])

                if curvas[6] == 1:
                    self.Data_curva6,self.Time_curva6 = self.Curvas_add(self.Data_curva6, self.Time_curva6,float(x[5][2]),x[5][1])

                if curvas[7] == 1:
                    self.Data_curva7,self.Time_curva7 = self.Curvas_add(self.Data_curva7, self.Time_curva7,float(x[6][2])*1.0257-2.1852,x[6][1])
                    
                if curvas[8] == 1:
                    self.Data_curva8,self.Time_curva8 = self.Curvas_add(self.Data_curva8, self.Time_curva8,float(x[7][2])*1.0151-0.7786,x[7][1])
                        
            if curvas[9] == 1:
                self.Data_curva9,self.Time_curva9 = self.Curvas_add(self.Data_curva9, self.Time_curva9,SP_1,x[7][1])
                
            if curvas[10] == 1:
                HTR_1 = float(DataTemp2.Read_335('SETP?','1'))
                self.Data_curva10,self.Time_curva10 = self.Curvas_add(self.Data_curva10, self.Time_curva10,HTR_1,x[7][1])
                time.sleep(0.05)

            if curvas[11] == 1:
                self.Data_curva11,self.Time_curva11 = self.Curvas_add(self.Data_curva11, self.Time_curva11,SP_2,x[7][1])

            if curvas[12] == 1:
                HTR_2 = float(DataTemp2.Read_335('SETP?','2'))
                self.Data_curva12,self.Time_curva12 = self.Curvas_add(self.Data_curva12, self.Time_curva12,HTR_2,x[7][1])
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
            QtGui.QApplication.processEvents() 
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
            QtGui.QApplication.processEvents() 
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

            
#Se define la funcion x(t) de la ecuacion de posicion (movimiento horizontal)
def fx (t):
    #Se define la posicion inicial en 0
    x0 = 0
    #Se define la velocidad inicial en 2 mts/seg
    v0x = 2
    #Se define la aceleracion en 1 mts/seg^2
    ax = 1
    #Se hace el calculo de la posicion con respecto al tiempo
    x = x0 + v0x*t + 0.5*ax*t**2
    return x

#Se define la funcion y(t) de la ecuacion de posicion altura
def fy(t):
    #Se define la altura inicial en 100 mts
    y0 = 100
    #Se define la velocidad inicial en 10 mts/seg
    v0y = 10
    #Se define la gravedad en 9.81 mts/seg^2
    g = 9.81
    #Se realiza el calculo de l posicion en funcion del tiempo
    y = y0 + v0y*t - 0.5*g*t**2
    return y


class Lienzo(FigureCanvas):
    """Clase que represente a FigureCanvas"""
    def __init__(self):
        # Codigo para generar la grafica
        self.figura = Figure()
        self.ejes = self.figura.add_subplot(111)
        self.tiempo = np.arange(0.0, 5.65, 0.01)
        #Calculo de la posicion en el eje X y Y
        self.x = fx(self.tiempo)
        self.y = fy(self.tiempo)
        #Se crea la grafica
        self.ejes.plot(self.x, self.y)
        # inicializar el lienzo donde se crea la grafica.
        FigureCanvas.__init__(self, self.figura)

#############################################################



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
    HeaderText += "#Temperature Measurments using a {} {} {}\n".format(textDict['Brand'],textDict['Device'],textDict['Model'])
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
                QtGui.QApplication.processEvents() 
            QtGui.QApplication.processEvents() 
                
        tiempo.append(time.time())
        StrData = BinData.decode()
        ReadTime.append(tiempo[ps] - InitialTime)
        if (len(BinData) == 9):
            datos.append(StrData.rstrip('\r\n'))    
            QtGui.QApplication.processEvents()       
        elif (len(BinData) == 65):
            datos = StrData.rstrip('\r\n').split(',')
            break
            QtGui.QApplication.processEvents() 
            
        ps += 1
        flag = 1
        QtGui.QApplication.processEvents() 
    AvgTime = sum(ReadTime)/len(ReadTime)
    datosFormatted = '{:10.2f}'.format(AvgTime)
    QtGui.QApplication.processEvents() 
    for dato in datos:
        datosFormatted += '\t' + dato
        QtGui.QApplication.processEvents() 

    datosFormatted += '\n'
    QtGui.QApplication.processEvents() 
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
        QtGui.QApplication.processEvents() 
    try:
        
        for Num2 in range(LenSens):
            for Num in range(DataLen-AverageInt,DataLen):
                AvgData[Num2+1][0] += Data[Num][Num2][1]
                AvgData[Num2+1][1] += float(Data[Num][Num2][2])
                QtGui.QApplication.processEvents() 

            AvgData[Num2+1][0] /= AverageInt
            AvgData[Num2+1][1] /= AverageInt
            TProm += AvgData[Num2+1][0] / LenSens
            QtGui.QApplication.processEvents() 
              
        AvgDataStr += str(TProm) + '\t'
        for Num2 in range(LenSens):
            AvgDataStr += '{}'.format(float(AvgData[Num2+1][1])) + '\t'
            QtGui.QApplication.processEvents() 
        AvgDataStr += '\n'
        QtGui.QApplication.processEvents() 

    except:
        print('ERROR: "Average" of the configuration file must be an integer.')
        QtGui.QApplication.processEvents() 
    
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

def YesOrNo(ValidChar):
    while ValidChar == False:
        MenuKey = input('Press "y" (yes) or "n" (no): ')
        if MenuKey == 'y' or MenuKey == 'n':
            ValidChar = True
    return MenuKey

#----------------------------------------------------------
#Esta clase contendrá toda la información de las mediciones
#y los procedimientos para guardarlos y procesarlos.
#----------------------------------------------------------

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
        self.Header = FileHeader(self.root,self.name,self.textDict,'Complete Data')
        self.HeaderAvg = FileHeader(self.root,self.nameAvg,self.textDict,'Averaged') 
        self.ColumnText = ColumnText(self.Sensors)
        ColumnNames(self.root,self.name,self.ColumnText)
        ColumnNames(self.root,self.nameAvg,self.ColumnText)
        
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
        self.port = serial.Serial(textDict['Port'], textDict['BaudRate'], timeout=float(textDict['TimeOut']), bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_ONE)
        self.InitTime = 0 #Esta variable almacena el tiempo en el cual se inició la medición       
        self.Cont = 0   #Esta variable almacena el valor de muestras que se han guardado y que no han sido guardadas 
        self.Tiempo = ''
        self.DataRecovered = ''
        self.ConfigPlot = 1
        self.DataSerieOld = ''
        global label_scroll
        label_scroll += '------------------------------------------------------------\n'
        label_scroll += 'The aquisition of the temperature with ' + self.Brand +' '+ self.Device + ' has begun.\n'
        label_scroll += '------------------------------------------------------------\n'

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
#########        time.sleep(0.1)
        time.sleep(0.05)        
        if pid == 0:
            if self.ConfigPlot == 0:
                PlotData(Data)
            elif self.ConfigPlot == 1:
                self.RemoveHeader()
                PlotData(self.DataRecovered)
            sys.exit()

    def GetData(self):
        ListTupla = []
        if self.InitTime == 0:
            self.InitTime = time.time()
            QtGui.QApplication.processEvents() 
        
        As,Bs,Cs = GetDataFunction(self.port,self.Channels,self.InitTime)
        
        if self.SamplingPeriod != 0:
            time.sleep(self.SamplingPeriod)
            QtGui.QApplication.processEvents() 
        
        self.DataSerie += Cs
        if (len(Bs) != len(As)):
            Bs *= len(As) 
            QtGui.QApplication.processEvents() 
        
        
        for Num in range(len(As)):
            try:
                ListTupla.append([self.textDict['Sensor Type'][Num],Bs[Num],As[Num]])
                QtGui.QApplication.processEvents() 
            except IndexError:
                ListTupla.append([Num + 1,Bs[Num],As[Num]])
                QtGui.QApplication.processEvents() 
            QtGui.QApplication.processEvents() 
                
        
        self.Data.append(ListTupla)
        self.Cont += 1

        if self.Cont % float(self.Average) == 0:
            self.AverageCalc() 
            QtGui.QApplication.processEvents() 
        QtGui.QApplication.processEvents() 
            
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
            QtGui.QApplication.processEvents() 
        QtGui.QApplication.processEvents() 

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
        a = ' '
        if self.Data==[]:
            a += '------------------------------------------------------------\n'
            a += 'Currently, buffer is empty of temperature data. \n         Please try again in a moment.\n'
            a += '------------------------------------------------------------\n'
        else:
            a += '------------------------------------------------------------\n'
            for Vect in self.Data[-1]:
                a += str(Vect)+'\n'
            a += '------------------------------------------------------------\n'
        return a
            
    def Last_data(self):
        Return = []
        if self.Data==[]:
            pass
        else:
            for Vect in self.Data[-1]:
                Return.append(Vect)
        return Return
    
    def Change_root(self,file,new): 
        with open(file, "r") as f:
            lines = (line.rstrip() for line in f)
            altered_lines = ['Root: '+new+'/' if line== 'Root: '+self.root else line for line in lines]
        with open(file, "w") as f:
            f.write('\n'.join(altered_lines) + '\n')
#----------------------------------------------------------
#Esta clase contiene toda la información y métodos para 
#crear los diccionarios y configurar el módulo de temperatura
#----------------------------------------------------------

class ConfigModule:

    def __init__(self,configFileName,setCurvesFlag=1):
       
        self.ConfigDict = {}
        self.configFileName = configFileName
        self.getDictFromConfigFile()
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
        label_scroll +='Status\r'  #Print On/Iff Settings       
        label_scroll += str(out) + '\n'
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
                    time.sleep(.2)
                    #read curve value   
                    str2port='INCRV? '+str(Ch)+'\r\n'
                    self.Port.write(str2port.encode())
                    out.setdefault(key,self.Port.read(79).decode().strip())
                    time.sleep(.2)
                    Ch=Ch+1
                continue
            continue
        label_scroll += 'Curves\r' #Print Curve Settings
        label_scroll += str(out)+'\n' 
        #return   'Done\r\n'

    def ConfigPort(self):
        return serial.Serial(self.ConfigDict['Port'], self.ConfigDict['BaudRate'], serial.SEVENBITS,\
            serial.PARITY_ODD, serial.STOPBITS_ONE, float(self.ConfigDict['TimeOut']))
        

#----------------------------------------------------------
#Main code --- MAIN
#----------------------------------------------------------

#filename = sys.argv[1]
#filename = sys.argv[2]
global  label_scroll,Start,close_plot,status_heater_1,label_heater_1,SP_1,SP_2,ramp_stat,curvas_last

#Menu = CommandLine()
label_scroll,Start,close_plot,status_heater_1,label_heater_1,heater_1_estatus= '', False, False,False,'',True
ramp_stat,curvas_last = False,[]
def Update_Config():
    global textDict,textDict2,DataTemp,DataTemp2
    textDict = ConfigModule(filename)
    pg.QtGui.QApplication.processEvents()
    textDict2 = ConfigModule(filename2,0)
    pg.QtGui.QApplication.processEvents()
    DataTemp = TempClass(textDict.ConfigDict)
    pg.QtGui.QApplication.processEvents()
    DataTemp2 = TempClass(textDict2.ConfigDict,DataTemp.InitTime)
    pg.QtGui.QApplication.processEvents()
    
def launch():
    try:
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()
    except KeyboardInterrupt as KBI:
        pass

if __name__ == "__main__":
      launch()
