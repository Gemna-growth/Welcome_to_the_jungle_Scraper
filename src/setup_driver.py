#
# MALEK PROJECT, 2023
# Welcome to the jungle Scrapper
# File description:
# setup_driver
#


from selenium import webdriver
from time import sleep


def setup_driver(link, headless_mode):
    """
    Initializes and returns a Chrome WebDriver instance.

    Parameters:
    - link (str): The URL to navigate to after initializing the driver.
    - headless_mode (str): A string indicating whether to run Chrome in headless mode.
                           If set to "False", Chrome will run in headless mode.

    Returns:
    - driver (webdriver.Chrome): An instance of the Chrome WebDriver.
    """

    # Create an instance of ChromeOptions to specify additional options for the driver.
    chrome_options = webdriver.ChromeOptions()

    # Check if headless mode is set to "False".
    if headless_mode == "False":
        # Add arguments to run Chrome in headless mode.
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1080')

        # Specify the binary location of the Chromium browser.
        chrome_options.binary_location = "/usr/bin/chromium-browser"

    # Initialize the Chrome WebDriver with the specified options.
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the browser window.
    driver.maximize_window()

    # Navigate to the provided link.
    driver.get(link)

    # Pause the execution for 1 second to allow the page to load.
    sleep(1)

    # Return the initialized driver.
    return driver
