<template>
  <div class="rounded-container profile-container">
    <CreatePost :board="board" />
    <input type="radio" id="general" value="general" @click="$emit('switchboard','general')" />
    <label for="general">general</label>

    <input type="radio" id="animals" value="animals"  @click="$emit('switchboard','animals')" />
    <label for="animals">animals</label>
    
     <input type="radio" id="art" value="art"  @click="$emit('switchboard','art')" />
    <label for="art">art</label>
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
