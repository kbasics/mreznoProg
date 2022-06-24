#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

from multiprocessing import Process, Queue
import random

from datetime import datetime
from vj_zad1 import print_machine_info

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

def rand_num():
    num = random.random()
    print ("\n %f" % num)


if __name__ == "__main__":
    queue = Queue()
    processes = [Process(target=rand_num, args=()) for x in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
