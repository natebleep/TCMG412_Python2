import datetime
from urllib.request import urlretrieve 
import os.path
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
result = os.path.isfile('local_copy.log')

#create a dictionary for the parts of the log
log= {}
log["date"] = []
log["code"] = []
log["filename"] = []

if result == False:
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

#Amount of requests on each day 
fh = open(LOCAL_FILE)
line = fh.read()
# print(line)
regex = re.compile('.+\[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3}) (?<= ).*')
parts = regex.split(line)

for i in parts:
    if len(i) > 11:
        log['date'].append(i)
    elif len(i) > 3:
        log['filename'].append(i)
    elif len(i) == 3:
        log['code'].append(i)

print(log['date'][0])


