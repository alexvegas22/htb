<template>
<div id="app" class="layout mouse-container" @mousemove="updateMouseCoordinates" >
   <div :style="circleStyle" class="mouse-circle"></div>
    <Navbar />
    <router-view />
  </div>
</template>

<script setup>
import {ref, computed} from 'vue';
import Navbar from './components/navbar.vue';
import General from './components/general.vue';
import CreatePost from './components/create-post.vue';
import Profile from './components/profile.vue';
import Sock from './components/sock.vue';
const mouseX = ref(0);
const mouseY = ref(0);

const updateMouseCoordinates = (event) => {
  requestAnimationFrame(() => {
    mouseX.value = event.clientX;
    mouseY.value = event.clientY;
  });
};

const circleStyle = computed(() => ({

  left: `${mouseX.value}px`,
  top: `${mouseY.value}px`,
}));
</script>

<script>


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
.mouse-container {
  position: relative;
  width: 100%;
  height: 100vh;
}


.mouse-circle {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--primary);
  border: 1px solid var(--text);
  transform: translate3d(0, 0, 0);
  transition:  0.05s;
}
@media (max-width: 768px) {
    .mouse-circle {
	background: none;
	border:none;
    }
}

</style>
