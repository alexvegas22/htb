<script setup>
import { ref, computed } from 'vue';

// Destructure props
const { post, board } = defineProps(['post', 'board']);

</script>

<template>
  <div class="post rounded-container">
    <div class="post-image">
      <img :src="`http://localhost:5000/${board}/${post.image}`" />
      <router-link :to="{ name: 'image', params: { imageName: post.image }}" class="image-link">
        {{ post.image }}
      </router-link>
    </div>
    <div class="post-info">
      <h3 v-if="post.title">{{ post.title }}</h3>
      <div class="post-content" v-if="post.content">
        <p>{{ post.content }}</p>
      </div>
      {{ post.date }} - {{ post.id }}
    </div>
  </div>
</template>

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
    display : flex;
    flex-direction: column;
    
}
.post-info:last-child{
    jusitfy-self:flex-end;
}
.post-content{
    margin-left: 15px;
    padding : 15px;
    text-align: left;
    
}
</style>
