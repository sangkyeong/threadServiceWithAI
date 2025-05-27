<template>
    <div v-if="isLoading" class="modal-overlay">
        <img :src="loadingImg" alt="로딩 중..." class="loading-img" />
        <h1 class="fw-bold text-light">잠시만 기다려 주세요...</h1>
    </div>
</template>

<script setup>
import loadingImg from '@/assets/loading_pencil.gif'

defineProps({
  isLoading: Boolean
})
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.loading-img {
  width: 100px;
  height: 100px;
}
</style>