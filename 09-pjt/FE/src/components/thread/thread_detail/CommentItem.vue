<template>
    <p>{{ comment.content }}</p>
    <button @click="onCommentRemove(comment.id)">삭제</button>
</template>

<script setup>
    import { useThreadStore } from '@/stores/thread.js'
    import { useRoute } from 'vue-router'
    const route = useRoute()
    const threadStore = useThreadStore()
    const threadId = route.params.threadId

    defineProps({
        comment : Object
    })

    const onCommentRemove = async (commentId) => {
        if(confirm('삭제하시겠습니까?')){
            await threadStore.removeThreadComment(commentId)
            await threadStore.getThreadById(threadId) // 댓글 등록 후 상세 재조회
        }
    }
</script>

<style scoped>

</style>