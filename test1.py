from selenium.webdriver import Chrome
driver = Chrome()

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:\webdrivers"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://python.org')