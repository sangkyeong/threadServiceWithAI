<template v-if="accountStore.user">
  <div class="container-fluid bg-dark text-white min-vh-100 py-4">
    <div class="container">
      <h1 class="mb-4 border-bottom pb-2 fw-bold">쓰레드 수정</h1>
      <div v-if="accountStore.user.pk === thread.user ">
        <form @submit.prevent="onThreadUpdate">
          <div>
            <h3 class="mb-3">제목</h3>
            <input v-model="title" type="text" class="form-control mb-2" placeholder="제목을 입력하세요." />
                <div v-if="errors.title" class="text-danger small mb-2">
                    <i class="bi bi-exclamation-triangle-fill"></i>
                    {{ errors.title[0] }}
                </div>
          </div>
          <hr>
          <div>
            <h3 class="mb-3">내용</h3>
            <input v-model="content" type="text" class="form-control mb-2" placeholder="내용을 입력하세요." />
            <div v-if="errors.content" class="text-danger small mb-2">
                <i class="bi bi-exclamation-triangle-fill"></i>
                {{ errors.content[0] }}
            </div>
          </div>
          <hr>
          <div>
            <h3 class="mb-3">읽은 날짜</h3>
            <input v-model="readDate" type="date" class="form-control mb-2" />
            <div v-if="errors.reading_date" class="text-danger small mb-2">
                <i class="bi bi-exclamation-triangle-fill"></i>
                {{ errors.reading_date[0] }}
            </div>
          </div>
          <hr>
          <div>
            <h3 class="mb-3">도서정보</h3>
            <BookCard :book="book" :bookId="bookId" :showLink="false"/>
          </div>
          <hr>
          <div class="d-flex justify-content-between align-items-center">
            <button type="button" @click="onCancel" class="btn btn-outline-danger">취소</button>
            <button type="submit" class="btn btn-outline-primary">저장</button>
            <p v-if="threadStore.errors">
              <i class="bi bi-exclamation-triangle-fill"></i>
              {{ threadStore.errors }}
            </p>
          </div>
        </form>
      </div>
    </div>
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
        errors.value = err.response?.data || '알 수 없는 오류가 발생했습니다.'
      }
    }

    const onCancel = () => {
        router.back()
    }
</script>

<style scoped>

</style>