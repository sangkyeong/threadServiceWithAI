<template>
  <div class="container-fluid bg-dark text-white py-5" v-if="book.title">
    <div class="container">
    <!-- 메인 정보 -->
    <div class="row mb-5">
      <div class="col-md-3">
        <img :src="book.cover" alt="Book Cover" class="img-fluid rounded shadow-sm" />
      </div>

      <div class="col-md-9">
        <h2 class="fw-bold">{{ book.title }}</h2>
        <template v-if="accountStore.user">
          <RouterLink :to="{name:'threadWrite', params:{bookId:bookId}}" class="btn btn-outline-primary btn-sm mt-2">쓰레드 작성</RouterLink>
        </template>
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
    <!-- 작가 정보가 중앙이 별로면 text-center 지우기 -->
    <hr class="border-secondary" />
    <div>
      <h3 class="mb-4 text-center">작가 정보</h3>
      <div class="d-flex align-items-start gap-4">
        <img 
          :src="book.author_photo || 'http://127.0.0.1:8000/static/default_author_img/default_author.jpg'" 
          alt="Author Image" 
          class="rounded-circle" 
          style="width: 100px; height: 100px; object-fit: cover;" 
        />
        <div>
          <p class="mb-1 fw-bold" style="font-size: 24px;">{{ book.author }}</p>
          <p>{{ book.author_info }}</p>
        </div>
      </div>
    </div>

    <!-- 유사 도서 추천 -->
    <hr class="border-secondary" />
    
    <div>
      <h3 class="mb-4 text-center">AI 기반 유사 도서 추천</h3>
      <div class="row gx-4 gy-4 justify-content-center text-center">
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
</div>

</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'
import { ref, watch, computed } from 'vue'
import { useBookStore } from '@/stores/book'
import BookCard from '@/components/book/BookCard.vue'
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()

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
