#
# MALEK PROJECT, 2023
# Welcome to the jungle Scrapper
# File description:
# setup_driver
#


from selenium import webdriver
from time import sleep


def setup_driver(link, headless_mode):
    chrome_options = webdriver.ChromeOptions()
    if headless_mode == "False":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.binary_location = "/usr/bin/chromium-browser"
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(link)
    sleep(1)
    return driver

