<template>
    <h2>새로운 쓰레드 작성</h2>
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
    import { useRoute } from 'vue-router'
    const route = useRoute()
    // import BookCard from '@/'
    const store = useThreadStore()
    const title = ref('')
    const bookId = ref(route.params.bookId)
    const content = ref('')
    const readDate = ref('')

    
    const onThreadSave = () => {
        console.log(bookId.value)
        store.addThreads(title.value, bookId.value, content.value, readDate.value)
    }
</script>

<style scoped>

</style>