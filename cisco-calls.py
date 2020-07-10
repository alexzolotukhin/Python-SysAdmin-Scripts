from selenium import webdriver
import time
from datetime import date
import requests
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path="C:/Users/Alexander Zolotukhin/Desktop/chromedriver.exe")

driver.maximize_window()

driver.get("https://var-bc.broadcloudpbx.com/rep")

time.sleep(3)

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

for i in range(43200):

    run_button = driver.find_element_by_xpath('//*[@id="reportsSearchButton"]').click()
    time.sleep(3)
    abandoned = driver.find_element_by_xpath('//*[@id="table_container"]/div/table/tbody/tr/td[5]')
    answered = driver.find_element_by_xpath('//*[@id="table_container"]/div/table/tbody/tr/td[8]')
    wait_time = driver.find_element_by_xpath('//*[@id="table_container"]/div/table/tbody/tr/td[7]')
    print(abandoned.text, answered.text, wait_time.text)
#fact
    page = requests.get('https://www.factmonster.com/dayinhistory')
    page = page.text
    soup = BeautifulSoup(page, 'lxml')

    for x in range(6):
        year = soup.find_all('h3')[x].text
        data = soup.find_all('p')[x].text
        fact = "On this day, in" + year + "," + data
        print(fact)

#html parsing
    today = date.today()
    f = open('sample.html', 'w')
    message = """<html>
    <head><meta http-equiv="refresh" content="60"></head>
    <h1 style="color: #5e9ca0;">&nbsp;</h1>
    <h1 style="color: #5e9ca0; text-align: center;"><span style="color: #99cc00;">340</span><span style="color: #000080;">Basics</span> - CSR calls for """ + str(today) + """</h1>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <table style="height: 90px; width: 696px; margin-left: auto; margin-right: auto;">
    <tbody>
    <tr style="height: 109px;">
    <td style="width: 192px; text-align: center; height: 109px;">
    <h1>Answered</h1>
    </td>
    <td style="width: 192px; text-align: center; height: 109px;">
    <h1>Abandoned</h1>
    </td>
    <td style="width: 290px; text-align: center; height: 109px;">
    <h1>&nbsp;Avg. wait time (min)</h1>
    </td>
    </tr>
    <tr style="height: 96.5px;">
    <td style="width: 192px; text-align: center; height: 96.5px;">
    <h1>""" + str(answered.text) + """</h1>
    </td>
    <td style="width: 192px; text-align: center; height: 96.5px;">
    <h1>""" + str(abandoned.text) + """</h1>
    </td>
    <td style="width: 290px; text-align: center; height: 96.5px;">
    <h1>""" + str(wait_time.text) + """</h1>
    </td>
    </tr>
    </tbody>
    </table>
    <body><h1>""" + fact + """"</h1></body>
    <p>&nbsp;</p>
    </html>"""
    f.write(message)
    f.close()
    f = open("sample.html", "r")
    print(f.read())
    time.sleep(60)

