crontab -l > scheduler.cron
echo "0 * * * * root /home/pi/station_meteo/code/scheduler >> /var/log/meteokit.log" >> scheduler.cron
crontab scheduler.cron
rm scheduler.cron
