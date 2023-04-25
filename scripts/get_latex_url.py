import requests
import traceback
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3
import time
from random import randint
from random_header import get_header
import re

headers = get_header()

def setup_database():
    now=datetime.now()
    date_time = now.strftime("%Y%m%d")
    eom_db =  "Encyclopedia_of_Math-" + date_time + ".db"
    conn = sqlite3.connect(eom_db)
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists latex
        (id integer primary key autoincrement,
        eid integer NOT NULL UNIQUE,
        url text not null unique,
        src text not null unique
        )''')
    conn.commit()
    return conn

def query_database(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    # Fetch the results and store them in a list
    result = cursor.fetchall()
    return result

def insert_data(conn, data):
    cursor = conn.cursor()
    cursor.execute('insert into latex(eid, url, src) VALUES (?,?,?)', data)
    conn.commit()

def scrape_latex(href):
    url = "https://encyclopediaofmath.org" + href
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    latex = soup.find('textarea', {'class': 'mw-editfont-monospace'}).text
    
    return latex

def scrape_latex_link(href):
    url = "https://encyclopediaofmath.org" + href
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    latex_link = soup.find('li', {'id': 'ca-viewsource'}).find('a')['href']
    return latex_link

def main():
    item_number=0
    while True:
        conn = setup_database()
        #query = "select * from entry where entry.id not in (select eid from latex) order by random() limit 30;"
        query = "select * from entry where entry.id not in (select eid from latex) and redirect = 0  order by random() limit 30;"
        result = query_database(conn, query)
    
        for row in result:
            eid = row[0]
            title = row[1]
            href = row[2]
            try:
                latex_link = scrape_latex_link(href)
           
                print(title, href, latex_link)
                latex_content = scrape_latex(latex_link)
    
                time.sleep(randint(3, 5))
                insert_data(conn, (eid, latex_link, latex_content))
                time.sleep(randint(3, 5))
                item_number += 1
            except Exception:
                traceback.print_exc()
                print("\n\t\nError: ", title, href)
                time.sleep(randint(10, 30))
                pass
            if item_number % 10 == 0:
                print(item_number)
                conn.commit()
                time.sleep(randint(3, 4))
    
    conn.close()
if __name__ == '__main__':
    main()
