from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#executable path for chromedriver
#driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

options = Options()
options.add_argument("--headless")
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# Replace 'your_email' and 'your_password' with your outlook credentials.
driver = webdriver.Chrome()
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=16&ct=1699615128&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fnlp%3d1%26state%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC9pbmJveC8%26RpsCsrfState%3d0153df72-2fce-a28e-a1fc-32c0ace43678&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
time.sleep(2)  # Wait for the page to load


email_input = driver.find_element(By.CSS_SELECTOR, 'input#i0116')
email_input.send_keys("chaitu579@live.com")	

# Press the "Enter" key to proceed to the next step
email_input.send_keys(Keys.RETURN)

# Alternatively, you can locate the "Next" button by its class name and click it
# next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-RLmnJb")
# next_button.click()

time.sleep(5)
password_input = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password_input.send_keys("143225143")

# Press the "Enter" key to proceed to the next step
password_input.send_keys(Keys.RETURN)

# Find and click the "Next" button
#next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
#next_button.click()

#as i have set-up verification for mobile "2-step verification" so wait for the apporval msg on phone
time.sleep(10)

# Wait for the "Promotions" tab to load (you may need to use WebDriverWait)
# Find the "Promotions" tab by its attributes and click it
promotions_tab = driver.find_element(By.ID, ":1w")
promotions_tab.click()

# Loop to select and delete emails until the count is zero
while True:
    # Find and click the checkbox element
    checkbox = driver.find_element(By.XPATH, '//span[@aria-checked="false"]')
    checkbox.click()

    # Find and click the "Delete" button
    delete_button = driver.find_element(By.CLASS_NAME, "T-I-J3")
    delete_button.click()

    # Wait for the "undo" element to disappear
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, ":6t")))
    time.sleep(5)
    
    # Check the count of emails
    count_element = driver.find_element(By.CLASS_NAME, "ts")
    count = int(count_element.text.replace(",", ""))  # Remove commas from the count

    if count == 0:
        break

driver.quit()


