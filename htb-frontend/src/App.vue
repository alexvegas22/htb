<template>
  <div id="app" class="layout">
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/navbar.vue';
import General from './components/general.vue';
import CreatePost from './components/create-post.vue';
import Profile from './components/profile.vue';
import Sock from './components/sock.vue';

export default {
  name: 'App',
  components: {
      Navbar,
      General,
      CreatePost,
      Profile,
      Sock
  },
};

</script>

<style>
.layout {
    display:flex;
    flex-direction : column;
    height : 100vh;
}
  
#app {
  text-align: center;
}
</style>
