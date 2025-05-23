<template>
    <p>{{ comment.content }}</p>
    <button>삭제</button>
</template>

<script setup>
    defineProps({
        comment : Object
    })
</script>

<style scoped>

</style>