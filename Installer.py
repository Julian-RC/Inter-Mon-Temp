import os
import subprocess
try:
  os.system('apt-get install python3-pip')
  os.system('pip3 install setuptools')
  os.system('pip3 install -r requeriments.txt')
  os.system('python3 setup.py install')
  path = subprocess.getoutput("pwd")+"/MonTemp/prueba1.py"
  print(path)
  #print(type(path))
  #os.system('pwd')
  #os.system("echo '" + path + "'+>> run.py")
  os.system("mkdir -p ~/.myPrograms")
  os.system("cd ~/.myPrograms && ln -s "+ patch + " MonTemp")
  os.system("echo 'export PATH=$PATH:~/.myPrograms' >> ~/.bashrc")
except:
  print('Error de instalación')
