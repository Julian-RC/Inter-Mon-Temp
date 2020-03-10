import os, serial, sys, time, datetime, subprocess, pickle
#os.system('cd '++'cfg && sudo chmod 777 /dev/ttyUSB*')
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
from MonTemp.ramp_ui import Ui_ramp
from MonTemp.terminal_ui import Ui_Terminal
from MonTemp.icon_ui import Ui_Icon
from PyQt5 import QtWidgets,QtGui,QtCore
import pyqtgraph as pg
from numpy import append,array
from matplotlib.backends.backend_qt5agg \
  import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None,*args, **kwargs):
        self.ramp_stat,self.Start,self.close_plot,self.status_heater_1,self.heater_1_estatus,self.cfg,self.bt\
             = False,False,False,False,True,False,False
        self.ramp_count = 0
        super(MainWindow, self).__init__()
        self.num_matplotlib,self.num_ramp = 0,0
        self.patch = os.path.realpath(__file__).strip('prueba1.py')
        self.patch_cfg = self.patch +'cfg'
        os.system("xrdb " + self.patch + "cfg/terminal.cfg")
        self.filename_218 = self.patch + "cfg/file_218.cfg"
        self.filename_335 = self.patch + "cfg/file_335.cfg"
        filename_color = self.patch + "cfg/color.cfg"
        filename_fit = self.patch + "cfg/sensores_fit.cfg"
        self.textDict_218 = ConfigModule(self.filename_218,0,0)
        self.textDict_335 = ConfigModule(self.filename_335,0,0)
        self.file_plot_names = [self.textDict_335.ConfigDict['Name'],self.textDict_218.ConfigDict['Name'],'Plot of data']
        self.textDict_color = ConfigModule(filename_color,0,0)
        for a in self.textDict_color.ConfigDict:
            self.textDict_color.ConfigDict[a]=self.textDict_color.ConfigDict[a].split(',')
        self.color=[0]*(len(self.textDict_color.ConfigDict)+1)
        for a in self.textDict_color.ConfigDict:
            self.color[self.color[len(self.textDict_color.ConfigDict)]]=array([int(self.textDict_color.ConfigDict[a][0]),\
                                int(self.textDict_color.ConfigDict[a][1]),\
                                int(self.textDict_color.ConfigDict[a][2])])
            self.color[len(self.textDict_color.ConfigDict)] += 1
        self.color[len(self.textDict_color.ConfigDict)]=0
        self.textDict_fit = ConfigModule(filename_fit,0,0)
        for a in self.textDict_fit.ConfigDict:
            self.textDict_fit.ConfigDict[a]=self.textDict_fit.ConfigDict[a].split(',')
        self.fit_number=[0]*(len(self.textDict_fit.ConfigDict)+1)
        for a in self.textDict_fit.ConfigDict:
            self.fit_number[self.fit_number[len(self.textDict_fit.ConfigDict)]]=[float(self.textDict_fit.ConfigDict[a][0])\
                                                                            ,float(self.textDict_fit.ConfigDict[a][1])]
            self.fit_number[len(self.textDict_fit.ConfigDict)] += 1
        self.Data_218 = TempClass(self.textDict_218.ConfigDict,patch=self.patch)
        self.Data_335 = TempClass(self.textDict_335.ConfigDict,self.Data_218.InitTime,patch=self.patch)
        self.names_sensor=[]
        for a in [self.textDict_335,self.textDict_218]:
            for b in a.ConfigDict['Sensor Type']:
                self.names_sensor.append(b)
        
        self.setupUi(self)
        self.setWindowTitle("Temperature 4.0")
        self.sensor_ramp = [self.ramp_CA,self.ramp_CB,self.ramp_D1,self.ramp_D2,\
                        self.ramp_D3,self.ramp_D4,self.ramp_C5,self.ramp_C6]
        self.sensor_ramp_desbloquear = [self.desbloquear_sensores_ramp_CA,\
            self.desbloquear_sensores_ramp_CB, self.desbloquear_sensores_ramp_D1,\
            self.desbloquear_sensores_ramp_D2, self.desbloquear_sensores_ramp_D3,\
            self.desbloquear_sensores_ramp_D4, self.desbloquear_sensores_ramp_C5,\
            self.desbloquear_sensores_ramp_C6]
        i = 0
        while i < 8:
            self.sensor_ramp[i].toggled.connect(self.sensor_ramp_desbloquear[i])
            i += 1
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
        self.plot_checkbox = [self.CA,self.CB,self.D1,self.D2,self.D3,self.D4,\
                            self.C5,self.C6,self.SetPoint1,self.heater1,\
                            self.SetPoint2,self.heater2]
        self.plot_desbloquear = [self.desbloquear_sensores_CA,self.desbloquear_sensores_CB,\
            self.desbloquear_sensores_D1,self.desbloquear_sensores_D2,\
            self.desbloquear_sensores_D3,self.desbloquear_sensores_D4,\
            self.desbloquear_sensores_C5,self.desbloquear_sensores_C6,\
            self.desbloquear_SetPoint1,self.desbloquear_heater1,\
            self.desbloquear_SetPoint2,self.desbloquear_heater2]
        i = 0
        while i < len(self.plot_checkbox):
            self.plot_checkbox[i].toggled.connect(self.plot_desbloquear[i])
            i += 1

        self.directorio.clicked.connect(self.buscarDirectorio)
        self.start.clicked.connect(self.start_adquisition)
        self.stop.clicked.connect(self.stop_adquisition)
        self.ramp.clicked.connect(self.rampa)

        self.actionInfo.triggered.connect(self.show_dialog)
        self.action218.triggered.connect(self.show_218)
        self.action335.triggered.connect(self.show_335)
        self.actionAbout_Temperature_Monitor_218.triggered.connect(self.show_help_218)
        self.actionAbout_Temperature_Control_335.triggered.connect(self.show_help_335)
        self.action218_Data.triggered.connect(self.show_218_Data)
        self.action335_Data.triggered.connect(self.show_335_Data)
        self.actionFit_of_data.triggered.connect(self.show_Fit_of_data)
        self.actionPlot_File.triggered.connect(self.show_Plot_File)
        self.actionTerminal.triggered.connect(self.show_Terminal)
        self.actionAdd_Icon.triggered.connect(self.show_Icon)
        self.dialogs = []

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
        self.color_button = [self.color_H1,self.color_H2,self.color_S1,self.color_S2,self.color_D1,self.color_D2\
                            ,self.color_D3,self.color_D4,self.color_C5,self.color_C6,self.color_CA,self.color_CB]
        self.color_change = [self.change_color_H1,self.change_color_H2,self.change_color_S1,self.change_color_S2\
                            ,self.change_color_D1,self.change_color_D2,self.change_color_D3,self.change_color_D4\
                            ,self.change_color_C5,self.change_color_C6,self.change_color_CA,self.change_color_CB]
        i = 0
        while i < 12:
            self.color_button[i].clicked.connect(self.color_change[i])
            i += 1
        self.label_scroll='-------------------------------------------------------------------------\n'+\
                     '               Welcome, Temperature has begun\n                          '+\
                     '{:%d-%m-%Y %H:%M:%S}\n'.format(datetime.datetime.now())+\
                     '-------------------------------------------------------------------------\n '+\
                     '                   Please select a folder to start\n'\
                     '-------------------------------------------------------------------------\n'
        self.Update_label()
        self.tabWidget.clear()
        self.tabWidget.addTab(Terminal(),"Terminal")
        self.names_sensor_color = ['CA','CB','D1','D2','D3','D4','C5','C6']
        self.Action_button(0)
        pg.QtGui.QApplication.processEvents()
    def Action_button(self,Status):
        if Status == 1:
            self.action_flag = True
        else:
            self.action_flag = False
    def Update_label(self):
        self.scrollArea.setWidget(QtWidgets.QLabel(self.label_scroll))
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        pg.QtGui.QApplication.processEvents()
    def change_color(self,name_dat,num):
        color_rgb = self.textDict_color.ConfigDict[name_dat]
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor(int(color_rgb[0]),int(color_rgb[1]),int(color_rgb[2])))
        pg.QtGui.QApplication.processEvents()
        if color.isValid():
            color_rgb = color.getRgb()
            self.textDict_color.ConfigDict[name_dat]=[str(color_rgb[0]),str(color_rgb[1]),str(color_rgb[2])]
            self.color_button[num].setStyleSheet("background-color: rgb("+str(color_rgb[0])+','+str(color_rgb[1])+','\
                                        +str(color_rgb[2])+");border: 1px solid black;")
            pg.QtGui.QApplication.processEvents()
        for a in self.textDict_color.ConfigDict:
            self.color[self.color[len(self.textDict_color.ConfigDict)]]=array([int(self.textDict_color.ConfigDict[a][0]),\
                                int(self.textDict_color.ConfigDict[a][1]),\
                                int(self.textDict_color.ConfigDict[a][2])])
            self.color[len(self.textDict_color.ConfigDict)] += 1
        self.color[len(self.textDict_color.ConfigDict)]=0
    def change_color_H1(self):
        self.change_color('H1',0)
    def change_color_S1(self):
        self.change_color('s1',2)
    def change_color_H2(self):
        self.change_color('H2',1)
    def change_color_S2(self):
        self.change_color('S2',3)
    def change_color_CA(self):
        self.change_color('CA',10)
    def change_color_CB(self):
        self.change_color('CB',11)
    def change_color_D1(self):
        self.change_color('D1',4)
    def change_color_D2(self):
        self.change_color('D2',5)
    def change_color_D3(self):
        self.change_color('D3',6)
    def change_color_D4(self):
        self.change_color('D4',7)
    def change_color_C5(self):
        self.change_color('C5',8)
    def change_color_C6(self):
        self.change_color('C6',9)
    def rampa_matplotlib(self):
            try:
                if self.num_ramp==0:
                    self.mpl_ramp=[]
                    self.mpl_ramp.append(Plot_ramp())
                    self.mpl_ramp[0].show()
                else:
                    self.mpl_ramp.append(Plot_ramp())
                    self.mpl_ramp[self.num_ramp].show()
                self.num_ramp += 1
            except:
                pass
    def rampa(self):
        Flag = 0
        self.curvas_ramp=[0,0,0,0,0,0,0,0]
        for i in range(8):
            if self.sensor_ramp[i].isChecked():
                self.curvas_ramp[i] = 1
                Flag = 1
                self.ramp_sensor = i + 1
        if Flag == 1: 
            if self.grafica2.isChecked():
                if self.ramp_stat:
                    self.ramp_stat = False
                    self.ramp_live.close()
                self.rampa_matplotlib()
            else:
                if self.ramp_stat:
                    self.ramp_live.close()
                    self.ramp_live = Rampa_live(self)
                    self.ramp_live.show()
                else:
                    self.ramp_value = []
                    self.ramp_stat = True
                    self.ramp_live = Rampa_live(self)
                    self.ramp_live.show()
    def last(self):
        self.label_scroll +='                              See Last Data\n                           '+\
                       '{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+\
                       '\n-------------------------------------------------------------------------\n'
        self.Update_label()
        self.label_scroll +='               ' + 'Sensor'+'           '+'Time[s]'+ '        ' +'Data[K]\n'
        for Obj in [self.Data_335,self.Data_218]:
               self.label_scroll += Obj.PrintValue()
        self.Update_label()
    def see_data(self):
        try:
            for Obj in [self.Data_218,self.Data_335]:
                Obj.__str__()
        except:
           self.label_scroll += '   ERROR: Text file cannot be shown.\n'
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
        Ramp_1 = str(self.Data_335.Read_335('RAMP?','1')[2:7])
        self.ramp_1.setValue(float(Ramp_1))
        SetP_1 = str(self.Data_335.Read_335('SETP?','1'))
        self.SP_1 = float(SetP_1)
        self.setPoint_num_1.setValue(self.SP_1)
    def On_335_2(self):
        Ramp_2 = str(self.Data_335.Read_335('RAMP?','2')[2:7])

        self.ramp_2.setValue(float(Ramp_2))
        SetP_2 = self.Data_335.Read_335('SETP?','2')
        self.SP_2 = float(SetP_2)
        self.setPoint_num_2.setValue(self.SP_2)
    def Update_1(self):
        Ramp_1 = str(self.ramp_1.value())
        self.Data_335.Update_335('RAMP','1','1,'+Ramp_1)
        time.sleep(0.05)
        SetP_1 = str(self.setPoint_num_1.value())
        self.SP_1 = float(SetP_1)
        self.Data_335.Update_335('SETP','1',SetP_1)
        if self.range_manual_1.isChecked():
            time.sleep(0.05)
            self.RANGE_1 = False
            Range = str(self.range_1.currentIndex()+1)
            self.Data_335.Update_335('RANGE','1',Range)
            if Range == '1':
                Range_print='Low'
            elif Range == '2':
                Range_print='Med'
            elif Range == '3':
                Range_print='High'
            elif Range == '0' :
                Range_print='Off'
        else:
            self.RANGE_1 = True
            Range_print = 'Auto'

        self.label_scroll +='                            Update Heater 1\n                          '+\
                        '{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'\n'+\
                        '-------------------------------------------------------------------------\n'
        self.label_scroll +=' Ramp= '+Ramp_1+' k/min SetPoint= '+SetP_1+' k  Range= '+ Range_print +\
                        '\n-------------------------------------------------------------------------\n'
        self.Update_label()
    def Update_2(self):
        self.Data_335.Update_335('RANGE','2','1')
        time.sleep(0.05)
        Ramp_2 = str(self.ramp_2.value())
        self.Data_335.Update_335('RAMP','2','1,'+Ramp_2)
        time.sleep(0.05)
        SetP_2 = str(self.setPoint_num_2.value())
        self.SP_2 = float(SetP_2)
        self.Data_335.Update_335('SETP','2',SetP_2)
        if self.range_manual_2.isChecked():
            time.sleep(0.05)
            self.RANGE_2 = False
            Range = str(self.range_2.currentIndex()+1)
            self.Data_335.Update_335('RANGE','2',Range)
        else:
            self.RANGE_2 = True
    def start_adquisition(self):
        self.Action_button(0)
        self.Start,self.actual,self.bt = True,False, True
        self.pushButton.setEnabled(True)
        self.Data_218.Start()
        self.Data_335.Start()
        self.label_scroll+='                          Aquisition has begun\n'\
                        '                          '+'{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'\n'\
                        '-------------------------------------------------------------------------\n'
        self.Update_label()
        self.Data_335.Read_335('SETP?','1')
        self.Data_335.Read_335('SETP?','2')
        self.Data_335.Read_335('RAMP?','1')
        self.Data_335.Read_335('RAMP?','2')
        self.Data_335.Read_335('RANGE?','1')
        self.Data_335.Read_335('RANGE?','2')
        self.grafica1.setEnabled(True)
        self.grafica1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self.directorio.setEnabled(False)
        self.heater_1.setEnabled(True)
        self.heater_2.setEnabled(True)
        self.lastdata.setEnabled(True)

        while self.Start:
            try:
                    self.Data_218.GetData()
                    pg.QtGui.QApplication.processEvents()
                    pg.QtGui.QApplication.processEvents()
                    if self.Data_218.InitTime != 0: self.Data_335.InitTime = self.Data_218.InitTime
                    self.Data_335.GetData()
                    pg.QtGui.QApplication.processEvents()
            except:
                    self.label_scroll += '                             Error en la adquisición\n'
                    self.label_scroll+='-------------------------------------------------------------------------\n'
                    self.Update_label()
            if self.actual:
                          Data_2 = []
                          for Obj in [self.Data_335,self.Data_218]:
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
                              self.plot_pyqt.add(Data_2)
                              self.plot_pyqt.update()
                              pg.QtGui.QApplication.processEvents()
                          self.close_plot = True
                          pg.QtGui.QApplication.processEvents()
            elif self.close_plot:
                            self.plot_pyqt.close()
                            self.close_plot = False
            if self.ramp_stat:
                x = []
                for Obj in [self.Data_335,self.Data_218]:
                    a=Obj.Last_data()
                    if a==[]:
                        pass
                    else:
                        for algo in a:
                            x.append(algo)
                            pg.QtGui.QApplication.processEvents()
                if x == []:
                    pass
                else:
                    self.value_actual,self.time_actual=float(x[self.ramp_sensor][2]),x[self.ramp_sensor][1]
                    if self.ramp_count == 3:
                        self.ramp_value.append((self.value_actual-self.value_last)/((self.time_actual-self.time_last)/60.0))
                        rampa = 0
                        for a in self.ramp_value:
                            rampa += a
                        self.ramp_live.charges(float(rampa/len(self.ramp_value)))
                        self.ramp_count = 0
                        self.ramp_value = []
                    elif self.ramp_count == 0:
                        self.ramp_count += 1
                    else:
                        self.ramp_value.append((self.value_actual-self.value_last)/((self.time_actual-self.time_last)/60.0))
                        self.ramp_count += 1
                    self.value_last,self.time_last = self.value_actual,self.time_actual

            else:
                try:
                    self.ramp_live.close()
                except:
                    pass
            if self.status_heater_1:
                            Ramp_1 = str(self.Data_335.Read_335('HTR?','1'))
                            time.sleep(0.05)
                            self.label_heater_1 +=str(Ramp_1)+'%'
                            SetP_1 = str(self.Data_335.Read_335('SETP?','1'))
                            time.sleep(0.05)
                            self.label_heater_1 +='   '+str(SetP_1)+'K'
                            Ran_1 = str(self.Data_335.Read_335('RANGE?','1'))
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
                            self.label_heater_1 += '   '+Range+'\n'
                            self.label_heater_1 += '--------------------------------------\n'
                            self.status_1.setWidget(QtWidgets.QLabel(self.label_heater_1))
                            self.status_1.verticalScrollBar().setValue(self.status_1.verticalScrollBar().maximum())
    def stop_adquisition(self):
        self.Start = False
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
                    for a in [self.Data_218,self.Data_335]:
                        a.Save()
                    if self.actual:
                        self.plot_pyqt.close()
                        self.actual = False
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
                    #self.off_heater_2()
                    self.label_scroll+='                        Acquisition has stopped\n'
                    self.label_scroll+='                          '+'{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'\n'
                    self.label_scroll+='-------------------------------------------------------------------------\n'
                    self.Update_label()
    def closeEvent(self, event):
        try:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Exit',
                                    "¿Realmente desea cerrar la aplicacion?",
                                    self.box.Yes | self.box.No, self.box.No)
            pg.QtGui.QApplication.processEvents()
            if reply == self.box.Yes:
                    if self.Start == True:
                        reply = self.box.question(self,
                                    'Stop',
                                    "Hay una adquisición en proceso, ¿Desea detenerla?",
                                    self.box.Yes | self.box.No, self.box.No)
                        if reply == self.box.Yes:
                                for a in [self.Data_218,self.Data_335]:
                                    a.Save()
                                self.Start = False
                                if self.actual:
                                            self.plot_pyqt.close()
                                            self.actual = False
                                #self.off_heater_1()
                                #self.off_heater_2()
                        else:
                                event.ignore()
                    if self.bt == True:
                        reply = self.box.question(self,
                                                        'Bitácora',
                                                        "¿Desea guardar la bitácora?\n(Se guardará en:  "+self.patch+")",
                                                        self.box.Yes | self.box.No, self.box.Yes)
                        if reply == self.box.Yes:
                            f = open (self.patch+'/Temperature.bt','a')
                            f.write(self.label_scroll)
                            f.close()
                    try:
                        for i in range(len(self.mpl)):
                            self.mpl[i].close()
                    except:
                        pass
                    try:
                        for i in range(len(self.mpl_ramp)):
                            self.mpl_ramp[i].close()
                    except:
                        pass
                    try:
                        for i in range(len(self.dialogs)):
                            self.dialogs[i].close()
                    except:
                        pass
            else:
                    event.ignore()
        except KeyboardInterrupt as KBI:
            pass
    def show_dialog(self):
        self.dialogs.append(Dialog(self)) 
        self.dialogs[-1].show()
    def show_218(self):
        self.dialogs.append(Segunda(self)) 
        self.dialogs[-1].show()
    def show_335(self):
        self.dialogs.append(Tercera(self)) 
        self.dialogs[-1].show()
    def show_help_218(self):
        self.dialogs.append(Help_218(self)) 
        self.dialogs[-1].show()
    def show_help_335(self):
        self.dialogs.append(Help_335(self)) 
        self.dialogs[-1].show()
    def show_218_Data(self):
        self.dialogs.append(D218_Data(self)) 
        self.dialogs[-1].show()
    def show_335_Data(self):
        self.dialogs.append(D335_Data(self)) 
        self.dialogs[-1].show()
    def show_Fit_of_data(self):
        self.dialogs.append(Fit_of_data(self)) 
        self.dialogs[-1].show()
    def show_Plot_File(self):
        self.dialogs.append(Plot_File(self)) 
        self.dialogs[-1].show()
    def show_Terminal(self):
        self.dialogs.append(Terminal_settings(self)) 
        self.dialogs[-1].show()
    def show_Icon(self):
        if os.path.isfile('/usr/share/applications/Temperature.desktop'):
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                    'Icon',
                    "Icon already exists",
                    self.box.Ok , self.box.Ok)
        else:
            self.dialogs.append(Icon(self)) 
            self.dialogs[-1].show()
    def buscarDirectorio(self):
        self.label_scroll+='                           Wait a moment Please\n'
        self.label_scroll+='-------------------------------------------------------------------------\n'
        self.Update_label()
        config_filename = self.patch_cfg + "/file_218.cfg"
        config_filename2 = self.patch_cfg + "/file_335.cfg"
        self.buscarDirectorio_2()
        if self.patch2:
            self.filename_218 = self.patch2 + '/file_218.cfg'
            self.filename_335 = self.patch2 + '/file_335.cfg'
            if os.path.isfile( self.patch2 +'/file_218.cfg') and\
                os.path.isfile( self.patch2 +'/file_335.cfg') :
                self.textDict_218 = ConfigModule(self.filename_218,0,0)
                self.textDict_335 = ConfigModule(self.filename_335,0,0)
                if os.path.isfile( self.patch2 +'/'+self.textDict_218.ConfigDict['Name']) and\
                    os.path.isfile( self.patch2 +'/'+self.textDict_218.ConfigDict['NameAverage']) and\
                    os.path.isfile( self.patch2 +'/'+self.textDict_335.ConfigDict['Name']) and\
                    os.path.isfile( self.patch2 +'/'+self.textDict_335.ConfigDict['NameAverage']) :
                    self.label_scroll += '                         The folder contains data\n'
                    self.label_scroll+='-------------------------------------------------------------------------\n'
                    self.Action_button(0)
                    self.Data_218 = TempClass(self.textDict_218.ConfigDict,patch=self.patch2)
                    self.Data_335 = TempClass(self.textDict_335.ConfigDict,self.Data_218.InitTime,patch=self.patch2)
                    self.Update_label()
                    self.start.setEnabled(False)
                    self.SeeData.setEnabled(True)
                    self.Time.setStyleSheet("color:rgb(255,255,255);border: 0px solid black;background-color: a( 0);")
                    self.grafica2.setEnabled(True)
                    self.grafica2.setChecked(True)
                    self.grafica2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                    self.Type.setStyleSheet("color:rgb(255,255,255);border: 0px solid black;background-color: a( 0);")
                    self.radioButton_2.setEnabled(True)
                    self.radioButton_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                    self.color_sensor.setStyleSheet("color:rgb(255,255,255);")
                    self.pushButton.setEnabled(True)
                    self.Todos.setEnabled(True)
                    self.Todos.setChecked(True)
                    i = 0
                    while i < len(self.sensor_ramp):
                        self.sensor_ramp[i].setEnabled(True)
                        i += 1
                    self.ramp_la.setStyleSheet("color:rgb(255,255,255);")
                    self.graph_sensor.setStyleSheet("color:rgb(255,255,255);")
                    self.patch = self.patch2
                    self.patch_cfg = self.patch + '/'
                    self.linePatch.setText(self.patch)
                else:
                    self.label_scroll+='                               Data no found\n'
                    self.label_scroll+='-------------------------------------------------------------------------\n'
                    self.Update_label()
                    self.Action_button(0)
            else:
                    self.label_scroll+='                               Selected folder\n'
                    self.label_scroll+='-------------------------------------------------------------------------\n'
                    self.Update_label()
                    try:
                        print(config_filename+self.patch2)
                        os.system('cp ' + config_filename + ' ' + self.patch2)
                        os.system('cp ' + config_filename2 + ' ' + self.patch2)
                        os.system('cd && cd ' + self.patch2+' && chmod =r file_218.cfg')
                        os.system('cd && cd ' + self.patch2+' && chmod =r file_335.cfg')
                        self.textDict_218 = ConfigModule(self.filename_218,1,1)
                        self.Update_label()
                        pg.QtGui.QApplication.processEvents()
                        self.textDict_335 = ConfigModule(self.filename_335,0,1)
                        pg.QtGui.QApplication.processEvents()
                        self.Data_218 = TempClass(self.textDict_218.ConfigDict,patch=self.patch2)
                        pg.QtGui.QApplication.processEvents()
                        self.Update_label()
                        self.Data_335 = TempClass(self.textDict_335.ConfigDict,self.Data_218.InitTime,patch=self.patch2)
                        pg.QtGui.QApplication.processEvents()
                        self.Update_label()
                        self.label_scroll+='                               Config File Ok\n'
                        self.start.setEnabled(True)
                        self.SeeData.setEnabled(True)
                        self.grafica2.setEnabled(True)
                        self.grafica2.setChecked(True)
                        self.grafica2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                        self.radioButton_2.setEnabled(True)
                        self.radioButton_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                        self.Todos.setEnabled(True)
                        self.Todos.setChecked(True)
                        i = 0
                        while i < len(self.sensor_ramp):
                            self.sensor_ramp[i].setEnabled(True)
                            i += 1
                        self.label_scroll+='               Push "Start" for begin adquisition\n'
                        self.label_scroll+='-------------------------------------------------------------------------\n'
                        self.Update_label()
                        pg.QtGui.QApplication.processEvents()
                        self.ramp_la.setStyleSheet("color:rgb(255,255,255);")
                        self.graph_sensor.setStyleSheet("color:rgb(255,255,255);")
                        self.color_sensor.setStyleSheet("color:rgb(255,255,255);")
                        self.Action_button(1)
                        self.patch = self.patch2
                        self.patch_cfg = self.patch+'/'
                        self.linePatch.setText(self.patch)
                    except Exception as e:
                        self.label_scroll += '       Error al cargar la configuración de los modulos\n'
                        self.label_scroll+='-------------------------------------------------------------------------\n'
                        os.system('cd && cd ' + self.patch2+' && rm file_218.cfg')
                        os.system('cd && cd ' + self.patch2+' && rm file_335.cfg')
                        self.Update_label()
                        self.start.setEnabled(False)
                        self.SeeData.setEnabled(False)
                        self.grafica2.setEnabled(False)
                        self.grafica2.setChecked(False)
                        self.grafica2.setStyleSheet("background-color: a(0);")
                        self.radioButton_2.setEnabled(False)
                        self.radioButton_2.setStyleSheet("background-color: a(0);")
                        self.Todos.setEnabled(False)
                        self.Todos.setChecked(False)
                        self.Todos.setStyleSheet("background-color: a(0);")
                        i = 0
                        while i < 8:
                            self.plot_checkbox[i].setEnabled(False)
                            self.plot_checkbox[i].setChecked(False)
                            self.plot_checkbox[i].setStyleSheet("background-color: a(0);")
                            i += 1
                        self.Time.setStyleSheet(" ")
                        self.Type.setStyleSheet(" ")
                        self.ramp_la.setStyleSheet(" ")
                        self.graph_sensor.setStyleSheet(" ")
                        self.color_sensor.setStyleSheet(" ")
                        self.pushButton.setEnabled(False)
                        self.ramp.setEnabled(False)
                        self.Action_button(0)
        else:
            self.label_scroll+='                               No selected folder\n'
            self.label_scroll+='-------------------------------------------------------------------------\n'
            self.Update_label()
            self.Action_button(0)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    def buscarDirectorio_2(self):
        self.patch2 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Search folder', self.patch)
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
                self.ramp.setEnabled(True)
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
            for a in self.sensor_ramp:
                if a == self.ramp_CA:
                    a.setChecked(True)
                else:
                    a.setChecked(False)
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
            i = 0
            while i < 8:
                self.plot_checkbox[i].setEnabled(False)
                self.plot_checkbox[i].setChecked(True)
                self.plot_checkbox[i].setStyleSheet("background-color: a(0);")
                i += 1
        else:
            self.Todos.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            i = 0
            while i < 8:
                self.plot_checkbox[i].setEnabled(True)
                self.plot_checkbox[i].setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
                i += 1
    def desbloquear_heater_1(self):
        if self.heater_1.isChecked():
            try:
                self.On_335_1()
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
                self.label_scroll += '                     Error al cargar Heater 1'
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
        if self.heater_2.isChecked():
            try:
                self.On_335_2()
            except:
                self.label_scroll += '                                   Error al cargar Heater 2'
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
            self.status_heater_1 = True
            if self.heater_1_estatus:
                self.label_heater_1 = '--------------------------------------\n'
                self.label_heater_1 += '       Status Heater 1      \n'
                self.label_heater_1 += '--------------------------------------\n'
                self.heater_1_estatus = False
            self.status_1.setWidget(QtWidgets.QLabel(self.label_heater_1))
        else:
            self.seeStatus_1.setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);font: 12pt 'Sans Serif';")
            self.status_heater_1 = False
            self.status_1.verticalScrollBar().setValue(self.status_1.verticalScrollBar().maximum())
    def desbloquear_seeStatus_2(self):
        if self.seeStatus_2.isChecked():
            self.seeStatus_2.setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.status_2.setEnabled(True)
        else:
            self.seeStatus_2.setStyleSheet("background-color: a(0);rgb(88, 160, 255);")
    def desbloquear_sensores(self,num,col):
        if self.plot_checkbox[num].isChecked():
            self.plot_checkbox[num].setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_button[col].setEnabled(True)
            color_rgb = self.textDict_color.ConfigDict[self.names_sensor_color[num]]
            self.color_button[col].setStyleSheet("background-color: rgb("+color_rgb[0]+','\
                                        +color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        elif self.sensor_ramp[num].isChecked():
            self.plot_checkbox[num].setStyleSheet("background-color: a(0);\
                                                color: rgb(88, 160, 255);")
        else:
            self.plot_checkbox[num].setStyleSheet("background-color: a(0);\
                                                color: rgb(88, 160, 255);")
            self.color_button[col].setEnabled(False)
            self.color_button[col].setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_CA(self):
        self.desbloquear_sensores(0,10)
    def desbloquear_sensores_CB(self):
        self.desbloquear_sensores(1,11)
    def desbloquear_sensores_C5(self):
        self.desbloquear_sensores(6,8)
    def desbloquear_sensores_C6(self):
        self.desbloquear_sensores(7,9)
    def desbloquear_sensores_D1(self):
        self.desbloquear_sensores(2,4)
    def desbloquear_sensores_D2(self):
        self.desbloquear_sensores(3,5)
    def desbloquear_sensores_D3(self):
        self.desbloquear_sensores(4,6)
    def desbloquear_sensores_D4(self):
        self.desbloquear_sensores(5,7)
    def desbloquear_sensores_ramp(self,num,col):
        if self.sensor_ramp[num].isChecked():
            if self.grafica1.isChecked():
                self.block(self.sensor_ramp[num])
            self.color_button[col].setEnabled(True)
            color_rgb = self.textDict_color.ConfigDict[self.names_sensor_color[num]]
            self.color_button[col].setStyleSheet("background-color: rgb("+color_rgb[0]\
                                        +','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        elif self.plot_checkbox[num].isChecked():
            pass
        else:
            self.color_button[col].setEnabled(False)
            self.color_button[col].setStyleSheet("background-color: a(0);")
    def desbloquear_sensores_ramp_CA(self):
        self.desbloquear_sensores_ramp(0,10)
    def desbloquear_sensores_ramp_CB(self):
        self.desbloquear_sensores_ramp(1,11)
    def desbloquear_sensores_ramp_C5(self):
        self.desbloquear_sensores_ramp(6,8)
    def desbloquear_sensores_ramp_C6(self):
        self.desbloquear_sensores_ramp(7,9)
    def desbloquear_sensores_ramp_D1(self):
        self.desbloquear_sensores_ramp(2,4)
    def desbloquear_sensores_ramp_D2(self):
        self.desbloquear_sensores_ramp(3,5)
    def desbloquear_sensores_ramp_D3(self):
        self.desbloquear_sensores_ramp(4,6)
    def desbloquear_sensores_ramp_D4(self):
        self.desbloquear_sensores_ramp(5,7)
    def block(self,ramp):
        for a in self.sensor_ramp:
            if a==ramp:
                pass
            else:
                a.setChecked(False)
    def desbloquear_heaters(self,col,num):
        Names = ['H1','H2','S1','S2']
        if self.plot_checkbox[num].isChecked():
            self.plot_checkbox[num].setStyleSheet("background-color: a(0);color: rgb(0, 255, 0);")
            self.color_button[col].setEnabled(True)
            color_rgb = self.textDict_color.ConfigDict[Names[col]]
            self.color_button[col].setStyleSheet("background-color: rgb("+color_rgb[0]+','+color_rgb[1]+','+color_rgb[2]+\
                                        ");border: 1px solid black;")
        else:
            self.plot_checkbox[num].setStyleSheet("background-color: a(0);color: rgb(88, 160, 255);")
            self.color_button[col].setEnabled(False)
            self.color_button[col].setStyleSheet("background-color: a(0);")
    def desbloquear_heater1(self):
        self.desbloquear_heaters(0,9)
    def desbloquear_heater2(self):
        self.desbloquear_heaters(1,11)
    def desbloquear_SetPoint1(self):
        self.desbloquear_heaters(2,8)
    def desbloquear_SetPoint2(self):
        self.desbloquear_heaters(3,10)
    def graficar(self):
        self.curvas = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        if self.Todos.isChecked():
                for i in range(9):
                    self.curvas[i]=1

        else:
                if self.CA.isChecked():
                    self.curvas[1] = 1
                if self.CB.isChecked():
                    self.curvas[2] = 1
                if self.D1.isChecked():
                    self.curvas[3] = 1
                if self.D2.isChecked():
                    self.curvas[4] = 1
                if self.D3.isChecked():
                    self.curvas[5] = 1
                if self.D4.isChecked():
                    self.curvas[6] = 1
                if self.C5.isChecked():
                    self.curvas[7] = 1
                if self.C6.isChecked():
                    self.curvas[8] = 1
        if self.SetPoint1.isChecked():
                self.curvas[9] = 1
        if self.heater1.isChecked():
                self.curvas[10] = 1
        if self.SetPoint2.isChecked():
                self.curvas[11] = 1
        if self.heater2.isChecked():
                self.curvas[12] = 1
        if self.radioButton.isChecked():
            horas = self.hh.value()
            minutos = self.mm.value()
            segundos = self.ss.value()
            self.Time_graph = horas*3600 + minutos*60 + segundos
        else:
            self.Time_graph = float('inf')
        if self.grafica1.isChecked():
            if self.actual:
                self.plot_pyqt.close()
            self.actual, self.close_plot = True, False
            self.plot_pyqt = Live_plot()
        else:
            self.actual = False
            self.matplotlib()
    def matplotlib(self):
        try:
            if self.num_matplotlib==0:
                self.mpl=[]
                self.mpl.append(Plot_matplotlib())
                self.mpl[0].show()
            else:
                self.mpl.append(Plot_matplotlib())
                self.mpl[self.num_matplotlib].show()
            self.num_matplotlib += 1
        except:
            pass
class Tercera(QtWidgets.QDialog,Ui_Tercera):
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
            self.setWindowTitle("335 TemperatureController")
            self.name.setText(window.textDict_335.ConfigDict['Name'])
            self.nameAverage.setText(window.textDict_335.ConfigDict['NameAverage'])
            self.model.setText(window.textDict_335.ConfigDict['Model'])
            if len(window.textDict_335.ConfigDict['Channels'])==2:
                self.sensor1.setText(window.textDict_335.ConfigDict['Sensor Type'][0])
                self.sensor2.setText(window.textDict_335.ConfigDict['Sensor Type'][1])
                self.sensor1_on.setChecked(True)
                self.sensor2_on.setChecked(True)
            elif window.textDict_335.ConfigDict['Channels']=='A':
                self.sensor1.setText(window.textDict_335.ConfigDict['Sensor Type'])
                self.sensor1_on.setChecked(True)
            elif window.textDict_335.ConfigDict['Channels']=='B':
                self.sensor2.setText(window.textDict_335.ConfigDict['Sensor Type'])
                self.sensor2_on.setChecked(True)
            self.sensor1_on.toggled.connect(self.desbloquear_sensor1)
            self.sensor2_on.toggled.connect(self.desbloquear_sensor2)
            self.port.setText(window.textDict_335.ConfigDict['Port'])
            self.savedata.setValue(int(window.textDict_335.ConfigDict['SaveData']))
            self.average.setValue(int(window.textDict_335.ConfigDict['Average']))
            self.samplinperiod.setValue(float(window.textDict_335.ConfigDict['SamplingPeriod']))
            self.timeOut.setValue(float(window.textDict_335.ConfigDict['TimeOut']))

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
        if window.action_flag:
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
                                        "Valor inválido TypeSensor 1",
                                        self.box.Ok , self.box.Ok)
                pg.QtGui.QApplication.processEvents()
            elif not self.sensor2.text() or self.sensor2.text().isspace():
                self.box = QtWidgets.QMessageBox()
                reply = self.box.question(self,
                                        'Error',
                                        "Valor inválido TypeSensors 2",
                                        self.box.Ok , self.box.Ok)
                pg.QtGui.QApplication.processEvents()
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                        'Settings',
                                        "Are you sure you want to change the settings?",
                                        self.box.Yes | self.box.No, self.box.No)
            pg.QtGui.QApplication.processEvents()
            if reply == self.box.Yes:
                Change(window.filename_335,self.model.text(),'Model',window.textDict_218.ConfigDict) 
                Change(window.filename_335,self.name.text(),'Name',window.textDict_218.ConfigDict)
                Change(window.filename_335,self.nameAverage.text(),'NameAverage',window.textDict_218.ConfigDict)
                Change(window.filename_335,self.savedata.value(),'SaveData',window.textDict_218.ConfigDict)
                Change(window.filename_335,self.timeOut.value(),'TimeOut',window.textDict_218.ConfigDict)
                Change(window.filename_335,self.port.text(),'Port',window.textDict_218.ConfigDict)
                Change(window.filename_335,self.average.value(),'Average',window.textDict_218.ConfigDict)
                Change(window.filename_335,self.samplinperiod.value(),'SamplingPeriod',window.textDict_218.ConfigDict)
            self.close()
        else:
            self.close
class Rampa_live(QtWidgets.QDialog,Ui_ramp):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Ramp Monitor")
            layout = QtGui.QGridLayout(self.widget)
            self.widget.setLayout(layout)
            for i in range(len(window.curvas_ramp)):
                if window.curvas_ramp[i] == 1:
                    name = i
                    break
            self.ramp_live = Dashboard(window.names_sensor[i], "K/min", 0, 5)
            layout.addWidget(self.ramp_live)
            pg.QtGui.QApplication.processEvents()
        except KeyboardInterrupt as KBI:
            pass
    def charges(self,num):
        self.ramp_live.charge(num)
    def closeEvent(self, event):
        window.ramp_stat = False
class Plot_File(QtWidgets.QDialog,Ui_plot_file):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Plot File")
            self.objets_dialog = [self.control,self.monitor,self.title]
            i = 0
            while i < 3:
                self.objets_dialog[i].setText(window.file_plot_names[i])
                i += 1
        except KeyboardInterrupt as KBI:
            pass
    def accept(self):
        i, flag = 0, True
        while i < 3:
                if not self.objets_dialog[i] or self.objets_dialog[i].text().isspace():
                    self.box = QtWidgets.QMessageBox()
                    reply = self.box.question(self,
                                            'Error',
                                            "Value invalid",
                                            self.box.Ok , self.box.Ok)
                    pg.QtGui.QApplication.processEvents()
                    flag = False
                    break
                i += 1
        if flag:
            window.file_plot_names = [self.control.text(),self.monitor.text(),self.title.text()]
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Change Plot File',
                                    "Successful",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
class Fit_of_data(QtWidgets.QDialog,Ui_fit):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Fit of Data")
            self.sensor_fit_M = [self.CA_M,self.CB_M,self.D1_M,self.D2_M,\
                                self.D3_M,self.D4_M,self.C5_M,self.C6_M]
            self.sensor_fit_I = [self.CA_I,self.CB_I,self.D1_I,self.D2_I,\
                                self.D3_I,self.D4_I,self.C5_I,self.C6_I]
            self.sensor = [self.CA,self.CB,self.D1,self.D2,self.D3,self.D4,\
                            self.C5,self.C6]
            i = 0
            while i < 8:
                self.sensor_fit_M[i].setDecimals(4)
                self.sensor_fit_I[i].setDecimals(4)
                self.sensor_fit_M[i].setRange(-100,100)
                self.sensor_fit_I[i].setRange(-100,100)
                self.sensor_fit_M[i].setValue(float(\
                    window.textDict_fit.ConfigDict[window.names_sensor_color[i]][0]))
                self.sensor_fit_I[i].setValue(float(\
                    window.textDict_fit.ConfigDict[window.names_sensor_color[i]][1]))
                if float(window.textDict_fit.ConfigDict[window.names_sensor_color[i]][0]) == 0:
                    if float(window.textDict_fit.ConfigDict[window.names_sensor_color[i]][1]) == 0:
                        self.sensor_fit_I[i].setEnabled(False)
                        self.sensor_fit_M[i].setEnabled(False)
                        self.sensor[i].setStyleSheet("background-color: a(0);\
                            color: rgb(85, 0, 127);")
                self.sensor_fit_I[i].setEnabled(True)
                self.sensor_fit_M[i].setEnabled(True)
                self.sensor[i].setStyleSheet(\
                    "background-color: a(0);color: rgb(255, 170, 255);;")
                self.sensor[i].setChecked(True)
                i += 1
                pg.QtGui.QApplication.processEvents()
            self.sensor_des = [self.CA_des,self.CB_des,self.D1_des,self.D2_des,\
                                self.D3_des,self.D4_des,self.C5_des,self.C6_des]
            i = 0
            while i < 8:
                self.sensor[i].toggled.connect(self.sensor_des[i])
                i += 1
        except KeyboardInterrupt as KBI:
            pass
    def CA_des(self):
        self.desbloquear(0)
    def CB_des(self):
        self.desbloquear(1)
    def D1_des(self):
        self.desbloquear(2)
    def D2_des(self):
        self.desbloquear(3)
    def D3_des(self):
        self.desbloquear(4)
    def D4_des(self):
        self.desbloquear(5)
    def C5_des(self):
        self.desbloquear(6)
    def C6_des(self):
        self.desbloquear(7)
    def desbloquear(self,num):
        if self.sensor[num].isChecked():
            self.sensor_fit_I[num].setEnabled(True)
            self.sensor_fit_M[num].setEnabled(True)
            self.sensor[num].setStyleSheet(\
                "background-color: a(0);color: rgb(255, 170, 255);;")
        else:
            self.sensor_fit_I[num].setEnabled(False)
            self.sensor_fit_M[num].setEnabled(False)
            self.sensor[num].setStyleSheet("background-color: a(0);\
                color: rgb(85, 0, 127);")
class D218_Data(QtWidgets.QDialog,Ui_fit_218):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.patch_last = window.patch
            self.setupUi(self)
            self.setWindowTitle("Fit Data Temperature Monitor 218")
            self.select.clicked.connect(self.buscarArchivo)
            self.fit.clicked.connect(self.fit_file)
            self.fit.setEnabled(False)
        except KeyboardInterrupt as KBI:
            pass
    def buscarArchivo(self):
        patch_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Search file', self.patch_last, "Text Files (*.txt)")
        if patch_file:
            self.patch_last = patch_file[0]
            self.file.setText(self.patch_last)
            self.fit.setEnabled(True)
        else:
            self.fit.setEnabled(False)
            self.file.setText(' ')
    def fit_file(self):
        try:
            myFile=self.patch_last
            myNewFile=myFile.strip('.txt')+'_fit.txt'
            for line in open(myFile,'r'):
                if line[0] == '#' or line[0]=='\n':
                    newLine=line
                    if line=='#Type of file: Complete Data\n':
                        newLine=line.strip('\n')+' '+'Fit'+'\n'
                else:
                    line = line.split('\t')
                    newLine = line[0] 
                    newLine+='\t'+str("{0:.2f}".format(float(line[1])*\
                                float(window.textDict_fit.ConfigDict['D1'][0])+\
                                float(window.textDict_fit.ConfigDict['D1'][1])))
                    newLine+='\t'+str("{0:.2f}".format(float(line[2])*\
                                float(window.textDict_fit.ConfigDict['D2'][0])+\
                                float(window.textDict_fit.ConfigDict['D2'][1])))
                    newLine+='\t'+str("{0:.2f}".format(float(line[3])*\
                                float(window.textDict_fit.ConfigDict['D3'][0])+\
                                float(window.textDict_fit.ConfigDict['D3'][1])))
                    newLine+='\t'+str("{0:.2f}".format(float(line[4])*\
                                float(window.textDict_fit.ConfigDict['D4'][0])+\
                                float(window.textDict_fit.ConfigDict['D4'][1])))
                    newLine+='\t'+str("{0:.2f}".format(float(line[5])*\
                                float(window.textDict_fit.ConfigDict['C5'][0])+\
                                float(window.textDict_fit.ConfigDict['C5'][1])))
                    newLine+='\t'+str("{0:.2f}".format(float(line[6])*\
                                float(window.textDict_fit.ConfigDict['C6'][0])+\
                                float(window.textDict_fit.ConfigDict['C6'][1])))
                    newLine += '\n'
                file=open(myNewFile,'a')  
                file.write(newLine)
                pg.QtGui.QApplication.processEvents()
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                        'Fit',
                                        "The fit was successful",
                                        self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        except:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                        'Error',
                                        "Error fit",
                                        self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
class D335_Data(QtWidgets.QDialog,Ui_fit_335):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.patch_last = window.patch
            self.setWindowTitle("Fit Data Temperature Control 335")
            self.select.clicked.connect(self.buscarArchivo)
            self.fit.clicked.connect(self.fit_file)
            self.fit.setEnabled(False)
        except KeyboardInterrupt as KBI:
            pass
    def buscarArchivo(self):
        patch_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Search file', self.patch_last, "Text Files (*.txt)")
        if patch_file:
            self.patch_last = patch_file[0]
            self.file.setText(self.patch_last)
            self.fit.setEnabled(True)
        else:
            self.fit.setEnabled(False)
            self.file.setText(' ')
    def fit_file(self):
        try:
            myFile=self.patch_last
            myNewFile=myFile.strip('.txt')+'_fit.txt'
            for line in open(myFile,'r'):
                if line[0] == '#' or line[0]=='\n':
                    newLine=line
                    if line=='#Type of file: Complete Data\n':
                        newLine=line.strip('\n')+' '+'Fit'+'\n'
                else:
                    line = line.split('\t')
                    newLine = line[0] 
                    newLine+='\t'+str("{0:.2f}".format(float(line[1])*\
                                float(window.textDict_fit.ConfigDict['CA'][0])+\
                                float(window.textDict_fit.ConfigDict['CA'][1])))
                    newLine+='\t'+str("{0:.2f}".format(float(line[2])*\
                                float(window.textDict_fit.ConfigDict['CB'][0])+\
                                float(window.textDict_fit.ConfigDict['CB'][1])))
                    newLine += '\n'
                pg.QtGui.QApplication.processEvents()
                file=open(myNewFile,'a')  
                file.write(newLine)
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                        'Fit',
                                        "The fit was successful",
                                        self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
        except:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                        'Error',
                                        "Error fit",
                                        self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
class Help_218(QtWidgets.QDialog,Ui_help_218):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Help Temperature Monitor 218")
        except KeyboardInterrupt as KBI:
            pass
class Terminal_settings(QtWidgets.QDialog,Ui_Terminal):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Settings Terminal")
            self.passwo.setEchoMode(QtWidgets.QLineEdit.Password)
        except KeyboardInterrupt as KBI:
            pass
    def accept(self):
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Settings',
                                    "Are you sure you want to change the settings?",
                                    self.box.Yes | self.box.No, self.box.No)
            pg.QtGui.QApplication.processEvents()
            if reply == self.box.Yes:
                try:
                    password = self.passwo.text()
                    patch = os.path.realpath(__file__).strip('prueba1.py') + 'cfg/terminal.cfg'
                    command = 'sudo rm '+patch+' && sudo echo "'+self.textEdit.toPlainText()+'">> ' +patch
                    os.system('cd && ' + 'echo %s|sudo -S %s' % (password, command))
                    os.system("xrdb " + patch )
                    self.box = QtWidgets.QMessageBox()
                    window.tabWidget.clear()
                    window.tabWidget.addTab(Terminal(),"Terminal")
                    reply = self.box.question(self,
                                            'Change Plot File',
                                            "Successful",
                                            self.box.Ok , self.box.Ok)
                    pg.QtGui.QApplication.processEvents()
                    if reply == self.box.Ok:
                        self.close()
                except:
                    self.box = QtWidgets.QMessageBox()
                    reply = self.box.question(self,
                                            'Error',
                                            "Password Incorrect",
                                            self.box.Ok , self.box.Ok)
                    pg.QtGui.QApplication.processEvents()
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
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("About Temperature")
        except KeyboardInterrupt as KBI:
            pass
class Icon(QtWidgets.QDialog,Ui_Icon):
    def __init__(self, *args, **kwargs):
        try:
            QtWidgets.QDialog.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.setWindowTitle("Add Icon")
            self.passwo.setEchoMode(QtWidgets.QLineEdit.Password)
        except KeyboardInterrupt as KBI:
            pass
    def accept(self):
        password = self.passwo.text()
        which_Te = subprocess.getoutput('which Temperature')
        patch = os.path.realpath(__file__).strip('prueba1.py') + 'Temperature.png'
        command = 'sudo echo "[Desktop Entry]\nName=Temperature\nComment=Temperature\n\
                            Exec=' + which_Te + '\nIcon=' + patch + '\nTerminal=false\n\
                            Type=Application">>/usr/share/applications/Temperature.desktop'
        os.system('cd && ' + 'echo %s|sudo -S %s' % (password, command))
        if os.path.isfile('/usr/share/applications/Temperature.desktop'):
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Change Plot File',
                                    "Successful",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
            if reply == self.box.Ok:
                self.close()
        else:
            self.box = QtWidgets.QMessageBox()
            reply = self.box.question(self,
                                    'Error',
                                    "Password Incorrect",
                                    self.box.Ok , self.box.Ok)
            pg.QtGui.QApplication.processEvents()
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
            self.curves = [self.curve1,self.curve2,self.curve3,self.curve4\
                            ,self.curve5,self.curve6,self.curve7,self.curve8]
            self.sensors = [self.sensor1,self.sensor2,self.sensor3,self.sensor4,\
                            self.sensor5,self.sensor6,self.sensor7,self.sensor8]
            self.sensors_on = [self.sensor1_on,self.sensor2_on,self.sensor3_on,self.sensor4_on,\
                            self.sensor5_on,self.sensor6_on,self.sensor7_on,self.sensor8_on]
            self.desbloquear = [self.desbloquear_sensor1,self.desbloquear_sensor2,\
                                self.desbloquear_sensor3,self.desbloquear_sensor4,\
                                self.desbloquear_sensor5,self.desbloquear_sensor6,\
                                self.desbloquear_sensor7,self.desbloquear_sensor8]
            print(window.textDict_218.ConfigDict)
            for a in self.curves:
                a.setRange(0,28)
            self.setWindowTitle("218 TemperatureMonitor")
            self.name.setText(window.textDict_218.ConfigDict['Name'])
            self.nameaverage.setText(window.textDict_218.ConfigDict['NameAverage'])
            self.model.setText(window.textDict_218.ConfigDict['Model'])
            i = 0
            while i < len(window.textDict_218.ConfigDict['Sensor Type']):
                if window.textDict_218.ConfigDict['Sensor Status '+str(i+1)]=='1':
                    self.sensors[i].setText(window.textDict_218.ConfigDict['Sensor Type'][i])
                    self.sensors_on[i].setChecked(True)
                    self.curves[i].setValue(int(window.textDict_218.ConfigDict['CP'+str(i+1)]))
                self.sensors_on[i].toggled.connect(self.desbloquear[i])
                i += 1
            self.port.setText(window.textDict_218.ConfigDict['Port'])
            self.savedata.setValue(int(window.textDict_218.ConfigDict['SaveData']))
            self.average.setValue(int(window.textDict_218.ConfigDict['Average']))
            self.samplinperiod.setValue(float(window.textDict_218.ConfigDict['SamplingPeriod']))
            self.timeOut.setValue(float(window.textDict_218.ConfigDict['TimeOut']))
        except KeyboardInterrupt as KBI:
            pass
    def desbloquear_sensor1(self):
        self.desbloquear_sensors(0)
    def desbloquear_sensor2(self):
        self.desbloquear_sensors(1)
    def desbloquear_sensor3(self):
        self.desbloquear_sensors(2)
    def desbloquear_sensor4(self):
        self.desbloquear_sensors(3)
    def desbloquear_sensor5(self):
        self.desbloquear_sensors(4)
    def desbloquear_sensor6(self):
        self.desbloquear_sensors(5)
    def desbloquear_sensor7(self):
        self.desbloquear_sensors(6)
    def desbloquear_sensor8(self):
        self.desbloquear_sensors(7)
    def desbloquear_sensors(self,num):
        if self.sensors_on[num].isChecked():
            self.sensors[num].setEnabled(True)
            self.curves[num].setEnabled(True)
        else:
            self.sensors[num].setEnabled(False)
            self.curves[num].setEnabled(False)
    def accept(self): 
        i = 0
        flag = False
        while i < 8 :
            if self.sensors_on[i].isChecked():
                if 9 < self.curves[i].value() < 21:
                    self.box = QtWidgets.QMessageBox()
                    reply = self.box.question(self,
                                            'Error',
                                            "Invalid Curve Sensor "+str(i+1)+" value",
                                            self.box.Ok , self.box.Ok)
                    flag = True
                    break
                elif not self.sensors[i].text() or self.sensors[i].text().isspace():
                    self.box = QtWidgets.QMessageBox()
                    reply = self.box.question(self,
                                            'Error',
                                            "Valor inválido TypeSensor "+str(i+1),
                                            self.box.Ok , self.box.Ok)
                    flag = True 
                    break
            i += 1
            pg.QtGui.QApplication.processEvents()
        if flag:
            pass
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
        self.box = QtWidgets.QMessageBox()
        reply = self.box.question(self,
                                    'Settings',
                                    "Are you sure you want to change the settings?",
                                    self.box.Yes | self.box.No, self.box.No)
        pg.QtGui.QApplication.processEvents()
        if reply == self.box.Yes:
            Change(window.filename_218,self.model.text(),'Model',window.textDict_218.ConfigDict) 
            Change(window.filename_218,self.name.text(),'Name',window.textDict_218.ConfigDict)
            Change(window.filename_218,self.nameaverage.text(),'NameAverage',window.textDict_218.ConfigDict)
            Change(window.filename_218,self.savedata.value(),'SaveData',window.textDict_218.ConfigDict)
            Change(window.filename_218,self.timeOut.value(),'TimeOut',window.textDict_218.ConfigDict)
            Change(window.filename_218,self.port.text(),'Port',window.textDict_218.ConfigDict)
            Change(window.filename_218,self.average.value(),'Average',window.textDict_218.ConfigDict)
            Change(window.filename_218,self.samplinperiod.value(),'SamplingPeriod',window.textDict_218.ConfigDict)
            i = 0
            while i < 8:
                if self.sensors_on[i].isChecked():
                    Change(window.filename_218,self.sensors[i].text(),'Sensor Type',window.textDict_218.ConfigDict)
                    Change(window.filename_218,'Sensor '+str(i+1),'',window.textDict_218.ConfigDict)
                    window.textDict_218.ConfigDict['Sensor Type'].append(self.sensors[i].text())
                    window.textDict_218.ConfigDict['Sensors'].append('Sensor '+str(i+1))
                    window.textDict_218.ConfigDict['Channels'].append(i+1)
                    window.textDict_218.ConfigDict['Sensor Status '+str(i+1)] = str(1)
                    window.textDict_218.ConfigDict['CP'+str(i+1)] = str(self.curves[i].value())
                else:
                    window.textDict_218.ConfigDict['Sensor Status '+str(i+1)] = str(0)
                    window.textDict_218.ConfigDict['CP'+str(i+1)] = str(0)

        self.close()
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
class Dashboard(QtWidgets.QWidget):
    def __init__(self, title, unit, min, max, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.min = min
        self.max = max
        self.value = min
        self.title = title
        self.ramp_angle = 100.0 * (self.value-self.min)/(self.max-self.min)
        self.gradient =  QtGui.QConicalGradient(0, 0, 180)
        self.gradient.setColorAt(0, QtCore.Qt.red)
        self.gradient.setColorAt(0.3, QtCore.Qt.yellow)
        self.gradient.setColorAt(0.5, QtCore.Qt.green)
        self.unit = unit
    def charge(self, value):
        print(value)
        self.value = abs(value)
        if self.value < 0.0049:
            self.value = 0
        self.ramp_angle = 100.0 * (self.value-self.min)/(self.max-self.min)
        self.update()
    def paintEvent(self, event):
        pos_1 = QtCore.QPoint(0, -70)
        pos_2 = QtCore.QPoint(0, -90)
        extRect = QtCore.QRectF(-90,-90,180,180)
        intRect = QtCore.QRectF(-70,-70,140,140)
        unitRect = QtCore.QRectF(-54,60,110,50)
        labelvalue = self.value.__str__()[0:4]
        angle = self.ramp_angle * 270.0 / 100.0
        line = QtGui.QPainterPath()
        line.moveTo(pos_1)
        line.lineTo(pos_2)
        line.arcTo(extRect, 90, -1 * angle)
        line.arcTo(intRect, 90 - angle, angle)

        label = QtGui.QPainter(self)
        label.setRenderHint(QtGui.QPainter.Antialiasing)
        label.translate(self.width() / 2, self.height() / 2)
        side = min(self.width(), self.height())
        label.scale(side / 200.0, side / 200.0)

        label.save()
        label.rotate(-135)
        label.setBrush(self.gradient)
        label.setPen(QtCore.Qt.NoPen)
        label.drawPath(line)
        label.restore()
        label.save()
        label.translate(QtCore.QPointF(0, -50))

        Font = QtGui.QFont(self.font().family(), 18)
        label.setFont(Font)
        label.drawText(unitRect, QtCore.Qt.AlignCenter, "{}".format(self.unit))
        label.restore()

        label.setFont(Font)
        label.drawText(unitRect, QtCore.Qt.AlignCenter, "{}".format(self.title))
        speedWidth = QtGui.QFontMetrics(Font).width(labelvalue)

        leftPos = -1 * speedWidth - 20
        topPos = 10
        Font = QtGui.QFont(self.font().family(), 55)
        label.setPen(QtGui.QColor(QtCore.Qt.black))
        label.setFont(Font)
        label.drawText(leftPos, topPos, labelvalue)
class Live_plot(object):
    def __init__(self):
        self.win = pg.GraphicsWindow(title='Data')
        self.p = self.win.addPlot(title='Sensores')
        self.p.setLabel('left', 'Temperature ',units= 'K')
        self.p.setLabel('bottom', 'Time ',units='s')
        self.p.showGrid(x=False,y=True,alpha=0.3)
        self.names_curves = window.names_sensor
        self.names_curves_heater = []
        for a in ['SetPoint 1','Heater 1','SetPoint 2','Heater 2']:
            self.names_curves_heater.append(a)
            pg.QtGui.QApplication.processEvents()
        self.c=[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.d=[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.t=[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.p.addLegend()
        b = []
        if window.curvas[0] == 1:
            for i in range(len(window.names_sensor)):
                self.c[i]=self.p.plot(pen=window.color[i],name=self.names_curves[i])
                pg.QtGui.QApplication.processEvents()
        else:
            for i in range(len(window.names_sensor)):
                if window.curvas[1+i] == 1:
                    self.c[i]=self.p.plot(pen=window.color[i],name=self.names_curves[i])
                pg.QtGui.QApplication.processEvents()
        try:
            i_cnt = 0
            for name in [window.Data_335,window.Data_218]:
                a = name.Plot_inter(window.file_plot_names[i_cnt])
                for c in a:
                    b.append(c)
                    pg.QtGui.QApplication.processEvents()
                i_cnt += 1
                pg.QtGui.QApplication.processEvents()
        except:
            pass
        i_cnt = 0
        if window.curvas[0] == 1 and len(b)>0:
            for i in range(len(window.names_sensor)):
                for inte in range(len(b[i][0])):
                    self.d[i],self.t[i] = self.Curvas_add(self.d[i],self.t[i],\
                                                            b[i][1][inte]*window.fit_number[i][0]\
                                                                        +window.fit_number[i][1]\
                                                                        ,b[i][0][inte])
                    pg.QtGui.QApplication.processEvents()
        elif len(b)>0:
            for i in range(len(window.names_sensor)):
                for inte in range(len(b[i][0])):
                    if window.curvas[i+1] ==1:
                        self.d[i],self.t[i] = self.Curvas_add(self.d[i],self.t[i],\
                                                            b[i][1][inte]*window.fit_number[i][0]\
                                                                        +window.fit_number[i][1]\
                                                                        ,b[i][0][inte])
                    pg.QtGui.QApplication.processEvents()
        b = []
        for name in [window.Data_335,window.Data_218]:
            a = name.Plot_inter_header(window.file_plot_names[i_cnt])
            for c in a:
                b.append(c)
                pg.QtGui.QApplication.processEvents()
            i_cnt += 1
            pg.QtGui.QApplication.processEvents()
        if window.curvas[0] == 1:
            for i in range(len(window.names_sensor)):
                for inte in range(len(b[i][0])):
                    self.d[i],self.t[i] = self.Curvas_add(self.d[i],self.t[i],\
                                                            b[i][1][inte]*window.fit_number[i][0]\
                                                                        +window.fit_number[i][1]\
                                                                        ,b[i][0][inte])
                    pg.QtGui.QApplication.processEvents()
        else:
            for i in range(len(window.names_sensor)):
                for inte in range(len(b[i][0])):
                    if window.curvas[i+1] ==1:
                        self.d[i],self.t[i] = self.Curvas_add(self.d[i],self.t[i],\
                                                            b[i][1][inte]*window.fit_number[i][0]\
                                                                        +window.fit_number[i][1]\
                                                                        ,b[i][0][inte])
                    pg.QtGui.QApplication.processEvents()
        for i in [8,9,10,11]:
                if window.curvas[1+i] == 1:
                    self.c[i]=self.p.plot(pen=window.color[i],name=self.names_curves_heater[i-8])
                pg.QtGui.QApplication.processEvents()
        self.p.setRange(yRange=[50, 300])
    def add(self, x):
            if window.curvas[0] == 1:
                for i in range(len(window.names_sensor)):
                    self.d[i],self.t[i] = self.Curvas_add(self.d[i],self.t[i],\
                                                            float(x[i][2])*window.fit_number[i][0]\
                                                                        +window.fit_number[i][1]\
                                                                        ,x[i][1])
            else:
                for i in range(len(window.names_sensor)):
                    if window.curvas[i+1] ==1:
                        self.d[i],self.t[i] = self.Curvas_add(self.d[i],self.t[i],\
                                                            float(x[i][2])*window.fit_number[i][0]\
                                                                        +window.fit_number[i][1]\
                                                                        ,x[i][1])
            if window.curvas[9] == 1:
                self.d[8],self.t[8] = self.Curvas_add(self.d[8],self.t[8],self.SP_1,x[7][1])

            if window.curvas[10] == 1:
                HTR_1 = float(window.Data_335.Read_335('SETP?','1'))
                self.d[9],self.t[9] = self.Curvas_add(self.d[9],self.t[9],HTR_1,x[7][1])
                time.sleep(0.05)

            if window.curvas[11] == 1:
                self.d[10],self.t[10] = self.Curvas_add(self.d[10],self.t[10],self.SP_2,x[7][1])

            if window.curvas[12] == 1:
                HTR_2 = float(window.Data_335.Read_335('SETP?','2'))
                self.d[11],self.t[11] = self.Curvas_add(self.d[11],self.t[11],HTR_2,x[7][1])
                time.sleep(0.05)
            pg.QtGui.QApplication.processEvents()
    def Curvas_add(self, Datos_curvas, Tiempo_curvas,datos,tiempos):
       
        Datos_curvas.append(datos)
        Tiempo_curvas.append(tiempos)
        for i in range(len(Tiempo_curvas)):
            if Tiempo_curvas[-1]-Tiempo_curvas[0] > window.Time_graph:
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
            if window.curvas[0] == 1:
                for i in range(len(self.names_curves)):
                    self.c[i].setData(self.t[i],self.d[i])
            else:
                for i in range(len(self.names_curves)):
                    if window.curvas[i+1] == 1:
                        self.c[i].setData(self.t[i],self.d[i])
            for i in [8,9,10,11]:
                if window.curvas[i+1] == 1:
                    self.c[i].setData(self.t[i],self.d[i])
    def close(self):
        try:
            self.win.close()
        except Exception as e:
            pass
class Plot_matplotlib(FigureCanvas):
    def __init__(self):
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_qt5agg \
            import NavigationToolbar2QT as NavigationToolbar
        import matplotlib.pyplot as plt
        self.figura = Figure()
        self.figura_2 = Figure()
        self.ejes = self.figura.add_subplot(111)
        b = []
        i_cnt = 0
        for name in [window.Data_335,window.Data_218]:
            a = name.Plot_inter(window.file_plot_names[i_cnt])
            for c in a:
                b.append(c)
            i_cnt += 1
        if window.curvas[0] == 1:
            for i in range(8):
                self.ejes.plot(b[i][0], b[i][1],label=window.names_sensor[i],color=window.color[i]/255)
        else:
            for i in range(8):
                if window.curvas[i+1]==1:
                    self.ejes.plot(b[i][0], b[i][1],label=window.names_sensor[i],color=window.color[i]/255)
        self.ejes.title.set_text(window.file_plot_names[2])
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
class Plot_ramp(FigureCanvas):
    def __init__(self):
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_qt5agg \
            import NavigationToolbar2QT as NavigationToolbar
        import matplotlib.pyplot as plt
        self.figura = Figure()
        self.figura_2 = Figure()
        self.ejes = self.figura.add_subplot(111)
        b = []
        i_cnt = 0
        for name in [window.Data_335,window.Data_218]:
            a = name.Plot_inter(window.file_plot_names[i_cnt])
            for c in a:
                b.append(c)
            i_cnt += 1
        for i in range(8):
                if window.curvas_ramp[i]==1:
                    b[i][1] = array(self.deriv_h4_no_uniforme(b[i][1],b[i][0]))*60
                    self.ejes.plot(b[i][0], b[i][1],label = 'Ramp ' + window.names_sensor[i],\
                        color=window.color[i]/255)

        self.ejes.title.set_text("Plot Ramp of Data")
        self.ejes.set_xlabel("t [s]")
        self.ejes.set_ylabel("Ramp [K/min]")
        self.ejes.grid(),self.ejes.legend()
        FigureCanvas.__init__(self,self.figura_2)
        self.canvas = FigureCanvas(self.figura)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)
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

        AvgDataStr += '{:10.2f}'.format(TProm)
        for Num2 in range(LenSens):
            AvgDataStr += '\t'+'{:10.2f}'.format(float(AvgData[Num2+1][1]))
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
        
#------
#
#------

def Change(file,new,name,textDict):
        with open(file, "r") as f:
            lines = (line.rstrip() for line in f)
            altered_lines = [name+':'+new+'/' if line==name+':'+textDict[name] \
                            else line for line in lines]
        with open(file, "w") as f:
            f.write('\n'.join(altered_lines) + '\n')

#----------------------------------------------------------
#Esta clase contendrá toda la información de las mediciones
#y los procedimientos para guardarlos y procesarlos.
#----------------------------------------------------------

class TempClass:

    def __init__(self,textDict,TimeStamp=0,patch=''):
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
        window.label_scroll += '-------------------------------------------------------------------------\n'
        window.label_scroll += '      The aquisition of the temperature with\n ' +'    '+ self.Brand +' '+ \
                        self.Device + ' has begun.\n'
        window.label_scroll += '-------------------------------------------------------------------------\n'

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

    def Plot_inter(self,file_name):
        self.RemoveHeader(file_name)
        var = PlotData_Interface(self.DataRecovered)
        return var

    def Plot_inter_header(self,file_name):
        var = PlotData_Interface(self.DataSerie)
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

    def RemoveHeader(self,file_name):
        self.DataRecovered = RemoveHeaderFunction(self.root,file_name)

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
        window.label_scroll +='                                    Status\n'  #Print On/Iff Settings
        window.label_scroll+='-------------------------------------------------------------------------\n'
        i = 0
        for a in out:
            window.label_scroll +='      ' +a+':'+out[a].strip('\n')
            i += 1
            if i == 4:
                window.label_scroll += '\n'
                i = 0
        window.label_scroll+='-------------------------------------------------------------------------\n'

    def setCurves(self):
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
        window.label_scroll += '                                    Curves\n' #Print Curve Settings
        window.label_scroll+='-------------------------------------------------------------------------\n'
        i = 0
        for a in out:
            window.label_scroll += '       '+a+' :'+out[a].strip('\n')
            i += 1
            if i == 4:
                window.label_scroll += '\n'
                i=0
        window.label_scroll+='-------------------------------------------------------------------------\n'

    def ConfigPort(self):
        return serial.Serial(self.ConfigDict['Port'], self.ConfigDict['BaudRate'], serial.SEVENBITS,\
            serial.PARITY_ODD, serial.STOPBITS_ONE, float(self.ConfigDict['TimeOut']))

#----------------------------------------------------------
#Main code --- MAIN
#----------------------------------------------------------

def launch():
    try:
        global window
        app = QtWidgets.QApplication(['Temperature'])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt as KBI:
        pass

if __name__ == "__main__":
      launch()
