<template>
<div class="thread-card">
    <img :src="thread.image" :alt="thread.title" />
    <div class="thread-info">
    <div class="thread-title">{{ thread.title }}</div>
    <div class="thread-desc">{{ thread.desc }}</div>
    </div>
</div>
</template>

<script setup>
    defineProps({ thread: Object })
</script>

<style scoped>
    .thread-card {
    display: flex;
    align-items: center;
    background: #f8f8f8;
    border-radius: 10px;
    margin-bottom: 12px;
    padding: 12px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .thread-card img {
    width: 60px;
    height: 60px;
    object-fit: cover;
    border-radius: 8px;
    margin-right: 14px;
    }
    .thread-title {
    font-weight: bold;
    }
    .thread-desc {
    color: #666;
    font-size: 14px;
    }
</style>
