import requests 
from datetime import datetime 
import time 

#inputs [dane które możesz samodzielnie wpisać]
ticker = input("Enter the ticker symbol: ")
from_date = input("Enter the start date in YYYY-MM-DD format: ")
to_date = input("Enter the end date in YYYY-MM-DD format: ")

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = time.mktime(from_datetime.timetuple())
to_epoch = time.mktime(to_datetime.timetuple())

url = f"yahoo here"
headers = "webpack here"

