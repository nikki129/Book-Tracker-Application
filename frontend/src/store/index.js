import { createStore } from "vuex";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

export default createStore({
  state: {
    books: [],
    statusFilter: "all",
    loading: false,
    error: null
  },
  getters: {
    filteredBooks(state) {
      if (state.statusFilter === "all") {
        return state.books;
      }
      return state.books.filter((book) => book.status === state.statusFilter);
    }
  },
  mutations: {
    setBooks(state, books) {
      state.books = books;
    },
    setStatusFilter(state, status) {
      state.statusFilter = status;
    },
    setLoading(state, value) {
      state.loading = value;
    },
    setError(state, error) {
      state.error = error;
    },
    addBook(state, book) {
      state.books = [book, ...state.books];
    },
    updateBook(state, updated) {
      state.books = state.books.map((book) => (book.id === updated.id ? updated : book));
    }
  },
  actions: {
    async fetchBooks({ commit }) {
      commit("setLoading", true);
      commit("setError", null);
      try {
        let nextUrl = `${API_BASE_URL}/books/`;
        const allBooks = [];
        while (nextUrl) {
          const response = await fetch(nextUrl);
          const data = await response.json();
          if (!response.ok) {
            const detail = data?.detail || "Unable to load books.";
            throw new Error(detail);
          }
          if (Array.isArray(data)) {
            allBooks.push(...data);
            nextUrl = null;
          } else {
            allBooks.push(...(data.results || []));
            nextUrl = data.next;
          }
        }
        commit("setBooks", allBooks);
      } catch (error) {
        commit("setError", error.message || "Unable to load books.");
      } finally {
        commit("setLoading", false);
      }
    },
    async createBook({ commit }, payload) {
      commit("setError", null);
      try {
        const response = await fetch(`${API_BASE_URL}/books/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(payload)
        });
        const data = await response.json();
        if (!response.ok) {
          const detail = data?.detail || "Unable to add book.";
          throw new Error(detail);
        }
        commit("addBook", data);
      } catch (error) {
        commit("setError", error.message || "Unable to add book.");
      }
    },
    async updateStatus({ commit }, { id, status }) {
      commit("setError", null);
      try {
        const response = await fetch(`${API_BASE_URL}/books/${id}/`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ status })
        });
        const data = await response.json();
        if (!response.ok) {
          const detail = data?.detail || "Unable to update status.";
          throw new Error(detail);
        }
        commit("updateBook", data);
      } catch (error) {
        commit("setError", error.message || "Unable to update status.");
      }
    }
  }
});
