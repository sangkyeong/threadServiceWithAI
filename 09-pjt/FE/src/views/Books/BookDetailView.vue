<template>
  <div class="book-detail-container">
    <div class="book-main">
      <img :src="book.cover" alt="Book Cover" class="book-cover" />
      <div class="book-info">
        <h2 class="book-title">{{ book.title }}</h2>
        <p class="book-meta">
          {{ book.author }} | {{ book.publisher }} | {{ book.pub_date }}
        </p>
        <p class="book-subtitle">{{ book.subTitle }}</p>
        <p class="book-description">{{ book.description }}</p>
        <p class="book-isbn">ISBN: {{ book.isbn }}</p>
        <p class="book-score">고객 평점: {{ book.customer_review_rank }}</p>
      </div>
    </div>

    <div class="author-info">
      <h3>작가 정보</h3>
      <div class="author-detail">
        <img :src="book.author_image" alt="Author Image" class="author-img" />
        <p>{{ book.author_intro }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useBooksStore } from '@/stores/data'

const route = useRoute()
const bookId = route.params.bookId
const booksStore = useBooksStore()

const book = ref({})

onMounted(() => {
  const foundBook = booksStore.books.find(b => b.pk === parseInt(bookId))
  if (foundBook) {
    book.value = foundBook.fields
  }
})
</script>

<style scoped>
.book-detail-container {
  padding: 2rem;
  color: white;
  background-color: #121212;
  min-height: 100vh;
}

.book-main {
  display: flex;
  gap: 2rem;
}

.book-cover {
  width: 180px;
  height: 260px;
  object-fit: cover;
  border-radius: 5px;
}

.book-info {
  flex: 1;
}

.book-title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.book-meta,
.book-subtitle,
.book-description,
.book-isbn,
.book-score {
  margin-bottom: 0.5rem;
  color: #dddddd;
}

.author-info {
  margin-top: 3rem;
  padding-top: 1rem;
  border-top: 1px solid #333;
}

.author-detail {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.author-img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}
</style>