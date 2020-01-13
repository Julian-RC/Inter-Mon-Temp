import sys
import time
import datetime
import serial
import subprocess
import pickle
import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
import os
import matplotlib.pyplot as plt


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
    datos = []
    tiempo = []
    ReadTime = []
    ps = 0
    flag = 1
    for Channel in Channels:
        
        while flag == 1:
            str2port = 'KRDG? ' +str(Channel)+'\r\n'
            port.write(str2port.encode())
            BinData = port.read(79)
            if (len(BinData) == 9) or (len(BinData) == 65):
                flag = 0
                
        tiempo.append(time.time())
        StrData = BinData.decode()
        ReadTime.append(tiempo[ps] - InitialTime)
        if (len(BinData) == 9):
            datos.append(StrData.rstrip('\r\n'))          
        elif (len(BinData) == 65):
            datos = StrData.rstrip('\r\n').split(',')
            break
            
        ps += 1
        flag = 1

    AvgTime = sum(ReadTime)/len(ReadTime)
    datosFormatted = '{:10.2f}'.format(AvgTime)
    
    for dato in datos:
        datosFormatted += '\t' + dato

    datosFormatted += '\n'

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

    try:
        
        for Num2 in range(LenSens):
            for Num in range(DataLen-AverageInt,DataLen):
                AvgData[Num2+1][0] += Data[Num][Num2][1]
                AvgData[Num2+1][1] += float(Data[Num][Num2][2])

            AvgData[Num2+1][0] /= AverageInt
            AvgData[Num2+1][1] /= AverageInt
            TProm += AvgData[Num2+1][0] / LenSens
              
        AvgDataStr += str(TProm) + '\t'
        for Num2 in range(LenSens):
            AvgDataStr += '{}'.format(float(AvgData[Num2+1][1])) + '\t'
        AvgDataStr += '\n'

    except:
        print('ERROR: "Average" of the configuration file must be an integer.')
    
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
    
    def __init__(self,textDict,TimeStamp=0):
        self.textDict = textDict #Diccionario que incluye información sobre la medición que se realizará
        self.root = textDict['Root'] #Raiz del archivo en el que se guardarán los datos
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

        print('------------------------------------------------------------')
        print('The aquisition of the temperature with ' + self.Brand +' '+ self.Device + ' has begun.')
        print('------------------------------------------------------------\n')

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
        time.sleep(0.1)
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
        
        As,Bs,Cs = GetDataFunction(self.port,self.Channels,self.InitTime)
        
        if self.SamplingPeriod != 0:
            time.sleep(self.SamplingPeriod)
        
        self.DataSerie += Cs
        if (len(Bs) != len(As)):
            Bs *= len(As) 
        
        
        for Num in range(len(As)):
            try:
                ListTupla.append([self.Sensors[Num],Bs[Num],As[Num]])
            except IndexError:
                ListTupla.append([Num + 1,Bs[Num],As[Num]])
                
        
        self.Data.append(ListTupla)
        self.Cont += 1

        if self.Cont % float(self.Average) == 0:
            self.AverageCalc()   

    def AverageCalc(self):
        As, Bs = AverageFunction(self.Data,self.Average,self.Sensors)
        self.DataAverage.append(As)
        self.DataAverageText += Bs
        if self.Cont >= int(self.textDict['SaveData']):
            self.Save()

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
        if self.Data==[]:
            print('------------------------------------------------------------')
            print('Currently, buffer is empty of temperature data. Please try again in a moment.')
            print('------------------------------------------------------------')
        else:
            print('------------------------------------------------------------')
            for Vect in self.Data[-1]:    
                print(Vect)
            print('------------------------------------------------------------')

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
                    out.setdefault('Sens '+str(Ch),self.Port.read(79).decode().strip())
                    time.sleep(.1)
                    Ch=Ch+1
                continue
            continue
        print('Status\r')  #Print On/Iff Settings       
        print(out)
        #return 'Done\r\n'

    def setCurves(self): 
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
        print('Curves\r') #Print Curve Settings
        print(out)
        #return   'Done\r\n'

    def ConfigPort(self):
        return serial.Serial(self.ConfigDict['Port'], self.ConfigDict['BaudRate'], serial.SEVENBITS,\
            serial.PARITY_ODD, serial.STOPBITS_ONE, float(self.ConfigDict['TimeOut']))
        

#----------------------------------------------------------
#Main code --- MAIN
#----------------------------------------------------------

#filename = sys.argv[1]
#filename = sys.argv[2]
filename = "config_file.txt"
filename2 = "config_file2.txt"
textDict = ConfigModule(filename)
textDict2 = ConfigModule(filename2,0)
DataTemp = TempClass(textDict.ConfigDict)
DataTemp2 = TempClass(textDict2.ConfigDict,DataTemp.InitTime)
Menu = CommandLine()

while True:
    try:
        DataTemp.GetData()
        if DataTemp.InitTime != 0: DataTemp2.InitTime = DataTemp.InitTime
        DataTemp2.GetData()       
    except KeyboardInterrupt as KBI:
        Menu.Input([DataTemp,DataTemp2])


