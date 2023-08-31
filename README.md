# selenium-webdriver-automation-testing
# Web Scraper for Company Websites

## Overview

This Python script uses Selenium WebDriver to scrape a list of company websites. It navigates through a custom-scrolling container, dynamically loads the content, and extracts the URLs to a CSV file.

## Requirements

- Python 3.x
- Selenium WebDriver
- Google Chrome

## Installation

1. Clone the repository:
    ```bash
    git clone <repo_url>
    ```
   
2. Navigate into the project directory:
    ```bash
    cd path/to/directory
    ```

3. Install required packages:
    ```bash
    pip install selenium
    ```

## Usage

1. Open `application.py` in your favorite editor.
2. Configure the WebDriver to use your installed browser (default is Chrome).
3. Run the script:
    ```bash
    python application.py
    ```
   
4. The script will navigate through the website, scrape the URLs, and store them in `company_list.csv`.

## Troubleshooting

If you encounter issues related to Unicode characters during CSV export, make sure your Python environment is set to UTF-8.

## Credits

Developed by Colin Lemus.
