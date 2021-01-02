"""
Usage: will create a directory called links_csv that has a csv of image links found on pexel.com of the term.

Example of usage:
    python scrapping.py --term hotdogs --dirname hotdogs
"""

# packages
from selenium import webdriver
import datetime
import time 
import argparse
import os

# URl
url = 'https://www.pexels.com/search/'

# define the argument parser to read the url
parser = argparse.ArgumentParser()
parser.add_argument('-term', '--term', help='term to search')
parser.add_argument('-dirname', '--dirname', help='directory to save to')
args = vars(parser.parse_args())
term = args['term']
dir_name = args['dirname']

# full url
url = url + term

# chrome options to open in maximized mode
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# chromedriver version 79 or over: remove automation 
options.add_argument('--disable-blink-features=AutomationControlled')

# intialize chrome webdriver and open the url
driver = webdriver.Chrome(options=options)
driver.get(url)

# remove bot detection-ish
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# pause time
pause_time = 2

# get scroll height
last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# record start time
start = datetime.datetime.now()

while True:
    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # wait for page to load
    time.sleep(pause_time)

    # calculate new scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    # check to see end of scroll
    if new_height == last_height:
        break
    last_height = new_height

# Record time-lapse
end = datetime.datetime.now()
delta = end - start
print("[INFO] Total time taken to scroll to end {}".format(delta))

# extract all anchor tags
link_tags = driver.find_elements_by_tag_name("img")

# urls
href = []

# extract the urls of the images 
for tag in link_tags:
    if "photo-item__img" not in tag.get_attribute('class'):
        continue
    href.append(tag.get_attribute('src'))
# display the results
print("[INFO] Number of images found: {}".format(len(href)))

# Directory
DIR_PATH = 'links_csv'
if not os.path.exists(DIR_PATH):
    try:
        os.mkdir(DIR_PATH)
    except OSError:
        print("[INFO] Creation of directory \'{}\' failed.".format(os.path.abspath(DIR_PATH)))
    else:
        print("[INFO] Successfully created the directory \'{}\'.".format(os.path.abspath(DIR_PATH)))

# write into csv file
f = open("{}/{}.csv".format(DIR_PATH, dir_name), 'w')
f.write(",\n".join(href))
print("[INFO] Successfully created the file \'{}.csv\'".format(dir_name))