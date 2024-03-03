import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8880 });

let messageId = 1; // Counter for generating unique message IDs
const messages = [];
const rooms = new Map();
const clients = new Map();

wss.on('connection', function connection(ws, client) {
    ws.on('error', console.error);

  // Send the existing messages array to the new connection
    ws.send(JSON.stringify({ messages: messages.map(msg => ({ event: msg.event, username: msg.username, text: msg.text , room: msg.room})) }));

    ws.on('open', function open() {
	
    });
    
    ws.on('message', function message(data) {
	
	const parsedData = JSON.parse(data);
	const { event, username, text, room } = parsedData;
	if (event=='set-name'){
	    const metadata = {username, room}
	    clients.set(ws, metadata);
	}
	if ( event=='command'){
	    ws.send(JSON.stringify({event:event,username:username,text:text,room:room}))
	    const commandArray = text.split(' ');
	    switch  (commandArray[0]){
	    case '/help' :
		const helpMessage = [
		    "-> Available commands:",
		    "/msg [username] [message] : send a private message to a user",
		    "/users : list all active users in the room",
		    "/leave : leave the room"]
		helpMessage.forEach(help=>
		    ws.send(JSON.stringify({event:'output',username:username,text:help,room:room})));
		break;
	    case '/msg' :
		if (commandArray[1]){
		    const client = Array.from(clients.entries())
			  .filter(([client, metadata]) => metadata.username === commandArray[1])
			  .map(([client]) => client);
		    if (client[0]){
			if(commandArray[2]){
			    const filteredMessage = commandArray.splice(2).join(' ');
			    client[0].send(JSON.stringify({event: 'private', username: username, text: filteredMessage, room: room}));
			} else {
			    ws.send(JSON.stringify({event:'output',username:username,text:'No message has been provided',room:room}));
			}
		    } else {
			ws.send(JSON.stringify({event:'output',username:username,text:`User ${commandArray[1]} does not exist`,room:room}));
		    }
		}else {
		    ws.send(JSON.stringify({event:'output',username:username,text:'No username has been provided',room:room}));
	        }
	        break;
	    case '/users' :
		ws.send(JSON.stringify({ event: 'output', text: 'Users :', room: room }));
		const clientsInRoom = Array.from(clients.entries())
		      .filter(([client, metadata]) => metadata.room === room)
		      .map(([client, metadata]) => {
			  ws.send(JSON.stringify({ event: 'output', username:'server', text: metadata.username, room: room }));	
		      });
		break;
	    default :
		ws.send(JSON.stringify({ event: 'output', username:'server', text:`'${commandArray[0]}' is not a valid command`, room: room }));
	    }
	}
	else{
	    messages.push({ event, username, text, room});
	    broadcast({event, username, text, room});
	}
	console.log(`Received message ${data} from user ${username}`);
	
    });
    
    ws.on('close', () => {
	const clientMetadata = clients.get(ws);
	const username = clientMetadata ? clientMetadata.username : 'Unknown';
	
	broadcast({event : 'leave', username: username, room: clientMetadata.room});
	clients.delete(ws);
    });
});


function broadcast(message) {
    const clientsInRoom = Array.from(clients.entries())
        .filter(([client, metadata]) => metadata.room === message.room)
        .map(([client]) => client);
    for (const client of clientsInRoom) {
        client.send(JSON.stringify(message));
    }
}

