import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useBooksStore } from '@/stores/data.js'


export const useThreadStore = defineStore('threads', () => {
  let id = 1

  const threads = ref([])

  const addThreads = function(title, bookId, content, readDate){
    const bookStore = useBooksStore()
    const categoryId = computed(() => {
    const book = bookStore.books.find(book => book.id === bookId)
    const categoryId = book ? book.categoryId : null
    })
    threads.value.push({
      id: id++,
      bookId: bookId,
      categoryId: categoryId,
      title: title,
      content: content,
      readDate: readDate,
    })
  }

  const getThreadById = (threadId) => {
    return threads.value.find(thread => thread.id === Number(threadId))
  }

  const removeThread = (threadId) => {
    threads.value = threads.value.filter(thread => thread.id !== threadId)
  }

 const updateThread = (threadId, { title, content, readDate }) => {
  const idx = threads.value.findIndex(thread => thread.id === Number(threadId))
  if (idx !== -1) {
    threads.value[idx] = {
      ...threads.value[idx],
      title,
      content,
      readDate,
    }
  }
}

  return{
    threads, 
    addThreads, getThreadById, removeThread, updateThread
  }
}, { persist: true})