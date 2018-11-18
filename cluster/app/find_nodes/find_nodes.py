import os
import socket
import multiprocessing
import subprocess
from myip import *
from ping import *


def map_network(pool_size=255):

    ip_list = list()

    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(
        jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


def main():
    return map_network()


if __name__ == '__main__':
    print(main())