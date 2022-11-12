import socket
import dotenv
import os

dotenv.load_dotenv()

class Listener:
    def __init__(self,port):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(("0.0.0.0", int(port)))
        serversocket.listen(9)
        conn, addr = serversocket.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        while True:
            data = conn.recv(1024).decode("UTF-8")
            print(data, end="")
            if not data:
                break

print(os.getenv('LISTEN_PORT'))
listener = Listener(os.getenv('LISTEN_PORT'))
