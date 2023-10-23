# database_setup.py

import sqlite3

DATABASE_PATH = "foodieaidvisor.db"


def reset_database():
    """Delete all tables and then recreate them to reset the database."""

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Drop tables
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS active_user")
    cursor.execute("DROP TABLE IF EXISTS ingredients")
    cursor.execute("DROP TABLE IF EXISTS recipes")

    conn.commit()
    conn.close()


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
    CREATE TABLE IF NOT EXISTS active_user (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        username TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
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
        user_id INTEGER,
        name TEXT NOT NULL,
        ingredients TEXT,
        instructions TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    reset_database()
    setup_database()
