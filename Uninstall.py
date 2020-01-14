import os
try:
  os.system('pip3 uninstall -r requeriments.txt')
  os.system('python3 setup.py uninstall')
except:
  print('Error de desinstalación')
