from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = 'https://forecast.weather.gov/MapClick.php?lat=34.02990790000007&lon=-118.51033309999997#.X1qEvpNKg8M'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

items[0].find(class_='period-name').get_text()
items[0].find(class_='short-desc').get_text()
items[0].find(class_='temp').get_text()

period_names = [item.find(class_='period-name').get_text() for item in items]
desc = [item.find(class_='short-desc').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame({
    'period': period_names,
    'desc': desc,
    'temperatures': temps
})

print(weather_stuff)

weather_stuff.to_csv('result.csv')
