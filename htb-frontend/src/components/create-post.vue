<script setup>
import { ref } from 'vue';
import axios from 'axios';

const title = ref('');
const image = ref(null);
const content = ref('');
const isHidden = ref(true);
const postUrl = ref('http://localhost:5000/posts');


const handleFileChange = () => {
  const selectedFile = image.value.files[0];
  console.log('Selected File:', selectedFile);
};

const createPost = async () => {
    if (title.value && image.value && content.value){
    try {
        const postData = {
            title: title.value,
            image: image.value,
            content: content.value
        };
        const response = await axios.post(postUrl.value, postData);
        console.log('Response:', response.data); 
    } catch (error) {
        console.error('Error:', error.message);
    }
	isHidden.value = true;
	title.value = ""
	image.value = ""
	content.value = ""
    }
};

function hideForm() {
    isHidden.value = !isHidden.value;
}
</script>

<template>
  <div>
    <button @click="hideForm" :class="{ hidden: !isHidden }" >Create a new post</button>
    <form :class="{ hidden: isHidden }" class="post-form">
      <label for="title">Title :</label><br>
      <input v-model="title"><br>

      <label for="image">Image link :</label><br>
      <input ref="image" type="file" accept="image/*" @change="handleFileChange"><br>

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


.form-container {
  max-width: 350px;
  margin: auto;
}

.contact-form {
  display: grid;
  gap: 15px;
}

label {
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  box-sizing: border-box;
}

</style>
