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
  os.system("exit && mkdir -p ~/.myPrograms")
  print(1)
  a = "exit && cd ~/.myPrograms && ln -s "+ path + "   InterMonTemp_2"
  print(a)
  os.system(a)
  print(2)
  os.system("exit && echo 'export PATH=$PATH:~/.myPrograms' >> ~/.bashrc")
except:
  print('Error de instalación')
