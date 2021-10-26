import argparse
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

parser = argparse.ArgumentParser(description='Benchmark page load until document.readyState')
parser.add_argument('-u', '--url', default='https://www.enisyst.de')
parser.add_argument('-d', '--delay', default=200)
args = parser.parse_args()

options = Options()
options.headless = True

def page_has_loaded(self):
    page_state = self.execute_script('return document.readyState;')
    if page_state == 'complete':
        return True
    return False

browser = webdriver.Firefox(options=options)

start = time.time()

browser.get(args.url)

try:
    WebDriverWait(browser, args.delay).until(page_has_loaded)
    end = time.time()
    print(datetime.now(), ",", (end - start), ",", args.url, ",", args.delay)
except TimeoutException:
    print(datetime.now(), ",timeout", ",", args.url, ",", args.delay)

browser.quit()