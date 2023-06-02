from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os

# BrowserStack Credentials
userName = os.environ.get('BROWSERSTACK_USERNAME')
accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
buildName = os.environ.get('JENKINS_LABEL')

# Set up for the desired capabilities for each browser
caps = [
    {
      browserName: 'Chrome',
      'bstack:options': {
        browserVersion: 'latest',
        os: 'Windows',
        osVersion: '10'
      }
    },
    {
      browserName: 'Firefox',
      'bstack:options': {
        browserVersion: 'latest',
        os: 'OS X',
        osVersion: 'Ventura'
      }
    },
    {
      browserName: 'samsung',
      'bstack:options': {
        deviceOrientation: 'portrait',
        deviceName: 'Samsung Galaxy S22',
        osVersion: '12.0'
      }
    }
  ]

# BrowserStack Trial credentials
bs_email = os.getenv('BS_USR')  # BrowserStack email from Jenkinsfile
bs_password = os.getenv('BS_PW')  # BrowerStack password from JenkinsFile

def tech_challenge(browser):
    # Set up the WebDriver with the desired capabilities
    driver = webdriver.Remote(
        "http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", caps)

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

    # Close the browser
    driver.quit()

