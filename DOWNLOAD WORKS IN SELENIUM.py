"""
====================================================================
Project Title : Automated Excel Upload & Download Test
Author        : Anup Sharma
Tools Used    : Python, Selenium WebDriver, ChromeDriver
Skills Gained : Web Automation, File Handling in Selenium, Synchronization with WebDriverWait
Description   :
    This project automates the process of downloading an Excel file from a website,
    updating it locally (assumed in this demo), and then uploading the updated file back
    to the site. It also demonstrates toast message validation after upload.
====================================================================
"""

# ===================== Step 1: Import Required Libraries =====================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ===================== Step 2: Set File Path Variables =====================
file_path = r"C:\Users\Comp10\PycharmProjects\PythonProject\china.xlsx"

# ===================== Step 3: Launch Chrome Browser =====================
driver = webdriver.Chrome()
driver.implicitly_wait(20)

# ===================== Step 4: Open Target Website =====================
driver.get("https://rahulshettyacademy.com/upload-download-test/")

# ===================== Step 5: Download Excel File =====================
driver.find_element(By.ID, "downloadButton").click()

# ===================== Step 6: Upload Updated Excel File =====================
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

# ===================== Step 7: Wait for Toast Message =====================
wait = WebDriverWait(driver, 45)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(EC.visibility_of_element_located(toast_locator))

# ===================== Step 8: Capture and Print Toast Message =====================
toast_message = driver.find_element(*toast_locator).text
print("Upload Confirmation Message:", toast_message)

# ===================== Step 9: Close Browser =====================
driver.quit()
