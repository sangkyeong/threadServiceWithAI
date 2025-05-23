<template>
  <div class="container text-white mt-5">
    <h1>회원가입</h1>
    <form @submit.prevent="signupHandler">
      <input v-model="username" placeholder="아이디" class="form-control mb-2" />
      <input v-model="email" placeholder="이메일" class="form-control mb-2" />
      <input v-model="password1" type="password" placeholder="비밀번호" class="form-control mb-2" />
      <input v-model="password2" type="password" placeholder="비밀번호 확인" class="form-control mb-2" />
      <button class="btn btn-primary w-100">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const username = ref('')
const email = ref('')
const password1 = ref('')
const password2 = ref('')

const accountStore = useAccountStore()

const signupHandler = () => {
  accountStore.signup(username.value, email.value, password1.value, password2.value)
}
</script>

