<script setup>
import { ref } from 'vue';
import axios from 'axios';

const title = ref('');
const image = ref('');
const content = ref('');
const isHidden = ref(true);
const url = ref('http://localhost:5000/posts');

const createPost = async () => {
    if (title.value && image.value && content.value){
    try {
        const postData = {
            title: title.value,
            image: image.value,
            content: content.value
        };
        const response = await axios.post(url.value, postData);
        console.log('Response:', response.data);  // You can handle the response as needed
    } catch (error) {
        console.error('Error:', error.message);
    }}
};

function hideForm() {
    isHidden.value = !isHidden.value;
}
</script>

<template>
  <div>
    <button @click="hideForm" :class="{ hidden: !isHidden }" class="post-button">Create a new post</button>
    <form :class="{ hidden: isHidden }" class="post-form">
      <label for="title">Title :</label><br>
      <input v-model="title"><br>

      <label for="image">Image link :</label><br>
      <input v-model="image"><br>

      <label for="content"> Text :</label><br>
      <input v-model="content"><br>

      
      <button @click.prevent="createPost">Submit</button>
    </form>
  </div>
</template>


<script>
  export default {
  name: 'Create-post',
  };

</script>
<style scoped>
.post-form{
    display : flex;
    flex-direction : column;
    color : #49465d;
    background: #c9c6dd;
    padding : 10px;
    border-radius : 5px;
    transition:
    color 0.5s,
    filter 0.5s;
 
}
.hidden{
    display:none;
}
input{
    width : auto;
    margin : auto;
}
button {
    margin : auto;
    width : auto;
}
</style>
