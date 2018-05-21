import sys
print sys.path

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys

from widgets import loginpage
from widgets import header
from widgets import common
from framework import widgethelper

from threading import Thread
from time import sleep
import account



#----config----
CONFIG_URL = "http://www.briscoes.co.nz/"
#CONFIG_CHROMEDRIVER = "/home/tmp1/.local/chromedriver"

#----setUp----
#driver = webdriver.Chrome(CONFIG_CHROMEDRIVER)
driver = webdriver.Chrome()
driver.get(CONFIG_URL)

#----Login----
header.getLoginLink(driver).click()
loginpage.getEmailAddrTextfield(driver).send_keys(account.USERNAME)
loginpage.getPasswordTextfield(driver).send_keys(account.PASSWORD)
loginpage.getLoginButton(driver).click()
assert "Account Profile" in driver.page_source #https://stackoverflow.com/questions/7861775/python-selenium-accessing-html-source
widgethelper.move_over_element(driver, header.getBedAndBathMenu(driver))
common.getUnwantedSubscriptionPopupCloseButton(driver).click()


#----tearDown----
#header.getLogoutLink(driver).click()
#assert "You have been logged out." in driver.page_source
#driver.close() #close all browser tabs
#driver.quit() #close chromedriver and other processes created for this test run
