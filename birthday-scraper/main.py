#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import os

# Config
URL = "https://kisnaplo.karinthy.hu/app/interface.php"
DB_PATH = "/opt/birthday_scraper/students.db"

def fetch_html():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[ERROR] Failed to fetch HTML: {e}")
        return ""

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find('main', id='main_card_birthday')
    if not main:
        print("[WARN] No birthday data found.")
        return []

    entries = []
    spans = main.find_all('span', class_='PTitle')

    for span in spans:
        name = span.text.strip()

        # Find sibling text after span
        tail = ''
        sibling = span.next_sibling
        while sibling and (not isinstance(sibling, str) or sibling.strip() == ''):
            sibling = sibling.next_sibling

        if isinstance(sibling, str):
            tail = sibling.strip().strip(',').strip()
        else:
            continue

        try:
            student_class, birthdate = tail.rsplit('(', 1)
            student_class = student_class.strip()
            birthdate = birthdate.replace(')', '').strip()
            entries.append((name, student_class, birthdate))
        except ValueError:
            print(f"[WARN] Failed to parse: {name} | {tail}")
    return entries

def store_entries(entries):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        class TEXT,
        birthdate TEXT,
        scraped_at TEXT
    )''')

    for entry in entries:
        cur.execute('INSERT INTO students (name, class, birthdate, scraped_at) VALUES (?, ?, ?, ?)',
                    (*entry, datetime.now().date().isoformat()))

    conn.commit()
    conn.close()
    print(f"[INFO] Stored {len(entries)} entries.")

def main():
    print("[INFO] Birthday scraper started.")
    html = fetch_html()
    if html:
        entries = parse_html(html)
        store_entries(entries)
    print("[INFO] Done.")

if __name__ == "__main__":
    main()