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
    ws.send(JSON.stringify(messages));

    ws.on('message', function message(data) {
        console.log('received: %s', data);

        // Push a new message object to the messages array
        messages.push({ id, text: data });

        // Broadcast the new message to all connected clients
        broadcast(JSON.stringify({ type: 'message', data: { id, text: data } }));
    });

    ws.on('close', () => {
        clients.delete(ws);
    });
});

// Helper function to broadcast messages to all connected clients
function broadcast(message) {
    for (const client of clients.keys()) {
        client.send(message);
    }
}
