<template>
  <h1>쓰레드 상세</h1>
  <div>
    <h4>♥{{ likeCount }}</h4>
    <div v-if="thread && accountStore.user">
      <button @click="likeButton">
        {{ thread.liked ? '좋아요 취소' : '좋아요' }}
      </button>
    </div>
    <p>작성자: <RouterLink :to="{name:'userProfile', params:{userName:thread?.writers_name}}">{{ thread?.writers_name }}</RouterLink></p>
  </div>
  <div v-if="thread">
    <img :src="`http://127.0.0.1:8000${thread.cover_img}`" alt="Thread Cover Image" class="imgSize" @error="setDefaultImage">
    <h2>{{ thread.title }}</h2>
    <p>{{ thread.content }}</p>
    <p>읽은 날짜: {{ thread.reading_date }}</p>
    <template v-if="accountStore.user && accountStore.user.pk === thread.user ">
      <button type="button" @click="onDeleteThread(thread.id)">삭제</button>
      <button type="button" @click="onUpdateThread(thread.id)">수정</button>
    </template>
    <hr>
    <h3>댓글</h3>
    <div v-if="accountStore.user">
      <form @submit.prevent="onCommentCreate">
        <input type="text" placeholder="댓글을 입력하세요." v-model="commentModel">
        <button type="submit">등록</button>
        <div v-if="errors.content" class="text-danger small mb-2">{{ errors.content[0] }}</div>
      </form>
      <p v-if="threadStore.errors">{{ threadStore.errors }}</p>
    </div>
    <div v-else>
      <input type="text" placeholder="로그인 후 입력하세요." readonly="readonly">
    </div>
    <div v-if="thread.comments && thread.comments.length > 0">
      <div v-for="comment in thread.comments" :key="comment.id">
        <CommentItem 
          :comment="comment"
          :threadUser="thread.user"
          :loginUser="accountStore.user?.pk"
        />
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
    import { useUIStore } from '@/stores/ui.js'
    import { useAccountStore } from '@/stores/accounts.js'

    const router = useRouter()
    const route = useRoute()
    const threadStore = useThreadStore()
    const accountStore = useAccountStore()
    const threadId = route.params.threadId
    const thread = computed(() => threadStore.threadDetail)
    const commentModel = ref('')
    const errors = ref({})

    const uiStore = useUIStore()
    const likeCount = computed(() => {
      return thread.value && thread.value.like_count !== undefined
        ? thread.value.like_count
        : 0
    })
    
    onMounted(async () => {
      await threadStore.getThreadById(threadId)
      threadStore.errors = ''
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
      thread.value.like_count = result.like_count
      thread.value.liked = result.liked
    }

    const onCommentCreate = async () => {
      uiStore.isLoading = true
      errors.value = {}

      try {
        await threadStore.addThreadComment(threadId, commentModel.value)
        commentModel.value = '' // 입력창 초기화
        await threadStore.getThreadById(threadId) // 댓글 등록 후 상세 재조회
      } catch (err) {
        errors.value = err.response?.data || {}
      } finally {
        uiStore.isLoading = false
      }
    }
    
    const setDefaultImage = (e) => {
      e.target.src = "http://127.0.0.1:8000/static/threads/threadImage.jpg";
    }
</script>

<style scoped>
  .imgSize{
    width: 800px;
    height: 500px;
  }
</style>