<!-- general.vue -->
<script setup>
import { ref, watchEffect } from 'vue';
import Profile from './profile.vue';
import Posts from './posts.vue';
import Boards from './boards.vue';

const posts = ref([]);
const board = ref('general')

const fetchData = async () => {
  try {
    const response = await fetch(`http://localhost:5000/${board.value}/posts`);
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
    <Profile :board="board" @switchboard="switchBoard"/>
  
    
    <div class="feed">
      <Posts v-for="item in posts" :key="item.id" :post="item" />
    </div>
 
  </div>
</template>

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
