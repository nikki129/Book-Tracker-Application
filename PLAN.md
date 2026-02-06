# Book Tracker App: Django + DRF + Vue Plan

## Goals
- Build a clean, modern UI for tracking books across all key workflows: add, browse, update status, and view progress.
- Preserve a CLI for quick actions while adding a full web UI for day-to-day use.
- Provide a scalable backend using Django + Django REST Framework (DRF).
- Deliver a Vue frontend with Vuex state management and SCSS-based styling.

## Target Stack
- **Backend:** Django + DRF
- **Frontend:** Vue (Vuex for state management)
- **Styling:** SCSS
- **Database:** PostgreSQL

## Product Scope
- Track books with title, author, cover (optional), status, rating, and notes.
- Support core reading statuses: **To Read**, **Reading**, **Finished**, **Abandoned**.
- Make browsing and updating books fast and intuitive.

## UX / UI Principles
- Clean layout with clear spacing, simple typography, and a neutral color palette.
- Focus on primary actions (Add Book, Update Status) with minimal visual noise.
- Ensure the book list has strong scanability (title, author, status badges).
- Use predictable navigation: Dashboard, Books, Reading List, Stats.

## Backend Plan (Django + DRF)
1. **Project setup**
   - Create Django project and app (e.g., `books`).
   - Configure DRF and CORS for the Vue frontend.
   - Connect to PostgreSQL for the primary database.
2. **Models**
   - Book: title, author, status, rating, notes, created_at, updated_at.
   - Optional: tags, cover image URL, page count.
3. **API**
   - CRUD endpoints for books.
   - Filters by status, rating, and search term.
   - Pagination for list views.
4. **Auth (optional future)**
   - User accounts for personal libraries.
5. **CLI support**
   - Provide a lightweight CLI that calls the same API for quick add/list/status actions.

## Frontend Plan (Vue + Vuex + SCSS)
1. **Pages / Views**
   - Dashboard (summary stats + recently updated).
   - Books list (filters + sorting).
   - Book detail (edit status, rating, notes).
   - Add / Edit form.
2. **State management**
   - Vuex modules for books, filters, and UI state.
3. **Styling**
   - SCSS with variables for colors, spacing, and typography.
   - Reusable components: buttons, badges, inputs, cards.

## Milestones
1. **Foundation**: backend project + API skeleton + basic Vue app.
2. **Core CRUD**: book model + API endpoints + list/detail UI.
3. **Polish**: SCSS theme, status badges, and filter UX.
4. **Enhancements**: stats dashboard and optional user auth.
