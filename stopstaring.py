from gi.repository import Notify
from time import sleep
from os.path import expanduser
home = expanduser("~")

Notify.init ("stopstaring")
Notification=Notify.Notification.new("Stop Staring","take a break MAN!", "%s/projects/stopstaring/icon.png"%(home))
while 1:
	Notification.show ()
	sleep(20)

