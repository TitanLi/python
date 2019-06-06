import subprocess
import sys

while True:
	subprocess.call(['ping', '-c 4','localhost'])