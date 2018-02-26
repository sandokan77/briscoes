import sys; sys.path.insert(0, "..")
print (sys.path);

import framework

def getLogoutLink(driver):
    return framework.widgethelper.get_element_when_visible(driver, "//a[contains(.,'Log Out')]")

def getLoginLink(driver):
    return framework.widgethelper.get_element_when_visible(driver, "//a[contains(.,'Login')]")

def getBedAndBathMenu(driver):
    #return framework.widgethelper.wait_until_element_visible(driver,"/html/body/div[1]/div[2]/div[9]/ul/li[2]") #working but nasty xpath
    return framework.widgethelper.get_element_when_visible(driver, "//div[@class='header_nav megamenu']/ul/li[@data-catid='10453']") #visible



    
