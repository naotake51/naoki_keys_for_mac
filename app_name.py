from AppKit import NSWorkspace
import time

app_name = ""
while True:
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    if app_name != activeAppName:
        app_name = activeAppName
        with open("/Users/takeshitanaoki/Library/Application Support/Keyhac/app_name", mode='w') as f:
            print(app_name)
            f.write(app_name)
    time.sleep(0.2)