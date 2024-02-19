<!-- sock.vue -->
<script setup>
import { ref, onMounted } from 'vue';
 import ChatSock from './sock-chat.vue'

const chat =ref({
    room: '',
    name: ''
})

const joined=ref(false)

function join(){
    joined.value = true
}

</script>

<template>
  <div class="home-container">
  <div class="rounded-container">
    <h1>Rooms</h1>
    <label for="chat.name"> Username : </label>
    <input v-model="chat.name" placeholder="Enter your name" />
    <label for="chat.room"> Room : </label>
    <input v-model="chat.room" placeholder="Enter room number" />
    <button @click.prevent="join">Join Room</button>
  </div>
<ChatSock v-if="joined" :chat="chat"/>
</div>

</template>



<script>


export default {
    name : 'Sock',
    components : {
	ChatSock
    }
}
</script>

<style scoped>

.home-container {
    display: flex;
    flex-direction: row;
    width: 100%;
}

</style>
