<template>
  <div>
    <h3>비밀번호 변경</h3>
    <input type="password" v-model="currentPassword" placeholder="현재 비밀번호" />
    <div v-if="errors.current_password" class="text-danger small mb-2">{{ errors.current_password[0] }}</div>

    <input type="password" v-model="newPassword" placeholder="새 비밀번호" />
    <div v-if="errors.password1" class="text-danger small mb-2">{{ errors.password1[0] }}</div>

    <input type="password" v-model="confirmPassword" placeholder="새 비밀번호 확인" />
    <div v-if="errors.password2" class="text-danger small mb-2">{{ errors.password2[0] }}</div>

    <button @click="changePassword">변경</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'

const currentPassword = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const router = useRouter()
const errors = ref({})

const changePassword = async () => {
  const data = {
    current_password: currentPassword.value,
    password1: newPassword.value,
    password2: confirmPassword.value,
  }
  const res = await useAccountStore().passwordChange(data)
    .then(() => {
      alert('비밀번호 변경이 완료되었습니다!')
      router.push({ name: 'profile' })
    })
    .catch(err => {
      errors.value = err.response?.data || {}
    })
}
</script>