<template>
  <div class="app">
    <header class="app__header">
      <div>
        <p class="app__eyebrow">Book Tracker</p>
        <h1>Keep your reading on track</h1>
        <p class="app__subtitle">
          Track your reading list, update statuses, and keep notes in one clean dashboard.
        </p>
      </div>
      <div class="app__status">
        <label for="statusFilter">Filter</label>
        <select id="statusFilter" v-model="statusFilter">
          <option value="all">All</option>
          <option value="to_read">To Read</option>
          <option value="reading">Reading</option>
          <option value="finished">Finished</option>
          <option value="abandoned">Abandoned</option>
        </select>
      </div>
    </header>

    <section class="app__grid">
      <div class="panel">
        <h2>Add a book</h2>
        <form @submit.prevent="handleSubmit">
          <div class="form-row">
            <label for="title">Title</label>
            <input id="title" v-model="form.title" required />
          </div>
          <div class="form-row">
            <label for="author">Author</label>
            <input id="author" v-model="form.author" required />
          </div>
          <div class="form-row">
            <label for="status">Status</label>
            <select id="status" v-model="form.status">
              <option value="to_read">To Read</option>
              <option value="reading">Reading</option>
              <option value="finished">Finished</option>
              <option value="abandoned">Abandoned</option>
            </select>
          </div>
          <div class="form-row">
            <label for="notes">Notes</label>
            <textarea id="notes" v-model="form.notes" rows="3"></textarea>
          </div>
          <button type="submit">Add to library</button>
        </form>
      </div>

      <div class="panel">
        <div class="panel__header">
          <h2>Your library</h2>
          <button class="ghost" @click="refreshBooks">Refresh</button>
        </div>
        <p v-if="loading" class="helper">Loading books...</p>
        <p v-else-if="error" class="helper error">{{ error }}</p>
        <ul v-else class="book-list">
          <li v-for="book in books" :key="book.id" class="book-card">
            <div>
              <h3>{{ book.title }}</h3>
              <p class="author">{{ book.author }}</p>
              <p class="notes" v-if="book.notes">{{ book.notes }}</p>
            </div>
            <div class="status">
              <span :class="['badge', book.status]">{{ formatStatus(book.status) }}</span>
              <select v-model="book.status" @change="updateBookStatus(book)">
                <option value="to_read">To Read</option>
                <option value="reading">Reading</option>
                <option value="finished">Finished</option>
                <option value="abandoned">Abandoned</option>
              </select>
            </div>
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      form: {
        title: "",
        author: "",
        status: "to_read",
        notes: ""
      }
    };
  },
  computed: {
    books() {
      return this.$store.getters.filteredBooks;
    },
    loading() {
      return this.$store.state.loading;
    },
    error() {
      return this.$store.state.error;
    },
    statusFilter: {
      get() {
        return this.$store.state.statusFilter;
      },
      set(value) {
        this.$store.commit("setStatusFilter", value);
      }
    }
  },
  mounted() {
    this.refreshBooks();
  },
  methods: {
    formatStatus(status) {
      return status.replace("_", " ").replace(/\b\w/g, (char) => char.toUpperCase());
    },
    async handleSubmit() {
      await this.$store.dispatch("createBook", this.form);
      this.form = {
        title: "",
        author: "",
        status: "to_read",
        notes: ""
      };
    },
    async updateBookStatus(book) {
      await this.$store.dispatch("updateStatus", { id: book.id, status: book.status });
    },
    refreshBooks() {
      this.$store.dispatch("fetchBooks");
    }
  }
};
</script>
