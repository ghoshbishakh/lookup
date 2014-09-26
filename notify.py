from gi.repository import Gtk
from gi.repository import AppIndicator3
import os
currentDirectory = os.getcwd()

myIndicator=AppIndicator3.Indicator.new('indicatorId',"%s/icon.png"%(currentDirectory),AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
myIndicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
Gtk.main()
