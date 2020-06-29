import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = input("What is the page you want to download from? ")

folder_location = './docs_for_upload'

response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")

# Only look for these types of files
QUALIFIERS = [
    "a[href$='.tgz']",
    "a[href$='.gz']",
    "a[href$='.bz2']",
    "a[href$='.pdf']",
    "a[href$='.doc']",
    "a[href$='.docx']",
    "a[href$='.txt']",
    "a[href$='.wrf']",
    "a[href$='.xls']",
    "a[href$='.xlsx']"
]

count = 0

# Our downloader script
for qualifier in QUALIFIERS:
    for link in soup.select(qualifier):
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)
            count += 1
print("Done! Downloaded a total of %s documents!" % count)
