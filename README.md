Flight Search Automation Framework

Overview

This project is an end-to-end web automation framework developed using Python, Selenium WebDriver, and Pytest to automate the flight search functionality on the Yatra website. The framework follows the Page Object Model (POM) design pattern to improve code reusability, readability, and maintainability.

Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git & GitHub

Key Features

- Automated end-to-end flight search workflow
- Cross-browser execution (Chrome & Microsoft Edge)
- Dynamic travel date selection
- Explicit waits for stable test execution
- Assertions for result validation
- Data-driven testing using external test data
- Logging for execution tracking and debugging
- Modular and reusable Page Object Model structure
- Easy-to-maintain project architecture

Project Structure

Flight_Search_Automation/
│── pages/
│── tests/
│── utilities/
│── test_data/
│── logs/
│── conftest.py
│── pytest.ini
│── requirements.txt
│── README.md

How to Run

Run on Chrome:

pytest -s --browser=chrome

Run on Microsoft Edge:

pytest -s --browser=edge

Future Enhancements

- HTML reports using Pytest
- CI/CD integration with GitHub Actions
- Screenshot capture on test failures
- Parallel execution with Pytest-xdist

Author

Reetika Srivastava
QA Automation Engineer | Python | Selenium | Pytest
