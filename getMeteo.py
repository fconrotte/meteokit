#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys,csv,collections
sys.path.append(os.path.join("/home/pi/meteokit/Yocto/Sources"))
from yocto_api import *
from yocto_humidity import *
from yocto_temperature import *
from yocto_pressure import *
from datetime import datetime

def usage():
    scriptname = os.path.basename(sys.argv[0])
    print("Usage:")
    print(scriptname+' <serial_number>')
    print(scriptname+' <logical_name>')
    print(scriptname+' any  ')
    sys.exit()

def die(msg):
    sys.exit(msg+' (check USB cable)')

errmsg=YRefParam()

root_path='/home/pi/meteokit/'
target='METEOMK1'
database_path=root_path + 'data/database.csv'
deltatobepublished_path=root_path + 'data/deltatobepublished.csv'

# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

m = YModule.FindModule(target)

if not m.isOnline() : die('device not connected')

datetime    = datetime.strftime(datetime.now(),"%d/%m/%y %H:%M:%S")
temperature = "%2.1f" % YTemperature.FindTemperature(target+'.temperature').get_currentValue()
pressure    = "%4.0f" % YPressure.FindPressure(target+'.pressure').get_currentValue()
humidity    = "%2.0f" % YHumidity.FindHumidity(target+'.humidity').get_currentValue()

fieldnames = ['datetime', 'temperature','pressure','humidity']
row = collections.OrderedDict()
row['datetime']=datetime
row['temperature']=temperature
row['pressure']=pressure
row['humidity']=humidity
print row

file_exists = os.path.isfile(database_path)
with open(database_path, 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
    writer.writerow(row)

file_exists = os.path.isfile(deltatobepublished_path)
with open(deltatobepublished_path, 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
    writer.writerow(row)
