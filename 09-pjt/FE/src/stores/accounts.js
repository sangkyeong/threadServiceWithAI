import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useAccountStore = defineStore('accounts', () => {
  const token = ref(null)
  const user = ref(null)
  const API_URL = 'http://localhost:8000'

  const isLogin = computed(() => {
    return token.value !== null
  })

  // 로그인
  const login = function (username, password) {
    return axios({
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
        return axios.get(`${API_URL}/accounts/user/`)
      })
      .then(res => {
        user.value = res.data
        console.log('로그인 성공!! 유저 정보', user.value)
      })
      .catch(err => {
        console.error('로그인 실패', err)
      })
  }

  // 로그아웃
  const logout = function () {
    token.value = null
    user.value = null
    delete axios.defaults.headers.common['Authorization']
  }

  // 회원가입
  const signup = function (payload) {
    return axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: payload,
    })
      .then(res => {
        console.log('회원가입 성공', res.data)
      })
      .catch(err => {
        throw err  // view 쪽에서 catch해서 alert 띄우자
      })
  }

  return {
    token, user, isLogin,
    login, logout, signup
  }
}, { persist: true })