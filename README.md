Install the required dependencies:

```sh
pip install -r requirements.txt
```
Run the server

```sh
python3 server/udp_server.py

or 

python3 server/websocket_server.py
```

Expose server to the Internet: Use [pinggy](https://pinggy.io/) to expose the UDP port or [ngrok](https://ngrok.com/) to expose the WebSocket

#### UDP Client

Run the console client with the server host and port:

```sh
python3 client/console/client.py <host>:<port>
```

Example:
```sh
python3 client/console/client.py rnxdj-2405-4803-c93c-ba20-9600-2a8d-e9fe-237.a.free.pinggy.link:58528
```

Troubleshooting: If you encounter display issues, add the `DISPLAY` environment variable:

```sh
DISPLAY=":0" python3 client/console/client.py <host>:<port>
```

#### Web Client

For web-based usage:
Copy the script from `client/web/client.js` into the browser's web console, remember to update the host and port in the script

#### Data Processing

To convert logs to structured data format:

```sh
python3 server/convert_logs_to_data.py
```

Run this file for more information about log conversion options.