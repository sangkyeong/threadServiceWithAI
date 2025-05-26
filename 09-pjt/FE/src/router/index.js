import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '@/views/LandingView.vue'
import { useAccountStore } from '@/stores/accounts'
import { useThreadStore } from '@/stores/thread'

import ThreadsListView from '@/views/thread/ThreadListView.vue'
import ThreadDetailView from '@/views/thread/ThreadDetailView.vue'
import ThreadWriteView from '@/views/thread/ThreadWriteView.vue'
import ThreadUpdateView from '@/views/thread/ThreadUpdateView.vue'
import BookListView from '@/views/Books/BookListView.vue'
import BookDetailView from '@/views/Books/BookDetailView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdate from '@/views/ProfileUpdate.vue'
import userProfileView from '@/views/userProfileView.vue'
import passwordChangeView from '@/views/PasswordChangeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingView
    },
    {
      path: '/threads',
      name: 'threads',
      component: ThreadsListView
    },
    {
      path: '/threads/:threadId',
      name: 'threadDetail',
      component: ThreadDetailView
    },
    {
      path: '/threads/:threadId/update',
      name: 'threadUpdate',
      component: ThreadUpdateView,
      beforeEnter: async (to, from, next) => {
        const threadStore = useThreadStore()
        const accountStore = useAccountStore()
        await threadStore.getThreadById(to.params.threadId)
        if (accountStore.user.pk !== threadStore.threadDetail.user) {
          alert("잘못된 접근입니다.")
          next({ name: 'threads' })
        } else {
          next()
        }
      }
    },
    {
      path: '/threads/:bookId/write',
      name: 'threadWrite',
      component: ThreadWriteView
    },
    {
      path: '/books',
      name: 'books',
      component: BookListView
    },
    {
      path: '/books/:id',
      name: 'BookDetail',
      component: BookDetailView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profile/:userName',
      name: 'userProfile',
      component: userProfileView,
      props: true
    },
    {
      path: '/profileUpdate',
      name: 'ProfileUpdateView',
      component: ProfileUpdate,
    },
    {
      path: '/passwordChange',
      name: 'passwordChangeView',
      component: passwordChangeView,
    },
  ],
})

router.beforeEach((to, from, next) => {
  const accountStore = useAccountStore()

  if (to.meta.requiresAuth && !accountStore.token) {
    next({ name: 'login' })  // 로그인 안 했으면 login 페이지로 보내기
  } else {
    next()
  }
})

export default router
