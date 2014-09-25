from gi.repository import Notify
from time import sleep

Notify.init ("stopstaring")
Notification=Notify.Notification.new("Stop Staring","take a break MAN!", "")
while 1:
	Notification.show ()
	sleep(15)

