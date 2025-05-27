<template>
  <div class="container-fluid bg-dark text-white py-4 min-vh-100 d-flex justify-content-center align-items-start" v-if="user">
    <div class="w-100" style="max-width: 32rem;">
      <h1 class="text-white text-center fw-bold mb-4">마이페이지</h1>
      <div class="card bg-secondary text-white shadow-lg p-5 rounded-4">

        <div class="text-center mb-4">
          <div v-if="!user.profile_img">
            <img src="@/assets/profile.png" alt="profileImage" class="profile-img mb-3 rounded-circle border border-light"/>
          </div>
          <div v-else>
            <img :src="`${user.profile_img}`" alt="profileImage" class="profile-img mb-3 rounded-circle border border-light"/>
          </div>
        </div>

        <!-- 팔로우 정보 -->
        <div class="mb-3 text-center">
          <span><strong>팔로워:</strong> {{ user.followers_count }}명</span> |
          <span><strong>팔로잉:</strong> {{ user.followings_count }}명</span>
        </div>

        <div class="mb-3">
          <p><strong>아이디:</strong> {{ user.username }}</p>
          <p><strong>이메일:</strong> {{ user.email }}</p>
          <p><strong>성별:</strong> {{ user.gender_display }}</p>
          <p><strong>나이:</strong> {{ user.age }}세</p>
          <p><strong>주간 평균 독서 시간:</strong> {{ user.weekly_avg_reading_time }}시간</p>
          <p><strong>연간 독서량:</strong> {{ user.annual_reading_amount }}권</p>
          <p><strong>관심 장르</strong></p>
          <div class="d-flex flex-wrap gap-2">
            <span v-for="genre in user.interested_genres_name" :key="genre" class="badge rounded-pill bg-light text-dark px-3 py-2">
              {{ genre }}
            </span>
          </div>
        </div>


        <button class="btn btn-primary btn-lg w-100 rounded mt-2" @click="updateHandler">프로필 편집</button>
        <button class="btn btn-danger btn-lg w-100 rounded mt-2" @click="logoutHandler">로그아웃</button>
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
  .profile-img {
    width: 200px;  
    height: 200px;
    object-fit: contain; 
    background-color: white;
  }

  
</style>