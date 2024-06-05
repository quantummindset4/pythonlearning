import requests
from bs4 import BeautifulSoup

url = "https://www.quantummindset.click/linuxcommands.html"

# Fetch the HTML content from the URL
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract content within all <a> tags with class "content-title"
content_list = [tag.get_text(strip=True) for tag in soup.find_all('a', class_='content-title')]

# Print the extracted content
for content in content_list:
    print(content)


