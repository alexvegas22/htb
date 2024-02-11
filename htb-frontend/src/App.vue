<template>
  <div id="app">
    <Navbar />
    <General />
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/navbar.vue';
import General from './components/general.vue';
export default {
  name: 'App',
  components: {
Navbar,
General
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
