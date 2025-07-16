import socket
import datetime

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

filename = f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
f = open(filename, 'w')

print(f"Server started at {UDP_IP}:{UDP_PORT}, logging to {filename}")

while True:
    data, addr = sock.recvfrom(1024)
    print("received message: %s" % data)
    with open(filename, 'a') as f:
        f.write(f"{data.decode()}\n")