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

## Full Web App (Backend + Frontend) Checklist

Use this end-to-end checklist if you want to run the full interactive web app from a clean machine.

### 1) Prerequisites
- **Python 3.10+** (for Django/DRF)
- **Node.js 18+** (for Vite/Vue dev server)
- **PostgreSQL 13+** (recommended), or use SQLite for a quick local run

### 2) Clone + enter the repo
```bash
git clone <your-repo-url>
cd Book-Tracker-Application
```

### 3) Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```
> On Windows PowerShell: `.\.venv\Scripts\Activate.ps1`

### 4) Install Python dependencies
```bash
pip install -r requirements.txt
```

### 5) Configure the database
**Option A — PostgreSQL (recommended):**
1. Create a database and user (example commands):
   ```bash
   createdb book_tracker
   createuser book_tracker
   ```
2. Export connection settings:
   ```bash
   export DB_NAME=book_tracker
   export DB_USER=book_tracker
   export DB_PASSWORD=book_tracker
   export DB_HOST=localhost
   export DB_PORT=5432
   ```

**Option B — SQLite (quick local run):**
```bash
export USE_SQLITE=true
```

### 6) Run migrations and start the backend API
```bash
cd backend
python manage.py migrate
python manage.py runserver
```
✅ The API should now be available at `http://localhost:8000/api/books/`.

### 7) Install frontend dependencies
Open a **new terminal** (keep the backend running), then:
```bash
cd frontend
npm install
```

### 8) Configure the frontend API base URL (optional)
If you kept the backend default:
```bash
export VITE_API_BASE_URL=http://localhost:8000/api
```
If the backend runs on a different host/port, update the URL accordingly.

### 9) Start the Vue dev server
```bash
npm run dev
```
✅ Vite will print a local URL (typically `http://localhost:5173/`).

### 10) Verify the full app works
1. Open the Vite URL in your browser.
2. Add a book from the UI.
3. Refresh the page and confirm the book persists.
4. Update the book’s status and confirm the UI updates.

### 11) Common troubleshooting
- **CORS errors:** Ensure the backend is running and `VITE_API_BASE_URL` matches it.
- **Database auth errors:** Double-check `DB_*` env vars or switch to SQLite.
- **Port conflicts:** Change backend port with `python manage.py runserver 0.0.0.0:8001` and update `VITE_API_BASE_URL`.

## Roadmap

If you want to build the next version of the app with Django + DRF, PostgreSQL, and a Vue
frontend (plus a supporting CLI), see the detailed implementation plan in [`PLAN.md`](PLAN.md).

## Development

Run the tests with:

```bash
pytest
```
