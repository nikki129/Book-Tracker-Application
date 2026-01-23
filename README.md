# Book Tracker Application

A book tracking application with a Django + DRF backend, PostgreSQL database, and a Vue + Vuex UI.
The existing CLI still works for quick actions while the web UI is the primary experience.

## Quickstart (CLI)

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

## Backend (Django + DRF)

### Requirements
- PostgreSQL (local or hosted)
- Python 3.10+

### Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your database connection (defaults assume local Postgres):
   ```bash
   export DB_NAME=book_tracker
   export DB_USER=book_tracker
   export DB_PASSWORD=book_tracker
   export DB_HOST=localhost
   export DB_PORT=5432
   ```
   If you need to run with SQLite locally, set:
   ```bash
   export USE_SQLITE=true
   ```
3. Run migrations and start the server:
   ```bash
   cd backend
   python manage.py migrate
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/books/`.

## Frontend (Vue + Vuex + SCSS)

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Set the API base URL (optional, defaults to `http://localhost:8000/api`):
   ```bash
   export VITE_API_BASE_URL=http://localhost:8000/api
   ```
3. Start the dev server:
   ```bash
   npm run dev
   ```

## Roadmap

If you want to build the next version of the app with Django + DRF, PostgreSQL, and a Vue
frontend (plus a supporting CLI), see the detailed implementation plan in [`PLAN.md`](PLAN.md).

## Development

Run the tests with:

```bash
pytest
```
