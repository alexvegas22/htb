<script setup>
import {ref} from 'vue';
import axios from 'axios';
const title = ref()
const image = ref()
const content = ref()
const isHidden = ref(true)
function createPost(){
    try {
	const postData = {
	    title : title,
	    image : image,
	    content : content
	}
    } catch (error) {
	console.error('Error:', error.message);
    }
};
function  hideForm() {
    isHidden.value = !isHidden.value
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
