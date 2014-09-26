#!/usr/bin/env python

from gi.repository import Notify
from time import sleep
import os

currentDirectory = os.getcwd()


Notify.init ("stopstaring")
Notification=Notify.Notification.new("Stop Staring","take a break MAN!", "%s/icon.png"%(currentDirectory))
while 1:
	Notification.show ()
	sleep(20)

