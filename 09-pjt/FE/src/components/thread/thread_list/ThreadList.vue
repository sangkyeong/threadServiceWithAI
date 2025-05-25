<template>
  <div class="container-fluid bg-dark text-white min-vh-100">
    <h1>쓰레드 목록</h1>
    <div>
      <div v-if="threadStore.threads.length > 0" class="row g-4">
        <ThreadItem class="col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2"
          v-for="thread in threadStore.threads"
          :key="thread.id"
          :thread="thread"
        />
      </div>
      <div v-else>
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

</style>