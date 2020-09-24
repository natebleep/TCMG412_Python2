import datetime
from urllib.request import urlretrieve 
import os.path

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
result = os.path.isfile('local_copy.log')

if result == False:
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)