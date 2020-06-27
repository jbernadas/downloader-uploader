# You have to have the same version-as-your-browser Chrome WebDriver, Firefox GeckoDriver to use this. You have to install those separately from pip, and needs to be added to PATH.

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

# Target base URL
target_site = input("What is the name of the website? ")

# Login to site manually
driver.get(target_site + '/login')

# Ask for user's input
proceed = input(
    "Are you logged-in and ready to proceed? 'y' = yes, any key to abort: ")

# The directory where our soon-to-be uploaded documents reside 
FILESDIR = "docs_for_upload"

# List of file types we are looking to upload
QUALIFIERS = [
    '.pdf',
    '.docx',
    '.txt',
    '.doc',
    '.wrf',
    '.xls',
    '.xlsx'
    # '.tar',
    # '.tgz',
    # '.gz',
    # '.bz2'
]

if proceed == 'y':
    # For each qualifier in list of QUALIFIERS
    for qualifier in QUALIFIERS:
        # For each filename inside our document directory
        for filename in os.listdir('./' + FILESDIR):
            # and if filename ends with one of our qualifier
            if filename.endswith(qualifier):
                # initialize a wait variable that lets the driver to wait for how many seconds
                wait = WebDriverWait(driver, 60)
                # go to the /media/add/document of the Drupal 8 page
                driver.get(target_site + "/media/add/document")
                # looks for a particular id and fills it with the path to our file-to-upload
                driver.find_element_by_id(
                    "edit-field-document-0-upload").send_keys(os.getcwd() + '\\' + FILESDIR + '\\' + filename)
                # wait until the remove button appears before proceeding
                wait.until(presence_of_element_located(
                    (By.NAME, 'field_document_0_remove_button')))
                # look for the 'name' input box and fill it with the same name as the file
                driver.find_element(
                    By.ID, "edit-name-0-value").send_keys(filename)
                # wait for the 'save' button to appear, then click it.
                wait.until(element_to_be_clickable(
                    (By.XPATH, 'html/body/div[2]/div[1]/main/div[4]/div[1]/form/div[8]/input[@id="edit-submit"]'))).click()
                # rinse, repeat.
                continue
    print('Done!')
    # Exit the driver.
    driver.quit()
else:
    driver.quit()
