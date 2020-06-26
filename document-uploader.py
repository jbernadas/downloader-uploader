# You have to have the same version-as-your-browser Chrome WebDriver or Firefox GeckoDriver to use this. You have to install those separately from pip, and needs to be added to PATH.

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

# Initialize webdriver. We are using Firefox because Chrome is spotty on the login bit.
driver = webdriver.Firefox()

target_site = input("What is the name of the website? ")

# Login to site manually
driver.get(target_site + '/login')

proceed = input(
    "Are you logged-in and ready to proceed? 'y' = yes, any key to abort: ")

FILESDIR = "docs_for_upload"

if proceed == 'y':
    for filename in os.listdir('./' + FILESDIR):
        if filename.endswith('.pdf' or '.docx'):
            wait = WebDriverWait(driver, 60)
            driver.get(target_site + "/media/add/document")
            driver.find_element_by_id(
                "edit-field-document-0-upload").send_keys(os.getcwd() + '\\' + FILESDIR + '\\' + filename)
            wait.until(presence_of_element_located(
                (By.NAME, 'field_document_0_remove_button')))
            driver.find_element(
                By.ID, "edit-name-0-value").send_keys(filename)
            wait.until(element_to_be_clickable(
                (By.XPATH, 'html/body/div[2]/div[1]/main/div[4]/div[1]/form/div[8]/input[@id="edit-submit"]'))).click()
            continue
    driver.quit()
else:
    driver.quit()
