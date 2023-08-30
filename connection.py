from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")  # Replace with actual URL

# Test Text Input
def test_text_input():
    print("Testing Text Input...")
    text_input = driver.find_element(By.NAME, "my-text")
    text_input.send_keys("Sample Text")
    assert text_input.get_attribute('value') == "Sample Text"
    print("Text Input Test Passed.")

# Test Password Input
def test_password_input():
    print("Testing Password Input...")
    password_input = driver.find_element(By.NAME, "my-password")
    password_input.send_keys("password123")
    assert password_input.get_attribute('value') == "password123"
    print("Password Input Test Passed.")

# Test Textarea
def test_text_area():
    print("Testing Text Area...")
    text_area = driver.find_element(By.NAME, "my-textarea")
    text_area.send_keys("This is a sample text area.")
    assert text_area.get_attribute('value') == "This is a sample text area."
    print("Text Area Test Passed.")

# Test Dropdown (select)
def test_dropdown_select():
    print("Testing Dropdown (Select)...")
    dropdown_select = Select(driver.find_element(By.NAME, "my-select"))
    dropdown_select.select_by_value("1")
    assert dropdown_select.first_selected_option.get_attribute('value') == "1"
    print("Dropdown (Select) Test Passed.")

# Test Dropdown (datalist)
def test_dropdown_datalist():
    print("Testing Dropdown (Datalist)...")
    dropdown_datalist = driver.find_element(By.NAME, "my-datalist")
    dropdown_datalist.send_keys("San Francisco")
    assert dropdown_datalist.get_attribute('value') == "San Francisco"
    print("Dropdown (Datalist) Test Passed.")

# Test File Input
def test_file_input():
    print("Testing File Input...")
    # file_input = driver.find_element(By.NAME, "my-file")
    # Simulating file upload is dependent on your local files
    # file_input.send_keys("/path/to/file")
    # assert file_input.get_attribute('value') == "/path/to/file"
    print("File Input Test Skipped.")

# Test Checkbox
def test_checkbox():
    print("Testing Checkbox...")
    checkbox = driver.find_element(By.ID, "my-check-1")
    checkbox.click()
    assert not checkbox.is_selected()
    print("Checkbox Test Passed.")

# Test Radio Button
def test_radio_button():
    print("Testing Radio Button...")
    radio_button = driver.find_element(By.ID, "my-radio-2")
    radio_button.click()
    assert radio_button.is_selected()
    print("Radio Button Test Passed.")

# Test Date Picker
def test_date_picker():
    print("Testing Date Picker...")
    date_picker = driver.find_element(By.NAME, "my-date")
    date_picker.send_keys("2022-12-31")
    assert date_picker.get_attribute('value') == "2022-12-31"
    print("Date Picker Test Passed.")

# Test Range Input
def test_range_input():
    print("Testing Range Input...")
    range_input = driver.find_element(By.NAME, "my-range")
    range_input.send_keys("5")
    assert range_input.get_attribute('value') == "5"
    print("Range Input Test Passed.")

# Run Tests
print("Starting Tests...")
test_text_input()
test_password_input()
test_text_area()
test_dropdown_select()
test_dropdown_datalist()
# test_file_input()  # Uncomment when you have a file to upload
test_checkbox()
test_radio_button()
test_date_picker()
test_range_input()

# Close the driver
print("All Tests Completed.")
driver.quit()