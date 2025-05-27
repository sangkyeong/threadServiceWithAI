<template>
  <div class="container-fluid bg-dark text-white py-5 min-vh-100 d-flex justify-content-center align-items-start">
    <div class="w-100" style="max-width: 32rem;">
      <h1 class="text-white text-center fw-bold mb-4">회원가입</h1>
      <div class="card bg-secondary text-white shadow-lg p-5 rounded-4">

      <!-- 텍스트 창 크면 form-control-lg 삭제  -->

      <form @submit.prevent="signupHandler">
        <input v-model="username" type="text" placeholder="아이디" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.username }"/>
        <div v-if="errors.username" class="text-danger small mb-2">{{ errors.username[0] }}</div>
        
        <input v-model="password1" type="password" placeholder="비밀번호" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.username }"/>
        <div v-if="errors.password1" class="text-danger small mb-2">{{ errors.password1[0] }}</div>
        
        <input v-model="password2" type="password" placeholder="비밀번호 확인" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.username }"/>
        <div v-if="errors.password2" class="text-danger small mb-2">{{ errors.password2[0] }}</div>
        
        <input v-model="email" type="email" placeholder="이메일" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.username }"/>
        <div v-if="errors.email" class="text-danger small mb-2">{{ errors.email[0] }}</div>

        <select v-model="gender" class="form-select form-control-lg mb-2" :class="{ 'is-invalid': errors.username }">
          <option disabled value="">성별 선택</option>
          <option value="M">남성</option>
          <option value="F">여성</option>
        </select>
        <div v-if="errors.gender" class="text-danger small mb-2">{{ errors.gender[0] }}</div>

        <input v-model.number="age" type="number" min="1" placeholder="나이" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.username }"/>
        <div v-if="errors.age" class="text-danger small mb-2">{{ errors.age[0] }}</div>

        <label class="form-label fw-bold">관심 장르</label>
        <div class="form-check" v-for="genre in genreOptions" :key="genre.id">
          <input class="form-check-input" type="checkbox" :id="`genre-${genre.id}`" :value="genre.id" v-model="interestedGenres">
          <label class="form-check-label" :for="`genre-${genre.id}`">
            {{ genre.name }}
          </label>
        </div>
        <div v-if="errors.interested_genres" class="text-danger small mb-2">{{ errors.interested_genres[0] }}</div>

        <button class="btn btn-primary btn-lg w-100 rounded mt-3">가입하기</button>
      </form>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const accountStore = useAccountStore()

const username = ref('')
const email = ref('')
const password1 = ref('')
const password2 = ref('')
const gender = ref('')
const age = ref(null)
const interestedGenres = ref([])
const errors = ref({})

const genreOptions = ref([])

const signupHandler = () => {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    gender: gender.value,
    age: age.value,
    interested_genres: interestedGenres.value
  }

  accountStore.signup(payload)
    .then(() => {
      alert('회원가입이 완료되었습니다!')
      router.push({ name: 'login' })
    })
    .catch(err => {
      errors.value = err.response?.data || {}
    })
}

onMounted(() => {
  axios.get('http://localhost:8000/books/categories/')
    .then(res => {
      genreOptions.value = res.data
    })
})
</script>
