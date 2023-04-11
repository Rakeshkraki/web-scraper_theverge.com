Web Scraper for The Verge Articles
This is a Python script that scrapes articles from The Verge website and stores the information in a CSV file and an SQLite database. The script is designed to be run on a daily basis to fetch new articles and avoid duplicates.

How to Use
Install the required Python packages:

requests
beautifulsoup4
sqlite3
Update the url variable to point to the desired website.

Run the script using python scraper.py.

The script will create a CSV file with today's date in the format ddmmyyyy_verge.csv and store the article information in an SQLite database.

Files
scraper.py: the main Python script that scrapes the articles and stores them in a CSV file and an SQLite database.
theverge.db: the SQLite database file where the article information is stored.
read.md: the documentation file that explains how to use the script.
Functionality
The script performs the following tasks:

Defines the website URL and page headers.
Creates a connection to an SQLite database and creates a table for the articles if it doesn't already exist.
Sends a GET request to the website and uses Beautiful Soup to parse the HTML content of the page.
Finds all the article elements on the page and loops through each one, extracting the relevant information (URL, headline, author, and date) and storing it in both a CSV file and the SQLite database.
The CSV file is named using today's date, and the SQLite database is updated with the new articles. The INSERT OR IGNORE statement is used to avoid inserting duplicates into the database.
The script can be run on a daily basis to fetch new articles and avoid duplicates.
Dependencies
Python 3.x
requests
beautifulsoup4
sqlite3
