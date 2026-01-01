from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# xpath
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# css
message = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text
assert "You logged into a secure area!" in message

print("login successful")

# xpath
driver.find_element(By.XPATH, "//a[@class='button secondary radius']").click()
time.sleep(2)

print("logout successful")

driver.quit()
