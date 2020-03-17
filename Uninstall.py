import os
os.system('pip3 uninstall Interfaz-MonitorTemperature')
os.system('rm /usr/local/bin/Temperature')
if os.path.isfile('/usr/share/applications/Temperature.desktop'):
    os.system('rm /usr/share/applications/Temperature.desktop')
