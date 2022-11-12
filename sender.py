class Peer:
    default_ip = '127.0.0.1'
    default_port = os.getenv('LISTEN_PORT')

    def __init__(self,ip=default_ip,port=default_port):
        self.ip = ip
        self.port = ip



class Sender:
    peers = []

    def add_peer(self,peer):
        peers.add(peer)
