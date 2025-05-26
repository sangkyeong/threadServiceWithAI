<template v-if="accountStore.user">
  <h1>쓰레드 수정</h1>
  <div v-if="accountStore.user.pk === thread.user ">
    <form @submit.prevent="onThreadUpdate">
      <div>
        <p>제목</p>
        <input v-model="title" type="text" placeholder="제목을 입력하세요." />
        <div v-if="errors.title" class="text-danger small mb-2">{{ errors.title[0] }}</div>
      </div>
      <div>
        <p>내용</p>
        <input v-model="content" type="text" placeholder="내용을 입력하세요." />
        <div v-if="errors.content" class="text-danger small mb-2">{{ errors.content[0] }}</div>
      </div>
      <div>
        <p>읽은 날짜</p>
        <input v-model="readDate" type="date" />
        <div v-if="errors.reading_date" class="text-danger small mb-2">{{ errors.reading_date[0] }}</div>
      </div>
      <div>
        <p>도서정보</p>
        <BookCard :book="book" :bookId="bookId" :showLink="false"/>
      </div>
      <button type="button" @click="onCancel">취소</button>
      <button type="submit">저장</button>
      <p v-if="threadStore.errors">{{ threadStore.errors }}</p>
    </form>
  </div>
</template>
<script setup>
    import { ref, onMounted, computed } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRouter, useRoute } from 'vue-router'
    import { useAccountStore } from '@/stores/accounts.js'
    import BookCard from '@/components/book/BookCard.vue'
    import { useBookStore } from '@/stores/book'

    const route = useRoute()
    const router = useRouter()
    const threadStore = useThreadStore()
    const accountStore = useAccountStore()
    
    // 초기값 설정
    const thread = computed(() => threadStore.threadDetail)
    const title = ref('')
    const content = ref('')
    const readDate = ref('')
    const errors = ref({})
    
    const booksStore = useBookStore()
    const bookId = Number(route.params.threadId)
    const book = computed(() => booksStore.books.find(b => b.id === bookId) || {})

    onMounted(async () => {
      await threadStore.getThreadById(route.params.threadId)
      title.value = threadStore.threadDetail.title
      content.value = threadStore.threadDetail.content
      readDate.value = threadStore.threadDetail.reading_date
      threadStore.errors = ''
    })

    const onThreadUpdate = async () => {
      try {
          await threadStore.updateThread(route.params.threadId, {
            title: title.value,
            content: content.value,
            reading_date: readDate.value,
         })
      } catch (err) {
        errors.value = err.response?.data || {}
      }
    }

    const onCancel = () => {
        router.back()
    }
</script>

<style scoped>

</style>