import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = input("What is the page you want to download from? ")

folder_location = './docs_for_upload'

response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")

QUALIFIERS = [
    "a[href$='.pdf']",
    "a[href$='.doc']",
    "a[href$='.docx']",
    "a[href$='.txt']",
    "a[href$='.wrf']",
    "a[href$='.xls']",
    "a[href$='.xlsx']"
    # "a[href$='.tar']",
    # "a[href$='.tar.gz']"
]

for qualifier in QUALIFIERS:
    for link in soup.select(qualifier):
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        # print(filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)
