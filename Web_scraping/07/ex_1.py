from selenium import webdriver
import time
import getpass

gecko_path = 'C:/geckodriver/geckodriver.exe'

url = 'http://campuswire.com/signin'

options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox(options = options, executable_path = gecko_path)

# Actual program:
driver.get(url)
print(driver.page_source)

time.sleep(2)

#Get login to Campuswire
username = driver.find_element_by_xpath('//input[@placeholder="Email"]')
my_email = input('Please provide your email:')
username.send_keys(my_email)
time.sleep(5)

password = driver.find_element_by_xpath('//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your password:')
password.send_keys(my_pass)
time.sleep(5)

button = driver.find_element_by_xpath('//button[@type="submit"]')
button.click()

time.sleep(2)
print(driver.page_source)


dms = driver.find_element_by_xpath('/html/body/div[1]/div/aside[1]/div[1]/div[1]/ul/li[2]/button')
dms.click()

time.sleep(2)
print(driver.page_source)

tutorname = driver.find_element_by_xpath('//input[@placeholder="Search in people, classes and groups"]')
tutor = input("Search in people")
tutorname.send_keys(tutor)

time.sleep(5)
print(driver.page_source)

filtername = driver.find_element_by_xpath("html/body/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]")
filtername.click()

time.sleep(2)
print(driver.page_source)

#Send .py files
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('Hi there')
time.sleep(2)
print(driver.page_source)

time.sleep(5)

#Close browser:
driver.quit()
