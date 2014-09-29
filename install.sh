#! /bin/bash

if [[ $EUID -ne 0 ]]
then
	echo "This script must be run using sudo"
else
	cp indicator-lookup.py /usr/bin/indicator-lookup
	chmod 755 /usr/bin/indicator-lookup
	mkdir /etc/indicator-lookup
	cp icon.png /etc/indicator-lookup/
	cp beep.wav /etc/indicator-lookup/
	cp indicator-lookup.desktop /usr/share/applications/
	chmod 755 /usr/share/applications/indicator-lookup.desktop
	echo "Installed Successfully"
fi
