<template>
    <div class="book-card h-100 m-2 text-white border-0 shadow-sm">
      <div class="card-body d-flex flex-column justify-content-between">
        
        <RouterLink 
            :to="{name:'threadDetail', params:{'threadId':thread.id}}" 
            class="text-decoration-none text-light"
        >
          <img 
          :src="`http://127.0.0.1:8000${thread.cover_img}`" 
            alt="Thread Cover Image" 
            class="card-img-top mb-2"
            @error="setDefaultImage" 
            style="width: 100%; height: 200px; object-fit: cover;"
          >
          <h6 class="card-title fw-bold mb-1">{{ thread.title }}</h6>
          <div class="d-flex justify-content-between align-items-center small text-white-50">
            <span>{{ thread.writers_name }}</span>
            <span><i class="bi bi-heart-fill text-danger me-1"></i>{{ thread.like_count }}</span>
          </div>
          
        </RouterLink>
      </div>
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

    flex-direction: column;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s;
  }

  .book-card:hover {
    color: #ff5656;
    transform: translateY(-4px);
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