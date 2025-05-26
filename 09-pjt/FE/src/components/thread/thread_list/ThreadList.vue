<template>
  <div class="container-fluid bg-dark text-white min-vh-100 py-4">
    <div class="container">
      <h2 class="mb-4 border-bottom pb-2 fw-bold">쓰레드 목록</h2>
      <div v-if="threadStore.threads.length > 0" class="row g-4">
        <ThreadItem
          v-for="thread in threadStore.threads"
          :key="thread.id"
          :thread="thread"
          class="col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2"
        />
      </div>
      <div v-else class="text-center mt-5">
        <p>쓰레드가 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import ThreadItem from '@/components/thread/thread_list/ThreadItem.vue'
import { useThreadStore } from '@/stores/thread.js'
const threadStore = useThreadStore()
onMounted(() => {
  threadStore.getAllThreads()
})

</script>

<style scoped>
h2 {
  border-color: rgba(255, 255, 255, 0.1);
}
</style>