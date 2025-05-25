<template>
  <div class="container py-5">
    <h2>마이페이지</h2>
    <div v-if="!user.profile_img">
      <img src="@/assets/profile.png" alt="profileImage" class="profile" />
    </div>
    <div v-else>
      <img :src="`http://127.0.0.1:8000${user.profile_img}`" alt="profileImage" class="profile" />
    </div>
    <div class="me-auto">
      <p>
        <strong>팔로워 : </strong><span id="followers-count">{{user.followers_count}}명</span> |
        <strong>팔로잉 : </strong><span id="followings-count">{{user.followings_count}}명</span>
      </p>
      <button class="btn btn-info" @click="updateHandler">팔로잉</button>
    </div>
    <p><strong>아이디:</strong> {{ user.username }}</p>
    <p><strong>이메일:</strong> {{ user.email }}</p>
    <p><strong>성별:</strong> {{ user.gender }}</p>
    <p><strong>나이:</strong> {{ user.age }}</p>
    <p><strong>주간 평균 독서 시간:</strong> {{ user.weekly_avg_reading_time }}</p>
    <p><strong>연간 독서량:</strong> {{ user.annual_reading_amount }}</p>
    <p><strong>관심 장르:</strong></p>
    <ul>
      <div v-for="genre in user.interested_genres_name">
        <li>{{ genre }}</li>
      </div>
    </ul>
    <button class="btn btn-primary" @click="updateHandler">수정</button>
    <button class="btn btn-danger" @click="logoutHandler">로그아웃</button>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'

const accountStore = useAccountStore()
const router = useRouter()

const user = accountStore.user

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