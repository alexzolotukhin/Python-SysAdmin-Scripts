from selenium import webdriver
import time
import emailutils


#driver - chrome
driver = webdriver.Chrome(executable_path="C:/Users/Alexander Zolotukhin/Desktop/chromedriver.exe")
driver.maximize_window()

#UI interface
driver.get("http://10.2.40.130/")
time.sleep(1)
username = driver.find_element_by_xpath('/html/body/form/div/div/div/div/div[2]/div/div/fieldset/div[1]/input')
username.send_keys("azolotukhin")
pwd = driver.find_element_by_xpath('/html/body/form/div/div/div/div/div[2]/div/div/fieldset/div[2]/input')
pwd.send_keys("Leeandricoand123")
login = driver.find_element_by_xpath('/html/body/form/div/div/div/div/div[3]/button').click()
time.sleep(1)
menu = driver.find_element_by_xpath('/html/body/div[1]/header/nav/a').click()
time.sleep(1)
reports = driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[10]/a').click()
time.sleep(1)
asset_report = driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[10]/ul/li[8]/a').click()
time.sleep(1)
checkoff = driver.find_element_by_xpath('//*[@id="webui"]/div/div/form/div/div[2]/div[1]/div[1]/label/div/ins').click()
time.sleep(1)

limit = [3, 4, 5, 6, 7, 16, 18]
for i in limit:
    i = str(i)
    checkmark = driver.find_element_by_xpath('//*[@id="webui"]/div/div/form/div/div[2]/div[1]/div[' + i + ']/label/div/ins').click()
time.sleep(1)
generate = driver.find_element_by_xpath('//*[@id="webui"]/div/div/form/div/div[3]/button').click()

# df = pd.read_excel (r"C:/Users/Alexander Zolotukhin/Downloads/custom-assets-report-2020-04-24-024141.csv")
# print (df)


