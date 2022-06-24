# -- coding: utf-8 --
#echo_client.py

import socket
import ssl
import pprint
from datetime import datetime
t1 = datetime.now()
from vj1_zad1 import print_machine_info

t1 = datetime.now()
if __name__ == '__main__':
    print_machine_info()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s, ca_certs="c.cert", cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('localhost', 10023))
t2 = datetime.now()
print(ssl_sock.getpeername())
print(ssl_sock.cipher())
print(pprint.pformat(ssl_sock.getpeercert()))

total = t2 - t1
print("Time: ", total)

ssl_sock.write("boo!")
