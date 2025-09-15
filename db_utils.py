
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'coding_purposes.db')

def setup_database_and_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Favorited (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            mission_id TEXT,
            favorited_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_date TEXT UNIQUE,
            result TEXT,
            cached_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    setup_database_and_tables()
    return sqlite3.connect(DB_PATH)

def get_cached_result(conn, query_date):
    cursor = conn.cursor()
    cursor.execute("SELECT result FROM Cache WHERE query_date = ?", (query_date,))
    row = cursor.fetchone()
    return row[0] if row else None

def cache_result(conn, query_date, result):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO Cache (query_date, result) VALUES (?, ?)",
        (query_date, result)
    )
    conn.commit()
