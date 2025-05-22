<template>
  <div>
    <h1>ThreadList</h1>
    <div
      v-for="category in categoryStore.categories"
      :key="category.fields.pk"
      :category="category"
      @click="selectedCategoryId = category.fields.pk"
    >
      {{ category.fields.name }}
    </div>

    <div>
      <div v-if="threads">
        <ThreadItem
          v-for="thread in threads"
          :key="thread.id"
          :thread="thread"
        />
      </div>
      <div v-else>
        <h2>스레드가 없습니다.</h2>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ThreadItem from '@/components/thread/thread_list/ThreadItem.vue'
// import { useCategoryStore } from '@/stores/data.js'
import { useThreadStore } from '@/stores/thread.js'

const threadStore = useThreadStore()
// const categoryStore = useCategoryStore()

const selectedCategoryId = ref(null)

const threads = computed(() => {
  if (!selectedCategoryId.value) return threadStore.threads
  return threadStore.threads.filter(thread => thread.categoryId === selectedCategoryId.value)
})

</script>

<style scoped>

</style>