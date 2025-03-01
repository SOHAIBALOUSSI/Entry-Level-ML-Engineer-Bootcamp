from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the URL
response = requests.get("https://data.1337ai.org/")
parsed = BeautifulSoup(response.content, 'html5lib')

data = parsed.find_all('tr')

head = parsed.find_all('th')
csvContent = []

for col in head:
    headData = [col.text.strip() for col in head]
    csvContent = ','.join(headData)

for tr in data:
    tds = tr.find_all('td')    
    row_data = [td.text.strip() for td in tds]
    csvContent += ','.join(row_data)
    csvContent += '\n'
with open("data.csv", 'w') as csvfile:
    csvfile.write(csvContent)
# print(csvContent)