import os
import subprocess
  
path = subprocess.getoutput("pwd")+"/MonTemp/prueba1.py"
os.system("mkdir -p ~/.myPrograms")
a = "cd ~/.myPrograms && ln -s "+ path + "   InterMonTemp_4"
os.system(a)
print(2)
os.system("echo 'export PATH=$PATH:~/.myPrograms' >> ~/.bashrc")
print(3)
#os.system("cd MonTemp && chmod u+x prueba1.py")
