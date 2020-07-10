import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromSender = "it@340basics.com"
toaddr = "azolotukhin@340basics.com", "aminano@340basics.com", "jmandracchia@340basics.com"
toRecipient = "azolotukhin@340basics.com"
msg = MIMEMultipart()
msg['From'] = fromSender
msg['To'] = "azolotukhin@340basics.com"
    #; "aminano@340basics.com"; "jmandracchia@340basics.com"
msg['Subject'] = "SFDC backups were executed successfully."
body = "Please, see the export files in G:\My Drive\IT & Communication (Managed by Tracy)\Salesforce Export Files\SFDC_MMDDYYYY"
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromSender, "161GaitherDr!")
text = msg.as_string()
s.sendmail(fromSender, toRecipient, text)
s.quit()