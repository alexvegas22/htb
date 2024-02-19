<!-- WebSocketExample.vue -->
<template>
<div class="chatbox rounded-container">
  <div class='header'>
    <h1 class="titlex">{{chat.room}}</h1>
    
  </div>
  <div class="response">
    
    <div v-for="msg in messages"
	 :key="msg.username" >
      
      <p v-if="msg.event=='message'" :class="[{'message-sent': msg.username===name}]" class="message">
	{{msg.username}} : {{ msg.text }}
      </p>
      <div v-if="msg.event=='join'" class="event">
	{{msg.username}} joined the room
      </div>
       <div v-if="msg.event=='leave'" class="event">
	{{msg.username}} left the room
	</div>
    </div>
  </div>
  <div class="prompt">
     <input v-model="message" placeholder="Type a message" />
    <button @click="sendMessage">Send Message</button>
</div>
</div>

</template>

<script setup>
import { ref, onMounted } from 'vue';
const message = ref('');
const messages = ref([]);
let socket = null;
const props = defineProps({
    chat: Object
})
const name = ref(props.chat.name)
const room=ref(props.chat.room)
const initWebSocket = () => {
  socket = new WebSocket('ws://localhost:8080');

  socket.addEventListener('open', () => {
      console.log('WebSocket connected');
        socket.send(JSON.stringify({ event: 'set-name', username : name.value ,room : room.value}));
       if (socket.readyState === WebSocket.OPEN) {
	   socket.send(JSON.stringify({event: 'join', username: name.value, room: room.value }));
	   //messages.value.push({ event : 'join', username: name.value });
       } else {
	   socket.send(JSON.stringify({event: 'leave', username: name.value, room: room.value }));
       }

    
  });

    socket.addEventListener('message', (event) => {
	const data = JSON.parse(event.data);
	    messages.value.push({ event : data.event, username: data.username, text: data.text, room: data.room });
	    
  });

    socket.addEventListener('close', () => {
	socket.send(JSON.stringify({event: 'leave', username:name.value , room: room.value}));
	console.log('WebSocket closed');
  });
}; 

const sendMessage = () => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({event: 'message', username:name.value,  text: message.value, room: room.value }));
    message.value = '';
  }
};

onMounted(() => {
  initWebSocket();
});
</script>

<script>
  export default{
      name : 'ChatSock',
      props: {
	  name : String
      }
  }
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
