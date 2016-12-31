#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import os,sys
import tweepy
import config

def publishline(line):
   formatted_line = now + "\ntemperature=%2.1f" % tempSensor.get_currentValue() + "°C\npressure=%4.0f" % pressSensor.get_currentValue() + "mb\nhumidity=%2.0f" % humSensor.get_currentValue() + "%"
   api.update_status(status=lines)



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps

root_path='/home/pi/station_meteo/'
deltatobepublished_path=root_path + 'data/deltatobepublished.csv'

lines=""
with open(deltatobepublished_path) as f:
   for line in f:
      publishline(line)
f.close()
