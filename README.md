# Welcome to the Jungle Scraper

This is a Python program for web scraping Welcome to the Jungle job search website. It allows users to extract job listings based on user-defined criteria such as date range, output format (CSV or JSON), output destination (print to console or write to file), and headless mode (default is False).

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the program, run `main.py` with the following arguments:

```
usage: main.py [-h] -l {LINK} [-n {NAME}] [-d {24h,1 week,1 month,3 month,all}] [-t {json,csv}] [-f {print,file}] [-w {False,True}]

Description de votre programme

optional arguments:
  -h, --help            show this help message and exit
  -l LINK, --link LINK  url of welcome to the jungle search
  -n NAME, --name NAME  name of the search
  -d {24h,1 week,1 month,3 month,all}, --date {24h,1 week,1 month,3 month,all}
                        date of the job
  -t {json,csv}, --type {json,csv}
                        type of the output
  -f {print,file}, --format {print,file}
                        format of the output
  -w {False,True}, --windowless {False,True}
                        window mode (default: False)
```

## Examples

Scrape job listings for"Data Analyst"jobs posted in the last week and save the results to a CSV file:

```
python main.py --link "{link}" --name DevOps --date 24h --format file --type json --windowless True
```
