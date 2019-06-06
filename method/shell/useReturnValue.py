# sudo apt-get install speedtest-cli
import subprocess
import sys
import csv
import json

process = subprocess.Popen(['speedtest-cli','--server','4413'], stdout=subprocess.PIPE)
out, err = process.communicate()
reader = csv.DictReader(
                        out.decode('ascii').splitlines(),
                        delimiter='\n', skipinitialspace=True,
                        fieldnames=['Retrieving']
                        )

for index, item in enumerate(reader):
    print(str(index)+json.dumps(item))

# 0{"Retrieving": "Retrieving speedtest.net configuration..."}
# 1{"Retrieving": "Retrieving speedtest.net server list..."}
# 2{"Retrieving": "Testing from HiNet (211.20.7.115)..."}
# 3{"Retrieving": "Hosted by Chief Telecom (Tainan) [3.18 km]: 9.415 ms"}
# 4{"Retrieving": "Testing download speed........................................"}
# 5{"Retrieving": "Download: 88.60 Mbit/s"}
# 6{"Retrieving": "Testing upload speed.................................................."}
# 7{"Retrieving": "Upload: 80.34 Mbit/s"}