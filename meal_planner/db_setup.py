# database_setup.py

import sqlite3

DATABASE_PATH = "foodieaidvisor.db"


def setup_database():
    """Initialize SQLite database and set up necessary tables."""

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        dietary_restrictions TEXT,
        preferences TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        name TEXT NOT NULL,
        expiration_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        ingredients TEXT,
        instructions TEXT
    )
    """
    )

    conn.commit()
    conn.close()
