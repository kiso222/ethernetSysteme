import socket

from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff, AsyncSniffer

from constants import managementServerMAC


def receiveEthernetFrame(interface):
    # sniff(iface=interface, prn=lambda x: x.show(), filter="ether src 00:0c:29:e2:35:30")
    sniff(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    # sniff(iface = interface, prn=lambda x: x.show())

def asyncReceiveEthernetFrame(interface):
    #return AsyncSniffer(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    return AsyncSniffer(iface=interface, prn=lambda x: incomingFrameHandler(x))

def incomingFrameHandler(frame):
    #if frame[Ether].dst == managementServerMAC:
        print('Da ist etwas reingekommen:')
        frame.show()