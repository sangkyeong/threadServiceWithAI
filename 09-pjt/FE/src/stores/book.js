import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBookStore = defineStore('books', () => {
  const books = ref([])
  const DJANGO_URL = 'http://127.0.0.1:8000/books'

  const fetchBooks = function () {
    axios({
      url: `${DJANGO_URL}/books`,
      method: 'get',
    })
      .then(res => {
        books.value = res.data
      })
      .catch(err => {
        console.error('책 불러오기 실패 확인하세요', err)
      })
  }

  
  return{
    books,
    fetchBooks,
  }
}, { persist: true})