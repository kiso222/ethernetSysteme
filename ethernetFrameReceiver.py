import socket

from scapy.sendrecv import sniff, AsyncSniffer


def receiveEthernetFrame(interface):
    # sniff(iface=interface, prn=lambda x: x.show(), filter="ether src 00:0c:29:e2:35:30")
    sniff(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    # sniff(iface = interface, prn=lambda x: x.show())

def asyncReceiveEthernetFrame(interface):
    return AsyncSniffer(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))