"""Tests for the database layer."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from book_tracker import db


def test_add_and_list_books(tmp_path):
    db_path = tmp_path / "books.db"
    db.init_db(db_path)
    book_id = db.add_book("1984", "George Orwell", db_path=db_path)
    books = db.list_books(db_path=db_path)
    assert len(books) == 1
    assert books[0][1] == "1984"
    assert books[0][2] == "George Orwell"
    assert books[0][3] == "to-read"

    db.update_status(book_id, "finished", db_path=db_path)
    books = db.list_books(db_path=db_path)
    assert books[0][3] == "finished"
