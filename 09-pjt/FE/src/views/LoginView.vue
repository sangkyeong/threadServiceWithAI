<template>
  <div class="container-fluid bg-dark text-white py-5 min-vh-100 d-flex justify-content-center align-items-start">
    <div class="w-100" style="max-width: 32rem;">
      <h1 class="text-white text-center fw-bold mb-4">로그인</h1>

      <div class="card bg-secondary text-white shadow-lg p-5 rounded-4">

        <form @submit.prevent="loginHandler">
          <input v-model="username" placeholder="아이디" class="form-control form-control-lg mb-3 rounded" />
          <input v-model="password" type="password" placeholder="비밀번호" class="form-control form-control-lg mb-3 rounded" />
          <div class="form-check mb-4">
            <input v-model="saveId" class="form-check-input" type="checkbox" id="saveIdCheck" />
            <label class="form-check-label text-white-50" for="saveIdCheck">
              아이디 저장
            </label>
          </div>
          <button type="submit" class="btn btn-primary btn-lg w-100 rounded">로그인</button>
          <br>
        </form>

        <div class="text-center mt-2">
          <RouterLink :to="{ name: 'signup' }" class="btn btn-secondary w-100 rounded text-decoration-none">
            아직 회원이 아니신가요?
          </RouterLink>
        </div>

      </div>
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

<style scoped>
  .form-check-input:focus {
    box-shadow: none;
    outline: none;
  }
</style>
