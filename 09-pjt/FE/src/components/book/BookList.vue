<template>
  <div class="container-fluid bg-dark text-white min-vh-100">
    <div class="row">

      <!-- Sidebar -->
      <aside class="col-md-2 bg-dark py-4">
        <ul class="list-unstyled">
          <li
            v-for="category in categoriesWithAll"
            :key="category.id"
            @click="selectedCategory = category.id"
            :class="['category-item', selectedCategory === category.id ? 'active-category' : '']"
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
            class="form-control bg-dark text-white border-0"
            placeholder="검색어를 입력하세요..."
          />
        </div>

        <!-- Book Grid -->
        <div class="row g-4">
          <div
            class="col-6 col-sm-6 col-md-4 col-lg-3"
            v-for="book in visibleBooks"
            :key="book.id"
          >
            <BookCard :book="book" :bookId="book.id"/>
          </div>
        </div>
        
        <!-- 펼처보기 btn -->
        <div class="text-center mt-4">
          <button
            v-if="visibleCount < filteredBooks.length"
            @click="visibleCount += 20"
            class="btn btn-outline-light"
          >
            + 펼처보기
          </button>
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
  import { useRoute } from 'vue-router'

  const booksStore = useBookStore()
  const categoryStore = useCategoryStore()
  const route = useRoute()
  const selectedCategory = ref(0)
  const searchQuery = ref('')
  const visibleCount = ref(20)

  onMounted(() => {
    booksStore.fetchBooks()
    categoryStore.fetchCategories()

    const categoryFromQuery = Number(route.query.category)
    if (categoryFromQuery) {
      selectedCategory.value = categoryFromQuery
    }
    window.scrollTo(0, 0)
  })

  const categoriesWithAll = computed(() => [
  { id: 0, name: '전체' },
  ...categoryStore.categories
  ])

  const filteredBooks = computed(() => {
    return booksStore.books.filter(book => {
      const matchCategory =
        selectedCategory.value === 0 ||
        book.category === selectedCategory.value
      const matchSearch = book.title.includes(searchQuery.value)
      return matchCategory && matchSearch
    })
  })

  const visibleBooks = computed(() => {
      return filteredBooks.value.slice(0, visibleCount.value)
    })
</script>

<style scoped>
  input::placeholder {
    color: #ccc;
  }

  aside ul {
    text-align: center;
  }

  aside li {
    width: 100%;
  }

  .category-item {
    color: #bbb;
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    border-radius: 4px;
  }

.category-item:hover {
    /* background-color: #2f2f2f; */
    color: #fff;
    transform: translateX(5px); /* 부드럽게 오른쪽으로 슥 밀리는 느낌 */
  }

.active-category {
    color: #fff;
    font-weight: bold;
    background-color: #1c1c1c;
    border-left: 4px solid #ff5656;
  }
</style>
