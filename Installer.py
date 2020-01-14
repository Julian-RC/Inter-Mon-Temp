import os
import subprocess
try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install setuptools')
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
  path="pyhon3 "+subprocess.getoutput("pwd")+"/MonTemp/prueba1.py"
  os.system('pwd')
  #os.system("echo " + patch + ">> run")
  
except:
  print('Error de instalación')
