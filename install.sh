#!/usr/bin/env bash
crontab -l > scheduler.cron
echo "0 * * * * pi /home/pi/meteokit/code/scheduler >> /var/log/meteokit.log" >> scheduler.cron
crontab scheduler.cron
rm scheduler.cron
sudo touch /var/log/meteokit.log
sudo chown pi:pi /var/log/meteokit.log
