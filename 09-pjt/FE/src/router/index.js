import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '@/views/LandingView.vue'

import ThreadsListView from '@/views/thread/ThreadListView.vue'
import ThreadDetailView from '@/views/thread/ThreadDetailView.vue'
import ThreadWriteView from '@/views/thread/ThreadWriteView.vue'
import ThreadUpdateView from '@/views/thread/ThreadUpdateView.vue'
import BookListView from '@/views/Books/BookListView.vue'

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
    // {
    //   path: '/books/:bookid',
    //   name: 'BookDetail',
    //   component: BookDetailView,
    //   props: true
    // }
  ],
})

export default router
