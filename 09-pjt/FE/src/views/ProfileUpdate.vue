<template>
  <div class="container-fluid bg-dark text-white py-5 min-vh-100 d-flex justify-content-center align-items-start">
    <div class="w-100" style="max-width: 32rem;">
      <h1 class="text-white text-center fw-bold mb-4">프로필 수정</h1>
      <div class="card bg-secondary text-white shadow-lg p-5 rounded-4">

        <div class="text-center mb-4">
          <img
            v-if="!user.profile_img"
            src="@/assets/profile.png"
            alt="profileImage"
            class="profile-img rounded-circle border border-light shadow-sm"
          />
          <img
            v-else
            :src="`http://127.0.0.1:8000${user.profile_img}`"
            alt="profileImage"
            class="profile-img rounded-circle border border-light shadow-sm"
          />
        </div>
        
        <!-- 텍스트 창 크면 form-control-lg 삭제  -->
        <form @submit.prevent="signupHandler">
          <input type="file" class="form-control form-control-lg mb-2" @change="onFileChange" />
          
          <input v-model="username" readonly type="text" placeholder="아이디" class="form-control form-control-lg mb-2" />


          <input v-model="email" type="email" placeholder="이메일" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.email }"/>
          <div v-if="errors.email" class="text-danger small mb-2">{{ errors.email[0] }}</div>

          <select v-model="gender" class="form-select form-select-lg mb-2">
            <option disabled value="">성별 선택</option>
            <option value="M">남성</option>
            <option value="F">여성</option>
          </select>
          <div v-if="errors.gender" class="text-danger small mb-2">{{ errors.gender[0] }}</div>

          <input v-model.number="age" type="number" min="1" placeholder="나이" class="form-control form-control-lg mb-2" :class="{ 'is-invalid': errors.age }"/>
          <div v-if="errors.age" class="text-danger small mb-2" >{{ errors.age[0] }}</div>

          <input v-model.number="weeklyAvgReadingTime" type="number" min="0" placeholder="주간 평균 독서 시간" class="form-control form-control-lg mb-2" />

          <input v-model.number="annualReadingAmount" type="number" min="0" placeholder="연간 독서량" class="form-control form-control-lg mb-2" />

          <label class="form-label fw-bold">관심 장르</label>
          <div class="d-flex flex-wrap gap-2 mb-2">
            <div class="form-check form-check-inline" v-for="genre in genreOptions" :key="genre.id">
              <input class="form-check-input" type="checkbox" :id="`genre-${genre.id}`" :value="genre.id" v-model="interestedGenres">
              <label class="form-check-label text-white" :for="`genre-${genre.id}`">{{ genre.name }}</label>
            </div>
          </div>
          <div v-if="errors.interested_genres" class="text-danger small mb-2">{{ errors.interested_genres[0] }}</div>

          <button class="btn btn-primary btn-lg w-100 rounded mt-2">수정</button>
        </form>

        <button class="btn btn-secondary btn-lg w-100 rounded mt-2" @click="goToChangePassword">비밀번호 변경</button>
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
.profile-img {
  width: 200px;
  height: 200px;
  object-fit: contain; 
  background-color: white;
}
</style>
