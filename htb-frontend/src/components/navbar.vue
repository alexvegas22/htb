<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <!-- Your logo or brand text goes here -->
        Awesome Boards
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
  background-color: #344459;
  padding: 1rem;
  color: #fff;
  margin-bottom: 1rem;
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
