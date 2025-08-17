"""
====================================================================
Project Title : Automated Excel Upload & Download Test
Author        : Anup Sharma
Tools Used    : Python, Selenium WebDriver, ChromeDriver
Skills Gained : Web Automation, File Handling, Explicit Waits
Description   :
    Automates download of an Excel file, assumes local update,
    uploads updated file, and validates the toast message.
====================================================================
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

upload_path = r"C:\Users\Comp10\PycharmProjects\PythonProject\china.xlsx"

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/upload-download-test/")

driver.find_element(By.ID, "downloadButton").click()

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
assert os.path.exists(upload_path), f"File not found: {upload_path}"
file_input.send_keys(upload_path)

wait = WebDriverWait(driver, 45)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body")
wait.until(EC.visibility_of_element_located(toast_locator))

print("Upload Confirmation Message:", driver.find_element(*toast_locator).text)
driver.quit()
