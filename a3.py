from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://blazedemo.com/")

assert "BlazeDemo" in driver.title

Select(driver.find_element(By.NAME, "fromPort")).select_by_visible_text("Portland")
Select(driver.find_element(By.NAME, "toPort")).select_by_visible_text("Berlin")

driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//input[@type='submit'])[1]").click()
time.sleep(2)

driver.find_element(By.ID, "inputName").send_keys("Azamat Test")
driver.find_element(By.ID, "address").send_keys("Test Street")
driver.find_element(By.ID, "city").send_keys("Astana")
driver.find_element(By.ID, "creditCardNumber").send_keys("4111111111111111")

driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
time.sleep(10)

print("test passed")

driver.quit()
