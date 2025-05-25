import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    proxy: {
      "/books": {
        target: "http://localhost:8000", // Django 서버 주소
        changeOrigin: true,
        // 필요시 아래 옵션 추가
        // rewrite: (path) => path.replace(/^\/books/, '/books'),
      },
      "/threads": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      // 필요시 다른 api 경로도 추가
    },
  },
});
