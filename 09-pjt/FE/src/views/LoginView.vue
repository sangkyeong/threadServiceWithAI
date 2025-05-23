<template>
  <div class="container">
    <h1>로그인</h1>
    <form @submit.prevent="loginHandler">
      <input v-model="username" placeholder="아이디" class="form-control mb-2" />
      <input v-model="password" type="password" placeholder="비밀번호" class="form-control mb-2" />
      <button class="btn btn-primary w-100">로그인</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const username = ref('')
const password = ref('')
const accountStore = useAccountStore()

const loginHandler = () => {
  accountStore.login(username.value, password.value)
}
</script>
