<!-- sock-chat.vue -->
<template>
<div class="chatbox rounded-container">
  <div class="response">
    
    <div v-for="msg in messages">
      
      <div v-if="msg.event==='message' || msg.event==='command'" >
	<span v-if="msg.username==name">[</span>{{msg.username}}#{{msg.room}}<span v-if="msg.username==name">]</span> <span v-if="msg.username!=name">: </span>{{ msg.text }}
      </div>
      <div v-if="msg.event==='output'" class='output' >
	 {{ msg.text }}
      </div>
      <div v-if="msg.event==='private'" class="privateMessage">
	[Private Message] {{msg.username}} : {{msg.text}}
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
     <span>>>> </span><input v-model="message" placeholder="Type a message" @keydown.enter="sendMessage"/>
  </div>
</div>

</template>
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
const message = ref('');
const messages = ref([]);
let socket = null;
const props = defineProps({
    chat: Object
})
const emit = defineEmits(['inFocus', 'submit'])
const name = ref(props.chat.name)
const room=ref(props.chat.room)
const websocket_url = import.meta.env.VITE_WEBSOCKET_URL;
const websocket_port = import.meta.env.VITE_WEBSOCKET_PORT;
const initWebSocket = () => {
    socket = new WebSocket(`${websocket_url}:${websocket_port}`);

  socket.addEventListener('open', () => {
      console.log('WebSocket connected');
        socket.send(JSON.stringify({ event: 'set-name', username : name.value, room : room.value}));
       if (socket.readyState === WebSocket.OPEN) {
	   socket.send(JSON.stringify({event: 'join', username: name.value, room: room.value }));
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
	if (message.value==='/leave'){
	    emit('leave')
	}
	if (message.value[0]=='/'){
	    socket.send(JSON.stringify({event: 'command', username:name.value,  text: message.value, room: room.value }));
	    
	}
	else{socket.send(JSON.stringify({event: 'message', username:name.value,  text: message.value, room: room.value }));}
    
    message.value = '';
  }
};

onMounted(() => {
  initWebSocket();
});
onUnmounted(() => {
      if (socket && socket.readyState === WebSocket.OPEN) {
        socket.close();
      }
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
.output{
    color: gray;
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
