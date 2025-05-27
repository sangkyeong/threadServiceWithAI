<template>
  <div class="container-fluid bg-dark text-white min-vh-100">
    <div class="container py-4">
      <h2 class="mb-4 border-bottom pb-2 fw-bold">쓰레드 목록</h2>
        <div v-if="threadStore.threads?.length > 0" class="row g-4 justify-content-center">
          <ThreadItem
            v-for="thread in visibleThreads"
            :key="thread.id"
            :thread="thread"
            :threadId="thread.id"
            class="col-6 col-sm-6 col-md-4 col-lg-3 m-2 "
          />
        </div>
        <div v-else class="text-center mt-5">
          <p>쓰레드가 없습니다.</p>
        </div>

        <!-- 펼처보기 btn -->
        <div class="text-center mt-4">
          <button
            v-if="visibleCount < threadStore.threads.length"
            @click="visibleCount += 20"
            class="btn btn-outline-light"
          >
            + 펼처보기
          </button>
        </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed  } from 'vue'
import ThreadItem from '@/components/thread/thread_list/ThreadItem.vue'
import { useThreadStore } from '@/stores/thread.js'
const visibleCount = ref(20)
const threadStore = useThreadStore()
onMounted(() => {
  threadStore.getAllThreads()
})

const visibleThreads = computed(() => {
  return threadStore.threads.slice(0, visibleCount.value)
})

</script>

<style scoped>
h2 {
  border-color: rgba(255, 255, 255, 0.1);
}
</style>