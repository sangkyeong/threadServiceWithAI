<template>
  <div class="container py-5" v-if="user">
    <div>
      <template v-if="!user.profile_img">
        <img src="@/assets/profile.png" alt="profileImage" class="profile" />
      </template>
      <template v-else>
        <img :src="`${user.profile_img}`" alt="profileImage" class="profile" />
      </template>
      <strong>{{ user.username }}</strong>
    </div>
    <div class="me-auto">
      <p>
        <strong>팔로워 : </strong><span id="followers-count">{{user.followers_count}}명</span> |
        <strong>팔로잉 : </strong><span id="followings-count">{{user.followings_count}}명</span>
      </p>
      <div v-if="accountStore.user && accountStore.user?.username !== user.username">
        <button @click="followHandler" class="btn btn-info">
          {{ user.is_follow ? '팔로우 취소' : '팔로우' }}
        </button>
      </div>
    </div>
    <p><strong>아이디:</strong> {{ user.username }}</p>
    <p><strong>이메일:</strong> {{ user.email }}</p>
    <p><strong>성별:</strong> {{ user.gender_display }}</p>
    <p><strong>나이:</strong> {{ user.age }}</p>
    <p><strong>주간 평균 독서 시간:</strong> {{ user.weekly_avg_reading_time }}</p>
    <p><strong>연간 독서량:</strong> {{ user.annual_reading_amount }}</p>
    <p><strong>관심 장르:</strong></p>
    <ul>
      <div v-for="genre in user.interested_genres_name">
        <li>{{ genre }}</li>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'

const accountStore = useAccountStore()
const route = useRoute()

const user = ref(null)
const isFollowClass = ref(user.is_follow ? 'info':'danger')


onMounted(async ()=> {
  user.value = await accountStore.getUser(route.params.userName)
})

const followHandler = async () => {
  await accountStore.follow(user.value.pk)
  user.value = await accountStore.getUser(route.params.userName)
}
</script>

<style scoped>
 .profile {
  width: 200px;
  height: 200px;
 }
</style>