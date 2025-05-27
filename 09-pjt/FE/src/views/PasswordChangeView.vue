<template>
    <div class="container-fluid bg-dark text-white py-5 min-vh-100 d-flex justify-content-center align-items-start">
    <div class="w-100" style="max-width: 32rem;">
      <h1 class="text-white text-center fw-bold mb-4"> 비밀번호 변경</h1>

      <div class="card bg-secondary text-white shadow-lg p-5 rounded-4">
        <div>
          <input type="password" v-model="currentPassword" class="form-control form-control-lg mb-2" placeholder="현재 비밀번호를 입력하세요." :class="{ 'is-invalid': errors.current_password }" />
              <div v-if="errors.current_password" class="text-danger small mb-2">
                  <i class="bi bi-exclamation-triangle-fill"></i>
                  {{ errors.current_password[0] }}
              </div>
        </div>

        <div>
          <input type="password"  v-model="newPassword" class="form-control form-control-lg mb-2" placeholder="새 비밀번호를 입력하세요."  :class="{ 'is-invalid': errors.password1 }"/>
              <div v-if="errors.password1" class="text-danger small mb-2">
                  <i class="bi bi-exclamation-triangle-fill"></i>
                  {{ errors.password1[0] }}
              </div>
        </div>
        <div>
          <input type="password"  v-model="confirmPassword" class="form-control form-control-lg mb-2" placeholder="새 비밀번호 확인을 입력해주세요." :class="{ 'is-invalid': errors.password2 }"/>
              <div v-if="errors.password2" class="text-danger small mb-2">
                  <i class="bi bi-exclamation-triangle-fill"></i>
                  {{ errors.password2[0] }}
              </div>
        </div>
        <button @click="changePassword" class="btn btn-primary">변경</button>
      </div>
    </div>
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
      errors.value = err.response?.data || '알 수 없는 오류가 발생했습니다.'
    })
}
</script>