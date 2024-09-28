from bs4 import BeautifulSoup
import requests


# Url being used to scrape
url = "https://discord.com/register"

# Send a GET request to the URL 
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    text = response.text
    print("HTML content:")
    print(text)
else:
    print("Failed to retrieve HTML:", response.status_code)

soup = BeautifulSoup(text, 'html.parser')

print("\nLinks found:")
for link in soup.find_all('a'):
    print(link.get('href'))