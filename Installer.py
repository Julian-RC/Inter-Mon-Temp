import os
import subprocess

try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install -r requeriments.txt')
except:
  print('Error de instalación de Paquetes')
