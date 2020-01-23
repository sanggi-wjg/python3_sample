import scapy.all as scapy


def sniff():
    a = scapy.sniff(count = 10)
    a.nsummary()


def scapy_send():
    scapy.send(scapy.IP(dst = '192.168.1.59') / scapy.ICMP())
    scapy.sendp(scapy.Ether() / scapy.IP(dst = '192.168.1.59', ttl = (1, 4,)), iface = 'eth0')


def show_traceroute_graph():
    res, unans = scapy.traceroute(['kr01.warehouse.pickby.us', ], maxttl = 50, retry = 3, dport = [80, 443, ])
    # res.graph()


def simple_send_n_show():
    p = scapy.sr1(scapy.IP(dst = '192.168.1.59') / scapy.ICMP())
    if p:
        p.show()


if __name__ == '__main__':
    simple_send_n_show()
