<script setup>
  const apiUrl = import.meta.env.VITE_API_URL
  const apiPort = import.meta.env.VITE_API_PORT
  const url = `${apiUrl}:${apiPort}`
</script>
<template>
  <img :src="'$url/'+$route.params.boardName+'/'+$route.params.imageName" />
 {{$route.params.imageName}}
</template>
<style scoped>
img{
    height:auto;
    width:auto;
    
    max-height: 70%;
    max-width:70%;
    margin:0;
    padding:0;
    border-radius: 5px;
    border: 3px solid var(--primary);
    align-self: center;
}

  
</style>
