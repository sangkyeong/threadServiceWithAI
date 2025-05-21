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

    <h1>detail</h1>
    <div>
      <ThreadItem
        v-for="thread in filteredThreads"
        :key="thread.id"
        :thread="thread"
      />
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import ThreadItem from '@/components/thread/thread_list/ThreadItem.vue'
  import { useCategoryStore, useBooksStore } from '@/stores/data.js'
  import { useThreadStore } from '@/stores/thread.js'
  const bookStore = useBooksStore()
  const threadStore = useThreadStore()
  const categoryStore = useCategoryStore()

  const books = bookStore.books
  const threads = threadStore.threads

  const selectedCategoryId = ref(null)

  const filteredBooks = computed(() => {
    console.log(selectedCategoryId.value)
    if (!selectedCategoryId.value) return books
    return books.filter(book => book.fields.category === selectedCategoryId.value)
  })

  const filteredThreads = computed(() => {
    const bookIds = filteredBooks.value.map(book => book.fields.pk)
    return threads.filter(thread => bookIds.includes(thread.bookId))
  })

</script>

<style scoped>

</style>