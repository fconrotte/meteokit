#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, csv, tweepy, config


def publishline(row):
    formatted_line = row['datetime'] + "\n"
    formatted_line += "temperature=" + row['temperature'] + "°C\n"
    formatted_line += "pressure=" + row['pressure'] + "°mb\n"
    formatted_line += "humidity=" + row['humidity'] + "%"
    api.update_status(status=formatted_line)


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

root_path = '/home/pi/meteokit/'
deltatobepublished_path = root_path + 'data/deltatobepublished.csv'

with open(deltatobepublished_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        publishline(row)
csvfile.close()

# Empty the file
open(deltatobepublished_path, 'w').close()
