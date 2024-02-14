<template>
  <nav class="rounded-container">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item" href="#">
        <!-- Your logo or brand text goes here -->
        Awesome Boards
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-end">
        <router-link to="/" class="navbar-item">Home</router-link>
        <router-link to="/about" class="navbar-item">About</router-link>
        <!-- Add more navigation links as needed -->
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
/* Your navbar styles go here */

.navbar-brand {
    font-size: 1.5rem;
    color : black;
}

.navbar-item {
  color: black;
  margin-right: 1rem;
}

.navbar-item:hover {
    color : gray;
}
</style>
