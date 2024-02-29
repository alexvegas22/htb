<template>
  <div class="rounded-container profile-container">
    <CreatePost :board="board" />

    <select v-model="selected">
      <option @click="$emit('switchboard','general')">General</option>
      <option @click="$emit('switchboard','animals')" >Animals</option>
      <option @click="$emit('switchboard','art')">Art</option>
    </select>
  </div>
    
</template>

<script>
import CreatePost from './create-post.vue';

export default {
    name : 'Profile',
    components : {
	CreatePost
    }
}
</script>

<style scoped>
    .profile-container{
	display : flex;
	flex-direction : column;
    }
</style>



