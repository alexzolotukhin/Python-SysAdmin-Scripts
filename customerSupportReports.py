from selenium import webdriver
import time
from datetime import date
import requests
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path="C:/Users/Alexander Zolotukhin/Desktop/chromedriver.exe")

driver.maximize_window()

driver.get("https://var-bc.broadcloudpbx.com/rep")

time.sleep(5)

login_page_drop_down = driver.find_element_by_xpath('//*[@id="dropdownLoginBtn"]').click()

time.sleep(2)

login_page_webexid = driver.find_element_by_xpath('//*[@id="cisco"]').click()

login_page_email = driver.find_element_by_xpath('//*[@id="textEmailAddress"]').send_keys("azolotukhin@340basics.com")

login_page_submit = driver.find_element_by_xpath('//*[@id="signInBtn"]').click()

time.sleep(2)

login_page_pwd = driver.find_element_by_xpath('//*[@id="IDToken2"]').send_keys("977Password!977")

login_page_pwd2 = driver.find_element_by_xpath('//*[@id="Button1"]').click()

time.sleep(12)

reports = driver.find_element_by_xpath('//*[@id="reportsLink"]').click()

time.sleep(2)

drop_down = driver.find_element_by_xpath('//*[@id="reportsTypeSelection"]')
drop_down.click()
q_status = driver.find_element_by_xpath('//*[@id="reportsTypeSelection"]/option[2]')
q_status.click()
location = driver.find_element_by_xpath('//*[@id="reportsSiteSelectorDiv"]/div/button')
location.click()
nj = driver.find_element_by_xpath('//*[@id="reportsSiteSelectorDiv"]/div/div/ul/li[2]/a/span[1]')
nj.click()
time.sleep(2)
call_queue = driver.find_element_by_xpath('//*[@id="reportsAutoAttendantsSelectorDiv"]/div/button')
call_queue.click()
time.sleep(2)
call_queue1 = driver.find_element_by_xpath('//*[@id="reportsAutoAttendantsSelectorDiv"]/div/div/ul/li[2]/a')
call_queue1.click()

runButton = driver.find_element_by_xpath('//*[@id="reportsSearchButton"]').click()
time.sleep(6)

exportButton = driver.find_element_by_xpath('//*[@id="export"]').click()
