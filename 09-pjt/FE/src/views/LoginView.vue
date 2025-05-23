<template>
    <div class="container d-flex justify-content-center align-items-center min-vh-100">
      <div class="card p-4 shadow" style="max-width: 500px; width: 100%;">

        <h1 class="text-center mb-4">로그인</h1>
        <form @submit.prevent="loginHandler">
          <input v-model="username" placeholder="아이디" class="form-control mb-2" />
          <input v-model="password" type="password" placeholder="비밀번호" class="form-control mb-3" />
          <input type="checkbox" class="mb-3">아이디 저장
          <button class="btn btn-primary w-100">로그인</button>
          <br>
        </form>
        <RouterLink :to="{ name: 'signup' }" >아직 회원이 아니신가요?</RouterLink>
      </div>
    </div>

</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

const router = useRouter()
const username = ref('')
const password = ref('')
const accountStore = useAccountStore()

const loginHandler = () => {
  accountStore.login(username.value, password.value)
    .then(() => {
      router.push({ name: 'home' })
    })
    .catch(err => {
      console.error('로그인 실패2:', err)
      alert('로그인 정보가 올바르지 않습니다.')
    })
  }
  

</script>
