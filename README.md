# Usage

Install dependencies:

```sh
pip install -r requirements.txt
```

Run the server:
```sh
python3 server/udp_server.py

# or

python3 server/websocket_server.py
```

You can expose the UDP port using [pinggy](https://pinggy.io/) or expose the WebSocket using [ngrok](https://ngrok.com/).

Client command:

```
python3 client.py <host>:<port>

Example: python3 client.py rnxdj-2405-4803-c93c-ba20-9600-2a8d-e9fe-237.a.free.pinggy.link 58528

If there is an issue, add DISPLAY=":0" before the command.

For web-based, just copy the script into the web console or if you have XSS, remember to change the host and port.
```

Convert log to data: Run file convert_logs_to_data.py for more information