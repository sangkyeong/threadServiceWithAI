import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useThreadStore = defineStore('threads', () => {
  const threads = ref([])
  const BASE_URL = 'http://127.0.0.1:8000/threads'
  const router = useRouter()
  const errors = ref('')
  const threadDetail = ref(null)

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

  const addThreads = function(title, bookId, content, reading_date){
    axios.post(
     `${BASE_URL}/${bookId}/create/`,
      {
        title: title,
        content: content,
        reading_date: reading_date,
      },
      // headers: {
      //   Authorization: `Token ${token}`
      // }
  ).then((res) => {
    alert("쓰레드가 저장되었습니다.")
    router.push({name: 'threads'})
  })
  .catch((err) => {
    console.log(err)
    errors.value = err.response.data
  })

    // const categoryId = computed(() => {
    // const book = bookStore.books.find(book => book.id === bookId)
    // // const categoryId = book ? book.categoryId : null
    // })
  }

  const getThreadById = (threadId) => {
    axios.get(
      `${BASE_URL}/${threadId}/detail/`
    ).then((res) => {
      threadDetail.value = res.data
    })
    .catch((err) => {
      threadDetail.value = null
      console.log(err)
    })
  }

  const removeThread = (threadId) => {
      axios.delete(
        `${BASE_URL}/${threadId}/delete/`
      ).then((res) => {
        alert("쓰레드가 삭제되었습니다.")
        router.push({name: 'threads'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

 const updateThread = (threadId, { title, content, reading_date }) => {
  axios.patch(
     `${BASE_URL}/${threadId}/update/`,
      {
        title: title,
        content: content,
        reading_date: reading_date,
      },
      // {
      //   headers: {
      //     Authorization: `Token ${token}`
      //   }
      // }
  ).then((res) => {
    alert("쓰레드가 수정되었습니다.")
    router.push({name: 'threads'})
  })
  .catch((err) => {
    console.log(err)
    errors.value = err.response.data
  })
}

const addThreadComment = function(threadId, content){
  axios.post(
      `${BASE_URL}/${threadId}/comment/create/`,
        {
          content
        },
        // headers: {
        //   Authorization: `Token ${token}`
        // }
    ).then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
      errors.value = err.response.data
    })
  }

  const removeThreadComment = (threadId) => {
    axios.delete(
        `${BASE_URL}/comment/${threadId}/delete/`
      ).then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }

  return{
    threads, errors, threadDetail, 
    getAllThreads, addThreads, getThreadById, removeThread, updateThread,
    addThreadComment, removeThreadComment
  }
}, { persist: {
    paths: ['token', 'threads']
  }
})