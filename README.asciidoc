MeteoKit
--------

== Install Raspbian
	
 Enable SSH
	 https://www.raspberrypi.org/documentation/remote-access/ssh/
	 Configure keyboard
	 sudo raspi-config => 
		 expand disk usage to full SD card	
		 enable camera
	 gconftool-2 --type bool --set /apps/gksu/sudo-mode true => no more password required when connecting with pi user
	 change pi user password

== Connect remotely
== Install Python Tweepy

 	pip install tweepy
	 git clone https://github.com/tweepy/tweepy.git
	 cd tweepy/examples
	 vi oauth.py
	 set the 4 Twitter API keys and tokens
	 python oauth.py
	
== Install Yocto Virtual Hub 
http://www.yoctopuce.com/projects/yoctometeo/METEOMK1.usermanual-EN.pdf

Note: armhf architecture !

http://www.yoctopuce.com/projects/yoctometeo/METEOMK1.usermanual-EN.pdf

== Install Yocto-Meteo Python library:
http://www.yoctopuce.com/EN/products/usb-sensors/yocto-meteo

== Install Google drive backup data
https://github.com/iwonbigbro/gsync
Fix this:
https://github.com/iwonbigbro/gsync/issues/66

== Install cron to fetch weather hourly
echo "0 * * * * root 

== publish weather on twitter
== Commit codes to github + flash SD card
== Check for values accuracy !
== Health checks
== Test camera
== Enable wifi router to connect to our weather station
http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/
https://jacobsalmela.com/2014/05/19/raspberry-pi-and-routing-turning-a-pi-into-a-router/

== Move install to Docker to make installations and upgrade easier

= Useful links:
http://blog.hypriot.com/getting-started-with-docker-and-windows-on-the-raspberry-pi/
http://asciidoctor.org/