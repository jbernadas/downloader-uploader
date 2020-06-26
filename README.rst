============
DOCUMENT UPLOADER
============

A Python3 multiple PDF/Docx uploader for Drupal 8 user interface.

Features:

- Uploads multiple images to Drupal 8 user interface.
- Waits for user to input 'alt' text before proceeding.
- Can upload hundreds of images stored in a predefined directory.

Contributions and comments are welcome at: 
http://github.com/jbernadas/pdf-uploader

These are the dependencies it requires:

- Selenium
- Os

Installation
============

Clone as usual:
:: 
  git clone https://github.com/jbernadas/pdf-uploader

Go inside the created directory: 
:: 
  cd pdf-uploader

Use pip to install all the above requirements:
::
  pip install selenium

Configuration
=============

None.

Documentation
=============

You can tweak the arguments and parameters to make it find the necessary table targets.

Usage
=====

cd into the root directory:
::
  cd pdf-uploader

Put all the images you want to upload into files_for_upload folder.

Fire it up:
::
  python3 pdf-uploader.py

The script will wait for you to login to your Drupal site. When you are logged in, hit the 'y' key to let the script proceed.

Repeat.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/jbernadas/pdf-uploader

:author: Joseph Bernadas
:version: 1.0.0
:date: 2020/06/26
:license: GPL version 3
