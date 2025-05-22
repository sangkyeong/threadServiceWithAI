<template>
  <h1>수정</h1>
  <form @submit.prevent="onThreadUpdate">
    <div>
      <p>제목</p>
      <input v-model="title" type="text" placeholder="제목을 입력하세요." />
    </div>
    <div>
      <p>내용</p>
      <input v-model="content" type="text" placeholder="내용을 입력하세요." />
    </div>
    <div>
      <p>읽은 날짜</p>
      <input v-model="readDate" type="date" />
    </div>
    <div>
      <p>도서정보</p>
      <!-- bookId 등 필요하면 추가 -->
    </div>
    <button type="button" @click="onCancel">취소</button>
    <button type="submit">저장</button>
  </form>
</template>
<script setup>
    import { ref, onMounted } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRouter, useRoute } from 'vue-router'

    const route = useRoute()
    const router = useRouter()
    const store = useThreadStore()

    const threadId = route.params.threadId

    const thread = store.threads.find(t => t.id === Number(threadId))

    // 초기값 설정
    const title = ref(thread ? thread.title : '')
    const content = ref(thread ? thread.content : '')
    const readDate = ref(thread ? thread.readDate : '')

    const onThreadUpdate = () => {
    store.updateThread(threadId, {
        title: title.value,
        content: content.value,
        readDate: readDate.value,
    })
    router.push({ name: 'threads' })
    }

    const onCancel = () => {
        router.back()
    }
</script>

<style scoped>

</style>