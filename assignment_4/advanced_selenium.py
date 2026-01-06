import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import HtmlTestRunner
import os

# Make sure reports folder exists
if not os.path.exists("reports"):
    os.makedirs("reports")


class AmazonAdvancedSeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com")

    def test_advanced_selenium(self):
        driver = self.driver

        # Step 1: Explicit wait
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(
            EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("laptop")
        print("\n[STEP] Entered 'laptop' in search box using explicit wait")

        # Step 2: Select class
        dropdown = driver.find_element(By.ID, "searchDropdownBox")
        Select(dropdown).select_by_visible_text("Electronics")
        print("[STEP] Selected 'Electronics' category from dropdown")

        # Step 3: Click search
        driver.find_element(By.ID, "nav-search-submit-button").click()
        print("[STEP] Clicked search button")

        # Step 4: Fluent wait
        fluent_wait = WebDriverWait(
            driver, timeout=15, poll_frequency=2, ignored_exceptions=[NoSuchElementException]
        )
        first_result = fluent_wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
            )
        )
        assert first_result.is_displayed()
        print("[STEP] First search result loaded using fluent wait")

        # Step 5: Action class (hover)
        actions = ActionChains(driver)
        account_menu = driver.find_element(By.ID, "nav-link-accountList")
        actions.move_to_element(account_menu).perform()
        print("[STEP] Hovered over 'Account & Lists' using ActionChains")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reports",
            report_name="Amazon_Advanced_Selenium_Report",
            combine_reports=True
        )
    )
