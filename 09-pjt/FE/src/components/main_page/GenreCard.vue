<template>
  <section class="genre-section">
    <div class="genre-list">
      <RouterLink
        v-for="genre in genres"
        :key="genre.id"
        :to="{ name: 'books', query: { category: genre.id } }"
        class="genre-card"
      >
        <img :src="`http://127.0.0.1:8000/static/${genre.image}`" :alt="genre.name" />
        <div class="genre-name">{{ genre.name }}</div>
      </RouterLink>
    </div>
  </section>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useCategoryStore } from '@/stores/category.js'
import { RouterLink } from 'vue-router'

const categoryStore = useCategoryStore()
const genres = ref([])

onMounted(async () => {
  await categoryStore.fetchCategories()
  genres.value = categoryStore.categories
})
</script>

<style scoped>

  .genre-section {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .genre-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 40px 32px;
    width: fit-content; 
  }

  .genre-card {
    width: 200px;
    text-align: center;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s ease;
  }

  .genre-card img {
    width: 100%;
    aspect-ratio: 3 / 4;
    object-fit: cover;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  .genre-name {
    margin-top: 12px;
    font-weight: 600;
    font-size: 15px;
  }

  .genre-card:hover {
    transform: scale(1.08);
  }

</style>

