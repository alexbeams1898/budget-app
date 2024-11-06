import sqlite3
import uuid

from constants import DB_NAME


def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserData (
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            key TEXT NOT NULL,
            value TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Budget (
            budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            total_amount REAL NOT NULL
        )
    ''')

    # Insert a new row
    # cursor.execute("INSERT INTO vals (value) VALUES (?)", (0,))

    conn.commit()
    conn.close()


def set_db_val(val):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    current_id = cursor.lastrowid
    cursor.execute('UPDATE vals SET value = ? WHERE id = ?', (val, current_id))

    conn.commit()
    conn.close()


def get_db_val():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    current_id = cursor.lastrowid
    cursor.execute('SELECT value FROM vals WHERE id = ?', (current_id,))

    value = cursor.fetchone()

    conn.commit()
    conn.close

    return value


def add_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())

    # Insert a new user
    cursor.execute("INSERT INTO Users (user_id, username) VALUES (?, ?)",
                   (user_id, username,))

    conn.commit()
    conn.close()


def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())
    # Insert a new user
    cursor.execute("""
        SELECT Users.user_id, Users.username
        FROM Users
        WHERE Users.username = ?
    """, (username,))
    user_data = cursor.fetchall()

    # Commit the transaction
    conn.commit()
    conn.close()

    return user_data
