from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys

import time

from widgets import loginpage
from widgets import header
from framework import widgethelper

#----------------------------configuration--------------------------------------------------
CONFIG_URL = "http://www.briscoes.co.nz/";


#----test script----
USERNAME = '';
PASSWORD = '';

#----setUp----
#not a nice solution but python could not find chromedriver even if it's on the sys.path
driver = webdriver.Chrome(r"/home/tmp1/.local/chromedriver")
#driver = webdriver.Chrome()
driver.get(CONFIG_URL);

#----Login----
header.getLoginLink(driver).click();
loginpage.getEmailAddrTextfield(driver).send_keys(USERNAME);
loginpage.getPasswordTextfield(driver).send_keys(PASSWORD);
loginpage.getLoginButton(driver).click();
assert "Account Profile" in driver.page_source #https://stackoverflow.com/questions/7861775/python-selenium-accessing-html-source

#----tearDown----
#header.getLogoutLink(driver).click()
assert "You have been logged out." in driver.page_source
driver.close() #close all browser tabs
driver.quit() #close chromedriver and other processes created for this test run
