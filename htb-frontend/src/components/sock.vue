<!-- WebSocketExample.vue -->
<template>
  <div class="home-container">
  <div class="rounded-container">
    <h1>Rooms</h1>
    <label for="name"> Username : </label>
    <input v-model="name" placeholder="Enter your name" />
    <label for="room"> Username : </label>
    <input v-model="room" placeholder="Enter room number" />
  </div>
<div class="chatbox rounded-container">
  <div class='header'>
    <h1 class="titlex">Sock Chat</h1>
    
  </div>
  <div class="response">
   
    
    <div v-for="msg in messages"
	 :key="msg.id" >
      
      <p v-if="msg.event=='message'" :class="[{'message-sent': msg.id===name}]" class="message">
	{{msg.id}} : {{ msg.text }}
      </p>
      <div v-if="msg.event=='join'" class="event">
	{{msg.id}} joined the room
      </div>
       <div v-if="msg.event=='leave'" class="event">
	{{msg.id}} left the room
	</div>
    </div>
  </div>
  <div class="prompt">
     <input v-model="message" placeholder="Type a message" />
    <button @click="sendMessage">Send Message</button>
</div>
</div>
</div>

{{messages}}
</template>

<script setup>
import { ref, onMounted } from 'vue';
const name = ref('veal')
const message = ref('');
const messages = ref([]);
const room=ref()
let socket = null;

const initWebSocket = () => {
  socket = new WebSocket('ws://localhost:8080');

  socket.addEventListener('open', () => {
      console.log('WebSocket connected');
       if (socket.readyState === WebSocket.OPEN) {
	   socket.send(JSON.stringify({event: 'join', id:name.value }));
	   //messages.value.push({ event : 'join', id: name.value });
  }

    
  });

    socket.addEventListener('message', (event) => {
	const data = JSON.parse(event.data);
	    messages.value.push({ event : data.event, id: data.id, text: data.text });
	    
  });

  socket.addEventListener('close', () => {
      console.log('WebSocket closed');
      socket.send(JSON.stringify({event: 'leave', id:name.value }));
  });
};

const sendMessage = () => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({event: 'message', id:name.value,  text: message.value }));
    message.value = '';
  }
};

onMounted(() => {
  initWebSocket();
});
</script>
<style scoped>

.home-container {
  display: flex;
  flex-direction: row;
  width: 100%;
}
.chatbox{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: stretch;
    width: 100%;
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
.event{
    color : red;
    text-align : center;
    
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
