from socket import *

from scapy.layers.l2 import Ether
from scapy.sendrecv import sendp

import EthernetFrame

# def sendEthernetFrame(ethernetFrame: EthernetFrame):
#      assert(len(ethernetFrame.src) == len(ethernetFrame.dst) == 6)
#      assert(len(ethernetFrame.type) == 2)  # 16-bit Ethernet type
#
#     s = socket(AF_PACKET, SOCK_RAW)
#     s.bind(ethernetFrame.interface, 0)
#     return s.send(ethernetFrame.dst + ethernetFrame.src + ethernetFrame.type + ethernetFrame.payload)
from main import sendingNetworkInterface


def sendEthernetFrame(scapyEthernetFrame):
    return sendp(scapyEthernetFrame)