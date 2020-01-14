from setuptools import setup, find_packages
from MonTemp import __version__

setup(name='Interfaz Monitor Temperatura',
      version=__version__,
      description='A simple interfaz',
      url='https://github.com/Julian-RC/Inter-Mon-Temp.git',
      author='Laboratorio-Criogenia',
      packages=find_packages(),
      install_requires=[
            "pyqtwebengine",
            "PyQt5",
            "pyqtgraph",
            "numpy",
            "serial",
            "matplotlib",
            "datetime"
          ],
      entry_points={
            'console_scripts': [
            'MonTemp=MonTemp.prueba1:launch',
          ],
        },
      include_package_data=True,
      zip_safe=False)
