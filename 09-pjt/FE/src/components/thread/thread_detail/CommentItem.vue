<template>
    <div class="d-flex justify-content-between align-items-center">
        <p>{{ comment.content }}</p>
        <template v-if="threadUser === loginUser || loginUser === comment.user">
            <button 
                @click="onCommentRemove(comment.id)"
                class="border rounded-4"  
                @mouseenter="isHover = true"
                @mouseleave="isHover = false"
            >
                <i :class="isHover ? 'bi bi-trash-fill' : 'bi bi-trash'"></i>
            </button>            
        </template>
    </div>
    <div class="text-danger small mb-2" v-if="errors.msg">
        <i class="bi bi-exclamation-triangle-fill"></i>
        {{ errors.msg }}
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import { useThreadStore } from '@/stores/thread.js'
    import { useRoute } from 'vue-router'
    const route = useRoute()
    const threadStore = useThreadStore()
    const threadId = route.params.threadId
    const errors = ref({})
    const isHover = ref(false)

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
                errors.value = err.response?.data || '알 수 없는 오류가 발생했습니다.'
            }
        }
    }
</script>