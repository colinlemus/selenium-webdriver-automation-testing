from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

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

print("All done. Check your emails for confirmations.")
driver.quit()
