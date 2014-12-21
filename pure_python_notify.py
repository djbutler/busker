#!/usr/bin/env python
import mmap, os, re, sys
from PyObjCTools import AppHelper
import Foundation
import objc
import AppKit
import time
from threading import Timer

from datetime import datetime, date

# objc.setVerbose(1)

class MountainLionNotification(Foundation.NSObject):
    # Based on http://stackoverflow.com/questions/12202983/working-with-mountain-lions-notification-center-using-pyobjc

    def init(self):
        self = super(MountainLionNotification, self).init()
        if self is None: return None

        # Get objc references to the classes we need.
        self.NSUserNotification = objc.lookUpClass('NSUserNotification')
        self.NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

        return self

    def clearNotifications(self):
        """Clear any displayed alerts we have posted. Requires Mavericks."""

        NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
        NSUserNotificationCenter.defaultUserNotificationCenter().removeAllDeliveredNotifications()

    def notify(self, title, subtitle, text, url):
        """Create a user notification and display it."""

        notification = self.NSUserNotification.alloc().init()
        notification.setTitle_(str(title))
        notification.setSubtitle_(str(subtitle))
        notification.setInformativeText_(str(text))
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
        notification.setHasActionButton_(True)
        notification.setActionButtonTitle_("View")
        notification.setUserInfo_({"action":"open_url", "value":url})

        self.NSUserNotificationCenter.defaultUserNotificationCenter().setDelegate_(self)
        self.NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

        # Note that the notification center saves a *copy* of our object.
        return notification

    # We'll get this if the user clicked on the notification.
    def userNotificationCenter_didActivateNotification_(self, center, notification):
        """Handler a user clicking on one of our posted notifications."""

        userInfo = notification.userInfo()
        if userInfo["action"] == "open_url":
            import subprocess
            # Open the log file with TextEdit.
            subprocess.Popen(['open', userInfo["value"]])
            
if __name__=='__main__':
    print('executing notify.py')
    a = MountainLionNotification.alloc().init()
    a.notify("Title","Subtitle","Text","http://www.google.com")
    