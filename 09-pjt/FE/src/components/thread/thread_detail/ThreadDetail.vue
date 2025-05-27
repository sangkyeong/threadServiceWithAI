<template>
  <div class="container-fluid bg-dark text-white min-vh-100 py-4">
    <div class="container">
      <h1 class="mb-4 border-bottom pb-2 fw-bold">{{ thread?.title }}</h1>
      <div v-if="thread">
        <div class="text-center mb-4">
          <img :src="`http://127.0.0.1:8000${thread.cover_img}`" alt="Thread Cover Image" class="imgSize align-items-center " style="max-width: 600px; height: 350px;" @error="setDefaultImage">
        </div>
        <p>{{ thread.content }}</p>
        
        <h5 class="d-flex justify-content-between align-items-center">
          <div>
            <template v-if="thread && accountStore.user">
              <button @click="likeButton" class="btn p-0 border-0 bg-transparent">
                <i 
                  :class="[
                    'bi',
                    thread.liked ? 'bi-heart-fill text-danger' : 'bi-heart text-danger',
                    'fs-4'
                  ]"
                ></i>
              </button>
            </template>
            <template v-else>
                <i class="bi-heart text-danger fs-4"></i>
            </template>
            {{ likeCount }}
          </div>
          
          <span><i class="bi bi-book"></i> {{ thread.reading_date }}</span>
          <template v-if="thread?.writers_name">
            <span><i class="bi bi-pencil"></i> <RouterLink class="writer-name text-decoration-none" :to="{name:'userProfile', params:{'userName':thread?.writers_name}}">{{ thread?.writers_name }}</RouterLink></span>
          </template>
        </h5>
        <hr>

        <template v-if="accountStore.user && accountStore.user.pk === thread.user " >
          <div class="d-flex justify-content-between align-items-center">
            <button type="button" @click="onDeleteThread(thread.id)" class="btn btn-outline-danger">삭제</button>
            <button type="button" @click="onUpdateThread(thread.id)" class="btn btn-outline-primary">수정</button>
          </div>
        </template> 

        <h3 class="mt-5 mb-3 pb-2">댓글</h3>
        <div v-if="accountStore.user">
          <form @submit.prevent="onCommentCreate">
            <div class="d-flex justify-content-between align-items-center input-group mb-2">
              <input class="form-control me-2" type="text" placeholder="댓글을 입력하세요." v-model="commentModel">
              <button type="submit" class="btn btn-outline-light">등록</button>
            </div>
            <div class="text-center text-danger mb-2">
              <div v-if="errors.content">
                <i class="bi bi-exclamation-triangle-fill"></i>
                {{ errors.content[0] }}
              </div>
              <div v-if="errors.notice">
                <i class="bi bi-exclamation-triangle-fill"></i>
                {{ errors.notice }}
              </div>
            </div>
          </form>
          <p v-if="threadStore.errors">{{ threadStore.errors }}</p>
        </div>
        <div v-else class="mb-4">
          <input
            type="text"
            placeholder="로그인 후 입력하세요."
            class="form-control"
            readonly
          />
        </div>
        <div v-if="thread.comments && thread.comments.length > 0">
          <div
            v-for="comment in thread.comments"
            :key="comment.id"
            class="border border-white rounded-4 text-white mb-3"
          >
            <div class="p-2">
              <CommentItem
                :comment="comment"
                :threadUser="thread.user"
                :loginUser="accountStore.user?.pk"
              />
            </div>
          </div>
        </div>
        <div v-else>
          <p class="text-center">가장 먼저 댓글을 달아보세요!😊</p>
        </div>
      </div>
      <div v-else class="text-center text-danger">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <p>해당 쓰레드를 찾을 수 없습니다.</p>
      </div>
    </div>
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
      try {
        const result = await threadStore.likeThread(threadId)
        thread.value.like_count = result.like_count
        thread.value.liked = result.liked
      } catch (err) {
        errors.value = err.response?.data || '알 수 없는 오류가 발생했습니다.'
      }
    }

    const onCommentCreate = async () => {
      uiStore.isLoading = true
      errors.value = {}

      try {
        await threadStore.addThreadComment(threadId, commentModel.value)
        commentModel.value = '' // 입력창 초기화
        await threadStore.getThreadById(threadId) // 댓글 등록 후 상세 재조회
      } catch (err) {
        errors.value = err.response?.data || '알 수 없는 오류가 발생했습니다.'
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
  .writer-name {
    color: cadetblue;
    transition: color 0.3s;
    cursor: pointer;
  }

  .writer-name:hover {
    color: white;
  }
</style>