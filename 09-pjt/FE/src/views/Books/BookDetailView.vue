<template>
  <div class="container text-muted py-5" v-if="book.title">
    <!-- 메인 정보 -->
    <div class="row mb-5">
      <div class="col-md-3">
        <img :src="book.cover" alt="Book Cover" class="img-fluid rounded shadow-sm" />
      </div>

      <div class="col-md-9">
        <h2 class="fw-bold">{{ book.title }}</h2>
        <RouterLink :to="{name:'threadWrite', params:{bookId:bookId}}" class="btn btn-outline-primary btn-sm mt-2">쓰레드 작성</RouterLink>
        <p class="mt-3">{{ book.description }}</p>
        <p class="text-muted mb-1">
          {{ book.author }} | {{ book.publisher }} | {{ book.pub_date }}
        </p>
        <p class="mb-1" v-if="book.subTitle">{{ book.subTitle }}</p>
        <p class="mb-1">ISBN: {{ book.isbn }}</p>
        <p>고객 평점: {{ book.customer_review_rank }}</p>
      </div>
      
    </div>

    <!-- 작가 정보 -->
    <hr class="border-secondary" />
    <div>
      <h4 class="mb-4">작가 정보</h4>
      <div class="d-flex align-items-start gap-4">
        <img :src="book.author_photo" alt="Author Image" class="rounded-circle" style="width: 100px; height: 100px; object-fit: cover;" />
        <div>
          <p class="mb-1 fw-bold">{{ book.author }}</p>
          <p>{{ book.author_info }}</p>
        </div>
      </div>
    </div>

    <!-- 유사 도서 추천 -->
    <hr class="border-secondary" />
    <div>
      <h4 class="mb-4">AI 기반 유사 도서 추천</h4>
      <div class="row gx-4 gy-4 justify-content-start">
        <div 
          v-for="rBook in recommendBooks"
          :key="rBook.id"
          class="col-12 col-sm-6 col-md-4 col-lg-3"
        >
          <BookCard :book="rBook" :bookId="rBook.id" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'
import { ref, watch, computed } from 'vue'
import { useBookStore } from '@/stores/book'
import BookCard from '@/components/book/BookCard.vue'

const route = useRoute()
const bookId = computed(() => route.params.id)
const booksStore = useBookStore()

const book = ref({})
const recommendBooks = ref([])

watch(bookId, async (newId) => {
  const foundBook = booksStore.books.find(b => b.id === parseInt(newId))
  if (foundBook) {
    book.value = foundBook
  }

  recommendBooks.value = await booksStore.recommendBooksForAI(newId)
}, { immediate: true })
</script>
