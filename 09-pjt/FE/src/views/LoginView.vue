<template>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <div class="card p-4 shadow" style="max-width: 500px; width: 100%;">
      <h1 class="text-center mb-4">로그인</h1>
      <form @submit.prevent="loginHandler">
        <input v-model="username" placeholder="아이디" class="form-control mb-2" />
        <input v-model="password" type="password" placeholder="비밀번호" class="form-control mb-3" />
        <label class="mb-3">
          <input v-model="saveId" type="checkbox" /> 아이디 저장
        </label>
        <button type="submit" class="btn btn-primary w-100">로그인</button>
        <br>
      </form>
      <RouterLink :to="{ name: 'signup' }">아직 회원이 아니신가요?</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
import { useCookies } from 'vue3-cookies'

const { cookies } = useCookies()
const router = useRouter()
const username = ref('')
const password = ref('')
const accountStore = useAccountStore()
const saveId = ref(false)

onMounted(() => {
  const savedId = cookies.get('saveId')
  if (savedId) {
    username.value = savedId
    saveId.value = true
  }
})

const loginHandler = () => {
  accountStore.login(username.value, password.value)
    .then(() => {
      // 로그인 성공 후에만 쿠키 set/remove!
      if (saveId.value) {
        cookies.set('saveId', username.value, '7d')
      } else {
        cookies.remove('saveId')
      }
      router.push({ name: 'home' })
    })
    .catch(err => {
      if (err.response && err.response.status === 400) {
        alert('아이디나 비밀번호를 확인해주세요.');
      }
      // alert('로그인 정보가 올바르지 않습니다.')
      username.value = ''
      password.value = ''
    })
}
</script>
