<template>
  <div>
    <h1>쓰레드 목록</h1>
    <div>
      <div v-if="threadStore.threads">
        <ThreadItem
          v-for="thread in threadStore.threads"
          :key="thread.id"
          :thread="thread"
        />
      </div>
      <div v-else>
        <h2>쓰레드가 없습니다.</h2>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import ThreadItem from '@/components/thread/thread_list/ThreadItem.vue'
import { useThreadStore } from '@/stores/thread.js'
const threads = ref('')
const threadStore = useThreadStore()

onMounted(() => {
  threadStore.getAllThreads()
})

</script>

<style scoped>

</style>