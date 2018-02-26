from selenium.common.exceptions import NoSuchElementException
import time

def get_element_when_visible_timeout(driver, xpath, timeoutsecs):
    visible = None;
    n1=dt.datetime.now()

    while (visible == None):
        try:
            element = driver.find_element_by_xpath(xpath);
            visible = element.is_displayed();
        except NoSuchElementException:
            #print (xpath + "is not visible");
            time.sleep(0.2);
            if (timeoutsecs > -1):
                n2=dt.datetime.now()
                diff = (n2-n1).seconds
                if (diff>=timeoutsecs):
                    raise TimeoutError


    print (xpath + "is visible");            
    return element;


import datetime as dt

def get_element_when_visible(driver, xpath):
    visible = None;
    timeout = -1; #infinite
    return get_element_when_visible_timeout(driver, xpath, timeout)

def is_element_visible(driver, xpath):
    visible = None;
    element = None;
    try:
        element = driver.find_element_by_xpath(xpath);
        visible = element.is_displayed();
        #print (xpath + "is visible");            
        return True
    except NoSuchElementException:
        #print (xpath + "is not visible");
        return False
                                                               
#http://selenium-python.readthedocs.io/api.html
from selenium.webdriver import ActionChains

def move_over_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()
    
