<template>
  
  <div class="container-fluid bg-dark text-white py-5 min-vh-100 d-flex justify-content-center align-items-center" v-if="user">
    <div class="d-flex justify-content-center">
      <div class="card bg-secondary text-white p-4" style="width: 30rem;">

        <div class="text-center">
          <h2>마이페이지</h2>
          <div v-if="!user.profile_img">
            <img src="@/assets/profile.png" alt="profileImage" class="profile" style="border-radius: 8px;"/>
          </div>
          <div v-else>
            <img :src="`${user.profile_img}`" alt="profileImage" class="profile" />
          </div>
          <h4 class="fw-bold">{{ user.username }}</h4>
          <p>{{ user.email }}</p>
          <p>{{ user.gender_display }} / {{ user.age }}세</p>
        </div>

        <hr class="border-light" />

        <!-- 팔로우 정보 -->
        <div class="mb-3">
          <span><strong>팔로워:</strong> {{ user.followers_count }}명</span> |
          <span><strong>팔로잉:</strong> {{ user.followings_count }}명</span>
        </div>

        <!-- 독서 정보 회원가입에 추가할 것인가 말 것인가 -->
        <div class="mb-3">
          <p><strong>주간 평균 독서 시간:</strong> {{ user.weekly_avg_reading_time }}</p>
          <p><strong>연간 독서량:</strong> {{ user.annual_reading_amount }}</p>
        </div>

        <!-- 관심 장르 -->
        <div class="mb-3">
          <p><strong>관심 장르:</strong></p>
          <ul class="list-unstyled ms-3">
            <li v-for="genre in user.interested_genres_name" :key="genre">📚 {{ genre }}</li>
          </ul>
        </div>
      
        <!-- 버튼 -->
        <div class="d-flex justify-content-between">
          <button class="btn btn-outline-light w-50 me-2" @click="updateHandler">프로필 편집</button>
          <button class="btn btn-danger w-50" @click="logoutHandler">로그아웃</button>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'
import { onMounted, ref} from 'vue'

const accountStore = useAccountStore()
const router = useRouter()

const user = ref(null)

onMounted(async ()=> {
  user.value = await accountStore.getUser(accountStore.user.username)
})

const logoutHandler = () => {
  accountStore.logout()
  router.push({ name: 'home' })
}

const updateHandler = () => {
  router.push({ name: 'ProfileUpdateView' })
}
</script>

<style scoped>
  .profile {
    width: 200px;
    height: 200px;
  }
</style>