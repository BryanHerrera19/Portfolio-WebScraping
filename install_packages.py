import sys
import subprocess


subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymongo'])