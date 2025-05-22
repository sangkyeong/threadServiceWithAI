<template>
  <h1>쓰레드 수정</h1>
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
    <p v-if="threadStore.errors">{{ threadStore.errors }}</p>
  </form>
</template>
<script setup>
    import { ref, onMounted, computed } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRouter, useRoute } from 'vue-router'

    const route = useRoute()
    const router = useRouter()
    const threadStore = useThreadStore()
    
    // 초기값 설정
    const title = ref('')
    const content = ref('')
    const readDate = ref('')
    
    onMounted(async () => {
      await threadStore.getThreadById(route.params.threadId)
      title.value = threadStore.threadDetail.title
      content.value = threadStore.threadDetail.content
      readDate.value = threadStore.threadDetail.reading_date
      threadStore.errors = ''
    })

    const onThreadUpdate = () => {
      threadStore.updateThread(route.params.threadId, {
          title: title.value,
          content: content.value,
          reading_date: readDate.value,
      })
    }

    const onCancel = () => {
        router.back()
    }
</script>

<style scoped>

</style>