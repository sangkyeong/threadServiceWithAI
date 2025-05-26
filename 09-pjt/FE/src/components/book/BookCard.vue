<template>
  <RouterLink :to="`/books/${bookId}`" class="book-card">
    <img :src="book.cover" alt="book cover" class="book-cover" />
    <div class="book-info">
      <h3 class="book-title" >{{ book.title }}</h3>
      <p class="book-meta">
        {{ book.author }} | {{ book.publisher }} | {{ book.pub_date }}
      </p>
      <p class="book-award">{{ book.subTitle }}</p>
    </div>
  </RouterLink>
</template>

<script setup>
  defineProps({
    book: Object,
    bookId: [Number, String],
    showLink: { type: Boolean, default: true }
  })
</script>

<style scoped>
  .book-card {
    height: 390px;
    overflow: hidden;
    background-color: #2a2a2a;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0,0,0,0.2);
    display: flex;
    gap: 1rem;
    align-items: center;
    color: inherit;
    text-decoration: none;
    flex-direction: column;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s;
  }

  .book-card:hover {
    color: #ff5656;
    transform: translateY(-4px);
  }

  .book-cover {
    width: 100%;
    height: 190px;
    object-fit: contain;
    border-radius: 8px;
  }

  .book-info {
    display: flex;
    flex-direction: column;
    margin-top: 0.75rem;
    overflow: hidden;
  }

  .book-title {
    font-weight: bold;
    font-size: 1.1rem;
    color: #ffffff;
    margin-bottom: 0.5rem;
    
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;     /* 딱 2줄까지만 보여줌 */
    -webkit-box-orient: vertical;
    line-clamp: 2;   
  }

  .book-meta {
    font-size: 0.9rem;
    color: #bbbbbb;
    margin-bottom: 0.5rem;
  }

  .book-award {
    font-size: 0.9rem;
    color: #dddddd;

    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    line-clamp: 2;
  }

</style>
