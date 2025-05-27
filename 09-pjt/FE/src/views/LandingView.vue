<template>
  <div class="bg-dark text-white min-vh-100">
    <HeroSection />

    <section class="bestseller-section">
      <h2 class="title">베스트셀러</h2>
      <BookSlider :books="store.bestsellers" />
    </section>

    <section class="genre-section">
      <h2 class="title">카테고리</h2>
      <GenreCard />
    </section>

    <section class="thread-section">
      <h2 class="title">Thread</h2>
      <ThreadCard  />
    </section>

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBookStore } from '@/stores/book'
import BookSlider from '@/components/main_page/BookSlider.vue'
import HeroSection from '@/components/main_page/HeroSection.vue'
import GenreCard from '@/components/main_page/GenreCard.vue'
import ThreadCard from '@/components/main_page/ThreadCard.vue'

const store = useBookStore()

onMounted(() => {
  store.fetchBestsellers()
})
</script>

<style scoped>
  .genre-section, .bestseller-section, .thread-section {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    max-width: 1100px;
    margin: 0 auto 0 auto;    
  }
  .title {
    margin-bottom: 20px;
    font-weight: 700;
    text-align: center;
    width: 100%; 
    margin: 60px 0 20px;
  }
  html, body {
    height: 100%;
    min-height: 100%;
    margin: 0;
    padding: 0;
  }
</style>