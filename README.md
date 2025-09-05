# Book Tracker Application

A simple command-line application to track your reading list.

## Quickstart

1. Clone this repository and change into its directory.
2. (Optional) create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add a book:
   ```bash
   python -m book_tracker.cli add "Book Title" "Author Name"
   ```
5. List all books:
   ```bash
   python -m book_tracker.cli list
   ```
6. Update a book's status:
   ```bash
   python -m book_tracker.cli status 1 finished
   ```

The SQLite database file will be created automatically at `book_tracker/books.db`.

## Features

- Add books with title and author
- List all tracked books
- Update the reading status of a book

## Development

Run the tests with:

```bash
pytest
```
