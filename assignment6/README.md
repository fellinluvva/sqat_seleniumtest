# Assignment 6 - Data-Driven & Cross-Browser Testing

## Project Overview
This project demonstrates **data-driven testing (DDT)** and **cross-browser automated testing** using **Selenium WebDriver** and **BrowserStack**. The automation tests the **login functionality** of the [Cogmento CRM](https://ui.cogmento.com/) web application with multiple sets of credentials stored in an Excel file.

Key objectives:
- Automate login tests using **multiple data sets**.
- Validate **successful and failed login scenarios**.
- Perform **cross-browser testing** on BrowserStack using Firefox and Chrome.
- Ensure proper **logout between tests** to avoid session conflicts.

---

## Prerequisites

- Python 3.9+
- Selenium 4.x
- openpyxl
- python-dotenv
- BrowserStack account (for cloud cross-browser testing)
- `.env` file with the following variables:
  (could be obtained at https://www.browserstack.com/accounts/profile/details)
```text
BROWSERSTACK_USERNAME=your_browserstack_username
BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key
```

---

## Project Files

| File | Description |
|------|-------------|
| `cross_test.py` | Main Selenium script for Firefox with BrowserStack integration and DDT. |
| `cogmento_login_data.xlsx` | Excel file containing test cases: email, password, and expected result. |
| `.env` | Stores BrowserStack credentials securely. |
| `README.md` | Project documentation. |

---

## Excel File Format

The `cogmento_login_data.xlsx` file should have the following columns:

| TestID | Email | Password | Expected Result |
|--------|-------|----------|----------------|
| TC01   | user1@example.com | password1 | SUCCESS |
| TC02   | invalid@example.com | wrongpass | FAILURE |
| TC03   | user2@example.com | password2 | SUCCESS |

> Note: `Expected Result` must be either `SUCCESS` or `FAILURE`.

---

## How to Run

1. Clone the repository and navigate to the project folder:

```bash
git clone <your_repo_url>
cd assignment6
```

2. Install dependencies:
```text
pip install selenium openpyxl python-dotenv
```
3. Create a .env file with your BrowserStack credentials. 
4. Run the test:
```text
python cross_test.py
```
5. The script will:
- Read all test cases from the Excel file.
- Execute each login attempt on BrowserStack Firefox.
- Verify login success by checking the presence of the user label (AITU).
- Perform logout after each successful login.
- Print PASSED or FAILED for each test case.

## Features

- Data-Driven Testing: Tests multiple credentials dynamically from Excel.
- Cross-Browser Testing: Supports Firefox and Chrome via BrowserStack.
- Secure Credentials: Uses .env to avoid exposing sensitive data.
- Robust Waits: Uses Selenium WebDriverWait to handle dynamic page elements.
- Error Handling: Catches exceptions and logs failed test cases without stopping execution.
- Session Management: Automatically logs out between tests to avoid session conflicts.

## BrowserStack Reporting

- Each test session is named according to the test ID and build.
- Test results can be viewed on the BrowserStack dashboard for detailed logs, screenshots, and video recordings.

## Notes

- Ensure BrowserStack credentials are correct in the .env file.
- Use the latest supported Selenium version (4.39.0) for compatibility with BrowserStack.
- Increase wait time (WebDriverWait) if tests fail due to slow network or BrowserStack server delays.

## Author

**Azamat Nagumanov SE-2328**
