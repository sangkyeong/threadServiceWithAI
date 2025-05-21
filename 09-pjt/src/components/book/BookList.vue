<template>
  <div class="container">
    <aside class="sidebar">
      <ul>
        <li
          v-for="category in categoryStore.categories"
          :key="category.pk"
          :class="{ active: selectedCategory === category.pk }"
          @click="selectedCategory = category.pk"
        >
          {{ category.fields.name }}
        </li>
      </ul>
    </aside>

    <main class="book-area">
      <div class="search-bar">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="검색어를 입력하세요..."
        />
      </div>

      <div class="book-grid">
        <BookCard
          v-for="book in filteredBooks"
          :key="book.pk"
          :book="book.fields"
        />
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useBooksStore, useCategoryStore } from '@/stores/data'
import BookCard from './BookCard.vue'

const booksStore = useBooksStore()
const categoryStore = useCategoryStore()

const selectedCategory = ref(0)
const searchQuery = ref('')

const filteredBooks = computed(() => {
  return booksStore.books.filter(book => {
    const matchCategory =
      selectedCategory.value === 0 ||
      book.fields.category === selectedCategory.value
    const matchSearch = book.fields.title.includes(searchQuery.value)
    return matchCategory && matchSearch
  })
})
</script>

<style scoped>
.container {
  display: flex;
  min-height: 100vh;
  background-color: #121212;
  color: white;
}

.sidebar {
  width: 220px;
  background-color: #1c1c1c;
  padding: 1rem;
}
.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}


.sidebar li {
  padding: 0.6rem 0;
  cursor: pointer;
  color: #ddd;
  border-left: 4px solid transparent;
  padding-left: 10px;
  transition: all 0.2s;
}

.sidebar li.active {
  font-weight: bold;
  color: #ffffff;
  border-left: 4px solid #ff5656;
}

.book-area {
  flex: 1;
  padding: 2rem;
  background-color: #1a1a1a;
}

.search-bar input {
  width: 100%;
  padding: 0.7rem;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  background-color: #2a2a2a;
  color: white;
  margin-bottom: 1.5rem;
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.5rem;
}
</style>
