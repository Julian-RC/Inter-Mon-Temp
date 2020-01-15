import os
try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
except:
  print('Error de instalación de Paquetes')
