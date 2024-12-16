from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys  # Import Keys
from selenium.webdriver.common.action_chains import ActionChains




chromedriver_autoinstaller.install()


chrome_options = Options()
chrome_options.add_argument('--disable-http2')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")


driver = webdriver.Chrome(options=chrome_options)


driver.maximize_window()


driver.get("https://www.goindigo.in")
print("Navigated to the website.")


try:
    banner_close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "flight-close"))
    )
    banner_close_button.click()
    print("Banner closed successfully.")
except Exception as e:
    print(f"Error while closing the banner: {e}")


try:
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='tab' and contains(text(), 'Book')]"))
    )
    dropdown.click()
    print("Dropdown clicked successfully.")
except Exception as e:
    print(f"Error while clicking the dropdown: {e}")


try:
    flight_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/flight-booking.html?linkNav=Flight%7CBook%7CBook']"))
    )
    flight_option.click()
    print("Flight option clicked successfully.")
except Exception as e:
    print(f"Error while clicking the flight option: {e}")


time.sleep(5)
print("Waited for 10 seconds after clicking the flight option.")
print('moving to the next step')


from_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='From']"))
)

from_input.clear()
driver.execute_script("arguments[0].value = '';", from_input)  # Force clear using JavaScript
from_input.send_keys("Hyderabad")  # Enter 'Hyderabad'
print("Cleared the 'From' field and entered 'Hyderabad'.")


# first_option = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.XPATH, "(//div[@class='destination-row'])[1]"))
# )
# first_option.click()
# print("Selected the first option from the dropdown.")
from_input.send_keys(Keys.TAB)  # Press Tab once
time.sleep(0.5)  # Optional delay to ensure the dropdown updates
from_input.send_keys(Keys.TAB)  # Press Tab again

from_input.send_keys(Keys.ENTER)  # Press Enter

to_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='To']"))
)
driver.execute_script("arguments[0].value = '';", to_input)  # Force clear using JavaScript
to_input.send_keys("Delhi")  # Enter 'Delhi'
print("Cleared the 'To' field and entered 'Delhi'.")


# to_input.send_keys(Keys.TAB)  # Press Tab once
# time.sleep(1)
# to_input.send_keys(Keys.TAB)  # Press Tab once

# to_input.send_keys(Keys.ENTER)  # Press Tab again

try:
    to_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='destination-row']//div[contains(text(), 'Delhi, IN')]"))
    )
    
    driver.execute_script("arguments[0].scrollIntoView();", to_dropdown)
    
    to_dropdown.click()
    to_input.send_keys(Keys.ALT)  
    print("Selected 'Delhi' from the dropdown.")
except Exception as e:  
    print("Error while exectuing the dropdown: ", e)



try:
    travel_dates_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Travel Dates']"))
    )
    travel_dates_input.click()
    print("Opened the calendar for Travel Dates.")
except Exception as e:
    print(f"Error while opening the calendar: {e}")

datepicker_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__navigation--next"))  
)
datepicker_button.click()


current_month = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__current-month").text
while current_month != "December 2024":
    next_button = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__navigation--next")
    next_button.click()
    current_month = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__current-month").text


day_to_select = 12
day_element = driver.find_element(By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day_to_select}']")
day_element.click()

#***********Now Selecting the Pax************

pax_dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '1 Pax')]"))
)
pax_dropdown_button.click()


adults_plus_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".stepper-input__btn--plus"))
)
adults_plus_button.click()


adults_count_input = driver.find_element(By.CSS_SELECTOR, ".stepper-input__input")
updated_count = adults_count_input.get_attribute("value")
print(f"Updated Adult(s) count: {updated_count}")

done_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Done')]"))
)
done_button.click()

time.sleep(3)


search_flight_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Search Flight']]"))
)

time.sleep(1)
search_flight_button.click()


select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//button[contains(@aria-label, 'Select Best Value Flight')])[1]"))
)
select_button.click()


next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
)
next_button.click()

time.sleep(8)

# male_radio_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='Male' and @type='radio']"))
# )

male_radio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "Male"))
)

print("clicked male radio button")
time.sleep(10)
male_radio_button.click()

# male_radio_button.click()
first_name_input = driver.find_element(By.XPATH, "//input[@name='userFields.0.name.first']")

first_name_input.clear()  
first_name_input.send_keys("Testing Name")

last_name_input = driver.find_element(By.XPATH, "//input[@name='userFields.0.name.last']")

last_name_input.clear()  
last_name_input.send_keys("Testing Last Name")


adult_2_section = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'accordion-title') and text()='Adult 2']"))
)

driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", adult_2_section)
time.sleep(1)  

adult_2_section.click()

# male_radio_button_passenger_2 = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='Male' and @name='userFields.1.gender']"))
# )
# male_radio_button_passenger_2.click()
second_male_radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="userFields.1.gender"]'))
    )

print("clicked male radio button2")
time.sleep(10)
second_male_radio_button.click()

first_name_input1 = driver.find_element(By.XPATH, "//input[@name='userFields.1.name.first']")

first_name_input1.clear()  
first_name_input1.send_keys("Testing second Passenger Name")

last_name_input1 = driver.find_element(By.XPATH, "//input[@name='userFields.1.name.last']")

last_name_input1.clear() 
last_name_input1.send_keys("Second passenger Last Name")


time.sleep(100)
driver.quit()
print("Browser closed.")