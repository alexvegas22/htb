<template>
  <div class="post rounded-container">
      <div class="post-image">
	<img v-bind:src="post.img" />
	<a v-bind:href="post.img" class="image-link">{{post.img}}</a>
      </div>
      <div class="post-info">
	<h3>{{post.title}} -{{post.id}}- SEP 22 2002</h3>
	<div class="post-content">
      <p>{{post.content}}</p>
      </div>
      </div>
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
.post{
    display : flex;
    flex-direction : row;
}

.post-image{
display : flex;
flex-direction : column;
width : 250px;
}

h3{
    text-align: left;
    padding-left: 15px;
}

img{
border-radius: 3px;
border : 3px solid var(--primary);
}

.image-link{
height : 25px;
overflow: hidden;

}
.post-info{
    width : 70%;
}
.post-content{
    margin-left: 15px;
    padding : 15px;
    text-align: left;
    
}
</style>
