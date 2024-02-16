<!-- WebSocketExample.vue -->
<template>
<div class="chatbox rounded-container">
  <div class='header'>
    <h1 class="titlex">Sock Chat</h1>
    <label for="name"> Username : </label>
    <input v-model="name" placeholder="Enter your name" />
  </div>
  <div class="response">
   
    
    <p v-for="msg in messages"
       :key="msg.id"
       :class="[{'message-sent': msg.id===name}]" class="message">{{msg.id}} : {{ msg.text }}</p>
  </div>
  <div class="prompt">
     <input v-model="message" placeholder="Type a message" />
    <button @click="sendMessage">Send Message</button>
</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
const name = ref('')
const message = ref('');
const messages = ref([]);
let socket = null;

const initWebSocket = () => {
  socket = new WebSocket('ws://localhost:8080');

  socket.addEventListener('open', () => {
    console.log('WebSocket connected');
  });

    socket.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    messages.value.push({ id: data.id, text: data.text });
  });

  socket.addEventListener('close', () => {
    console.log('WebSocket closed');
  });
};

const sendMessage = () => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({id:name.value,  text: message.value }));
    message.value = '';
  }
};

onMounted(() => {
  initWebSocket();
});
</script>
<style scoped>
  .chatbox{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: stretch;	   
}
.title{
    align-self: flex-start;
    padding: 5px 10px;
}
.header{
    display:flex;
    flex-direction: row;
    justify-content: space-between;
}

.response{
    min-height: 300px;
    max-height: 500px;
    align-self: center;
    display : flex;
    flex-direction : column;
    align-items: flex-start;
    overflow-y:auto;
    background : #e9e8f1;
    padding : 5px;
    height : 100%;
    width : 100%;
}
.prompt{
    display : flex;
    flex-direction : row;
    align-self: center;
    width : 100%;
    background-color: whitesmoke;
    align-items: stretch;
    justify-content : space-between;
		     
}
.prompt:last-child{
    align-self: flex-end;
    justify-self: flex-end;
}

button, input {
	padding: 5px;
	font: inherit;
	
	
}
input{
    color:black;
    width: 70%;
}

button {
    cursor: pointer;
    bakcground: green;
}

.message{
    border-radius: 5px;
    background :#c9c6dd;
    padding : 3px 7px 5px 7px;
    height : fit-content;
    width: fit-content;
    margin : 3px;
}

.message-sent{
    text-align: right;
   
    align-self:flex-end;
    margin-left : 15px;
 }

.message-received{
    
    text-align: left;
    justify-self:flex-start;
    margin-right : 15px;
}

.message-typing{
    text-align:center;
   justify-content:flex-start;
}

</style>
