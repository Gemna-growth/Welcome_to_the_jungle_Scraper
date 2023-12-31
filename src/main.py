#
# MALEK PROJECT, 2023
# scrapping_wttj
# File description:
# main
#

import csv
import json
import argparse
from get_data import loop_in_list_of_url
from setup_driver import setup_driver
from normalize_data import *
from datetime import datetime
import sys

# Mapping of functions to normalize data
function_map = {
    "company_name": normalize_string,
    "hiring_title": normalize_title,
    "hiring_published_date": convert_date,
    "company_founded_on": check_if_is_number,
    "company_staff_count": check_if_is_number,
    "hiring_url": is_valid_url,
    "company_logo_url": is_valid_url,
    "company_website": is_valid_url,
    "company_linkedin": is_valid_url,
}

def manage_arguments():
    """
    Parses and returns command line arguments.
    """
    parser = argparse.ArgumentParser(description='Scrapper of Welcome to the jungle')
    parser.add_argument('-l', '--link', help='URL of Welcome to the Jungle search', required=True)
    parser.add_argument('-n', '--name', help='Name of the search', default='nameless')
    parser.add_argument('-d', '--date', default='all', choices=['24h', '1 week', '1 month', '3 month', "all"],
                        help='Date of the job')
    parser.add_argument('-t', '--type', default='json', choices=['json', 'csv'], help='Type of the output')
    parser.add_argument('-f', '--format', default='print', choices=['print', 'file'], help='Format of the output')
    parser.add_argument('-w', '--windowless', default='False', choices=['False', 'True'],
                        help='Window mode (default: False)')
    args = parser.parse_args()
    return args

def get_name_of_file(date, name):
    """
    Generates a filename based on the given date and name.
    """
    return "scrapping_data_of_wttj_" + name + "_of_" + date + "_" + datetime.now().strftime("%d-%m-%Y-%H-%M")

def normalize_data(job_info):
    """
    Normalizes the data in the job_info dictionary using the function_map.
    """
    for key in job_info.job_data_dict:
        if key in function_map:
            job_info.job_data_dict[key] = function_map[key](job_info.job_data_dict[key])
    return job_info.job_data_dict

def extract_data_from_job_info(job_info_dict):
    """
    Extracts relevant data from the job_info dictionary.
    """
    return {key: job_info_dict[key] for key in job_info_dict}

def save_to_json(data, name_of_the_file):
    """
    Saves the given data to a JSON file.
    """
    with open(name_of_the_file + ".json", 'w') as f:
        json.dump(data, f)

def save_to_csv(data_of_get_url, name_of_the_file):
    """
    Saves the given data to a CSV file.
    """
    with open(name_of_the_file + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data_of_get_url[0].get_name_of_all_attributes())
        for p in data_of_get_url:
            writer.writerow(p.get_list())

def main():
    """
    Main function that manages the entire scraping process.
    """
    args = manage_arguments()
    driver = setup_driver(args.link, args.windowless)
    name_of_the_file = get_name_of_file(args.date, args.name)
    data_of_get_url = loop_in_list_of_url(driver, args.date)

    if not data_of_get_url:
        print("No data found", file=sys.stderr)
        return 84

    data = [normalize_data(job_info) for job_info in data_of_get_url]
    formatted_data = [extract_data_from_job_info(job_info) for job_info in data]

    if args.type == "json":
        if args.format == "print":
            print(json.dumps({"job": formatted_data}, indent=4))
        elif args.format == "file":
            save_to_json({"job": formatted_data}, name_of_the_file)
    elif args.type == "csv":
        if args.format == "print":
            print(";".join(data_of_get_url[0].get_name_of_all_attributes()))
            for p in data_of_get_url:
                print(";".join(p.get_list()))
        elif args.format == "file":
            save_to_csv(data_of_get_url, name_of_the_file)
    return 0

if __name__ == '__main__':
    main()
