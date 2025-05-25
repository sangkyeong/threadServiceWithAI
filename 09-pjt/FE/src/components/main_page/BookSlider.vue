<template>
    <div class="carousel-wrapper">
      <button class="carousel-btn prev" @click="prevSlide">◀</button>
      <div class="carousel-window">
        <div class="carousel-track" :style="trackStyle" @transitionend="handleTransitionEnd">
          <!-- 앞 클론 -->
          <div class="carousel-slide" v-if="slideGroups.length > 1">
            <div class="slide-inner">
              <div v-for="book in slideGroups[slideGroups.length - 1]" :key="book.id" class="book-card text-center">
                <img :src="book.cover" :alt="book.title" class="img-fluid rounded shadow" />
                <div class="book-title mt-2">{{ book.title }}</div>
              </div>
            </div>
          </div>
  
          <!-- 실제 슬라이드 -->
          <div class="carousel-slide" v-for="(group, idx) in slideGroups" :key="idx">
            <div class="slide-inner">
              <div v-for="book in group" :key="book.id" class="book-card text-center">
                <img :src="book.cover" :alt="book.title" class="img-fluid rounded shadow" />
                <div class="book-title mt-2">{{ book.title }}</div>
              </div>
            </div>
          </div>
  
          <!-- 뒤 클론 -->
          <div class="carousel-slide" v-if="slideGroups.length > 1">
            <div class="slide-inner">
              <div v-for="book in slideGroups[0]" :key="book.id" class="book-card text-center">
                <img :src="book.cover" :alt="book.title" class="img-fluid rounded shadow" />
                <div class="book-title mt-2">{{ book.title }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-btn next" @click="nextSlide">▶</button>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from "vue";
  
  const props = defineProps({ books: Array });
  
  const books10 = computed(() => props.books.slice(0, 10));
  const size = 5;
  const slideGroups = computed(() => {
    const arr = [];
    for (let i = 0; i < books10.value.length; i += size) {
      arr.push(books10.value.slice(i, i + size));
    }
    return arr;
  });
  
  const current = ref(1);
  const transitioning = ref(false);
  
  const trackStyle = computed(() => ({
    transform: `translateX(-${current.value * 100}%)`,
    transition: transitioning.value
      ? "transform 0.5s cubic-bezier(.77,0,.18,1)"
      : "none",
    display: "flex",
  }));
  
  function prevSlide() {
    if (transitioning.value) return;
    transitioning.value = true;
    current.value--;
  }
  function nextSlide() {
    if (transitioning.value) return;
    transitioning.value = true;
    current.value++;
  }
  
  function handleTransitionEnd() {
    if (current.value === 0) {
      transitioning.value = false;
      current.value = slideGroups.value.length;
    } else if (current.value === slideGroups.value.length + 1) {
      transitioning.value = false;
      current.value = 1;
    } else {
      transitioning.value = false;
    }
  }
  </script>
  
  <style scoped>
  .carousel-wrapper {
    position: relative;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .custom-carousel {
    position: relative;
    width: 100%;
    margin: 0 auto;
  }
  
  .carousel-window {
    overflow: hidden;
    width: 1100px;
    box-sizing: border-box;
    position: relative;
  }
  
  .carousel-track {
    display: flex;
    transition: transform 0.5s ease;
  }
  
  .carousel-slide {
    min-width: 100%;
    box-sizing: border-box;
  }
  
  .slide-inner {
    display: flex;
    justify-content: center;
    gap: 16px;
    padding: 16px 0;
  }
  
  .book-card {
    width: 130px;
    margin: 0 8px;
  }
  
  .book-title {
    font-size: 14px;
    font-weight: 500;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    height: 2.8em;
  }
  
  .carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.5rem;
    background-color: rgba(255, 255, 255, 0.8);
    border: none;
    border-radius: 50%;
    padding: 6px 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    cursor: pointer;
    z-index: 2;
  }
  
  .prev {
    left: 0;
  }
  
  .next {
    right: 0;
  }
  
  .book-card:hover {
    transform: scale(1.13);
    transition: transform 0.2s;
  }
  </style>
  