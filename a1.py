from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://duckduckgo.com/")

search_box = driver.find_element(By.ID, "searchbox_input")
search_box.send_keys("astanaituniversity")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

results = driver.find_elements(By.CSS_SELECTOR, "article[data-testid='result']")
assert len(results) > 0

print("test passed")

driver.quit()
