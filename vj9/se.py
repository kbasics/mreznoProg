#tcp_server.py

import socket
import ssl

bindsocket = socket.socket()
bindsocket.bind(('', 10023))
bindsocket.listen(5)


def do_something(connstream, data):
    print(data)
    return False


def deal_with_client(connstream):
    data = connstream.read()
    while data:
        if not do_something(connstream, data):
            break
        data = connstream.read()


while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket, server_side=True, certfile="c.cert", keyfile="k.key")
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
