import os
import subprocess
try:
  os.system('pip install --upgrade pip')
  os.system('pip3 install -r requeriments.txt')
  os.system('apt install rxvt-unicode')
  os.system('python3 setup.py install')
  if not os.path.isfile('/usr/share/applications/Temperature.desktop'):
      which_Te = subprocess.getoutput('which Temperature').strip('\n')
      patch = subprocess.getoutput('Temperature')
      texto = '[Desktop Entry]\nName=Temperature\nComment=Temperature\nExec=' +\
              which_Te + '\nIcon=' + patch + '\nTerminal=false\nType=Application'
      command = 'sudo touch /usr/share/applications/Temperature.desktop'
      os.system('cd && ' + command)
      command = 'sudo chmod 777 /usr/share/applications/Temperature.desktop'
      os.system(command)
      os.system('echo "'+texto+'" >> /usr/share/applications/Temperature.desktop')
      with open('/usr/share/applications/Temperature.desktop', "r") as f:
              lines = (line.rstrip() for line in f)
              altered_lines = []
              for line in lines:
                if (line[0:14] == '[Desktop Entry' \
                  or line[0:4]=='Name' or line[0:7] == 'Comment' \
                    or line[0:4]=='Icon' or line[0:4] == 'Exec'\
                      or line[0:4]=='Type' or line[0:8] =='Terminal'):
                  altered_lines.append(line)
      with open('/usr/share/applications/Temperature.desktop', "w") as f:
              f.write('\n'.join(altered_lines) + '\n')
      command = 'sudo chmod 644 /usr/share/applications/Temperature.desktop'
      os.system(command)
except:
  print('Error de instalación de Paquetes')
