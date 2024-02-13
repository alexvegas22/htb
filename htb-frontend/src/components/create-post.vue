<script setup>
import {ref} from 'vue'
const title = ref()
const image = ref()
const content = ref()
const isHidden = ref(true)
function createPost(){
    alert("Post created (Not!) \n Title : "+ title.value+"\n Image : "+image.value+"\n Text : "+content.value)
}
function hideForm(){
    isHidden = false
}
</script >
<template>
<button  @click="hideForm" class="post-button">Create a new post</button>
<form :class="{ hidden : isHidden }" class="post-form">
   <label for="title">Title :</label><br>
  <input v-model="title"><br>
   <label for="image">Image link :</label><br>
  <input v-model="image"><br>
   <label for="content"> Text :</label><br>
   <input v-model="content"><br>
   <button @click="createPost">Post</button><br>
  </form>
</template>
<script>

  export default {
  name: 'Create-post',
};
</script>
<style scoped>
  .post-button{
  font-size:24px;
  background:none;
  color : whitesmoke;
  text-decoration:underline;
  }
  
  .post-button:hover{
  color : #934488
  }

  .post-form{
 display : flex;
    flex-direction : column;
    background : #334455;
    width: 95%;
    margin : auto;
    border-top : 2px solid gray;
    border-bottom : 2px solid gray;
    padding:30px;
  }
  .hidden{
     display:none;
  }
</style>
