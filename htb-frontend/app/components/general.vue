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

function update() {
    fetchData();
}
function switchBoard(newBoard){
    board.value = newBoard
    fetchData();
}

watchEffect(() => {
  fetchData();
});
</script>

<template>
<div class="home-container">
  <div class="sidebar">
    
  <Board :board="board"  @switchboard="switchBoard"/>
  <CreatePost :board="board" @update="update"/>
</div>
    <div class="feed">
      <Posts v-for="item in posts" :key="item.id" :post="item" :board="board"/>
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
  @media (max-width: 768px) {
    .home-container {
        flex-direction: column;
    }
    .feed {
  overflow-y: none;
  width: 100%;
    }
    .sidebar{
	display:flex;
	flex-direction:row;
    justify-content:space-between}
}

.feed {
  overflow-y: auto;
  width: 100%;
}
</style>
