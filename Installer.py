import os
import subprocess
#try:
#  os.system('apt upgrade python3-pip')
#  os.system('pip3 install -r requeriments.txt')
#  os.system('python3 setup.py install')
os.system('cd MonTemp && cp config_file.txt config_file2.txt '+ subprocess.getoutput(' whereis ls'))
  
#except:
 # print('Error de instalación de Paquetes')
