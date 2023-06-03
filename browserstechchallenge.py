from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from browserstack.local import Local
from threading import Thread
import time
import json
import os

# Environment Variables
userName = os.environ.get('BROWSERSTACK_USERNAME')
accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
URL = "https://hub.browserstack.com/wd/hub" 
buildName = os.environ.get('JENKINS_LABEL')

# BrowserStack Trial credentials
bs_email = os.getenv('BS_USR')  # BrowserStack email from Jenkinsfile
bs_password = os.getenv('BS_PW')  # BrowerStack password from JenkinsFile

# Set up capabilities for each browser
browsers = [
    {
        "os": "OS X",
        "osVersion": "Ventura",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack parallel python",
        "browserName": "firefox",
        "browserVersion": "latest"
    },
    {
        "os": "Windows",
        "osVersion": "10",
        "buildName": "browserstack-tech-challenge",
        "sessionName": "BStack parallel python",
        "browserName": "chrome",
        "browserVersion": "latest"
    },
    {
        "osVersion": "12.1",
        "deviceName": "Samsung Galaxy S22",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack parallel python",
        "browserName": "samsung",
    },
]

# Creates an instance of Local
bs_local = Local()
  
# You can also use the environment variable - "BROWSERSTACK_ACCESS_KEY".
bs_local_args = { "key": "BROWSERSTACK_ACCESS_KEY" }
  
# Starts the Local instance with the required arguments
bs_local.start(**bs_local_args)
  
# Check if BrowserStack local instance is running
print(bs_local.isRunning())
  
# Your test code goes here, from creating the driver instance till the end.

# Function switch for desired browser
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())

# Run function for test
def tech_challenge(browser):
    # Set up the WebDriver with the desired capabilities
    bstack_options = {
        "osVersion": browser["osVersion"],
        "buildName": browser["buildName"],
        "sessionName": browser["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY,
        "local": "true"
    }
    if "os" in browser:
        bstack_options["os"] = browser["os"]
    if "deviceName" in browser:
        bstack_options['deviceName'] = browser["deviceName"]
    bstack_options["source"] = "python:tech-challenge:v1.1"
    if browser['browserName'] in ['ios']:
        browser['browserName'] = 'safari'
    options = get_browser_option(browser["browserName"].lower())
    if "browserVersion" in browser:
        options.browser_version = browser["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    if browser['browserName'].lower() == 'samsung':
        options.set_capability('browserName', 'samsung')
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
  
    try:
        # 1. Go to homepage and login to account
        driver.get("https://www.browserstack.com/")
        time.sleep(3)  # Wait for the page to load

        # Login using your trial credentials
        user_input = driver.find_element_by_id("user_email_login")
        user_input.send_keys(bs_email)
        pass_input = driver.find_element_by_id("user_password")
        pass_input.send_keys(bs_password)
        pass_input.send_keys(Keys.RETURN)

        # 2. Make sure that the homepage includes a link to invite users and retrieve the link’s URL


        # 3. Log out of BrowserStack
        user_account = driver.find_element_by_class_name("account-dropdown-toggle")
        user_account.click()
        time.sleep(1)  # Wait for the dropdown menu to open
        logout_button = driver.find_element_by_link_text("Logout")
        logout_button.click()
    
    except NoSuchElementException as err:
        message = "Exception: " + str(err.__class__) + str(err.msg)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
    except Exception as err:
        message = "Exception: " + str(err.__class__) + str(err.msg)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

    # Close the browser
    driver.quit()
    
    for browser in browsers:
        Thread(target=tech_challenge, args=(browser,)).start()
        
# Stop the Local instance after your test run is completed. 
bs_local.stop()





