# Selenium WebDriver Automation – Assignment 3

## Azamat Nagumanov SE-2328 SQAT course

**Project Name:** Selenium_Testing
**Course:** Software Quality Assurance and Testing
**Assignment:** Assignment 3 – Selenium WebDriver Practice

This repository contains automated UI tests developed using **Selenium WebDriver** as part of Assignment 3.

---

## Technologies Used

* **Programming Language:** Python 3.x
* **Automation Framework:** Selenium WebDriver
* **Browser:** Google Chrome
* **WebDriver:** ChromeDriver

---

## 📁 Project Structure

```text
squat/
│
├── a1.py         # Search functionality test
├── a2.py         # Login and logout test
├── a3.py         # Flight booking test
├── README.md     # Project documentation
```

---

## ⚙ Setup Instructions

### 1. Prerequisites

* Python 3.x installed
* Google Chrome installed
* ChromeDriver matching Chrome version

### 2. Install Dependencies

```bash
pip install selenium
```

### 3. ChromeDriver Setup

* Download ChromeDriver
* Add it to system PATH or place it in the project folder
```text
most of the time it is preinstalled with Chrome so skip this
```
---

## ✅ Automated Test Cases

### 1️⃣ Search Functionality Test

**Website:** [https://duckduckgo.com/](https://duckduckgo.com/)
```text
also can simply use https://google.com/
```
**Description:**

* Opens the search engine
* Enters a search query
* Submits the search
* Verifies that results are displayed

**Locators Used:**

* ID
* CSS Selector

---

### 2️⃣ Login & Logout Test

**Website(special for this kindof test):** [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

**Credentials Used:**

* Username: `tomsmith`
* Password: `SuperSecretPassword!`

**Description:**

* Performs login with valid credentials
* Verifies successful login message
* Performs logout

**Locators Used:**

* ID
* XPath
* CSS Selector

---

### 3️⃣ Flight Booking Test with Title Checkpoints

**Website:** [https://blazedemo.com/](https://blazedemo.com/)

**Description:**

* Selects departure and destination cities
* Searches available flights
* Chooses a flight
* Enters passenger details
* Confirms booking
* Validates booking using page title/content checkpoints

**Locators Used:**

* Name
* ID
* CSS Selector
* XPath
---

## ▶ How to Run the Tests

Execute each test file separately:

```bash
python a1.py
python a2.py
python a3.py
```

---

## 📝 Notes

* Public demo websites are used for testing purposes
* `time.sleep()` is used for simplicity
* Tests are intended for educational use only

---

## 📌 Conclusion

This project demonstrates practical usage of Selenium WebDriver for automated web testing. It includes multiple test scenarios, different locator strategies, and validation checkpoints required for Assignment 3.

---

**Author:** Azamat Nagumanov
**Group:** SE-2328
**Instructor:** Akbope Murat
