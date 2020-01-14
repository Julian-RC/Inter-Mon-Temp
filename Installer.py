import os
import subprocess
try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install setuptools')
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
  path="\n python3 "+subprocess.getoutput("pwd")+"/MonTemp/prueba1.py"
  print(path)
  print(type(path))
  os.system('pwd')
  os.system("echo '" + path + "'+>> run.py")
  
except:
  print('Error de instalación')
