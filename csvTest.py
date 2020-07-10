import csv
import pandas

with open('C:\\Users\\Alexander Zolotukhin\Desktop\\PyCharm\\test.csv', newline='') as f:
    reader = csv.reader(f)
    for lines in reader:
        print(lines["Calls Abandoned"])


