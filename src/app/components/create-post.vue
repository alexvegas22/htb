<script setup>
import { ref } from 'vue';
import axios from 'axios';

const props = defineProps(['board'])

const title = ref('');
const image = ref(null);
const content = ref('');
const isHidden = ref(true);
const apiUrl = import.meta.env.VITE_API_URL
const apiPort = import.meta.env.VITE_API_PORT 
const postUrl = ref(`${apiUrl}/`);
const selectedFile = ref(null)
const emit = defineEmits(['update'])

const handleFileChange = () => {
  selectedFile.value = image.value.files[0];
  console.log('Selected File:', selectedFile);
};

const createPost = async () => {
    if (title.value && image.value && content.value){
        try {
            const formData = new FormData();
            formData.append('title', title.value);
            formData.append('image', selectedFile.value);
            formData.append('content', content.value);
	    let url = `${postUrl.value}${props.board}/posts`;
            const response = await axios.post(url, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
	     emit('update')
            console.log('Response:', response.data); 
        } catch (error) {
            console.error('Error:', error.message);
        }
        isHidden.value = true;
        title.value = "";
        image.value = null;
        content.value = "";
    }
};

function hideForm() {
    isHidden.value = !isHidden.value;
}
</script>

<template>
  <div class="rounded-container">
    <button @click="hideForm" :class="{ hidden: !isHidden }" >Create a new post</button>
    <form :class="{ hidden: isHidden }" class="post-form">
      <label for="title">Title :</label><br>
      <input v-model="title"><br>

      <label for="image">Image link :</label><br>
      <input ref="image" type="file" accept="image/*" @change="handleFileChange"><br>

      <label for="content"> Text :</label><br>
      <input v-model="content"><br>
      
      <button @click.prevent="createPost">Post to {{props.board}}</button>
    </form>
  </div>
</template>

<script>
  export default {
  name: 'CreatePost',
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
