from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# exceptions
from selenium.common.exceptions import NoSuchElementException
import time, os, sys, logging, json
# dotenv
from dotenv import load_dotenv
from config.config import get_xpaths
import httpx

xpaths = get_xpaths()

# load env
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)
headers = os.environ.get('headers')
# convert headers to dict
headers = json.loads(headers)
baseurl = os.environ.get('base_url')

# Create a new instance of the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)
driver.get("https://localhost:8834/#/")

time.sleep(5)

# login to page
def host_enumeration(ip):
    try:
        username = driver.find_element(By.XPATH, xpaths['username'])
        password = driver.find_element(By.XPATH, xpaths['password'])
        login_button = driver.find_element(By.XPATH, xpaths['login_button'])
        username.send_keys('kali')
        password.send_keys('kali')
        login_button.click()
        time.sleep(3)
        while True:
            try:
                trigger_folder = driver.find_element(By.XPATH, xpaths['trigger_folder'])
                print('Trigger Folder Found')
                trigger_folder.click()
                time.sleep(3)
                break
            except NoSuchElementException:
                print('Still loading...')
                time.sleep(3)
                continue
        while True:
            try:
                new_scan = driver.find_element(By.CSS_SELECTOR, xpaths['new_scan'])
                new_scan.click()
                print('New Scan Clicked')
                break
            except NoSuchElementException:
                print('New Scan button not found, trying again...')
                time.sleep(5)
                continue
        while True:
            try:
                host_discovery = driver.find_element(By.CSS_SELECTOR, xpaths['host_discovery'])
                host_discovery.click()
                print('Host Discovery Clicked')
                time.sleep(5)
                break
            except NoSuchElementException:
                print('Scan Type not found, trying again...')
                time.sleep(5)
                continue

        while True:
            try:
                name = driver.find_element(By.CSS_SELECTOR, xpaths['name'])
                description = driver.find_element(By.CSS_SELECTOR, xpaths['description'])
                target = driver.find_element(By.CSS_SELECTOR, xpaths['target'])
                scan_name = 'Test_Scan'
                name.send_keys(f'{scan_name}')
                description.send_keys('This is a test scan')
                target.send_keys(ip)
                dropdown = driver.find_element(By.XPATH, '/html/body/section[3]/section[3]/section/form/div[2]/i')
                time.sleep(20)
                dropdown.click()
                save_and_launch = driver.find_element(
                    By.XPATH, '/html/body/section[3]/section[3]/section/form/div[2]/ul/li')
                save_and_launch.click()
                print('Successfully saved and launched scan')
            except NoSuchElementException:
                print('Scan not Launched, trying again...')
                time.sleep(5)
                continue
            # Check scan status via API using httpx
            scans = httpx.get('https://localhost:8834/scans/', headers=headers, verify=False, timeout=60)
            # scans dict 
            print(json.dumps(scans.json()))
            # driver quit
            time.sleep(5)
            driver.quit()
    except Exception:
        # suppress errors
        driver.quit()

host_enumeration('127.0.0.1')
