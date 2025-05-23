<template>
  <div class="container text-muted py-5" v-if="book.title">
    <!-- 메인 정보 -->
    <div class="row mb-5">
      <div class="col-md-3">
        <img :src="book.cover" alt="Book Cover" class="img-fluid rounded shadow-sm" />
      </div>
      <div class="col-md-9">
        <h2 class="fw-bold">{{ book.title }}</h2>
        <p class="mt-3">{{ book.description }}</p>
        <p class="text-muted mb-1">
          {{ book.author }} | {{ book.publisher }} | {{ book.pub_date }}
        </p>
        <p class="mb-1">{{ book.subTitle }}</p>
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
  </div>
</template>

<script setup>
  import { useRoute } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { useBookStore } from '@/stores/book'

  const route = useRoute()
  const bookId = route.params.id
  const booksStore = useBookStore()

  const book = ref({})

  onMounted(() => {
    const foundBook = booksStore.books.find(b => b.id === parseInt(bookId))
    if (foundBook) {
      book.value = foundBook
    }
  })
</script>
