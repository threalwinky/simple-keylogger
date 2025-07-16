import asyncio
import websockets
import datetime

IP = "127.0.0.1"
PORT = 5005

filename = f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
f = open(filename, 'w')

async def handler(websocket):
    async for message in websocket:
        print(f"received message: {message}")
        with open(filename, 'a') as f:
            f.write(f"{message}\n")

async def main():
    async with websockets.serve(handler, IP, PORT):
        print(f"WebSocket server started on ws://{IP}:{PORT}, logging to {filename}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
