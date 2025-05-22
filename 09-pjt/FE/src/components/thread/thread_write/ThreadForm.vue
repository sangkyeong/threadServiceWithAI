<template>
    <h1>쓰레드 작성</h1>
    <form @submit.prevent="onThreadSave">
        <div>
            <p>제목</p>
            <input v-model="title" type="text" :placeholder="'제목을 입력하세요.'">
            
        </div>
        <div>
            <p>내용</p>
            <input v-model="content" type="text" :placeholder="'내용을 입력하세요.'">
        </div>
        <div>
            <p>읽은 날짜</p>
            <input v-model="readDate" type="date" :placeholder="'제목을 입력하세요.'">
        </div>
        <div>
            <p>도서정보</p>
        </div>
        <button>취소</button>
        <button type="submit">저장</button>
        <p v-if="store.errors">{{ store.errors }}</p>
    </form>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRouter, useRoute } from 'vue-router'
    const route = useRoute()
    const router = useRouter()
    // import BookCard from '@/'
    const store = useThreadStore()
    const title = ref('')
    const bookId = Number(route.params.bookId)
    const content = ref('')
    const readDate = ref('')

    const onThreadSave = () => {
        store.addThreads(title.value, bookId, content.value, readDate.value)
    }

    onMounted(() => {
        store.errors = ''
    })
</script>

<style scoped>

</style>