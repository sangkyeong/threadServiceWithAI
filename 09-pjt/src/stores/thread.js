import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useBooksStore } from '@/stores/data.js'


export const useThreadStore = defineStore('threads', () => {
  let id = 0

  const threads = ref([
    {
      id: 1,
      bookId: 1,
      categoryId: 1,
      title: 'title',
      content: 'content',
      readDate: '2025-05-16',
    },
    {
      id: 2,
      bookId: 2,
      categoryId: 1,
      title: 'title2',
      content: 'content2',
      readDate: '2025-05-16',
    },
  ])

  const addThreads = function(title, bookId, content, readDate){
    const bookStore = useBooksStore()
    const categoryId = computed(() => {
      const book = bookStore.books.find(book => book.id === bookId)
      return book?.categoryId ?? null
    })
    threads.value.push({
      id: id++,
      bookId: bookId,
      categoryId: categoryId,
      title: title,
      content: content,
      readDate: readDate,
    })
    console.log(threads)
  }
  return{
    threads, addThreads
  }
}, { persist: true})