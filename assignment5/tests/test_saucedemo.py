from utils.logger import get_logger

logger = get_logger()


def login(driver, username, password):
    driver.find_element("id", "user-name").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()


def test_valid_login(setup):
    driver = setup
    logger.info("TEST START: Valid Login")

    login(driver, "standard_user", "secret_sauce")

    expected_url = "inventory.html"
    actual_url = driver.current_url

    logger.info(f"Expected: {expected_url}")
    logger.info(f"Actual: {actual_url}")

    assert expected_url in actual_url
    logger.info("TEST PASSED: Valid Login")


def test_add_to_cart(setup):
    driver = setup
    logger.info("TEST START: Add to Cart")

    login(driver, "standard_user", "secret_sauce")
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    expected = "1"
    actual = driver.find_element("class name", "shopping_cart_badge").text

    logger.info(f"Expected cart count: {expected}")
    logger.info(f"Actual cart count: {actual}")

    assert expected == actual
    logger.info("TEST PASSED: Add to Cart")


def test_invalid_login_failure(setup):
    """
    THIS TEST IS DESIGNED TO FAIL
    """
    driver = setup
    logger.info("TEST START: Invalid Login Failure Test")

    login(driver, "locked_out_user", "secret_sauce")

    expected_message = "Login successful"
    actual_message = driver.find_element(
        "css selector", "h3[data-test='error']"
    ).text

    logger.error(f"Expected: {expected_message}")
    logger.error(f"Actual: {actual_message}")

    assert expected_message in actual_message
