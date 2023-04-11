import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime


def scrape_theverge():
    url = 'https://www.theverge.com/'

    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    articles = soup.find_all('article')

    data = []

    for article in articles:
        headline = article.find(
            'h2', {'class': 'c-entry-box--compact__title'}).text.strip()

        link = article.find(
            'a', {'class': 'c-entry-box--compact__image-wrapper'}).get('href')

        author = article.find('span', {'class': 'c-byline__item'}).text.strip()

        date = article.find(
            'time', {'class': 'c-byline__item'}).get('datetime')

        data.append((link, headline, author, date))

    csv_filename = datetime.now().strftime('%d%m%Y') + '_verge.csv'

    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(['id', 'URL', 'headline', 'author', 'date'])

        # Loop over the data and write each row to the CSV file
        for i, row in enumerate(data):
            writer.writerow([i+1] + list(row))

    # Define the database name
    db_name = 'theverge.db'

    # Connect to the database or create it if it doesn't exist
    conn = sqlite3.connect(db_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Create the articles table
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                      (id INTEGER PRIMARY KEY, URL TEXT, headline TEXT, author TEXT, date TEXT)''')

    # Insert the data into the table
    cursor.executemany(
        '''INSERT INTO articles (URL, headline, author, date) VALUES (?, ?, ?, ?)''', data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    scrape_theverge()
