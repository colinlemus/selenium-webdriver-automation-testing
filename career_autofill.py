from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize job titles to search for
job_titles = [
    "Software Engineer",
    "Front End Engineer",
    "Back End Engineer",
    "Full Stack Engineer",
]

# This is the data we want to use to fill out the form
application_data = {
    "first name": "Colin",
    "last name": "Lemus",
    "name": "Colin Lemus",
    "email": "colin@thelemus.com",
    "address": "Valencia CA",
    "phone": "6616456689",
    "salary": "100000",
    "current title": "Software Engineer",
    "current company org": "Moving Mountain Distribution",
    "citizenship employment eligibility": "U.S. Citizen",
    "require sponsorship": "No",
    "race ethnicity": "White",
    "veteran": "I am not a protected veteran I am not a veteran",
    "gender identity?": "Male",
    "identify as transgender?": "No",
    "disability?": "No",
    "pronoun": "He Him His He/Him/His",
    "sexual orientation?": "Straight Heterosexual Cisgender",
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
    "cover letter": [
        """Dear Hiring Manager:
          It is with great interest that I submit my resume in response to your opportunity. As an accomplished Software Engineer, I have
          superior development skills and Fortune 500 client service experience. This experience serving in a critical, hands-on, and
          high-impact role will allow me to make significant contributions to the team!
          Here are some examples of how I have developed innovative websites, applications, databases, and service enhancements
          throughout my career:
          ● Created an augmented reality application displaying SAP’s logistics for manufacturing capability.
          ● Completed a project with a ReactJS front-end application for Abbott Elementary Hulu TV Show. Created a tower to run the Unity
          application that connected to the camera and enabled a takeaway shot stored in an MP4 file for the user.
          ● Developed an application for Disney’s Spidey and His Amazing Friends leveraging the Xbox Kinect for motion control.
          ● Created a Unity tablet application for the Golden State Warriors that produced a selfie of a raised fist for the user to accessorize
          with a championship ring from a specific year.
          ● Partnered closely with CEO Russ Miller and the video team to produce quality content and cutting-edge website designs.
          ● Managed all front-end and back-end web development to rebuild the company’s eCommerce website from scratch.
          ● Consulted for Candyband to develop a virtual product personalizer for laser engravings on Apple watchbands.
          Please see my enclosed resume for a more in-depth view of my qualifications and expertise as it relates to your position
          requirements. I would love the opportunity to speak with you and learn more about your needs and expectations and how I might be
          able to help. Feel free to contact me at your earliest convenience via email, colin@thelemus.com, or cell phone, 661-645-6689, to set
          up a time to meet. Thank you for your time and consideration. I look forward to hearing from you soon.
          Sincerely, Colin Lemus"""
    ],
}

# Read the CSV
df = pd.read_csv("company_list.csv")

# Initialize WebDriver
driver = webdriver.Chrome()

# JavaScript to inject button, autofill button, and data box
js_script = f"""
console.log('Script loaded.');  // Debug line

// Function to autofill application data
function autofillData() {{
    let data = {application_data};
    let textFields = document.querySelectorAll('input[type=text], input[type=email], textarea');
    let selectFields = document.querySelectorAll('select');
    let radioFields = document.querySelectorAll('input[type=radio]');
    let checkboxFields = document.querySelectorAll('input[type=checkbox]');

    textFields.forEach(field => {{
        let attributes = [field.name, field.id, field.className, field.placeholder];
        let attributesStr = attributes.join(' ').toLowerCase();
        for (const [key, value] of Object.entries(data)) {{
          let keyWords = key.split(" ");  // Split by space for words
          let isMatch = keyWords.some(word => attributesStr.includes(word.toLowerCase()));
          if (isMatch) {{
            field.value = value;
            break;
          }}
        }};
    }});

    selectFields.forEach(field => {{
        let attributes = [field.name, field.id, field.className];
        let attributesStr = attributes.join(' ').toLowerCase();
        for (const [key, value] of Object.entries(data)) {{
          let keyWords = key.split(" ");  // Split by space for words
          let isMatch = keyWords.some(word => attributesStr.includes(word.toLowerCase()));
          if (isMatch) {{
            for (let i = 0; i < field.options.length; i++) {{
              if(value.toLowerCase().includes(field.options[i].text.toLowerCase())) {{
                field.selectedIndex = i;
                break;
              }}
            }}
          }}
        }};
    }});

    radioFields.forEach(field => {{
        let attributes = [field.name, field.id, field.className, field.value];
        let associatedLabel = document.querySelector(`label[for='${{field.id}}']`);
        if (associatedLabel) {{
            attributes.push(associatedLabel.textContent);
        }}
        let attributesStr = attributes.join(' ').toLowerCase();
        
        for (const [key, value] of Object.entries(data)) {{
          let keyWords = key.split(" ");  // Split by space for words
          let isMatch = keyWords.some(word => attributesStr.includes(word.toLowerCase()));
          if (isMatch) {{
            if (attributesStr.includes(key.toLowerCase())) {{
                if (value.toLowerCase().includes(field.value.toLowerCase())) {{
                    field.checked = true;
                    break;
                }}
            }}
          }}
        }};
    }});

    checkboxFields.forEach(field => {{
        let attributes = [field.name, field.id, field.className, field.value];
        let associatedLabel = document.querySelector(`label[for='${{field.id}}']`);
        if (associatedLabel) {{
            attributes.push(associatedLabel.textContent);
        }}
        let attributesStr = attributes.join(' ').toLowerCase();
        for (const [key, value] of Object.entries(data)) {{
          let keyWords = key.split(" ");  // Split by space for words
          let isMatch = keyWords.some(word => attributesStr.includes(word.toLowerCase()));
          if (isMatch) {{
            if (value.toLowerCase().includes(field.value.toLowerCase()) || (associatedLabel && associatedLabel.textContent.toLowerCase().includes(value.toLowerCase()))) {{
              field.checked = true;
              break;
            }}
          }}
        }};
    }});
}}

let lastFocusedElement = null;

// Track the last focused text field
document.addEventListener('focus', function(event) {{
    if (event.target.tagName.toLowerCase() === 'input' || event.target.tagName.toLowerCase() === 'textarea') {{
        lastFocusedElement = event.target;
    }}
}}, true);

// Function to insert text at cursor position
function insertAtCursor(input, textToInsert) {{
    document.execCommand('insertText', false, textToInsert);
}}

// Function to fill specific fields
function fillField(name, value) {{
    if (lastFocusedElement) {{
        insertAtCursor(lastFocusedElement, value);
    }}
}}

// Function to create a button for a specific field
function createButton(name, value) {{
    let btn = document.createElement('button');
    btn.innerHTML = name;
    btn.style.position = 'fixed';
    btn.style.top = `${{50 + 40 * buttons.length}}px`;
    btn.style.right = '10px';
    btn.style.zIndex = '10000';
    btn.onclick = function() {{ fillField(name, value); }};
    document.body.appendChild(btn);
    buttons.push(btn);
}}

let buttons = [];

// Create specific buttons
createButton('Full Name', "{application_data['name']}");
createButton('LinkedIn URL', "{application_data['linkedin']}");
createButton('GitHub URL', "{application_data['github']}");
createButton('Cover Letter', "{application_data['cover letter']}");
createButton('Salary', "{application_data['salary']}");
createButton('Current Company', "{application_data['current company org']}");

// Create Next button
let nextBtn = document.createElement('button');
nextBtn.innerHTML = 'Next';
nextBtn.style.position = 'fixed';
nextBtn.style.top = '10px';
nextBtn.style.right = '10px';
nextBtn.style.zIndex = '10000';
nextBtn.id = 'proceedButton';
document.body.appendChild(nextBtn);

// Create Autofill button
let autofillBtn = document.createElement('button');
autofillBtn.innerHTML = 'Autofill';
autofillBtn.style.position = 'fixed';
autofillBtn.style.top = '10px';
autofillBtn.style.right = '70px';
autofillBtn.style.zIndex = '10000';
autofillBtn.id = 'autofillButton';
autofillBtn.onclick = autofillData;
document.body.appendChild(autofillBtn);

// Create data box
let dataBox = document.createElement('pre');
dataBox.textContent = JSON.stringify({application_data}, null, 4);
dataBox.style.position = 'relative';
dataBox.style.top = '0px';
dataBox.style.right = '0px';
dataBox.style.zIndex = '10000';
dataBox.style.border = '1px solid black';
dataBox.style.padding = '10px';
dataBox.style.fontFamily = 'monospace';
dataBox.style.width = '100%';
//document.body.insertBefore(dataBox, document.body.firstChild);

// Add click event to Next button
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

            if (
                driver.execute_script("return localStorage.getItem('proceed');")
                == "true"
            ):
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
