import os
from datetime import datetime

def take_screenshot(driver, test_name):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(file_path)
    return file_path
