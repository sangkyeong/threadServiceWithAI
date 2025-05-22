import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useThreadStore = defineStore('threads', () => {
  const threads = ref([])
  const BASE_URL = 'http://127.0.0.1:8000/threads'

  const getAllThreads = function(){
    axios({
      method: 'get',
      url: `${BASE_URL}`
    })
    .then((res) => {
      threads.value = res.data
    })
    .catch((err) => console.log(err))
  }

  const addThreads = function(title, bookId, content, readDate){
    axios({
      method: 'post',
      url: `${BASE_URL}/${bookId}/create`,
      data: {
        title: title,
        content: content,
        reading_date: readDate,
        // headers: {
        //   Authorization: `Token ${token}`
        // }
      }
    })
    .then((res) => {
      console.log("create")
      console.log(res)
    })
    .catch((err) => console.log(err))

    // const categoryId = computed(() => {
    // const book = bookStore.books.find(book => book.id === bookId)
    // // const categoryId = book ? book.categoryId : null
    // })
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
    getAllThreads, addThreads, getThreadById, removeThread, updateThread
  }
}, { persist: true})