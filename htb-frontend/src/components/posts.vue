<template>
  <div class="post rounded-container">
      <div class="post-image">
	<img v-bind:src="'http://localhost:5000/general/'+post.image" />
	<router-link :to="{ name: 'image', params: { imageName: post.image }}" class="image-link">{{post.image}}</router-link>
      </div>
      <div class="post-info">
	<h3>{{post.title}} </h3>
	<div class="post-content">
      <p>{{post.content}}</p>
	</div>
	{{post.date}} - {{post.id}}
      </div>
  </div>
</template>
<script>
export default {
    props: {
	post: Object,
	board : String
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
