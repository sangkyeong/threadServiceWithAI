<template>
  <div class="app-wrapper">
    <header class="site-header">
      <RouterLink to="/" class="logo">Th<span>Read</span></RouterLink>
      <nav>
        <RouterLink to="/threads">쓰레드</RouterLink>
        <RouterLink to="/books">도서 검색</RouterLink>
      </nav>
    </header>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
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
