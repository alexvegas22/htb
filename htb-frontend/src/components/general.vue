<!-- general.vue -->
<script setup>
import { ref, watchEffect } from 'vue';
import Posts from './posts.vue';
import CreatePost from './create-post.vue'
import Board from './boards.vue';

const posts = ref([]);
const board = ref('general')

const apiUrl = import.meta.env.VITE_API_URL
const apiPort = import.meta.env.VITE_API_PORT

const fetchData = async () => {
  try {
    const response = await fetch(`${apiUrl}:${apiPort}/${board.value}/posts`);
    posts.value = await response.json();
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
};

function switchBoard(newBoard){
    board.value = newBoard
}

watchEffect(() => {
  fetchData();
});
</script>

<template>
  <div class="home-container">
    <div class="feed">
      <Posts v-for="item in posts" :key="item.id" :post="item" :board="board"/>
    </div>
<div>
  <CreatePost :board="board"/>
  
   <Board :board="board"  @switchboard="switchBoard"/>
</div>
  </div>
</template>

<script>
export default {
    name : 'General',
    components : {
	CreatePost,
	Board,
	Posts
    }
}

</script>
<style scoped>
.home-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  overflow-y: auto;
}

.feed {
  overflow-y: auto;
  width: 100%;
}
</style>
