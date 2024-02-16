import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

let messageId = 1; // Counter for generating unique message IDs
const messages = [];
const clients = new Map();

wss.on('connection', function connection(ws) {
  const id = messageId++;
  const color = Math.floor(Math.random() * 360);
  const metadata = { id, color };

  clients.set(ws, metadata);

  // Send the existing messages array to the new connection
 // ws.send(JSON.stringify({ messages: messages.map(msg => ({ id: msg.id, text: msg.text })) }));

  ws.on('message', function message(data) {
    console.log('received: %s', data);

    const parsedData = JSON.parse(data);
      const { id, text } = parsedData;
      

    // Push a new message object to the messages array
    messages.push({ id, text });

    // Broadcast the new message to all connected clients
      broadcast({id,text});
  });

  ws.on('close', () => {
    clients.delete(ws);
  });
});

// Helper function to broadcast messages to all connected clients
function broadcast(message) {
  for (const client of clients.keys()) {
      client.send(JSON.stringify(message));
  }
}
