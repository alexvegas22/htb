<script setup>
import {ref} from 'vue'  
const post_id = ref(0);
const title = ref('Dumbass cat');
const img = ref("https://external-preview.redd.it/_SAG0sDDTrhFv33-mJmfvBuA9sxKN4qq5X7Mbk-NztQ.jpg?auto=webp&s=bf2014f99fbda79ed9cd8fb4b9673e7ff09825f5");
const user = ref('veal');
const content = ref('Look at this image of this cat. Why is he standing...');
</script>

<template>
  <div class="post">
    <div class="post-header">
      <div class="post-image">
	<img v-bind:src="img" />
	<a v-bind:href="img" class="image-link">{{img}}</a>
      </div>
      <div class="post-info">
	<h2>{{title}} - #{{post_id}}</h2>
	<div class="post-content">
      <p>{{content}}</p>
      </div>
      </div>
      </div>
    <p class="user-name">Posted by {{user}}</p>
  </div>
</template>
<script>
export default {
name: 'Posts',
};
</script>
<style scoped>
/* Add styles for what the posts should look like*/
.post{
    display : flex;
    flex-direction : column;
    background : #334455;
    width: 95%;
    margin : auto;
    border-top : 2px solid gray;
    border-bottom : 2px solid gray;
}

.post-header{
    display : flex;
justify-content: space-between;
    padding :10px 15px;
}
.post-image{
display : flex;
flex-direction : column;
width: 30%;
}
.image-link{
height : 25px;
overflow: hidden;
color : #999999
}
.post-info{
    width : 70%;
}
.post-content{

    color : whitesmoke;
    margin : 0;
    padding : 15px;
    text-align: left;
    
}

.user-name{
    align-self: flex-start;
    padding : 0 15px;
}
</style>
