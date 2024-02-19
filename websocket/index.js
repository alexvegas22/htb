import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

let messageId = 1; // Counter for generating unique message IDs
const messages = [];
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
	console.log(`Received message ${data} from user ${username}`);

	// Push a new message object to the messages array
	messages.push({ event, username, text, room});
	
	// Broadcast the new message to all connected clients
	broadcast({event, username, text, room});
    });
    
    ws.on('close', () => {
	const clientMetadata = clients.get(ws);
        const username = clientMetadata ? clientMetadata.username : 'Unknown';

	broadcast({event : 'leave', username: username, room: room});
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

