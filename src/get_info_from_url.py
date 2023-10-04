#
# MALEK PROJECT, 2023
# scrapping_wttj
# File description:
# get_info_from_url
#

from selenium.webdriver.common.by import By
from time import sleep
from class_info import JobInfo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_info_from_url(driver, url, date, list_of_categories) -> JobInfo:
    # GO TO THE URL
    driver.get(url)
    sleep(1)

    # CREATE THE OBJECT
    _info = JobInfo(url)

    # GET CATEGORIES
    _info.job_data_dict["hiring_categories"] = list_of_categories

    # GET PUBLISHED DATE
    _info.job_data_dict["hiring_published_date"] = date

    # GET JOB TITLE
    _info.job_data_dict["hiring_title"] = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/h1").text

    # TRY TO GET JOB LOCATION
    try:
        _info.job_data_dict["hiring_location"] = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/li/span[2]/a/span").text
    except:
        pass

    # GET JOB CONTRACT AND LEVEL
    elements = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/div")
    iy = 0
    for uno in elements.find_elements(By.CLASS_NAME, "sc-imwsjW"):
        iy += 1
        try:
            uno.find_element(By.NAME, "contract")
            if uno.text[:-1] == "\n":
                _info.job_data_dict["hiring_contract"] = uno.text[:-1]
            else:
                _info.job_data_dict["hiring_contract"] = uno.text
        except:
            pass
        try:

            uno.find_element(By.NAME, "education_level")
            _info.job_data_dict["hiring_level"] = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/div/div[" + str(iy) + "]/span[2]").text
        except:
            pass

    # GET JOB DESCRIPTION
    _info.job_data_dict["hiring_description"] = driver.find_element(By.ID, "description-section").text

    # GET COMPANY NAME
    _info.job_data_dict["company_name"] = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/a/span").text

    # GET COMPANY LOGO URL
    _info.job_data_dict["company_logo_url"] = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/a/div/figure/img").get_attribute("src")

    # GET COMPANY DESCRIPTION
    _info.job_data_dict["company_description_wttj"] = driver.find_element(By.ID, "about-section").text

    # GET COMPANY STAFF RANGE
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[2]/div/div[2]/aside/div[1]/div[2]/span"))
    )
    _info.job_data_dict["company_staff_range"] = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[2]/div/div[2]/aside/div[1]/div[2]/span").text

    # GET COMPANY INDUSTRY
    try:
        _info.job_data_dict["company_industry"] = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[2]/div/div[2]/aside/div[1]/div[3]/span").text
    except:
        pass

    # GO TO COMPANY PAGE
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div/a").click()
    sleep(1)
    # GET COMPANY STAFF COUNT
    try:
        _info.job_data_dict["company_staff_count"] = driver.find_element(
            By.CSS_SELECTOR, "#pages_organizations_show > main > div > div > section > div.sc-1tceu7y-0.dtBzLT > "
                             "div:nth-child(1) > div > div:nth-child(4) > div > div > article > div > ul >"
                             " li:nth-child(2) > span").text
    except:
        pass
    if _info.job_data_dict["company_staff_count"] == "":
        _info.job_data_dict["company_staff_count"] = "0"

    # GET COMPANY LINKEDIN URL
    try:
        tempo_2 = driver.find_element(By.CLASS_NAME, "sc-16kqxrj-4").find_elements(By.TAG_NAME, "a")
        for one in tempo_2:
            if "linkedin" in one.get_attribute("href"):
                _info.job_data_dict["company_linkedin"] = one.get_attribute("href")
                break
    except:
        pass

    # GET COMPANY FOUNDED ON
    try:
        _info.job_data_dict["company_founded_on"] = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div/div/section/div[1]/div[1]/div/div[4]/"
            "div/div/article/div/ul/li[1]/span").text
    except:
        pass

    # GET COMPANY WEBSITE AND DOMAIN
    for one in driver.find_elements(By.CLASS_NAME, "sc-hqpNSm"):
        try:
            _info.job_data_dict["company_website"] = one.find_element(By.TAG_NAME, "a").get_attribute("href")
            _info.job_data_dict["company_domain"] = _info.job_data_dict["company_website"].split("://")[1].split("/")[0]
            if _info.job_data_dict["company_domain"].startswith("www."):
                _info.job_data_dict["company_domain"] = _info.job_data_dict["company_domain"][4:]
            break
        except Exception as e:
            _info.job_data_dict["company_country"] = "France"
            adress = one.text
            try:
                _info.job_data_dict["company_city"] = adress
            except:
                _info.job_data_dict["company_city"] = adress
            pass
        except:
            pass

    # GO TO TECH PAGE
    save_url = driver.current_url
    driver.get(driver.current_url + "/tech")
    sleep(0.5)
    try:
        if driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/main/div/div/div/div/h2/span").text\
                == "Erreur 404":
            driver.get(save_url + "/tech-1")
            sleep(0.5)
    except:
        pass
    # GET COMPANY TOOLS
    temps = driver.find_elements(By.CLASS_NAME, "f9afj1-0")
    for one in temps:
        _info.job_data_dict["company_tools"] += one.text
        if one != temps[-1]:
            _info.job_data_dict["company_tools"] += ", "
    return _info
