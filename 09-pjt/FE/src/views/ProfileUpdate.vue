<template>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <div class="card p-4 shadow" style="max-width: 500px; width: 100%;">
      <h2 class="text-center mb-4">프로필 수정</h2>

      <form @submit.prevent="signupHandler">
        <div v-if="!user.profile_img">
          <img src="@/assets/profile.png" alt="profileImage" class="profile" />
        </div>
        <div v-else>
          <img :src="`http://127.0.0.1:8000${user.profile_img}`" alt="profileImage" class="profile" />
        </div>
        <input type="file" class="form-control mb-2" @change="onFileChange" />

        <input v-model="username" readonly="readonly" type="text" placeholder="아이디" class="form-control mb-2" />
        <div v-if="errors.username" class="text-danger small mb-2">{{ errors.username[0] }}</div>
        
        <input v-model="password1" type="password" placeholder="비밀번호" class="form-control mb-2" />
        <div v-if="errors.password1" class="text-danger small mb-2">{{ errors.password1[0] }}</div>
        
        <input v-model="password2" type="password" placeholder="비밀번호 확인" class="form-control mb-2" />
        <div v-if="errors.password2" class="text-danger small mb-2">{{ errors.password2[0] }}</div>
        
        <input v-model="email" type="email" placeholder="이메일" class="form-control mb-2" />
        <div v-if="errors.email" class="text-danger small mb-2">{{ errors.email[0] }}</div>

        <select v-model="gender" class="form-select mb-2">
          <option disabled value="">성별 선택</option>
          <option value="M">남성</option>
          <option value="F">여성</option>
        </select>
        <div v-if="errors.gender" class="text-danger small mb-2">{{ errors.gender[0] }}</div>

        <input v-model.number="age" type="number" min="1" placeholder="나이" class="form-control mb-3" />
        <div v-if="errors.age" class="text-danger small mb-2">{{ errors.age[0] }}</div>

        <input v-model.number="weeklyAvgReadingTime" type="number" min="0" placeholder="주간 평균 독서 시간" class="form-control mb-3" />

        <input v-model.number="annualReadingAmount" type="number" min="0" placeholder="연간 독서량" class="form-control mb-3" />

        <label class="form-label fw-bold">관심 장르</label>
        <div class="form-check" v-for="genre in genreOptions" :key="genre.id">
          <input class="form-check-input" type="checkbox" :id="`genre-${genre.id}`" :value="genre.id" v-model="interestedGenres">
          <label class="form-check-label" :for="`genre-${genre.id}`">
            {{ genre.name }}
          </label>
        </div>
        <div v-if="errors.interested_genres" class="text-danger small mb-2">{{ errors.interested_genres[0] }}</div>

        <button class="btn btn-primary w-100 mt-4">수정</button>
      </form>
      <button class="btn btn-secondary w-100 mt-2" @click="goToChangePassword">비밀번호 변경</button>
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

const user = accountStore.user
const username = ref(user.username)
const email = ref(user.email)
const password1 = ref('')
const password2 = ref('')
const gender = ref(user.gender)
const age = ref(user.age)
const interestedGenres = ref([])
const errors = ref({})
const profileImg = ref(null)
const genreOptions = ref([])
const weeklyAvgReadingTime = ref(user.weekly_avg_reading_time)
const annualReadingAmount = ref(user.annual_reading_amount)

const signupHandler = () => {
  const formData = new FormData()
  formData.append('userId', accountStore.user.pk)
  formData.append('username', username.value)
  formData.append('email', email.value)
  formData.append('password1', password1.value)
  formData.append('password2', password2.value)
  formData.append('gender', gender.value)
  formData.append('age', age.value)
  formData.append('weekly_avg_reading_time', weeklyAvgReadingTime.value)
  formData.append('annual_reading_amount', annualReadingAmount.value)
  if (profileImg.value) {
    formData.append('profile_img', profileImg.value)
  }
  // 관심 장르 배열은 반드시 반복해서 append!
  interestedGenres.value.forEach(id => formData.append('interested_genres', id))

  accountStore.profileUpdate(formData)
    .then(() => {
      alert('회원수정이 완료되었습니다!')
      router.push({ name: 'profile' })
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
  
    interestedGenres.value = [...user.interested_genres]
})

const onFileChange = (event) => {
  const file = event.target.files[0]
  profileImg.value = file
}

const goToChangePassword = () => {
  router.push({ name: 'passwordChangeView' })
}

</script>
<style scoped>
 .profile {
  width: 200px;
  height: 200px;
 }
</style>