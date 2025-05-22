<template>
    <div>
        <RouterLink :to="{name:'threadDetail', params:{'threadId':thread.id}}" >{{ thread.title }}</RouterLink>
    </div>
</template>

<script setup>
    import { RouterLink } from 'vue-router'
    defineProps({
        thread: Object,
        category: Object
    })
</script>

<style scoped>

</style>