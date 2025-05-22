<template>
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
    </form>
</template>

<script setup>
    import { ref } from 'vue'
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
        router.push({name: 'threads'})
    }
</script>

<style scoped>

</style>