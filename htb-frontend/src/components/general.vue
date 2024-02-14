<template>
  <h1>General</h1>
  <Posts
    v-for="(item) in posts"
    
    :post='item'
    />
</template>

<script>
  import {ref, watchEffect} from 'vue'
import Posts from './posts.vue'
export default {
    components: {
	Posts
    },
setup() {
    const posts = ref([]);
    watchEffect( async () => {
    posts.value = await (await fetch(`http://localhost:5000/posts`)).json()
    });
    return {
	posts
    };
}
};
</script>

<style scoped>
background : --color-background-soft
</style>
