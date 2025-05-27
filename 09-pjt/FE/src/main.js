// 뒤로가기 및 새로고침 시 페이지 0,0 시작
if ("scrollRestoration" in history) {
    history.scrollRestoration = "manual";
}

import { createApp } from "vue";
import { createPinia } from "pinia";
import VueCookies from "vue3-cookies";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);
app.use(router);
app.use(VueCookies);

//pinia 사용처리
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
app.use(pinia);

app.mount("#app");
