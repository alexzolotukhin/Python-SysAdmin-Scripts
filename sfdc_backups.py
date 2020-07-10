from datetime import datetime
import os
import shutil
from selenium import webdriver
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#driver - chrome
driver = webdriver.Chrome(executable_path="C:/Users/Alexander Zolotukhin/Desktop/chromedriver.exe")
driver.maximize_window()

#UI interface
# driver.get("https://340basics.my.salesforce.com/")
driver.get("https://340basics.my.salesforce.com/ui/setup/export/DataExportPage/d?setupid=DataManagementExport&retURL=%2Fui%2Fsetup%2FSetup%3Fsetupid%3DDataManagement")
time.sleep(1)
username = driver.find_element_by_xpath('//*[@id="username"]').send_keys("azolotukhin@340basics.com")
pwd = driver.find_element_by_xpath('//*[@id="password"]').send_keys("161GaitherDr!")
submit_button = driver.find_element_by_xpath('//*[@id="Login"]').click()
time.sleep(6)

###

# settings = driver.find_element_by_xpath('//*[@id="66:223;a"]/div/div/a').click()
# time.sleep(2)
# manage = driver.find_element_by_xpath('//*[@id="setup"]/path').click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[-1])
# close_pop_up = driver.find_element_by_xpath('//*[@id="tryLexDialogX"]').click()
# setup = driver.find_element_by_xpath('//*[@id="setupLink"]').click()
# time.sleep(2)
# data_management = driver.find_element_by_xpath('//*[@id="DataManagement_font"]').click()
# data_export = driver.find_element_by_xpath('//*[@id="DataManagementExport_font"]').click()
# time.sleep(2)


for i in range(2, 99):
    try:
        i = str(i)
        back_up = driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr/td[2]/div[5]/div[1]/div/div[2]/table/tbody/tr[' + i + ']/td[1]/a').click()
        time.sleep(100)
    except:
        pass



#create directory
today = datetime.now()
dir = "G:/My Drive/IT & Communication (Managed by Tracy)/Salesforce Export Files/SFDC" + "_" + today.strftime('%m%d%Y')
os.mkdir(dir)

#copyingfiles
src = "C:/Users/Alexander Zolotukhin/Downloads"
files = os.listdir(src)
print(dir)

for file in files:
    if file.endswith(".ZIP"):
        print(file)
        shutil.move(src + "/" + file, dir + "/")

#email
fromaddr = "it@340basics.com"
toaddr = "azolotukhin@340basics.com", "aminano@340basics.com", "jmandracchia@340basics.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = "azolotukhin@340basics.com"; "aminano@340basics.com"; "jmandracchia@340basics.com"
msg['Subject'] = "SFDC backups were executed successfully."
body = "Please, see the export files in G:\My Drive\IT & Communication (Managed by Tracy)\Salesforce Export Files\SFDC_MMDDYYYY"
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "161GaitherDr!")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()