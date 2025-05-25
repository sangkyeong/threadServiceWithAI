<template>
  <div>
    <HeroSection />

    <section class="bestseller-section">
      <h2 class="title">베스트셀러</h2>
      <BookSlider :books="bestsellers" />
    </section>

    <section class="genre-section">
      <h2 class="title">장르별 둘러보기</h2>
      <div class="genre-list">
        <GenreCard v-for="genre in genres" :key="genre.id" :genre="genre" />
      </div>
    </section>

    <section class="thread-section">
      <h2 class="title">실시간 추천 글</h2>
      <div>
        <ThreadCard v-for="thread in threads" :key="thread.id" :thread="thread" />
      </div>
    </section>

  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import BookSlider from '@/components/main_page/BookSlider.vue';
  import GenreCard from '@/components/main_page/GenreCard.vue';
  import HeroSection from '@/components/main_page/HeroSection.vue';
  import ThreadCard from '@/components/main_page/ThreadCard.vue';

  const bestsellers = ref([])
  const genres = ref([])
  const threads = ref([])

onMounted(async () => {
  const bookRes = await fetch('/books/books/')
  bestsellers.value = await bookRes.json()

  const genreRes = await fetch('/books/categories/')
  genres.value = await genreRes.json()


  const threadRes = await fetch('/threads/')
  threads.value = await threadRes.json()
})

</script>

<style scoped>
  .genre-section, .bestseller-section, .thread-section {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    max-width: 1100px;
    margin: 0 auto 48px auto;
  }
  .title {
    margin-bottom: 20px;
    font-weight: 700;
    text-align: center;
    width: 100%; 
    margin: 60px 0 20px
  }
  .genre-list {
    display: flex;
    gap: 16px;
    margin-top: 16px;
  }
</style>