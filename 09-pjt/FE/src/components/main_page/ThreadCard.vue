<template>
  <div class="text-center container">
    <div class="thread-list">
      <RouterLink
        v-for="thread in visibleBooks"
        :key="thread.id"
        :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
        class="thread-card"
        >
          <img :src="`http://127.0.0.1:8000${thread.cover_img}`" :alt="thread.title" @error="setDefaultImage">
          <div class="thread-info">
            <div class="thread-title">{{ thread.title }}</div>
            <div class="thread-desc">{{ thread.desc }}</div>
        </div>
      </RouterLink>
    </div>
    <!-- 펼처보기 btn -->
    <div class="text-center mt-4">
      <button
        v-if="visibleCount < threads.length"
        @click="visibleCount += 8"
        class="btn btn-outline-dark"
      >
        + 펼처보기
      </button>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useThreadStore } from '@/stores/thread.js'
  import { RouterLink } from 'vue-router';

  const threadStore = useThreadStore()
  const threads = ref([])
  const visibleCount = ref(8)


  onMounted(async () => {
    await threadStore.getAllThreads()
    threads.value = threadStore.threads
  })

  const setDefaultImage = (e) => {
    e.target.src = "http://127.0.0.1:8000/static/threads/threadImage.jpg";
  }

  const visibleBooks = computed(() => {
    return threads.value.slice(0, visibleCount.value)
  })
</script>

<style scoped>
  .thread-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 40px 32px;
    max-width: 100%;
    margin: 0 auto;
    padding: 5px 0;
  }

  .thread-card {
    width: 240px;
    text-decoration: none;
    color: inherit;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    overflow: hidden;
    transition: transform 0.2s;
  }

  .thread-card:hover {
    transform: scale(1.05);
  }

  .thread-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
  }

  .thread-info {
    padding: 12px;
  }

  .thread-title {
    font-weight: bold;
    font-size: 16px;
    margin-bottom: 6px;
  }

  .thread-desc {
    font-size: 14px;
    color: #555;
  }

</style>
