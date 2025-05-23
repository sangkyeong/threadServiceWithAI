<template>
  <div class="container-fluid bg-dark text-white min-vh-100">
    <div class="row">
      <!-- Sidebar -->
      <aside class="col-md-2 bg-dark py-4">
        <ul class="list-unstyled">
          <li
            v-for="category in categoryStore.categories"
            :key="category.id"
            @click="selectedCategory = category.id"
            :class="['px-3 py-2', selectedCategory === category.id ? 'active-category' : 'text-secondary']"
            style="cursor: pointer;"
          >
            {{ category.name }}
          </li>
        </ul>
      </aside>

      <!-- Main Content -->
      <main class="col-md-10 p-4 bg-dark">
        <!-- Search Bar -->
        <div class="mb-4">
          <input
            v-model="searchQuery"
            type="text"
            class="form-control bg-secondary text-white border-0"
            placeholder="검색어를 입력하세요..."
          />
        </div>

        <!-- Book Grid -->
        <div class="row g-4">
          <div
            class="col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2"
            v-for="book in filteredBooks"
            :key="book.id"
          >
            <BookCard :book="book" :bookId="book.id" :showLink="false"/>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useBookStore } from '@/stores/book'
  import { useCategoryStore } from '@/stores/category'
  import BookCard from './BookCard.vue'

  const booksStore = useBookStore()
  const categoryStore = useCategoryStore()

  const selectedCategory = ref(0)
  const searchQuery = ref('')

  onMounted(() => {
    booksStore.fetchBooks()
    categoryStore.fetchCategories()
    
  })

  const filteredBooks = computed(() => {
    return booksStore.books.filter(book => {
      const matchCategory =
        selectedCategory.value === 0 ||
        book.category === selectedCategory.value
      const matchSearch = book.title.includes(searchQuery.value)
      return matchCategory && matchSearch
    })
  })
</script>

<style scoped>
  .active-category {
    color: white;
    font-weight: bold;
    border-left: 4px solid #ff5656;
    background-color: #1c1c1c;
  }
</style>
