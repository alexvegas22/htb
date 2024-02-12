<script setup>
  import {ref} from 'vue'
  import Posts from './posts.vue'
  const posts = ref([
      {id:1, title :'Dumbass cat', img :"https://external-preview.redd.it/_SAG0sDDTrhFv33-mJmfvBuA9sxKN4qq5X7Mbk-NztQ.jpg?auto=webp&s=bf2014f99fbda79ed9cd8fb4b9673e7ff09825f5", user:'veal', content :'Look at this image of this cat. Why is he standing...'},
      
      {id:2, title :'Strange dog', img :"https://i.redd.it/2adub8se2dlb1.jpg", user:'veal', content :'Okay, this dog is kinda freaky'},
      
  ]);
</script>

<template>
  <h1>General</h1>
  <Posts
    v-for="post in posts"
    
    :post='post'
    />
</template>

<script>
  export default {
      name : 'General',
      components: {Posts},
      props: ['posts']
  }
</script>

<style scoped>

</style>
