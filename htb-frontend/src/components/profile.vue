<template>
  <div class="rounded-container profile-container">
    Profile Section
    
  <CreatePost />
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
	grid-area:profile;
	
    }
</style>
