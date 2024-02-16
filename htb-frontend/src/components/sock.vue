<!-- WebSocketExample.vue -->
<template>
  <div class="rounded-container">
    <h1>WebSocket Example</h1>
    <input v-model="name" placeholder="Enter your name" />
    <input v-model="message" placeholder="Type a message" />
    <button @click="sendMessage">Send Message</button>
    
      <p v-for="msg in messages" :key="msg.id">{{msg.id}} : {{ msg.text }}</p>
    
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

