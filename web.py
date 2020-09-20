import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.google.com')

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())

posts = soup.find_all(class_="gb1")

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='post-title').get_text().replace('\n', '')
        link = post.find('a')['href']
        date = post.select('.post-date')[0].get_text()
        csv_writer.writerow([title, link, date])