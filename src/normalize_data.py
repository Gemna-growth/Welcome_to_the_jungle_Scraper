#
# MALEK PROJECT, 2023
# Normalise_Airtable
# File description:
# normalize_function.py
#

import re
from urllib.parse import urlparse
from datetime import datetime

# Define the desired date format
MY_DATE_FORMAT = "%d/%m/%Y"  # Format : "17/07/2023"


def convert_date(input_date):
    """
    Convert a given date string into a standardized format.

    Parameters:
    - input_date (str): The date string to be converted.

    Returns:
    - str: The converted date string in the format "17/07/2023".
    """
    global MY_DATE_FORMAT
    try:
        parsed_date = datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        try:
            parsed_date = datetime.strptime(input_date, "%d/%m/%Y")
        except ValueError:
            try:
                parsed_date = datetime.strptime(input_date, "%m/%d/%Y")
            except ValueError:
                return "Format de date non pris en charge"

    formatted_date = parsed_date.strftime(MY_DATE_FORMAT)
    return formatted_date


def is_valid_url(url):
    """
    Check if the given URL is valid.

    Parameters:
    - url (str): The URL to be checked.

    Returns:
    - str: The original URL if valid, otherwise an empty string.
    """
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return url
        return ""
    except ValueError:
        return ""


def normalize_string(input_string):
    """
    Normalize a string by capitalizing each word.

    Parameters:
    - input_string (str): The string to be normalized.

    Returns:
    - str: The normalized string.
    """
    words = input_string.split()
    normalized_words = [word.capitalize() for word in words]
    normalized_string = ' '.join(normalized_words)
    return normalized_string


def del_the_h_and_f_in_my_string(input_string):
    """
    Remove specific patterns from a string.

    Parameters:
    - input_string (str): The string from which patterns should be removed.

    Returns:
    - str: The string with patterns removed.
    """
    patterns_to_remove = [
        "(H/F)", "H/F", "(f/h)", "f/h", " - Cdi", "(m/f)"
        "- (F/h)", "- F/h", "Hf", "(f/h)",
        "F/h", "H-f", "F-h", "(x/f/m)",
        "(f/m/x)", " - Cdi", "F/h", "(f/h)", "F/H", " (F/H)", "f/m", "(CDI)", "- Stage", "h-f", "HF", "- CDI",
        " ( En Cdi)", "(lyon)", "(bordeaux)"
    ]

    for pattern in patterns_to_remove:
        if pattern in input_string:
            input_string = input_string.replace(pattern, "")
            input_string = input_string.replace("()", "")
            if input_string.endswith(" - "):
                input_string = input_string[:-3]
            if input_string.endswith(" -"):
                input_string = input_string[:-2]
    return input_string


def normalize_title(input_string):
    """
    Normalize a title string by removing specific patterns and capitalizing each word.

    Parameters:
    - input_string (str): The title string to be normalized.

    Returns:
    - str: The normalized title string.
    """
    return normalize_string(del_the_h_and_f_in_my_string(input_string))


def check_if_is_number(input_string):
    """
    Check if the given string is a number.

    Parameters:
    - input_string (str): The string to be checked.

    Returns:
    - str: The original string if it's a number, otherwise an empty string.
    """
    if re.match(r'^[0-9]+$', input_string):
        return input_string
    else:
        return ''
