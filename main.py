import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

# Load environment variables
load_dotenv()

# Read LinkedIn credentials from environment variables
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Setup web driver
options = Options()
# options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
# Wait for the login process to complete
browser.implicitly_wait(10)  # Adjust the wait time as needed

# Open LinkedIn login page
def login(browser, username, password):
    browser.get("https://www.linkedin.com/login")
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[1]/input').send_keys(username)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[2]/input').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "#sso_login-landing > form > button").click()
    print("Logged in")


# Login function
login(browser, username, password)



# Perform any other actions you need on LinkedIn after logging in

# Close the browser
browser.quit()
