import os
try:
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
except:
  print('Error de instalación')
