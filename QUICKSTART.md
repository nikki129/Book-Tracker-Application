# Quickstart

This guide walks you through using the Book Tracker CLI.

## Installation

1. Clone the repository and change into the project directory.
2. (Optional) create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Add a book:
```bash
python -m book_tracker.cli add "The Hobbit" "J.R.R. Tolkien"
```

List tracked books:
```bash
python -m book_tracker.cli list
```

Update a book's status:
```bash
python -m book_tracker.cli status 1 finished
```

The SQLite database is stored in `book_tracker/books.db` and is created on first use.

## Running tests

```bash
pytest
```
