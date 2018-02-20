from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys

import time

#----------------------------framework-----------------------------------

def wait_until_element_visible(xpath):
    visible = None;

    while (visible == None):
        try:
            element = driver.find_element_by_xpath(xpath);
            visible = element.is_displayed();
        except NoSuchElementException:
            print (xpath + "is not visible");
            time.sleep(0.2);

    print (xpath + "is visible");            
    return element;


def is_element_visible(xpath):
    visible = None;
    element = None;
    try:
        element = driver.find_element_by_xpath(xpath);
        visible = element.is_displayed();
        print (xpath + "is visible");            
        return element;
    except NoSuchElementException:
        print (xpath + "is not visible");


def debug_xpath(xpath): #https://stackoverflow.com/questions/5585343/getting-the-return-value-of-javascript-code-in-selenium
    script1 = "function getElementByXpath(path) {"
    script2 = "return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}"
    #script3 = "result = getElementByXpath(\""+xpath+"\")); return result;"
    script3 = "return getElementByXpath(\""+xpath+"\")" #returns WebElement 
    
    script = script1 + script2 + script3
    print(script)
    result = driver.execute_script(script)
    #print(driver.execute_script(script))
    print(result)

    element_text = result.text
    element_attribute_value = result.get_attribute('value')
    element_id = result.getProperty("id");
    #element_class = result.class

    print ('element.text: {0}'.format(element_text))
    print ('element.get_attribute(\'value\'): {0}'.format(element_attribute_value))
    print ('element.id: {0}'.format(element_id))
    #print ('element.class: {0}'.format(element_class))

#----------------------------configuration--------------------------------------------------
CONFIG_URL = "http://www.briscoes.co.nz/";


#----------------------------application elements API---------------------
def getLoginLink():
    return wait_until_element_visible("//a[contains(.,'Login')]")

def getEmailAddrTextfield():
    return wait_until_element_visible("//input[@id='emailaddress']")

def getPasswordTextfield():
    return wait_until_element_visible("//input[@name='password']")

def getLoginButton():
    return wait_until_element_visible("//input[@title='Login']")

def getLogoutLink():
    return wait_until_element_visible("//a[contains(.,'Log Out')]")

#----test script----
USERNAME = 'xyzabcd';
PASSWORD = 'xyzabcd';

#----setUp----
driver = webdriver.Chrome()
driver.get(CONFIG_URL);

#----Login----
getLoginLink().click();
getEmailAddrTextfield().send_keys(USERNAME);
getPasswordTextfield().send_keys(PASSWORD);
getLoginButton().click();
assert "Account Profile" in driver.page_source #https://stackoverflow.com/questions/7861775/python-selenium-accessing-html-source

#----tearDown----
getLogoutLink().click()
assert "You have been logged out." in driver.page_source
driver.close() #close all browser tabs
driver.quit() #close chromedriver and other processes created for this test run

