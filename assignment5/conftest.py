import pytest
import pytest_html
from selenium import webdriver
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger()


@pytest.fixture
def setup():
    logger.info("Browser setup started")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    logger.info("Browser closing")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["setup"]
        screenshot_path = take_screenshot(driver, item.name)

        if screenshot_path:
            report.extra = getattr(report, "extra", [])
            report.extra.append(pytest_html.extras.png(screenshot_path))
