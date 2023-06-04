from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

dates = csv.reader(open("./3.csv", "r"))
print(dates)
for date in dates:
    time.sleep(1)
    print(date)


