<template>
  <div>
    <NavBar />
    <Loading :isLoading="uiStore.isLoading"/>
    <!-- <RouterView /> -->
  </div>
</template>

<script setup>
import NavBar from '@/components/main_page/NavBar.vue'
import { RouterView } from 'vue-router'
import Loading from '@/components/common/Loading.vue'
import { useUIStore } from '@/stores/ui.js'
const uiStore = useUIStore()
</script>

<style>
  html, body {
    margin: 0;
    padding: 0;
  }

</style>
