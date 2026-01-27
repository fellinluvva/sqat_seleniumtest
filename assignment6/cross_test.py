import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook

load_dotenv()
USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
if not USERNAME or not ACCESS_KEY:
    raise Exception("BrowserStack credentials not found in .env")

workbook = load_workbook("cogmento_login_data.xlsx")
sheet = workbook.active

firefox_options = Options()
firefox_options.set_capability("browserName", "Firefox")
firefox_options.set_capability("browserVersion", "latest")
firefox_options.set_capability("pageLoadStrategy", "normal")  # avoids script timeout
firefox_options.set_capability("bstack:options", {
    "os": "Windows",
    "osVersion": "10",
    "projectName": "Assignment 6 Cogmento DDT",
    "buildName": "Cogmento Login Tests",
    "sessionName": "Data Driven Login Test",
    "seleniumVersion": "4.39.0",
    "userName": USERNAME,
    "accessKey": ACCESS_KEY,
    "local": False
})

driver = webdriver.Remote(
    command_executor="https://hub-cloud.browserstack.com/wd/hub",
    options=firefox_options
)

wait = WebDriverWait(driver, 5)
print("DATA-DRIVEN LOGIN TEST STARTED ON BROWSERSTACK (FIREFOX)")

for row in range(2, sheet.max_row + 1):
    test_id = sheet.cell(row, 1).value
    email = sheet.cell(row, 2).value
    password = sheet.cell(row, 3).value
    expected = sheet.cell(row, 4).value

    driver.get("https://ui.cogmento.com/")

    try:
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Login']")))
        login_button.click()

        if expected.upper() == "SUCCESS":
            user_label = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='AITU']")))
            assert user_label.is_displayed()
            print(f"{test_id}: PASSED")

            # Logout for next test
            user_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ui.dropdown")))
            user_menu.click()
            logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']")))
            logout_button.click()
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))

        else:
            error_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ui.error.message")))
            assert error_msg.is_displayed()
            print(f"{test_id}: PASSED")

    except Exception as e:
        print(f"{test_id} Exception: {str(e)}")
        print(f"{test_id}: FAILED")

driver.quit()
print("BROWSERSTACK FIREFOX TEST EXECUTION FINISHED")
