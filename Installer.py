import os
import subprocess
try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install setuptools')
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
  path=subprocess.getoutput("pwd")
  os.system('pwd')
  os.system("echo "+"   return " + patch ">> MonTemp/prueba1.py")
  
except:
  print('Error de instalación')
