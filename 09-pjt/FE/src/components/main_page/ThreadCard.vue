<template>
  <div class="thread-list">
    <RouterLink
      v-for="thread in threads"
      :key="thread.id"
      :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
      class="thread-card"
      >
        <img :src="thread.image" :alt="thread.title" />
        <div class="thread-info">
          <div class="thread-title">{{ thread.title }}</div>
          <div class="thread-desc">{{ thread.desc }}</div>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useThreadStore } from '@/stores/thread.js'
  import { RouterLink } from 'vue-router';

  const threadStore = useThreadStore()
  const threads = ref([])

  onMounted(async () => {
    await threadStore.getAllThreads()
    threads.value = threadStore.threads
  })
</script>

<style scoped>
  .thread-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 32px;
    max-width: 1000px;
    margin: 0 auto;
    padding: 40px 0;
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
