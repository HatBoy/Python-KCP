#coding=UTF-8

import time
import socket
import random
from lkcp import KcpObj

g_ScriptStartTime = time.time()

def getms():
    return int((time.time()-g_ScriptStartTime)*1000)


def GetMillisecond():
    return int(time.time() * 1000)


def kcp_callback(uid, data):
    s.sendto(data, addr)


def recv_udp(sock):
    try:
        data, udp_addr = sock.recvfrom(65535)
        return data
    except Exception as e:
        pass
    return None


# socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(0)
addr = ("127.0.0.1", 9999)

kcp = KcpObj(123, 1, kcp_callback)
kcp.nodelay(1, 10, 2, 1)
kcp.wndsize(128, 128)
kcp.setmtu(1000)

start_ts = getms()  # 获取代码运行一直到此时的时间差
slap = start_ts

while True:
    current = getms()
    kcp.update(time.time())

    while current >= slap:  # 发送sleep()/100次
        data = str(random.randint(0, 10000))
        print("Send: ", data)
        kcp.send(data)
        slap += 100

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










