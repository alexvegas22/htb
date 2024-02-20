<!-- sock-chat.vue -->
<template>
<div class="chatbox rounded-container">
  <div class='header'>
    <h2 class="titlex">{{chat.room}}</h2>
    
  </div>
  <div class="response">
    
    <div v-for="msg in messages"
	 :key="msg.username"
	 :class="{
        'event': msg.event !== 'message',
        'message': msg.event === 'message'
     }">
      
      <div v-if="msg.event=='message'" >
	 <div  class="chat-bubble">[{{msg.username}}]$ {{ msg.text }} </div>
      </div>
      
      <div v-if="msg.event=='join'" class="event">
	{{msg.username}} joined the room
      </div>
      
       <div v-if="msg.event=='leave'" >
	{{msg.username}} left the room
       </div>
       
    </div>
  </div>
  <div class="prompt">
     <span>>>></span><input v-model="message" placeholder="Type a message" @keydown.enter="sendMessage"/>
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

    
}

.response{
    min-height: 300px;
    max-height: 500px;
    align-self: center;
    display : flex;
    flex-direction : column;
    align-items: flex-start;
    overflow-y:auto;
    padding : 5px;
    height : 100%;
    width : 100%;
}
.prompt{
    display : flex;
    flex-direction : row;
    align-self: center;
    width : 100%;
    align-items: stretch;		     
}
.prompt:last-child{
    align-self: flex-end;
    justify-self: flex-end;
}

input{

    border : none;
}

button {
    cursor: pointer;
    bakcground: green;
}
</style>
