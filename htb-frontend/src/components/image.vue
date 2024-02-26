<script setup>
</script>
<template>
  <img :src="'http://localhost:5000/general/'+$route.params.imageName" />
  {{$route.params.imageName}}
</template>
