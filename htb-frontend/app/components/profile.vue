<template>
  <div class="rounded-container profile-container">
    <CreatePost :board="board" />

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
	justify-content:space-between;
    }
</style>



