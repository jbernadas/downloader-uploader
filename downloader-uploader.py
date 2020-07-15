# This is a document downloader/uploader.
# You have to have the same version-as-your-browser
# Firefox GeckoDriver to use this. You have to install
# those separately from pip, and needs to be added to PATH.

import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

# This is the downloader part of the script
def downloader():
    url = input("What is the page you want to download from? ")
    year = input("What year report is this? ")

    # DO NOT RENAME THIS FOLDER, BOTH FUNCTIONS RELY ON THE SAME FOLDER NAME.
    folder_location = './docs_for_upload'

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    # Only look for these types of files
    QUALIFIERS = [
        # "a[href$='.tgz']",
        # "a[href$='.gz']",
        # "a[href$='.bz2']",
        # "a[href$='.tar']",
        "a[href$='.pdf']",
        "a[href$='.doc']",
        "a[href$='.docx']",
        "a[href$='.txt']",
        "a[href$='.wrf']",
        "a[href$='.xls']",
        "a[href$='.xlsx']"
    ]

    count = 0

    ### Our actual downloader script ###
    # For each qualifier in our list of QUALIFIERS
    for qualifier in QUALIFIERS:
        # and for each link inside our soup with the above qualified extension
        for link in soup.select(qualifier):
            # create a variable called filename which corresponds to the address of our downloadable file 
            filename = os.path.join(folder_location,  year + '-' + link['href'].split('/')[-1])
            # open the filename address
            with open(filename, 'wb') as f:
                # get the file and writes it
                f.write(requests.get(urljoin(url, link['href'])).content)
                count += 1
    
    print("Done! Downloaded a total of {} document/s!".format(count))

# This is the uploader part of script
def uploader():
    # Initialize webdriver. We are using Firefox because Chrome is spotty on the login bit.
    driver = webdriver.Firefox()

    # Target base URL
    target_site = input("What is the name of the website? ")

    # Login to site manually
    driver.get(target_site + '/login')

    # Ask if user has logged-in to site and ready to proceed
    proceed = input(
        "Are you logged-in and ready to proceed? 'y' = yes, any key to abort: ")

    # The directory where our soon-to-be uploaded documents reside
    FILESDIR = "docs_for_upload"

    fileCount = sum([len(files) for r, d, files in os.walk(FILESDIR)])

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
    count = 0
    ### Our uploader script ###
    if proceed == 'y':
        # For each qualifier in list of QUALIFIERS
        for qualifier in QUALIFIERS:
            # for each filename inside our document directory
            for filename in os.listdir('./' + FILESDIR):
                # and if filename ends with the qualifier being iterated
                if filename.endswith(qualifier):
                    # initialize a wait variable that makes the driver wait for so many seconds
                    wait = WebDriverWait(driver, 120)
                    # go to the /media/add/document of the Drupal site
                    driver.get(target_site + "/media/add/document")
                    # look for the id of input area and fill it with the path to our file-to-upload
                    driver.find_element_by_id(
                        "edit-field-document-0-upload").send_keys(os.getcwd() + '\\' + FILESDIR + '\\' + filename)
                    # wait until the page is finished uploading, in this case 
                    # when the remove button appears, before proceeding
                    wait.until(presence_of_element_located(
                        (By.NAME, 'field_document_0_remove_button')))
                    # look for the 'name' input box and fill it with the same name as the file
                    driver.find_element(
                        By.ID, "edit-name-0-value").send_keys(filename)
                    # wait for the 'save' button to appear, then click it.
                    wait.until(element_to_be_clickable(
                        (By.XPATH, 'html/body/div[2]/div[1]/main/div[4]/div[1]/form/div[8]/input[@id="edit-submit"]'))).click()
                    # rinse, repeat.
                    count += 1
                    continue
        
        print('Done! Uploaded a total of {}/{} document/s.'.format(count, fileCount))
        
        # Exit the driver.
        driver.quit()
    else:
        driver.quit()

upload_or_download = input("Welcome to DOWNLOADER/UPLOADER!\nType d for download, u for upload. ")

if (upload_or_download == 'u'):
    uploader()
elif (upload_or_download == 'd'):
    downloader()
else:
    upload_or_download = input("You need to type d for download, u for upload. ")

print('\a')