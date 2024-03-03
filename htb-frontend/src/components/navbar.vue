<template>
  <nav class="nav rounded-container">
    <div class="navbar-brand">

      <h2><router-link to="/" class="navbar-item" href="#">
	HTB
      </router-link>
      </h2>
    </div>

    <div class="navbar-menu">
      <div class="navbar-end">
        <router-link to="/" class="navbar-item">Feed</router-link>
        <router-link to="/sock" class="navbar-item">Sock</router-link>
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
}

.navbar-item {
    color : var(--text);
  margin-right: 1rem;
}

.navbar-item:hover {
    background : var(--secondary)
}
</style>
