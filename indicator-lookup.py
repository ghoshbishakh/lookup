#!/usr/bin/env python

from gi.repository import Gtk
from gi.repository import AppIndicator3
from gi.repository import GLib
from gi.repository import Notify
import sys
from subprocess import call


def stopAll(*args):
    Gtk.main_quit()


def showNotification(*args):
    Notification.show()
    if sys.platform == 'linux2':
        call(["aplay", "/etc/indicator-lookup/beep.wav"])
    return True


menu = Gtk.Menu()
menuItem = Gtk.MenuItem("Stop Disturbing Me")
menu.append(menuItem)
menuItem.connect("activate", stopAll)
menuItem.show()


myIndicator = AppIndicator3.Indicator.new(
    'indicatorId', "/etc/indicator-lookup/icon.png",
    AppIndicator3.IndicatorCategory.APPLICATION_STATUS)

myIndicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
myIndicator.set_attention_icon("indicator-messages-new")
myIndicator.set_menu(menu)

Notify.init("lookup")
Notification = Notify.Notification.new(
    "Look Up",
    "Time to give your eyes a break.",
    "/etc/indicator-lookup/icon.png")


GLib.timeout_add_seconds(1200, showNotification, None, None)

#showNotification()

Gtk.main()
