import os
import subprocess
try:
  os.system('pip install --upgrade pip')
  os.system('pip3 install -r requeriments.txt')
  os.system('apt install rxvt-unicode')
  os.system('python3 setup.py install')
 
except:
  print('Error de instalación de Paquetes')
