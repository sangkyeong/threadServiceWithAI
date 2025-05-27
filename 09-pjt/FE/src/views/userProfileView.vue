<template>
  <div class="container-fluid bg-dark text-white py-5 min-vh-100 d-flex justify-content-center align-items-start" v-if="user">
    <div class="w-100" style="max-width: 32rem;">
      <h1 class="text-white text-center fw-bold mb-4">유저 정보</h1>
      <div class="card bg-secondary text-white shadow-lg p-5 rounded-4">

        <div class="text-center">
          <div v-if="!user.profile_img">
            <img src="@/assets/profile.png" alt="profileImage" class="profile-img mb-3 rounded-circle border border-light"/>
          </div>
          <div v-else>
            <img :src="`${user.profile_img}`" alt="profileImage" class="profile-img mb-3 rounded-circle border border-light"/>
          </div>
        </div>

        <div class="mb-3 text-center">
          <span class="me-2"><strong>팔로워:</strong> {{ user.followers_count }}명</span> |
          <span class="ms-2"><strong>팔로잉:</strong> {{ user.followings_count }}명</span>
        </div>

        <div class="text-center mb-4" v-if="accountStore.user && accountStore.user?.username !== user.username">
          <button
            @click="followHandler"
            :class="['btn', user.is_follow ? 'btn-danger' : 'btn-outline-light']"
          >
            <i :class="iconClass"></i>
            {{ buttonText }}
          </button>
        </div>

        <div>
          <p><strong>아이디:</strong> {{ user.username }}</p>
          <p><strong>이메일:</strong> {{ user.email }}</p>
          <p><strong>성별:</strong> {{ user.gender_display }}</p>
          <p><strong>나이:</strong> {{ user.age }}</p>
          <p><strong>주간 평균 독서 시간:</strong> {{ user.weekly_avg_reading_time }}시간</p>
          <p><strong>연간 독서량:</strong> {{ user.annual_reading_amount }}권</p>
          <p><strong>관심 장르</strong></p>
          <div class="d-flex flex-wrap gap-2">
            <span v-for="genre in user.interested_genres_name" :key="genre" class="badge rounded-pill bg-light text-dark px-3 py-2">
              {{ genre }}
            </span>
          </div>
        </div>
        
      </div>
    </div>
  </div>

</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'
import { useRoute } from 'vue-router'
import { onMounted, ref, computed } from 'vue'

const accountStore = useAccountStore()
const route = useRoute()

const user = ref(null)

onMounted(async ()=> {
  user.value = await accountStore.getUser(route.params.userName)
})

const iconClass = computed(() =>
  user.value.is_follow ? 'bi bi-person-dash-fill' : 'bi bi-person-plus-fill'
)

const buttonText = computed(() =>
  user.value.is_follow ? '팔로우 취소' : '팔로우'
)

const followHandler = async () => {
  await accountStore.follow(user.value.pk)
  user.value = await accountStore.getUser(route.params.userName)
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
