<template>
  <h1>쓰레드 상세</h1>
  <div v-if="thread">
    <h2>{{ thread.title }}</h2>
    <p>{{ thread.content }}</p>
    <p>읽은 날짜: {{ thread.readDate }}</p>
    <button type="button" @click="onDeleteThread(thread.id)">삭제</button>
    <button type="button" @click="onUpdateThread(thread.id)">수정</button>
  </div>
  <div v-else>
    <p>해당 쓰레드를 찾을 수 없습니다.</p>
  </div>
</template>

<script setup>
    import { useRouter, useRoute } from 'vue-router'
    import { useThreadStore } from '@/stores/thread.js'

    const router = useRouter()
    const route = useRoute()
    const threadStore = useThreadStore()
    const threadId = route.params.threadId
    const thread = threadStore.getThreadById(threadId)

    const onDeleteThread = (threadId) => {
        threadStore.removeThread(threadId)
        router.push({name: 'threads'})
    }

    const onUpdateThread = (threadId) => {
        router.push({name: 'threadUpdate'})
    }
</script>

<style scoped>

</style>