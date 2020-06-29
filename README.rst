============
DOCUMENT UPLOADER
============

A Python3 multiple document dowloader/uploader for Drupal 8 user interface. Can download/upload PDF, DOCX, DOC, TXT, WRF, XLS, XLSX, BZ2, TAR, TAR.GZ files.

Features:

- Uploads multiple documents to Drupal 8 user interface.
- Downloads multiple documents from any website.
- Does not need any monitoring, will happily upload/download all downloadable documents.
- Can upload hundreds, even thousands (theoretically), of documents stored in its predefined directory.

Contributions and comments are welcome at: 
http://github.com/jbernadas/document-uploader

These are the requirements:

- selenium
- os
- lxml
- bs4
- requests
- urllib
- geckodriver - downloaded separately from Mozilla repository at https://github.com/mozilla/geckodriver

Installation
============

Clone as usual:
:: 
  git clone https://github.com/jbernadas/document-uploader

Go inside the created directory: 
:: 
  cd document-uploader

Use virtualenv by creating a virtual environment folder called venv inside the root folder:
::
  python3 -m venv venv

or:
::
  virtualenv venv

Fireup the virtualenv (Mac):
::
  source venv/bin/activate
  
Fireup the virtualenv (Windows):
::
  venv/Scripts/activate

Install all requirements by:
::
  pip install -r requirements.txt

Deactivate virtualenv:
::
  deactivate

Configuration
=============

None.

Documentation
=============

You can tweak the arguments and parameters to make it find the necessary targets.

Usage
=====

cd into the root directory:
::
  cd document-uploader

Put all the documents you want to upload into docs_for_upload folder.

Fire it up:
::
  python3 document-uploader.py

The script will first ask what URL to go to, then will wait for you to login. When you are logged in, hit the 'y' key to let the script proceed.

When script is done downloading it will tell you how many documents were downloaded and close by itself.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/jbernadas/document-uploader

:author: Joseph Bernadas
:version: 0.0.1
:date: 2020/06/26
:license: GPL version 3
