<template>
  <RouterLink 
    :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
    class="thread-card text-decoration-none text-light"
  >
    <img 
      :src="`http://127.0.0.1:8000${thread.cover_img}`"
      @error="setDefaultImage"
      alt="Thread Cover Image"
      class="thread-cover"
    />
    <div class="thread-info d-flex flex-column">
      <h3 class="thread-title">{{ thread.title }}</h3>

      <!-- 하단 정렬 영역 -->
      <div class="thread-meta d-flex justify-content-between align-items-center mt-auto small text-white-50">
        <span>{{ thread.writers_name }}</span>
        <span><i class="bi bi-heart-fill text-danger me-1"></i>{{ thread.like_count }}</span>
      </div>
    </div>
  </RouterLink>
</template>

<script setup>
defineProps({
  thread: Object,
  threadId: [Number, String],
  showLink: { type: Boolean, default: true }
})

const setDefaultImage = (e) => {
  e.target.src = "http://127.0.0.1:8000/static/threads/threadImage.jpg"
}
</script>

<style scoped>
.thread-card {
  width: 300px;
  height: 390px;
  overflow: hidden;
  background-color: #2a2a2a;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 0 5px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s;
}

.thread-card:hover {
  transform: translateY(-4px);
  color: #ff5656;
}

.thread-cover {
  width: 100%;
  height: 190px;
  object-fit: cover;
  border-radius: 8px;
}

.thread-info {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  margin-top: 0.75rem;
}

.thread-title {
  font-weight: bold;
  font-size: 1.1rem;
  color: #ffffff;
  margin-bottom: 0.5rem;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
