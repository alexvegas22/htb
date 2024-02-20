<template>
  <div class="rounded-container profile-container">
    <h3>Profile Section</h3>
    
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
