<template>
  <div class="home-container">
  <Profile />
<div class="feed">
  <Posts
    v-for="(item) in posts"
    
    :post='item'
    />
</div>
</div>
</template>

<script>
    import {ref, watchEffect} from 'vue'
import Profile from './profile.vue'
import Posts from './posts.vue'
export default {
    components: {
	Profile,
	Posts
    },
setup() {
    const posts = ref([]);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/posts');
      posts.value = await response.json();
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  watchEffect(() => {
    fetchData();
  });

  return {
    posts,
  };
}
};
</script>

<style scoped>
.home-container{
  display : flex;
  flex-direction : row;
  width : 100%;
}
  
.feed{
    grid-area: feed;
    overflow-y : auto;
    width : 100%
    
}
</style>
