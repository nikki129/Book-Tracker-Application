"""Database utilities for Book Tracker."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import List, Tuple

DB_PATH = Path(__file__).resolve().parent / "books.db"


def connect(db_path: Path = DB_PATH) -> sqlite3.Connection:
    """Return a connection to the SQLite database."""
    return sqlite3.connect(db_path)


def init_db(db_path: Path = DB_PATH) -> None:
    """Create the books table if it doesn't already exist."""
    with connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """
        )
        conn.commit()


def add_book(
    title: str, author: str, status: str = "to-read", db_path: Path = DB_PATH
) -> int:
    """Add a book to the database and return its ID."""
    init_db(db_path)
    with connect(db_path) as conn:
        cursor = conn.execute(
            "INSERT INTO books (title, author, status) VALUES (?, ?, ?)",
            (title, author, status),
        )
        conn.commit()
        return int(cursor.lastrowid)


def list_books(db_path: Path = DB_PATH) -> List[Tuple[int, str, str, str]]:
    """Return a list of all books."""
    init_db(db_path)
    with connect(db_path) as conn:
        cursor = conn.execute("SELECT id, title, author, status FROM books")
        return list(cursor.fetchall())


def update_status(book_id: int, status: str, db_path: Path = DB_PATH) -> None:
    """Update the reading status for a book."""
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
        conn.commit()
