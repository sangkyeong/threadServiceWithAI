<template>
    <p>{{ comment.content }}</p>
    <template v-if="threadUser === loginUser || loginUser === comment.user">
        <button @click="onCommentRemove(comment.id)">삭제</button>
        <p class="text-danger small mb-2" v-if="errors.msg">{{ errors.msg }}</p>
    </template>
</template>

<script setup>
    import { ref } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRoute } from 'vue-router'
    const route = useRoute()
    const threadStore = useThreadStore()
    const threadId = route.params.threadId
    const errors = ref({})

    defineProps({
        comment : Object,
        threadUser: Number,
        loginUser: Number
    })

    const onCommentRemove = async (commentId) => {
        if(confirm('삭제하시겠습니까?')){
            try {
                await threadStore.removeThreadComment(commentId)
                await threadStore.getThreadById(threadId) // 댓글 등록 후 상세 재조회
            } catch (err) {
                errors.value = err.response?.data || {}
            }
        }
    }
</script>

<style scoped>

</style>