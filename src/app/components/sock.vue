<!-- sock.vue -->
<script setup>
import { ref, onMounted } from 'vue';
 import ChatSock from './sock-chat.vue'

 navigator.browserSpecs = (function(){
        var ua = navigator.userAgent, tem, 
            M = ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];
        if(/trident/i.test(M[1])){
            tem = /\brv[ :]+(\d+)/g.exec(ua) || [];
            return {name:'IE',version:(tem[1] || '')};
        }
        if(M[1]=== 'Chrome'){
            tem = ua.match(/\b(OPR|Edge)\/(\d+)/);
            if(tem != null) return {name:tem[1].replace('OPR', 'Opera'),version:tem[2]};
        }
        M = M[2]? [M[1], M[2]]: [navigator.appName, navigator.appVersion, '-?'];
        if((tem = ua.match(/version\/(\d+)/i))!= null)
            M.splice(1, 1, tem[1]);
        return {name:M[0], version:M[1]};
    })();

const chat =ref({
    room: '',
    name: ''
})
const specs = "Sock 1.0 ("+navigator.browserSpecs.name+" ver. "+navigator.browserSpecs.version+")"
const log = ref([specs,'Type your username: '])
const command = ref('')

const joined=ref(false)

function join(){
    if (chat.value.room && chat.value.room){
	joined.value = true
    }
}

function leave(){
    joined.value = false
    chat.value.room = ''
}

function processCommand(){
    if (!chat.value.name){
	chat.value.name=command.value
	log.value.pop()
	log.value.push("Welcome "+chat.value.name)
	log.value.push("Type 'help' for more information")
    }
    else {
	log.value.push('['+chat.value.name+']$ '+command.value)
	const commandArray = command.value.split(' ');
	switch (commandArray[0]) {

	case 'help' :
	    log.value.push("These commands are defined internally. Type 'help' to see this list.")
	    log.value.push("chatroom [-j name] [--join name]")
	    log.value.push("clear")
	    log.value.push("logout")
	    log.value.push("exit")
	    break;

	case 'chatroom':
	    if (!commandArray[1]){
	    log.value.push("No arguments provided.")
	    log.value.push("Try 'chatroom --help' for more details.")
	    }
	    else if (commandArray[1] == '-j'| commandArray[1] == '--join'){
		if (commandArray[2]){
		    chat.value.room = commandArray[2]
		    join()
		} else {
		    log.value.push('Missing argument.')
		    log.value.push("Try 'chatroom --help' for more details.")
		}
	    }
	    else if (commandArray[1] == '-h'| commandArray[1] == '--help'){
		log.value.push('Usage : chatroom [options]')
		log.value.push('Options: ')
		log.value.push('-j --join  [arg]  join the provided room')
		log.value.push('-h --help         display this list')
	    }
	    
	    else {
		log.value.push("chatroom: unrecognized option '"+commandArray[1]+"'")
	    }
	    
	    break;

	case 'clear':
	    log.value=[]
	    break;
	case 'logout':
	    chat.value.name = ''
	    log.value=[specs,'Type your username: ']
	    break;
	default :
	    log.value.push(commandArray[0]+': command not found')
	    break;
	}
    }
    command.value = ''
}
onMounted(()=> joined.value=false )
</script>

<template>
  <div class="home-container">
  <div class="rounded-container join-room"  v-if="!joined">
    <h2>Sock</h2>

   <div class="terminal">
      <div v-for="command in log">
	{{command}}
      </div>
     <span v-if="!chat.name"> >>> </span><span v-if="chat.name">[{{chat.name}}]$ </span>  <input v-model="command" @keydown.enter="processCommand" />
   </div>
  </div>
  
  
<ChatSock v-if="joined" :chat="chat" @leave="leave"/>
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
 
    width: 100%;
}
.terminal{
    text-align: left;
}
input{
    border : none;
}
</style>
