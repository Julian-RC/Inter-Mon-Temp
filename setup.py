from setuptools import setup, find_packages
from MonTemp import __version__

setup(name='Interfaz MonitorTemperature',
      version=__version__,
      description='A simple interfaz',
      url='https://github.com/Julian-RC/Inter-Mon-Temp.git',
      author='Laboratorio-Criogenia',
      packages=find_packages(),
      install_requires=[
            "PyQt5",
            "pyqtgraph",
            "numpy",
            "pyserial",
            "matplotlib",
            "datetime"
          ],
      data_files=['MonTemp/cfg/file_218.cfg','MonTemp/cfg/file_335.cfg',\
                  'MonTemp/Icon.png','MonTemp/cfg/terminal.cfg',\
                  'MonTemp/cfg/color.cfg','MonTemp/cfg/sensores_fit.cfg'],
      entry_points={
            'console_scripts': [
            'Temperature=MonTemp.Temperature:launch',
          ],
        },
      include_package_data=True,
      zip_safe=False)
