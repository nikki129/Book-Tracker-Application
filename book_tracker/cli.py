"""Command-line interface for the Book Tracker app."""

from __future__ import annotations

import argparse

from . import db


def main() -> None:
    parser = argparse.ArgumentParser(description="Book Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new book")
    add_parser.add_argument("title")
    add_parser.add_argument("author")

    subparsers.add_parser("list", help="List all books")

    status_parser = subparsers.add_parser(
        "status", help="Update the reading status for a book"
    )
    status_parser.add_argument("book_id", type=int)
    status_parser.add_argument(
        "status", choices=["to-read", "reading", "finished"], help="New status"
    )

    args = parser.parse_args()

    if args.command == "add":
        book_id = db.add_book(args.title, args.author)
        print(f"Added book #{book_id}")
    elif args.command == "list":
        books = db.list_books()
        for book in books:
            print(f"{book[0]}: {book[1]} by {book[2]} - {book[3]}")
    elif args.command == "status":
        db.update_status(args.book_id, args.status)
        print(f"Updated book #{args.book_id} to {args.status}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
