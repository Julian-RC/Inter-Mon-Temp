import os
try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install setuptools')
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
  os.system('exit')
  os.system('nano ~/.bashrc')
except:
  print('Error de instalación')
