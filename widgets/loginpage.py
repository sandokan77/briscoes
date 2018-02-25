import sys; sys.path.insert(0, "..")
print (sys.path);

import framework


def getEmailAddrTextfield(driver):
    return framework.widgethelper.wait_until_element_visible(driver,"//input[@id='emailaddress']")

def getPasswordTextfield(driver):
    return framework.widgethelper.wait_until_element_visible(driver,"//input[@name='password']")

def getLoginButton(driver):
    return framework.widgethelper.wait_until_element_visible(driver,"//input[@title='Login']")
