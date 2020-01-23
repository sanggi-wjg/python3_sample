import argparse
import binascii
import codecs
import struct
from socket import socket, PF_PACKET, SOCK_RAW, htons, AF_PACKET

from uuid import getnode as get_mac

decode_hex = codecs.getdecoder('hex_codec')

trans_ip = lambda addr: ''.join(map(lambda x: chr(eval(x)), addr.split('.')))
trans_mac = lambda mac: ''.join(map(lambda x: decode_hex(x)[0], mac.split(':')))

reverse_ip = lambda addr: ''.join(map(lambda x: str(ord(x)), [x for x in addr]))
reverse_mac = lambda mac: ''.join(map(lambda x: x.encode('hex'), [x for x in mac]))

p16 = lambda x: struct.pack('>H', x)
p32 = lambda x: struct.pack('>I', x)
u16 = lambda x: struct.unpack('>H', x)[0]
u32 = lambda x: struct.unpack('>I', x)[0]


def get_local_mac():
    return ':'.join(("%012X" % get_mac())[i:i + 2] for i in range(0, 12, 2))


def get_target_mac(local_ip: str, local_mac: str, target_ip: str) -> str:
    # while True:
    print('Try get target mac address')
    SendSocket = socket(PF_PACKET, SOCK_RAW, htons(0x0800))

    source_ip = local_ip
    source_mac = local_mac
    dest_ip = target_ip
    dest_mac = "ff:ff:ff:ff:ff:ff"

    arp_protocol = 0x0806

    eth_hdr = trans_mac(dest_mac)
    eth_hdr += trans_mac(source_mac)
    eth_hdr += p16(arp_protocol)

    htype = 0x1
    ptype = 0x0800
    hlen = 0x6
    plen = 0x4
    operation = 0x1

    arp_hdr = ''
    arp_hdr += p16(htype)
    arp_hdr += p16(ptype)
    arp_hdr += chr(hlen)
    arp_hdr += chr(plen)
    arp_hdr += p16(operation)
    arp_hdr += trans_mac(source_mac)
    arp_hdr += trans_ip(source_ip)
    arp_hdr += trans_mac(dest_mac)
    arp_hdr += trans_ip(dest_ip)

    packet = eth_hdr + arp_hdr

    SendSocket.bind(("eth0", 0))
    SendSocket.send(packet)

    RecvSocket = socket(AF_PACKET, SOCK_RAW, htons(0x0003))
    packet = RecvSocket.recvfrom(65535)

    ETH_HEADER = struct.unpack("!6s6s2s", packet[0]['0:14'])

    if binascii.hexlify(ETH_HEADER[2]) == '0806':
        ARP_HEADER = packet[0][14:42]
        ARP = struct.unpack("2s2s1s1s2s6s4s6s4s", ARP_HEADER)
        ARP_HW_TYPE = binascii.hexlify(ARP[0])
        ARP_PR_TYPE = binascii.hexlify(ARP[1])
        ARP_HW_SIZE = binascii.hexlify(ARP[2])
        ARP_PR_SIZE = binascii.hexlify(ARP[3])
        ARP_OPCODE = binascii.hexlify(ARP[4])
        ARP_SRC_MAC = binascii.hexlify(ARP[5])
        ARP_SRC_IP = reverse_ip(ARP[6])
        ARP_DEST_MAC = binascii.hexlify(ARP[7])
        ARP_DEST_IP = reverse_ip(ARP[8])

        if u16(ARP[4]) == 2 and ARP_SRC_IP == target_ip:
            print("Dest Mac Address : ", reverse_mac(ARP_DEST_MAC))
            print("Dest Ip Address : ", ARP_DEST_IP)

            return reverse_mac(ARP[5])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Arp Spoof Python Script')
    parser.add_argument('-l', '--local_ip', default = '192.168.1.228', help = 'Local Server IP')
    parser.add_argument('-t', '--target_ip', default = '192.168.1.59', help = 'Target Window IP')
    parser.add_argument('-g', '--gateway_ip', default = '192.168.1.1', help = 'Gateway')
    args = parser.parse_args()

    local_ip = args.local_ip
    local_mac = get_local_mac()
    target_ip = args.target_ip
    target_mac = get_target_mac(local_ip = local_ip, local_mac = local_mac, target_ip = target_ip)
    gateway_ip = args.gateway_ip

    print('Local IP : ', local_ip)
    print('Local Mac : ', local_mac)
    print('Target IP : ', target_ip)
    print('Gateway : ', gateway_ip)

    print('Target Mac : ', target_mac)
