import sys; sys.path.insert(0, "..")
print (sys.path);

from framework import widgethelper

from threading import Thread
from time import sleep

#Webdriver is not thread-safe :(

##def startMonitorThread(driver):
##    thread1 = Thread(name = 'panda-monitor-thread', target = closeUnwantedPopups, args = (driver, ))
##    thread1.setDaemon(False)
##    thread1.start()
##    print ("***MonitorThread started.")
##    return thread1

##def closeMonitorThread(thread):
##    thread.join()
##    print ("***MonitorThread stop message.")
##    if (thread.isAlive()):
##        print ("***MonitorThread stop failed.")
    
    

##def closeUnwantedPopups(driver):
##         if (widgethelper.is_element_visible(driver, "//img[contains(@id,'popup-subcription-closes-icon')]")):
##             getUnwantedSubscriptionPopupCloseButton(driver).click()
     
def getUnwantedSubscriptionPopupCloseButton(driver):
    return widgethelper.get_element_when_visible_timeout(driver, "//img[contains(@id,'popup-subcription-closes-icon')]",4)

