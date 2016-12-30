#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.join("/home/pi/station_meteo/Yocto/Sources"))
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

root_path='/home/pi/station_meteo/'
target='METEOMK1'
database_path=root_path + 'data/database.csv'
deltatobepublished_path=root_path + 'data/deltatobepublished.csv'

# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

m = YModule.FindModule(target)

if not m.isOnline() : die('device not connected')

humSensor = YHumidity.FindHumidity(target+'.humidity')
pressSensor = YPressure.FindPressure(target+'.pressure')
tempSensor = YTemperature.FindTemperature(target+'.temperature')



now = datetime.strftime(datetime.now(),"%d/%m/%y %H:%M:%S")

line = now + ",%2.1f" % tempSensor.get_currentValue() + ",%4.0f" % pressSensor.get_currentValue() + ",%2.0f" % humSensor.get_currentValue() + "\n"

print line

f = open(database_path,'a')
f.write(line)
f.close()

formatted_line = now + "\ntemperature=%2.1f" % tempSensor.get_currentValue() + "°C\npressure=%4.0f" % pressSensor.get_currentValue() + "mb\nhumidity=%2.0f" % humSensor.get_currentValue() + "%"
f = open(deltatobepublished_path,'w')
f.write(formatted_line)
f.close()
