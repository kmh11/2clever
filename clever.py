from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class mkbot():
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get("http://cleverbot.com")
    def say(self,text):
        inputField = self.driver.find_element_by_name("stimulus")
        inputField.send_keys(text)
        inputField.send_keys(Keys.ENTER)
        snip = self.driver.find_elements_by_id("snipTextIcon")
        while snip == []:
            snip = self.driver.find_elements_by_id("snipTextIcon")
        output = self.driver.find_element_by_id("line1")
        return output.text
    def killbot(self):
        self.driver.quit()
