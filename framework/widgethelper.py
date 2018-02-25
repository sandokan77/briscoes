from selenium.common.exceptions import NoSuchElementException

def wait_until_element_visible(driver, xpath):
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
