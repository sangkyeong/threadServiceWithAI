import { defineStore } from "pinia";
import { ref, computed } from "vue";
import axios from "axios";

export const useAccountStore = defineStore(
  "accounts",
  () => {
    const token = ref(null);
    const user = ref(null);
    const API_URL = "http://localhost:8000";

    const isLogin = computed(() => {
      return token.value !== null;
    });

    // 로그인
    const login = function (username, password) {
      return axios({
        url: `${API_URL}/api/accounts/login/`,
        method: "post",
        data: {
          username: username,
          password: password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          axios.defaults.headers.common[
            "Authorization"
          ] = `Token ${token.value}`;
          return axios.get(`${API_URL}/accounts/user/`);
        })
        .then((res) => {
          user.value = res.data;
          console.log(user.value);
          // console.log("로그인 성공!! 유저 정보", user.value);
        });
      // .catch((err) => {
      //   throw err;
      //   // alert("로그인 정보가 올바르지 않습니다.");
      //   // console.error("로그인 실패", err);
      // });
    };

    // 로그아웃
    const logout = function () {
      token.value = null;
      user.value = null;
      delete axios.defaults.headers.common["Authorization"];
    };

    // 회원가입
    const signup = function (payload) {
      return axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: payload,
      })
        .then((res) => {
          // console.log('회원가입 성공', res.data)
        })
        .catch((err) => {
          throw err; // view 쪽에서 catch해서 alert 띄우자
        });
    };

    // 회원정보 수정
    const profileUpdate = function (payload) {
      return axios({
        method: "patch",
        url: `${API_URL}/accounts/signup/`,
        data: payload,
        headers: {
            'Authorization': `Token ${token.value}`,
            'Content-Type': 'multipart/form-data'
        }
      })
        .then((res) => {
          return axios.get(`${API_URL}/accounts/user/`, {
            headers: { 'Authorization': `Token ${token.value}` }
          });
        })
        .then((res) => {
          user.value = res.data;
          console.log(user.value);
          // console.log("로그인 성공!! 유저 정보", user.value);
        })
        .catch((err) => {
          throw err; // view 쪽에서 catch해서 alert 띄우자
        });
    };

    // 팔로우
    const follow = function (userId) {
      return axios({
        method: "post",
        url: `${API_URL}/accounts/${userId}/follow/`,
        headers: {
            'Authorization': `Token ${token.value}`,
        }
      })
        .then((res) => {
          console.log(res)
          user.value.follower_count = res.data.follower_count;

          return {
            follower_count: res.data.follower_count,
            isFollow: res.data.is_follow
          }
          // console.log("로그인 성공!! 유저 정보", user.value);
        })
        .catch((err) => {
          throw err; // view 쪽에서 catch해서 alert 띄우자
        });
    };

    // 비밀번호 변경
    const passwordChange = async function(data) {
      try {
        const res = await axios.post(
          `${API_URL}/accounts/change-password/`, 
        data, 
        {
          headers: {
            'Authorization': `Token ${token.value}`
          }
        })
        return res.data
      } catch (err) {
        throw err; // view 쪽에서 catch해서 alert 띄우자
      };
    };

    // 회원정보 가져오기
    const getUser = function (username) {
      const headers = {}
      if (token.value) {
        headers['Authorization'] = `Token ${token.value}` // 또는 Bearer
      }
      return axios({
        url: `${API_URL}/accounts/${username}/profile/`,
        method: "get",
        headers
      })
        .then((res) => {
          return res.data
          // console.log("로그인 성공!! 유저 정보", user.value);
        });
    }

    return {
      token,
      user,
      isLogin,
      login,
      logout,
      signup,
      profileUpdate,
      follow,
      getUser,
      passwordChange
    };
  },
  { persist: true }
);
