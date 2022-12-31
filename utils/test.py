from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'}
)

# Open google.com
driver.get('http://google.com')

# Find the search box
search_box = driver.find_element_by_name('q')

# Type in the search
search_box.send_keys('ChromeDriver')

# Submit the form (although google automatically searches now without submitting)
search_box.submit()

# Check the title
assert 'ChromeDriver' in driver.title

# Close the browser

driver.close()



driver.quit()
