from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re
import csv

# This is the data we want to use to fill out the form
application_data = {
    "first_name": "Colin",
    "last_name": "Lemus",
    "full_name": "Colin Lemus",
    "email": "colin@thelemus.com",
    "address": "Valencia CA",
    "linkedin": "https://www.linkedin.com/in/colin-lemus/",
    "github": "https://www.github.com/colinlemus",
    "position": "Software Engineer",
    "summary": "Accomplished Software Engineer with superior development skills and Fortune 500 client service experience.",
    "skills": "Software Engineering, Web Development, Client Service",
    "work_experience": [
        {
            "position": "Software Engineer",
            "company": "Moving Mountain Distribution",
            "location": "Los Angeles, CA (Remote)",
            "description": "Consulting for a cannabis company by creating a NFT project, website for it, as well as software for inventory.",
            "start_date": "Mar 2023",
            "end_date": "Now",
        },
        {
            "position": "Software Engineer",
            "company": "Helios Interactive",
            "location": "Remote",
            "description": "Assigned complex coding projects, primarily for live entertainment activations from SaaS to high-profile video games.",
            "start_date": "July 2021",
            "end_date": "Nov 2022",
        },
        {
            "position": "Full Stack Web Developer",
            "company": "RMI Music Productions Inc.",
            "location": "Los Angeles, CA",
            "description": "Partnered closely with CEO Russ Miller and the video team to produce quality content and cutting-edge website designs.",
            "start_date": "Aug 2020",
            "end_date": "July 2021",
        },
        {
            "position": "Full Stack Web Developer",
            "company": "Wholeloops",
            "location": "Los Angeles, CA",
            "description": "Managed all front-end and back-end web development to rebuild the company’s eCommerce website from scratch.",
            "start_date": "Nov 2018",
            "end_date": "Nov 2020",
        },
    ],
    "education": [
        {
            "degree": "Associates of Computer Science",
            "university": "College of the Canyons",
            "start_date": "Aug 2016",
            "end_date": "May 2020",
        },
        {
            "degree": "Full-Stack Web Development Certification",
            "university": "UCLA",
            "start_date": "May 2018",
            "end_date": "Nov 2018",
        },
    ],
}

# Initialize Selenium driver
driver = webdriver.Chrome()

# Navigate to stillhiring.today
driver.get("https://airtable.com/embed/shrI8dno1rMGKZM8y")

# Find the specific scrollable element with class 'antiscroll-inner'
scrollable_element = driver.find_element(By.CSS_SELECTOR, ".antiscroll-inner")

# Initialize variables
company_list = []
start_time = time.time()
time.sleep(2)  # Wait for page to load

while True:
    # Scroll within the specific scrollable element
    driver.execute_script("arguments[0].scrollTop += 500;", scrollable_element)

    # Fetch company names and websites
    # Debugging Step: Print out rows
    rows = driver.find_elements(By.CSS_SELECTOR, "[data-testid='data-row']")
    print(f"Number of rows: {len(rows)}")
    # rows = driver.find_elements(By.CSS_SELECTOR, '[data-rowindex]')
    for row in rows:
        try:
            match = re.search(r"\d+\n(.+?)\nOpen", row.text)
            if match:
                company_name = match.group(1)
                print(company_name)
                company_website = row.find_element(By.XPATH, ".//a[@target='_blank']")
                company_list.append(
                    (company_name, company_website.get_attribute("href"))
                )
        except:
            pass  # Skip stale or missing elements

    # Check for element with data-rowindex="1310"
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-rowindex="1310"]'))
        )
        break  # Exit loop if found
    except:
        pass  # Continue scrolling if not found

    # Exit loop after 600 seconds as a failsafe
    if time.time() - start_time > 600:
        print("Failsafe triggered: Exiting after 600 seconds.")
        break

# Remove duplicates (if any)
company_list = list(set(company_list))

# Export to CSV
def export_to_csv(company_list, filename='company_list.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Website'])
        for company in company_list:
            writer.writerow([company])

export_to_csv(company_list)

# TODO: Add correct logic to autofill_form function
# A function to guess and fill form fields
def autofill_form(driver, application_data):
    unfilled_fields = []
    for field, value in application_data.items():
        if value is None:
            print(f"Skipping {field}, no data available.")
            continue
        guessed_elements = driver.find_elements_by_xpath(
            f"//*[contains(@name, '{field}')]"
        )
        if not guessed_elements:
            guessed_elements = driver.find_elements_by_xpath(
                f"//*[contains(@id, '{field}')]"
            )
        if not guessed_elements:
            unfilled_fields.append(field)
            print(f"Couldn't find the field {field}")
            continue
        for el in guessed_elements:
            try:
                el.clear()
                el.send_keys(value)
                print(f"Filled {field} with {value}")
            except Exception as e:
                print(f"Couldn't fill {field}, error: {e}")
    if unfilled_fields:
        print(f"Fields left unfilled: {unfilled_fields}")

# Loop through each US-based company website
for website in company_list:
    # Navigate to the company website
    print(f"Visiting {website}")
    # driver.get(website)

    # Navigate to the career page and find the application form
    # Add logic here to navigate to the career page (this part will be company-specific)

    # Call the generalized autofill function
    # autofill_form(driver, application_data)

    # Submit the form - this will vary by site
    # Add logic here to find and click the submit button

    # Add logic here to check for email confirmations (this part will also be company-specific)

print("All done. Check your emails for confirmations.")
driver.quit()
