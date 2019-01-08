#coding=UTF-8

from . import core

__all__ = ["KcpObj"]

class KcpObj:
    def __init__(self, conv, id, callback):
        """
        :param conv: conv为一个表示会话编号的整数，和tcp的 conv一样，通信双方需保证 conv相同，相互的数据包才能够被认可
        :param id: user表示用户的id
        :param callback: KCP的下层协议输出函数，KCP需要发送数据时会调用它，需要传入id和要发送的数据buffer两个参数
        """
        self.cobj = core.lkcp_create(conv, id, callback)

    def recv(self, len=4*1024*1024):
        return core.lkcp_recv(self.cobj, len)

    def send(self, data):
        return core.lkcp_send(self.cobj, data)

    def update(self, current):
        """
        以一定频率调用 ikcp_update来更新 kcp状态，并且传入当前时钟（毫秒单位）如 10ms调用一次，或用 ikcp_check确定下次调用
        update的时间不必每次调用
        :param current: 当前时钟毫秒
        :return:
        """
        core.lkcp_update(self.cobj, current)

    def check(self, current):
        return core.lkcp_check(self.cobj, current)

    def input(self, data):
        """
        收到一个下层数据包（比如UDP包）时需要调用
        :param data:
        :return:
        处理了下层协议的输出/输入后 KCP协议就可以正常工作了，使用 ikcp_send 来向 远端发送数据。
        而另一端使用 ikcp_recv(kcp, ptr, size)来接收数据。
        """
        return core.lkcp_input(self.cobj, data)

    def flush(self):
        core.lkcp_flush(self.cobj)

    def peeksize(self):
        return core.lkcp_peeksize(self.cobj)

    def setmtu(self, mtu):
        """
        纯算法协议并不负责探测 MTU，默认 mtu是1400字节，可以使用ikcp_setmtu来设置该值。
        该值将会影响数据包归并及分片时候的最大传输单元。
        :param mtu:
        :return:
        """
        return core.lkcp_setmtu(self.cobj, mtu)

    def wndsize(self, sndwnd, rcvwnd):
        """
        该调用将会设置协议的最大发送窗口和最大接收窗口大小，默认为32. 这个可以理解为 TCP的 SND_BUF 和 RCV_BUF，
        只不过单位不一样 SND/RCV_BUF 单位是字节，这个单位是包。
        :param sndwnd:
        :param rcvwnd:
        :return:
        """
        return core.lkcp_wndsize(self.cobj, sndwnd, rcvwnd)

    def waitsnd(self):
        return core.lkcp_waitsnd(self.cobj)

    def nodelay(self, nodelay, interval, resend, nc):
        """
        协议默认模式是一个标准的 ARQ，需要通过配置打开各项加速开关
        :param nodelay: 是否启用 nodelay模式，0不启用；1启用
        :param interval: 协议内部工作的 interval，单位毫秒，比如 10ms或者 20ms
        :param resend: 快速重传模式，默认0关闭，可以设置2（2次ACK跨越将会直接重传）
        :param nc: 是否关闭流控，默认是0代表不关闭，1代表关闭
        :return:
        普通模式：`ikcp_nodelay(kcp, 0, 40, 0, 0);
        极速模式： ikcp_nodelay(kcp, 1, 10, 2, 1);
        """
        return core.lkcp_nodelay(self.cobj, nodelay, interval, resend, nc)





