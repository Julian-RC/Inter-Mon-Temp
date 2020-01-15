import os
import subprocess

try:
  os.system('apt-get install python3-pip')
  #os.system('pip3 install setuptools')
  os.system('pip3 install -r requeriments.txt')
  #os.system('python3 setup.py install')
  path = subprocess.getoutput("pwd")+"/MonTemp/prueba1.py"
  print(path)
  #print(type(path))
  #os.system('pwd')
  #os.system("echo '" + path + "'+>> run.py")
  os.system("mkdir -p ~/.myPrograms")
  print(1)
  os.system("cd ~/.myPrograms && ln -s "+ path + " MonTemp")
  print(2)
  os.system("echo 'export PATH=$PATH:~/.myPrograms' >> ~/.bashrc")
except:
  print('Error de instalación')
