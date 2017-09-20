from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import unittest
from Commands import select_drop_down, radio, check, text_field


class TestAgeDeduction(unittest.TestCase):
    @classmethod
    def setUp(self):
        base_url = "https://tax.virginia.gov/age-deduction-calculator"
        self.driver = webdriver.Chrome(executable_path="/Users/mkiseleva/Documents/2017/blog/selenium/chromedriver")
        self.driver.get(base_url)

    def tearDown(self):
        self.driver.quit()

    def test_happy(self):
        select_drop_down("taxable-year-input", "2015", self.driver)
        radio("filing-status-input", "Single", self.driver)
        select_drop_down("primary-birth-day-input", "4", self.driver)
        select_drop_down("primary-birth-month-input", "6", self.driver)
        select_drop_down("primary-birth-year-input", "1944", self.driver)
        text_field("fagi-input", "10000", self.driver)
        text_field("fdc-additions-input", "10000", self.driver)
        text_field("fdc-subtractions-input", "10000", self.driver)
        text_field("benefits-input", "10000", self.driver)
        self.driver.find_element_by_id("edit-calculate").click()

        primary = self.driver.find_element_by_id("primary-result").text
        self.assertEqual(float(primary.replace(',', '')) , 12000)

    def test_empty_fagi(self):
        select_drop_down("taxable-year-input", "2015", self.driver)
        radio("filing-status-input", "Single", self.driver)
        select_drop_down("primary-birth-day-input", "4", self.driver)
        select_drop_down("primary-birth-month-input", "6", self.driver)
        select_drop_down("primary-birth-year-input", "1944", self.driver)
        self.driver.find_element_by_id("edit-calculate").click()

        error = self.driver.find_element_by_id("edit-fagi-input-error")
        self.assertEquals("Please enter your Federal Adjusted Gross Income.", error.text)

    def test_primary_disability(self):
        select_drop_down("taxable-year-input", "2015", self.driver)
        radio("filing-status-input", "Single", self.driver)
        select_drop_down("primary-birth-day-input", "4", self.driver)
        select_drop_down("primary-birth-month-input", "6", self.driver)
        select_drop_down("primary-birth-year-input", "1944", self.driver)
        check("primary-disability-subtraction-input", self.driver)
        text_field("fagi-input", "10000", self.driver)
        self.driver.find_element_by_id("edit-calculate").click()

        error = self.driver.find_element_by_id("edit-page-error")
        self.assertEquals("Please note the following: - You may not claim a Disability Deduction and Age Deduction on the same return.", error.text)       

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestAgeDeduction("test_happy"))
    test_suite.addTest(TestAgeDeduction("test_empty_fagi"))
    test_suite.addTest(TestAgeDeduction("test_primary_disability"))
    return test_suite

agetests=suite()

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(agetests)





