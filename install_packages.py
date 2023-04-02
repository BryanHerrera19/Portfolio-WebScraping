import sys
import subprocess


subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymongo'])
subprocess.check.call([sys.excutable, '-m', 'pip', 'install', 'pyqt5-tools'])