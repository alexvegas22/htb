<template>
  <div class="post rounded-container">
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
    props: {
	post: Object
    }
};
</script>
<style scoped>
/* Add styles for what the posts should look like*/
.post{
    display : flex;
    flex-direction : column;
}

.post-header{
    display : flex;
    justify-content: space-between;
    padding :10px 15px;
}
.post-image{
display : flex;
flex-direction : column;
width : 250px;
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

    margin : 0;
    padding : 15px;
    text-align: left;
    
}

.user-name{
    align-self: flex-start;
    padding : 0 15px;
}
</style>
