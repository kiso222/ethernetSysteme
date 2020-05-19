import socket

from scapy.sendrecv import sniff


def receiveEthernetFrame(interface):
    sniff(iface=interface, prn=lambda x: x.show(), filter="ether src 00:0c:29:e2:35:30")
    # sniff(iface = interface, prn=lambda x: x.show())
