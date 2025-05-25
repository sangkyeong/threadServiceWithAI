<template>
  <div class="container py-5">
    <h2>마이페이지</h2>
    <p><strong>아이디:</strong> {{ user.username }}</p>
    <p><strong>이메일:</strong> {{ user.email }}</p>
    <p><strong>성별:</strong> {{ user.gender }}</p>
    <p><strong>나이:</strong> {{ user.age }}</p>
    <button class="btn btn-danger" @click="logoutHandler">로그아웃</button>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'

const accountStore = useAccountStore()
const router = useRouter()

const user = accountStore.user

const logoutHandler = () => {
  accountStore.logout()
  router.push({ name: 'home' })
}
</script>