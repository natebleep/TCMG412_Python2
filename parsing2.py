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

#-----Amount of requests on each day 
daysCounter = {
    'Monday': 0, 
    'Tuesday': 0,
    'Wednesday': 0, 
    'Thursday': 0, 
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0}


for i in log['date']:    
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

print('The following is the amount of files accessed on each weekday: ')
print(daysCounter)

print('\n ------------ \n')


# -------------------------------------
# -------------------------------------
 
datecount = (len(log['date']))
d1 = (log['date'][0])
d2 = (log['date'][-1])
totalDays = (d2 - d1).days
totalWeeks = int(totalDays / 7)
totalMonths = totalWeeks / 4
weekavg = int(datecount / totalWeeks)
monthavg = int(datecount / totalMonths)

print('There is an average of', weekavg, 'requests per week.' )
print('There is an average of', monthavg, 'requests per month.' )

print('\n ------------ \n')

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
print('Percent of unsuccessful requests (4xx codes): ', code4xPercent,'%' 
'\nPercent of successful requests (3xx codes): ', code3xPercent, "%")

print('\n ------------ \n')

# -------------------------------------
# -------------------------------------

filecounter = {}
filecounter['index.html'] = 1
for i in log['filename']:
    if i in filecounter:
        filecounter[i] += 1
    else:        
        filecounter[i] = 1       

filemax = max(filecounter, key=filecounter.get)
print('The most requested file is:', filemax, 'with', filecounter[filemax], 'requests.')

filemin = min(filecounter, key=filecounter.get)
print('The least requested file is:', filemin, 'with', filecounter[filemin], 'requests.')

# -------------------------------------
# -------------------------------------

fh = open(LOCAL_FILE)
loglines = fh.readlines()
fh.close()
Jan = open('January.txt', 'a')
Feb = open('February.txt', 'a')
Mar = open('march.txt', 'a')
Apr = open('April.txt', 'a')
May = open('May.txt', 'a')
Jun = open('June.txt', 'a')
Jul = open('July.txt', 'a')
Aug = open('August.txt', 'a')
Sep = open('September.txt', 'a')
Oct = open('October.txt', 'a')
Nov = open('November.txt', 'a')
Dec = open('December.txt', 'a')

for i in loglines:    
    date = re.split('\[(.+) .+0\]', i)    
    if len(i) > 100:
        continue
    else: 
        if len(date) == 3:
            d = date[1]        
            d = datetime.datetime.strptime(d, '%d/%b/%Y:%H:%M:%S')
            if d.month == 1:
                Jan.write(i)
            elif d.month == 2:
                Feb.write(i)
            elif d.month == 3:
                Mar.write(i)
            elif d.month == 4:
                Apr.write(i)
            elif d.month == 5:
                May.write(i)
            elif d.month == 6:
                Jun.write(i)
            elif d.month == 7:
                Jul.write(i)
            elif d.month == 8:
                Aug.write(i)
            elif d.month == 9:
                Sep.write(i)
            elif d.month == 10:
                Oct.write(i)
            elif d.month == 11:
                Nov.write(i)
            elif d.month == 12:
                Dec.write(i)
        
Jan.close()
Feb.close()
Mar.close()
Apr.close()
May.close()
Jun.close()
Jul.close()
Aug.close()
Sep.close()
Oct.close()
Nov.close()
Dec.close()
