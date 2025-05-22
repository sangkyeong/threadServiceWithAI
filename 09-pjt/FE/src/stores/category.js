import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCategoryStore = defineStore('categories', () => {
  const categories = ref([])
  const API_URL = 'http://localhost:8000/books'

  const fetchCategories  = function () {
    axios({
      url: `${API_URL}/books`,
      method: 'get',
    })
      .then(res => {
        categories.value = res.data
      })
      .catch(err => {
        console.error('책 불러오기 실패 확인하세요', err)
      })
  }

  
  return{
    categories,
    fetchCategories,
  }
}, { persist: true})