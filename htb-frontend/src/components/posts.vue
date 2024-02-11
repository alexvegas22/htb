<script setup>
//defineProps(['post_id'],['title'],['img'],['user'],['content'])
defineProps(['post'])
</script>

<template>
  <div class="post">
    <div class="post-header">
      <div class="post-image">
	<img v-bind:src="post.img" />
	<a v-bind:href="post.img" class="image-link">{{post.img}}</a>
      </div>
      <div class="post-info">
	<h2>{{post.title}} - #{{post.id}}</h2>
	<div class="post-content">
      <p>{{post.content}}</p>
      </div>
      </div>
      </div>
    <p class="user-name">Posted by {{post.user}}</p>
  </div>
</template>
<script>
export default {
    name: 'Posts',
    props: ['post']
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
