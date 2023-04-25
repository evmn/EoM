from bs4 import BeautifulSoup
from datetime import datetime
import requests
import sqlite3
import random
import re
from random_utils import get_header, sleep_random_seconds

def setup_database():
    now=datetime.now()
    date_time = now.strftime("%Y%m%d")
    eom_db =  "Encyclopedia_of_Math-" + date_time + ".db"
    
    conn = sqlite3.connect(eom_db)
    db = conn.cursor()
    db.execute('''
        CREATE TABLE if not exists entry
        (id integer primary key autoincrement,
        name text,
        url text,
        redirect BOOLEAN NOT NULL CHECK (redirect IN (0, 1))
        )''')
    conn.commit()
    return conn
def scrape_entries(url, headers):
    entries_list = []
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    allpages_chunk = soup.find_all(class_='mw-allpages-chunk')
    nav_page = soup.find(class_='mw-allpages-nav')
    
    for chunk in allpages_chunk:
        links = chunk.find_all('a')
        for link in links:
            title = link.text
            href = link['href']
            entries_list.append([title, href])
    next_page = nav_page.find_all('a')[-1]
    next_url = ""
    if re.search('Next page', next_page.text):
        next_url = next_page['href']
    return (entries_list, next_url)
def save_entries(conn, entries_list, redirect):
    db = conn.cursor()
    for row in entries_list:
        db.execute('''insert into entry(name, url, redirect)
                    values(?,?, ?)
                    ''', (row[0], row[1], redirect))
    conn.commit()

def main():
    
    # remove '&hideredirects=1' if interested with redirect entries
    href = '/index.php?title=Special:AllPages&hideredirects=1'
    conn = setup_database()
    item_number = 0

    while len(href) > 10:
        header = get_header()
        url=f"https://encyclopediaofmath.org{href}"
        entries_list, href  = scrape_entries(url, header)
        item_number += len(entries_list)
        print("total items:", item_number)
        print("Next page: ", href)

        redirect = 0
        save_entries(conn, entries_list, redirect)
        sleep_random_seconds(3, 5)

    conn.close()

if __name__ == '__main__':
    main()
