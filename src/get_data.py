# MALEK PROJECT, 2023
# Welcome to the jungle scrapper
# File description:
# get_data.py
#

from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from datetime import timedelta
import sys
from get_info_from_url import get_info_from_url
from selenium.common.exceptions import NoSuchElementException as UnableToLocateElementException
from selenium.common.exceptions import ElementNotInteractableException


def convert_str_to_delai(date):
    """Convert a string representation of a date to a delay in days."""
    date_to_delai = {
        "24h": 1,
        "1 week": 7,
        "1 month": 30,
        "3 months": 90,
        "all": 3650  # 10 years for "all" is a rough approximation
    }
    return date_to_delai.get(date)


def get_category(driver):
    try:
        element = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/button[2]")
        element.click()
    except ElementNotInteractableException:
        print("Element is not intractable.", file=sys.stderr)
    sleep(1)
    list_of_gate = ""
    for i in range(1, 16):
        element = None
        try:
            element = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div/div/div/section/div/div[" + str(
               i) + "]/button/div[1]/input")
        except ElementNotInteractableException:
            print("Element is not Intractable.", file=sys.stderr)
        except UnableToLocateElementException:
            element = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div/div/div/section/div/div[" + str(
                i) + "]/button/div[1]/input")
        if element.get_attribute("aria-checked") == "mixed":
            if list_of_gate != "":
                list_of_gate += ", "
            temp = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div/div/div/section/div/div[" + str(
                i) + "]/button/div[1]/div/p").text
            list_of_gate += driver.find_element(By.XPATH,
                                                "/html/body/div[11]/div/div/div/div/div/section/div/div[" + str(
                                                    i) + "]/button/div[1]/div").text
            list_of_gate = list_of_gate.replace(temp, "")
    driver.find_element(By.XPATH, "/html/body/div[11]/div/div/button").click()
    sleep(1)
    return list_of_gate


def get_list_of_url(driver):
    class_element_of_job_box = "iiwBSR"
    class_element_of_page = "sc-cXPBUD"
    list_of_element = []
    nb_next_page = 1
    page = driver.find_elements(By.CLASS_NAME, class_element_of_page)
    nb_page = len(page) - 2

    while True:
        for i in range(1, len(driver.find_elements(By.CLASS_NAME, class_element_of_job_box)) + 1):
            print(i, "//", len(driver.find_elements(By.CLASS_NAME, class_element_of_job_box)), file=sys.stderr)
            xpath_to_search_one = ("/html/body/div[1]/div[1]/div/div/div/div/div[2]/div/ol/div["
                                   + i.__str__() + "]/li/div/div/div[2]/a")
            try:
                xpath_to_search = ("/html/body/div[1]/div[1]/div/div/div/div/div[2]/div/ol/div["
                                   + i.__str__() + "]/li/div/div/div[2]/div[3]/div[1]/p/time")
                result_date = (driver.find_element(By.XPATH, xpath_to_search).get_attribute("datetime").split("T")[0])
                result_url = (driver.find_element(By.XPATH, xpath_to_search_one).get_attribute("href"))
                list_of_element.append((result_url, result_date))
            except:
                pass
        nb_next_page += 1
        if nb_next_page > nb_page:
            break
        page[nb_next_page].click()
        sleep(1)
    return list_of_element


def loop_in_list_of_url(driver, date):
    count = 0
    delai = convert_str_to_delai(date)
    last_date = None
    if delai is not None:
        last_date = datetime.now() - timedelta(days=delai)
    sleep(1)

    # Get the list of job categories
    list_of_categories = get_category(driver)

    # Get the list of job URLs
    list_of_url = get_list_of_url(driver)

    data_of_get_url = []
    for i in range(len(list_of_url)):
        print(
            "----------------------------------------------------------------------------------------------------------"
            "--------------------------------------------------------", file=sys.stderr)
        print(i.__str__() + "/" + str(len(list_of_url)), file=sys.stderr)
        date_of_job = datetime.strptime(list_of_url[i - 1][1], "%Y-%m-%d")
        if delai is None or date_of_job >= last_date:
            try:
                data_of_get_url.append(
                    get_info_from_url(driver, list_of_url[i - 1][0], list_of_url[i - 1][1], list_of_categories))
                print("is append nb " + i.__str__() + "/" + len(list_of_url).__str__(), file=sys.stderr)
                count += 1
            except Exception as e:
                print("Error in search url!(" + e.__str__() + ")\n", file=sys.stderr)
                exit(84)
        else:
            print("is not append nb " + i.__str__() + "/" + len(list_of_url).__str__(), file=sys.stderr)
    return data_of_get_url
