import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useAccountStore = defineStore('accounts', () => {
  const token = ref(null)
  const API_URL = 'http://localhost:8000'

  const login = function (username, password) {
    axios({
      url:`${API_URL}/api/accounts/login/`,
      method: 'post',
      data: {
        username: username,
        password: password
      }
    })
      .then(res => {
        token.value = res.data.key
        axios.defaults.headers.common['Authorization'] = `Token ${token.value}`
        console.log('로그인 성공', token.value)
      })
      .catch(err => {
        console.error('로그인 실패', err)
      })
  }

  const signup = function (username, email, password1, password2) {
    axios({
      method: 'post',
      url: `${API_URL}/api/accounts/signup/`,
      data: {
        username: username,
        email: email,
        password1: password1,
        password2: password2,
      }
    })
      .then(res => {
        console.log('회원가입 성공', res.data)
      })
      .catch(err => {
        console.error('회원가입 실패', err.response?.data || err)
      })
  }

  return {
    token,
    login, signup
  }
}, { persist: true })