import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = input("What is the page you want to download from? ")

folder_location = './docs_for_upload'

# html_page = requests.get(download_page).text

# initial_soup = BeautifulSoup(html_page, "lxml")

# soup = initial_soup.find('div', attrs={'class': 'content'})

# current_link = ''

# doc_ends = ['.pdf', '.docx', 'txt', 'doc', 'wrf', 'xls', 'xlsx']

# for link in soup.find_all('a'):
#     current_link = link.get('href')
#     # if current_link.endswith()
#     # for doc_end in doc_ends:
#     #     if current_link.endswith(doc_end):
#     print('I found a doc: ' + current_link)

response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")

QUALIFIERS = ["a[href$='.pdf']", "a[href$='.doc']", "a[href$='.docx']", "a[href$='.txt']",
              "a[href$='.wrf']", "a[href$='.xls']", "a[href$='.xlsx']"]

for qualifier in QUALIFIERS:
    for link in soup.select(qualifier):
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        # print(filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)
