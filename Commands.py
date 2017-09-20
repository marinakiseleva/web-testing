from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException



def select_drop_down(name, value, driver):
    inputElement = driver.find_element_by_name(name)
    for option in inputElement.find_elements_by_tag_name("option"):
        if (option.get_attribute("value") == value):
            option.click()

def radio(name, value, driver):
    inputElement = driver.find_elements_by_name(name)
    for radio in inputElement:
        if (driver.find_element_by_xpath("//label[@for='" + radio.get_attribute("id") + "']").text == value):
            radio.click()

def check(name, driver):
    driver.find_element_by_name(name).click()
    

def text_field(name, input_text, driver):
    driver.find_element_by_name(name).send_keys(input_text)

