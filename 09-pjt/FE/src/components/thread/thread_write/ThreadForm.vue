<template>
    <div v-if="accountStore.user">
        <div class="container-fluid bg-dark text-white min-vh-100 py-4">
            <div class="container">
                <h1 class="mb-4 border-bottom pb-2 fw-bold">쓰레드 작성</h1>
                <form @submit.prevent="onThreadSave">
                    <div>
                        <h3 class="mb-3">제목</h3>
                        <input v-model="title" class="form-control mb-2" type="text" :placeholder="'제목을 입력하세요.'">
                        <div v-if="errors.title" class="text-danger small mb-2">
                            <i class="bi bi-exclamation-triangle-fill"></i>
                            {{ errors.title[0] }}
                        </div>
                    </div>
                    <hr>
                    <div>
                        <h3 class="mb-3">내용</h3>
                        <textarea v-model="content" class="form-control mb-2" type="text" :placeholder="'내용을 입력하세요.'">
                        </textarea>
                        <div v-if="errors.content" class="text-danger small mb-2">
                            <i class="bi bi-exclamation-triangle-fill"></i>
                            {{ errors.content[0] }}
                        </div>
                    </div>
                    <hr>
                    <div>
                        <h3 class="mb-3">읽은 날짜</h3>
                        <input v-model="readDate" class="form-control mb-2" type="date" :placeholder="'제목을 입력하세요.'">
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
                        <p v-if="store.errors">
                            <i class="bi bi-exclamation-triangle-fill"></i>
                            {{ store.errors }}
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
    import { useRoute, useRouter } from 'vue-router'
    import BookCard from '@/components/book/BookCard.vue'
    import { useBookStore } from '@/stores/book'
    import { useUIStore } from '@/stores/ui.js'
    import { useAccountStore } from '@/stores/accounts'

    const accountStore = useAccountStore()

    const route = useRoute()
    const router = useRouter()
    const store = useThreadStore()
    const uiStore = useUIStore()
    const errors = ref({})

    const title = ref('')
    const bookId = Number(route.params.bookId)
    const content = ref('')
    const readDate = ref('')

    const booksStore = useBookStore()
    const book = computed(() => booksStore.books.find(b => b.id === bookId) || {})
    
    const onThreadSave = async () => {
        uiStore.isLoading = true
        try {
            await store.addThreads(title.value, bookId, content.value, readDate.value)
        } catch (err) {
            errors.value = err.response?.data || '알 수 없는 오류가 발생했습니다.'
        } finally{
            uiStore.isLoading = false
        }
    }
    
    onMounted(() => {
        if (!booksStore.books.length) {
            booksStore.fetchBooks()
        }
        store.errors = ''
    })

    const onCancel = () => {
        router.back()
    }
</script>

<style scoped>

</style>