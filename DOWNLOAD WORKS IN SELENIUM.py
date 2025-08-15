import driver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver



file_path= "C://Users//Comp10//PycharmProjects//PythonProject//exceldemo.xlsx"
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.find_element(By.ID,"downloadButton").click()
# edit the excel with updated value assume we have updated the data ans save
file_input= driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(r"C:\Users\Comp10\PycharmProjects\PythonProject\china.xlsx")
wait= WebDriverWait(driver,45)
toast_locator = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)"""
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
# Selenium WebDriver is used to automate browser actions.
# WebDriverWait & expected_conditions are used for synchronization and waiting for elements.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

# ===================== Step 2: Set File Path Variables =====================
# This is the file path for saving and retrieving the Excel file.
file_path = "C://Users//Comp10//PycharmProjects//PythonProject//exceldemo.xlsx"

# ===================== Step 3: Launch Chrome Browser =====================
# Initialize Chrome WebDriver instance with default settings.
driver = webdriver.Chrome()

# Set implicit wait for element loading (20 seconds max wait per action).
driver.implicitly_wait(20)

# ===================== Step 4: Open Target Website =====================
# This website provides the upload/download test page.
driver.get("https://rahulshettyacademy.com/upload-download-test/")

# ===================== Step 5: Download Excel File =====================
# Click on the "Download" button to download an Excel template.
driver.find_element(By.ID, "downloadButton").click()

# ===================== Step 6: Update Excel Locally =====================
# For this demo, we assume that we have manually updated the downloaded file
# and saved it as 'china.xlsx' at the given path.

# ===================== Step 7: Upload Updated Excel File =====================
# Locate the file input element and send the full file path of the updated file.
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(r"C:\Users\Comp10\PycharmProjects\PythonProject\china.xlsx")

# ===================== Step 8: Wait for Toast Message =====================
# Create an explicit wait instance to wait for the toast notification.
wait = WebDriverWait(driver, 45)

# Define locator for the toast message displayed after file upload.
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")

# Wait until the toast message becomes visible.
wait.until(expected_conditions.visibility_of_element_located(toast_locator))

# ===================== Step 9: Capture and Print Toast Message =====================
# Retrieve and print the toast message text for verification.
toast_message = driver.find_element(*toast_locator).text
print("Upload Confirmation Message:", toast_message)

# ===================== Step 10: Close Browser =====================
driver.quit()


