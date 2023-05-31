from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

dates = csv.reader(open("3.csv", "r"))

for date in dates:
    print(date)

