#
# MALEK PROJECT, 2023
# Welcome to the jungle scrapper
# File description:
# class_info
#

class JobInfo:
    """
    Class to store and manage job-related information.
    """

    def __init__(self, url: str):
        """
        Initialize the JobInfo object with the job URL.

        :param url: URL of the job posting.
        """
        self.job_data_dict = {
            "hiring_url": url,
            "hiring_title": "",
            "hiring_contract": "",
            "hiring_location": "",
            "hiring_categories": "",
            "hiring_published_date": "",
            "hiring_description": "",
            "hiring_level": "",
            "hiring_source": "WTTJ",
            "company_name": "",
            "company_website": "",
            "company_domain": "",
            "company_linkedin": "",
            "company_industry": "",
            "company_staff_count": "",
            "company_staff_range": "",
            "company_founded_on": "",
            "company_tools": "",
            "company_last_source": "WTTJ",
            "company_city": "",
            "company_country": "",
            "company_zip_code": "",
            "company_description_wttj": "",
            "company_logo_url": "",
        }

    def get_name_of_all_attributes(self) -> list:
        """
        Return a list of all attribute names (keys) in the job_data_dict dictionary.

        :return: List of attribute names.
        """
        return list(self.job_data_dict.keys())

    def get_list(self) -> list:
        """
        Return a list of values from the job_data_dict dictionary.

        :return: List of values.
        """
        return list(self.job_data_dict.values())

    def __str__(self):
        return self.job_data_dict.__str__()
