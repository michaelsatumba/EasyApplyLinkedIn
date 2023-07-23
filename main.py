import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Load environment variables
load_dotenv()

# Read LinkedIn credentials from environment variables
username = os.getenv("NAME")
password = os.getenv("PASSWORD")
# print(username, password)
# change the job title to whatever you want to search for
job_title = "Software Engineer"

# Setup web driver
options = Options()
# options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
# Wait for the login process to complete
browser.implicitly_wait(10)  # Adjust the wait time as needed

# Open LinkedIn login page
def login(browser, username, password):
    browser.get("https://www.linkedin.com/login")
    browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys(username)
    browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys(password)
    browser.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
    print("Logged in")

def click_on_jobs_tab(browser):
    browser.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]/a/span").click()
    print("Clicked on jobs tab")
    # time.sleep(5)
    
def click_on_search_bar(browser):
    browser.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]/a").click()
    print("Clicked on search bar")
    # time.sleep(5)
    
def search_for_job(browser, job_title):
    search_box = browser.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
    search_box.send_keys(job_title)
    search_box.send_keys(Keys.ENTER)
    # time.sleep(5)
    
    
    
# Login function
login(browser, username, password)
click_on_jobs_tab(browser)
click_on_search_bar(browser)
search_for_job(browser, job_title)


# Close the browser
browser.quit()
