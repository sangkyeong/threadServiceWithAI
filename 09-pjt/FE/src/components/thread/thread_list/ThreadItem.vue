<template>
    <div class="book-card">
        <img :src="`http://127.0.0.1:8000${thread.cover_img}`" alt="Thread Cover Image" class="book-cover" @error="setDefaultImage">
        <RouterLink 
            :to="{name:'threadDetail', params:{'threadId':thread.id}}" 
        >
            {{ thread.title }}
        </RouterLink>
    </div>
</template>

<script setup>
    import { RouterLink } from 'vue-router'
    defineProps({
        thread: Object,
        category: Object
    })
    const setDefaultImage = (e) => {
      e.target.src = "http://127.0.0.1:8000/static/threads/threadImage.jpg";
    }
</script>

<style scoped>
.book-card {
    background-color: #2a2a2a;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0,0,0,0.2);
    display: flex;
    gap: 1rem;
    align-items: center;
    color: inherit;
    text-decoration: none;
  }

  .book-card:hover {
    color: #ff5656;
  }

  .book-cover {
    width: 80px;
    height: 120px;
    object-fit: cover;
    border-radius: 5px;
  }

  .book-info {
    display: flex;
    flex-direction: column;
  }

  .book-title {
    font-weight: bold;
    font-size: 1.1rem;
    color: #ffffff;
    margin-bottom: 0.5rem;
  }

  .book-meta {
    font-size: 0.9rem;
    color: #bbbbbb;
    margin-bottom: 0.5rem;
  }

  .book-award {
    font-size: 0.9rem;
    color: #dddddd;
  }
</style>