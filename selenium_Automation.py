from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# exceptions
from selenium.common.exceptions import NoSuchElementException
import time, os, sys, logging, json
# dotenv
from dotenv import load_dotenv
import config

# load env
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)
xpaths = os.environ.get('xpaths')
# convert xpaths to dict
xpaths = json.loads(xpaths)

# Get Xpaths from config.py function
# xpaths = config.get_xpaths()
# print(xpaths)

# Create a new instance of the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=options)

driver.get("https://localhost:8834/#/")

# wait for page to load
time.sleep(5)
# log status p


# login to page
def login():
    # find the username field BY XPATH
    username = driver.find_element(By.XPATH, xpaths['username'])
    # find the password field BY XPATH
    password = driver.find_element(By.XPATH, xpaths['password'])
    # find the login button BY XPATH
    login_button = driver.find_element(By.XPATH, xpaths['login_button'])
    # enter username
    username.send_keys('kali')
    # enter password
    password.send_keys('kali')
    # click login button
    login_button.click()
    # wait for page to load
    time.sleep(10)
    # Until XPATH is found, keep trying to find it
    while True:
        try:
            # find the trigger folder BY XPATH
            trigger_folder = driver.find_element(By.XPATH, xpaths['trigger_folder'])
            # click the trigger folder
            trigger_folder.click()
            break
        except NoSuchElementException:
            print('Trigger Folder not found, trying again')
            continue
    # find the new scan button BY XPATH
    while True:
        try:
            # find the new scan button BY XPATH
            new_scan = driver.find_element(By.CSS_SELECTOR, xpaths['new_scan'])
            new_scan.click()
            print('New Scan Clicked')
            break
        except NoSuchElementException:
            print('New Scan button not found, trying again')
            time.sleep(5)
            continue
    # wait for page to load
    # Click the "Scan Type" 
    while True:
        try:
            host_discovery = driver.find_element(By.CSS_SELECTOR, xpaths['host_discovery'])
            host_discovery.click()
            print('Host Discovery Clicked')
            break
        except NoSuchElementException:
            print('Scan Type not found, trying again')
    # wait for page to load
    time.sleep(5)
    # fill out the form
    # find the name field BY XPATH
    name = driver.find_element(By.XPATH, xpaths['name'])
    # find the description field BY XPATH
    description = driver.find_element(By.XPATH, xpaths['description'])
    # target field
    target = driver.find_element(By.XPATH, '/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[5]/div/textarea')
    # Fill out the name field
    name.send_keys('Test Scan')
    # Fill out the description field
    description.send_keys('This is a test scan')
    # Fill out the target field
    target.send_keys('127.0.0.1')
    
    # click dropdown menu
    dropdown = driver.find_element(By.XPATH, '/html/body/section[3]/section[3]/section/form/div[2]/i')
    dropdown.click()
    # click the "Save and Launch" button
    save_and_launch = driver.find_element(
        By.XPATH, '/html/body/section[3]/section[3]/section/form/div[2]/ul/li')
    
    save_and_launch.click()
login()
