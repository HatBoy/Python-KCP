#coding=UTF-8

import socket
import time
from lkcp import KcpObj


# send回调函数
def kcp_callback(uid, data):
    s.sendto(data, uid_addr[uid])

def recv_udp(sock):
    try:
        data, udp_addr = sock.recvfrom(65535)
        uid_addr[1] = udp_addr
        return data
    except Exception as e:
        pass
    return None

# socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(0)
addr = ("127.0.0.1", 9999)
s.bind(addr)

# 存放连接客户端字典
uid_addr = {}
kcp = KcpObj(123, 1, kcp_callback)

kcp.nodelay(1, 10, 2, 1)
kcp.wndsize(128, 128)
kcp.setmtu(1000)

while True:
    kcp.update(time.time())

    while True:
        data = recv_udp(s)
        if data is None:
            break
        kcp.input(data)

    while True:
        lens, data = kcp.recv()
        if lens < 0:
            break
        print("Recv: ", data)
        kcp.send(data)
    time.sleep(0.1)