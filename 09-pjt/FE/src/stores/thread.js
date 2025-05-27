import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAccountStore } from './accounts'


export const useThreadStore = defineStore('threads', () => {
  const threads = ref([])
  const BASE_URL = 'http://127.0.0.1:8000/threads'
  const router = useRouter()
  const errors = ref('')
  const threadDetail = ref(null)
  const accountStore = useAccountStore()

  const getAllThreads = function(){
    axios({
      method: 'get',
      url: `${BASE_URL}/`
    })
    .then((res) => {
      threads.value = res.data
    })
    .catch((err) => {
      console.log(err) 
      throw err
    })
  }

  const addThreads = async (title, bookId, content, reading_date) => {
    return await axios.post(
      `${BASE_URL}/${bookId}/create/`,
        {
          title: title,
          content: content,
          reading_date: reading_date,
        },
        {
          headers: {
            'Authorization': `Token ${accountStore.token}`
          }
        }
    ).then((res) => {
      alert("쓰레드가 저장되었습니다.")
      router.push({name: 'threads'})
    })
    .catch((err) => {
      console.log(err)
      alert(err.response.data.msg)
      throw err
    })
  }

  const getThreadById = (threadId) => {
    const config = {}
    if (accountStore.token) {
      config.headers = {
        'Authorization': `Token ${accountStore.token}`
      }
    }
    axios.get(
      `${BASE_URL}/${threadId}/detail/`, config
    ).then((res) => {
      threadDetail.value = res.data
    })
    .catch((err) => {
      threadDetail.value = null
      console.log(err)
      throw err
    })
  }

  const removeThread = (threadId) => {
      axios.delete(
        `${BASE_URL}/${threadId}/delete/`,
        {
          headers: {
            'Authorization': `Token ${accountStore.token}`
          }
        }
      ).then((res) => {
        alert("쓰레드가 삭제되었습니다.")
        router.push({name: 'threads'})
      })
      .catch((err) => {
        console.log(err)
        alert(err.response.data.msg)
        throw err
      })
  }

  const updateThread = async (threadId, { title, content, reading_date }) => {
    return await axios.patch(
      `${BASE_URL}/${threadId}/update/`,
        {
          title: title,
          content: content,
          reading_date: reading_date,
        },
        {
          headers: {
            'Authorization': `Token ${accountStore.token}`
          }
        }
    ).then((res) => {
      alert("쓰레드가 수정되었습니다.")
      router.push({name: 'threads'})
    })
    .catch((err) => {
      console.log(err)
      alert(err.response.data.msg)
      throw err
    })
  }

  const likeThread = async function(threadId){
    try {
      const res = await axios.post(
        `${BASE_URL}/${threadId}/likes/`,
        {},
        {
          headers: {
            'Authorization': `Token ${accountStore.token}`
          }
        }
      )
      return res.data
    } catch (err) {
      console.log(err)
      throw err
    }
  }

  const addThreadComment = async (threadId, content) => {
    try {
      const res = await axios.post(
        `${BASE_URL}/${threadId}/comment/create/`,
        {content},
        {
          headers: {
            'Authorization': `Token ${accountStore.token}`
          }
        }
      )
      return res.data
    } catch (err) {
      console.log(err)
      if(err.response.data.msg){
          alert(err.response.data.msg)
        }
      throw err
    }
  }

  const removeThreadComment = async (commentId) => {
      return await axios.delete(
          `${BASE_URL}/comment/${commentId}/delete/`,
        {
          headers: {
            'Authorization': `Token ${accountStore.token}`
          }
        }
        ).then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
          alert(err.response.data.msg)
          throw err
        })
    }

  return{
    threads, errors, threadDetail, 
    getAllThreads, addThreads, getThreadById, removeThread, updateThread, likeThread,
    addThreadComment, removeThreadComment
  }
}, { persist: {
    paths: ['threads']
  }
})