<template>
    <div class="genre-card">
        <img :src="genre.image" :alt="genre.name" />
        <div class="genre-name">{{ genre.name }}</div>
    </div>
</template>

<script setup>
    defineProps({ genre: Object })
</script>

<style scoped>
    .genre-card {
    width: 120px;
    text-align: center;
    margin: 0 10px;
    cursor: pointer;
    }
    .genre-card img {
    width: 100%;
    height: 100px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .genre-name {
    margin-top: 8px;
    font-weight: bold;
    }
</style>
  