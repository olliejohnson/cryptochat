import socket
import dotenv
import os

dotenv.load_dotenv()

class Listener:
    def __init__(self,port):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((socket.gethostname(), int(port)))
        serversocket.listen(5)

print(os.getenv('LISTEN_PORT'))
listener = Listener(os.getenv('LISTEN_PORT'))
