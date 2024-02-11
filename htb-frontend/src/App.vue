<template>
  <div id="app">
    <Navbar />
    <Posts />
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/navbar.vue';
import Posts from './components/posts.vue';
export default {
  name: 'App',
  components: {
Navbar,
Posts
  },
};
</script>

<style>
/* Your global styles go here */
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}

#app {
  text-align: center;
}
</style>
