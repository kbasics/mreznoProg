#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

import socket
import subprocess
import sys
from datetime import datetime
from vj_zad1 import print_machine_info
from logging.handlers import TimedRotatingFileHandler
from multiprocessing import Process, Queue
import threading

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

print_lock = threading.Lock()
q = Queue(maxsize=0)


def threader():
    while True:
        port = q.get()
        tcp_scanner(port)


def main():
    for x in range(port1, port2, ):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    for port in range(port1, port2):
        q.put(port)

    q.join

hostname = input("Upisi host name: ")
hostnameIP = socket.gethostbyname(hostname)

port1 = int(input("Upisi početni port: "))
port2 = int(input("Upisi zavrsni port: "))
print("prvi port: {}, drugi port: {}".format(port1,port2))



def tcp_scanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        result = sock.connect_ex((hostnameIP, port))
        socket.setdefaulttimeout(0.5)
        if result == 0:
            print("Port {}:        Otvoren".format(port))

        else:
            print("Port {}:        Zatvoren".format(port))
            sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()



t2 = datetime.now()
total = t2 - t1

for port in range(port1, port2):
        tcp_scanner(port)
        print(total)
