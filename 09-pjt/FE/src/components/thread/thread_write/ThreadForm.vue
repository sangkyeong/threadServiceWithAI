<template>
    <h1>쓰레드 작성</h1>
    <form @submit.prevent="onThreadSave">
        <div>
            <p>제목</p>
            <input v-model="title" type="text" :placeholder="'제목을 입력하세요.'">
            
        </div>
        <hr>
        <div>
            <p>내용</p>
            <textarea v-model="content" type="text" :placeholder="'내용을 입력하세요.'">
            </textarea>
        </div>
        <hr>
        <div>
            <p>읽은 날짜</p>
            <input v-model="readDate" type="date" :placeholder="'제목을 입력하세요.'">
        </div>
        <hr>
        <div>
            <p>도서정보</p>
            <BookCard :book="book" :bookId="bookId" :showLink="false"/>
        </div>
        <hr>
        <button type="button" @click="onCancel">취소</button>
        <button type="submit">저장</button>
        <p v-if="store.errors">{{ store.errors }}</p>
    </form>
</template>

<script setup>
    import { ref, onMounted, computed } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRoute, useRouter } from 'vue-router'
    import BookCard from '@/components/book/BookCard.vue'
    import { useBookStore } from '@/stores/book'
    import { useUIStore } from '@/stores/ui.js'

    const route = useRoute()
    const router = useRouter()
    const store = useThreadStore()
    const uiStore = useUIStore()

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
        }finally{
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