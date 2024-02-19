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
    if (room.value && name.value){
	joined.value = true
    }
}

function leave(){
    joined.value = false
}
</script>

<template>
  <div class="home-container">
  <div class="rounded-container join-room"  v-if="!joined">
    <h1>Rooms</h1>
    <div class="row">
      <label for="chat.name"> Username : </label> 
      <input v-model="chat.name" placeholder="Enter your name" />  
    </div>
    <div class="row">
      <label for="chat.room"> Room : </label> 
      <input v-model="chat.room" placeholder="Enter room number" /> 
    </div>
      <button @click.prevent="join">Join Room</button>
  </div>

  <div class="rounded-container"  v-if="joined">
    <h1>Room</h1>
   <h3>Logged in as {{chat.name}} </h3>
    
    <button @click.prevent="leave">Leave Room</button>
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
.join-room{
    align-self: center;
    margin: auto;
    display : flex;
    flex-direction : column;
    padding : 25px;
}
.row{
    display : flex;
    justify-content: space-between;
    margin : 10px;
    width : 100%;
}

</style>
