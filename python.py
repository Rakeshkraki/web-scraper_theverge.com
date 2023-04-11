import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import datetime

url = 'https://www.theverge.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='c-entry-box--compact__body')

now = datetime.datetime.now()
id_prefix = now.strftime('%Y%m%d%H%M%S')

csv_file_name = now.strftime('%d%m%Y_verge.csv')
csv_file = open(csv_file_name, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['id', 'URL', 'headline', 'author', 'date'])

conn = sqlite3.connect('verge.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS articles
             (id TEXT PRIMARY KEY,
              url TEXT,
              headline TEXT,
              author TEXT,
              date TEXT)''')

for i, article in enumerate(articles):

    article_url = article.find('a')['href']
    headline = article.find(
        'h2', class_='c-entry-box--compact__title').text.strip()
    author = article.find('span', class_='c-byline__author-name').text.strip()
    date = article.find('time')['datetime']

    id = id_prefix + str(i + 1)

    csv_writer.writerow([id, article_url, headline, author, date])

    c.execute("INSERT OR IGNORE INTO articles VALUES (?, ?, ?, ?, ?)",
              (id, article_url, headline, author, date))


conn.commit()
conn.close()

csv_file.close()

