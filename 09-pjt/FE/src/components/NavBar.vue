<template>
  <div class="app-wrapper">
    <header class="site-header">
      <RouterLink :to="{ name: 'home' }" class="logo">Th<span>Read</span></RouterLink>
      <nav>
        <RouterLink :to="{ name: 'threads' }">쓰레드</RouterLink>
        <RouterLink :to="{ name: 'books' }">도서 검색</RouterLink>

    <template v-if="accountStore.isLogin">
      <RouterLink to="/profile">마이페이지</RouterLink>
      <a href="#" @click.prevent="logoutHandler">로그아웃</a>
    </template>
    <template v-else>
      <RouterLink to="/login">로그인</RouterLink>
    </template>
      </nav>
    </header>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

const router = useRouter()
const accountStore = useAccountStore()
const user = accountStore.user

const logoutHandler = () => {
  accountStore.logout()
  router.push({ name: 'home' })
}
</script>

<style scoped>

/* 마우스를 올렸을 때 시 붉은색 변경 */
.menu-item:hover {
  color: #fe4a51;
}

.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #1a1a1a;
  padding: 1rem 2rem;
}

.logo {
  font-weight: bold;
  color: white;
  font-size: 1.5rem;
  text-decoration: none;

}

.logo span {
  color: #ff5656;
}

nav a {
  margin-left: 1rem;
  text-decoration: none;
  color: white;
  font-size: 1rem;
}

nav a.router-link-exact-active {
  color: #ff5656;
}
</style>
