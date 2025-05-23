<template>
  <h1>쓰레드 상세</h1>
  <div>
    <h4>♥{{ likeCount }}</h4>
    <div v-if="thread">
    <button @click="likeButton">
      {{ thread.liked ? '좋아요 취소' : '좋아요' }}
    </button>
    </div>
  </div>
  <div v-if="thread">
    <h2>{{ thread.title }}</h2>
    <p>{{ thread.content }}</p>
    <p>읽은 날짜: {{ thread.reading_date }}</p>
    <button type="button" @click="onDeleteThread(thread.id)">삭제</button>
    <button type="button" @click="onUpdateThread(thread.id)">수정</button>
    <hr>
    <h3>댓글</h3>
    <form @submit.prevent="onCommentCreate">
      <input type="text" placeholder="댓글을 입력하세요." v-model="commentModel">
      <button type="submit">등록</button>
    </form>
    <div v-if="thread.comments.length > 0">
      <div v-for="comment in thread.comments" :key="comment.id">
        <CommentItem :comment="comment"/>
        <hr>
      </div>
    </div>
    <div v-else>
      <p>댓글이 없습니다.</p>
    </div>
  </div>
  <div v-else>
    <p>해당 쓰레드를 찾을 수 없습니다.</p>
  </div>
</template>

<script setup>
    import CommentItem from '@/components/thread/thread_detail/CommentItem.vue';
    import { ref, computed, onMounted } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
    import { useThreadStore } from '@/stores/thread.js'

    const router = useRouter()
    const route = useRoute()
    const threadStore = useThreadStore()
    const threadId = route.params.threadId
    const thread = computed(() => threadStore.threadDetail)
    const commentModel = ref('')
    const likeCount = computed(() => {
      return thread.value && thread.value.like_count !== undefined
        ? thread.value.like_count
        : 0
    })
    
    onMounted(async () => {
      await threadStore.getThreadById(threadId)
    })

    const onDeleteThread = () => {
      if(confirm('이 쓰레드를 삭제하시겠습니까?')){
        threadStore.removeThread(threadId)
      }
    }

    const onUpdateThread = () => {
        router.push({name: 'threadUpdate', params: {threadId}})
    }

    const likeButton = async () => {
      const result = await threadStore.likeThread(threadId)
      // likeThread에서 like_count, liked 반환
      thread.value.like_count = result.like_count
      thread.value.liked = result.liked
    }

    const onCommentCreate = async () => {
      await threadStore.addThreadComment(threadId, commentModel.value)
      await threadStore.getThreadById(threadId) // 댓글 등록 후 상세 재조회
      commentModel.value = '' // 입력창 초기화
    }
</script>

<style scoped>

</style>