import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '@/views/LandingView.vue'
import { useAccountStore } from '@/stores/accounts'

import ThreadsListView from '@/views/thread/ThreadListView.vue'
import ThreadDetailView from '@/views/thread/ThreadDetailView.vue'
import ThreadWriteView from '@/views/thread/ThreadWriteView.vue'
import ThreadUpdateView from '@/views/thread/ThreadUpdateView.vue'
import BookListView from '@/views/Books/BookListView.vue'
import BookDetailView from '@/views/Books/BookDetailView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
      component: ThreadUpdateView
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
      meta: { requiresAuth: true },
      component: ProfileView,
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
