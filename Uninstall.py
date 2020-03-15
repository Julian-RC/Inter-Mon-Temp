import os
os.system('pip3 uninstall Interfaz-MonitorTemperature')
if os.path.isfile('/usr/share/applications/Temperature.desktop'):
    os.system('rm /usr/share/applications/Temperature.desktop')
