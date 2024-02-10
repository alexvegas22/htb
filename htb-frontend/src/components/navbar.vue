<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <!-- Your logo or brand text goes here -->
        My Vue App
      </a>
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
.navbar {
  background-color: #3498db;
  padding: 1rem;
  color: #fff;
}

.navbar-brand {
  font-size: 1.5rem;
}

.navbar-item {
  color: #fff;
  margin-right: 1rem;
}

.navbar-item:hover {
  text-decoration: underline;
}
</style>
