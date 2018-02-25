import sys; sys.path.insert(0, "..")
print (sys.path);

import framework

def getLogoutLink(driver):
    return framework.widgethelper.wait_until_element_visible(driver, "//a[contains(.,'Log Out')]")

def getLoginLink(driver):
    return framework.widgethelper.wait_until_element_visible(driver, "//a[contains(.,'Login')]")
