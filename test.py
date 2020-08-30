from AppKit import *
from PyObjCTools import AppHelper

def main():
    nc = NSWorkspace.sharedWorkspace().notificationCenter()
    nc.addObserver_selector_name_object_(
        Observer.new(),
        "handle:",
        NSWorkspaceDidActivateApplicationNotification,
        None
    )
    AppHelper.runConsoleEventLoop(installInterrupt=True)

class Observer(NSObject):
    def handle_(self, noti):
        print("handle")
        info = noti.userInfo().objectForKey_(NSWorkspaceApplicationKey)
        for n in ["bundleIdentifier", "localizedName", "bundleURL",
                  "executableURL", "launchDate"]:
            v = info.valueForKey_(n)
            print("%s (%s):\t%s" % (n, v.className(), v))
        print("--")

print("start main")
main()
print("end main")
