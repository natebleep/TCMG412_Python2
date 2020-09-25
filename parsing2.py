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

fh = open(LOCAL_FILE)
line = fh.read()
fh.close()

regex = re.compile('.+\[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3}) (?<= ).*')        
parts = regex.split(line)

for i in parts:      
    if len(i) == 20:        
        if i[2] == '/':
            i = datetime.datetime.strptime(i, '%d/%b/%Y:%H:%M:%S')
            log['date'].append(i)
        else:
            continue
    elif 3 < len(i) <=10:
        log['filename'].append(i)
    elif len(i) == 3:
        log['code'].append(i)
    else:
        continue

# print(log['date'][0])

#-----Amount of requests on each day 
daysCounter = {
    'Monday': 0, 
    'Tuesday': 0,
    'Wednesday': 0, 
    'Thursday': 0, 
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0}

# for i in log.values['date']:
#     print(log.value['date'])

# print(log['date'])
for i in log['date']:
    # print(datetime.datetime.weekday(i))
    if datetime.datetime.weekday(i) == 0:
        daysCounter['Monday'] += 1
    elif datetime.datetime.weekday(i) == 1:
        daysCounter['Tuesday'] += 1
    elif datetime.datetime.weekday(i) == 2:
        daysCounter['Wednesday'] += 1
    elif datetime.datetime.weekday(i) == 3:
        daysCounter['Thursday'] += 1
    elif datetime.datetime.weekday(i) == 4:
        daysCounter['Friday'] += 1
    elif datetime.datetime.weekday(i) == 5:
        daysCounter['Saturday'] += 1 
    elif datetime.datetime.weekday(i) == 6:
        daysCounter['Sunday'] += 1

print(daysCounter)


# -------------------------------------
# -------------------------------------


d1 = (log['date'][0])
d2 = (log['date'][-1])
totalDays = (d2 - d1).days
totalWeeks = int(totalDays / 7)
print('days: ', totalDays, 'weeks: ', totalWeeks)

# -------------------------------------
# -------------------------------------

totalCodes = (len(log['code']))
codeAmounts = {'4': 0, '3': 0}
for i in log['code']:
    if i[0] == '4':
        codeAmounts['4'] += 1
    elif i[0] == '3':
        codeAmounts['3'] +=1
    else:
        continue

code4xPercent = int((codeAmounts['4'] / totalCodes) * 100)
code3xPercent = int((codeAmounts['3'] / totalCodes) * 100)
print('Percent of 4xx codes: ', code4xPercent,'%' 
'\nPercent of 3xx codes: ', code3xPercent, "%")

# -------------------------------------
# -------------------------------------

