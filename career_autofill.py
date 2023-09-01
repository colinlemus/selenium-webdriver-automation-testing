from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize job titles to search for
job_titles = ['Software Engineer', 'Front End Engineer', 'Back End Engineer', 'Full Stack Engineer']

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

# Read the CSV
df = pd.read_csv('company_list.csv')

# Initialize WebDriver
driver = webdriver.Chrome()

# JavaScript to inject button and data box
js_script = f"""
// Create button
let btn = document.createElement('button');
btn.innerHTML = 'Next';
btn.style.position = 'fixed';
btn.style.top = '10px';
btn.style.right = '10px';
btn.style.zIndex = '10000';
btn.id = 'proceedButton';
document.body.appendChild(btn);

// Create data box
let dataBox = document.createElement('pre');
let jsonData = {application_data};
dataBox.textContent = JSON.stringify(jsonData, null, 4);
dataBox.style.position = 'relative';
dataBox.style.top = '0px';
dataBox.style.right = '0px';
dataBox.style.zIndex = '10000';
dataBox.style.border = '1px solid black';
dataBox.style.padding = '10px';
dataBox.style.fontFamily = 'monospace';
dataBox.style.width = '100%';
document.body.insertBefore(dataBox, document.body.firstChild);

// Add click event to button
document.getElementById('proceedButton').addEventListener('click', function() {{
    localStorage.setItem('proceed', 'true');
    window.close();
}});
"""


# Loop through companies and visit career pages
for index, row in df.iterrows():
    # Use tuple unpacking to get company and URL
    company, career_url = eval(row.iloc[0])
    print(f"Visiting {company}'s career page at {career_url}")

    # Open a new tab
    driver.execute_script(f"window.open('{career_url}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(2)  # Wait for the page to load

    # Inject JavaScript
    driver.execute_script(js_script)
    current_url = driver.current_url  # Store the current URL

    # Search page for job titles
    page_text = driver.page_source.lower()
    for job in job_titles:
        if job.lower() in page_text:
            print(f"Found {job} position at {company}")

    # Wait for user to press the "Next" button or for a redirect
    while True:
        try:
            # Check for URL change (page redirect)
            if driver.current_url != current_url:
                driver.execute_script(js_script)  # Re-inject JavaScript
                current_url = driver.current_url  # Update the current URL

            if driver.execute_script("return localStorage.getItem('proceed');") == 'true':
                driver.execute_script("localStorage.setItem('proceed', 'false');")
                break
        except:
            # Handle exceptions like NoSuchWindowException
            break
        time.sleep(1)

    # Close current tab if it exists and switch back to the first tab
    if len(driver.window_handles) > 1:
        driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Inject JavaScript
    driver.execute_script(js_script)