from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sendp, sr

# def sendEthernetFrame(ethernetFrame: EthernetFrame):
#      assert(len(ethernetFrame.src) == len(ethernetFrame.dst) == 6)
#      assert(len(ethernetFrame.type) == 2)  # 16-bit Ethernet type
#
#     s = socket(AF_PACKET, SOCK_RAW)
#     s.bind(ethernetFrame.interface, 0)
#     return s.send(ethernetFrame.dst + ethernetFrame.src + ethernetFrame.type + ethernetFrame.payload)
from constants import managementServerNICName, managementServerMAC, profinetIOMulticastMAC


def sendEthernetFrame(scapyFrame):
    return sendp(scapyFrame, iface=managementServerNICName)


def sendAndReceiveEthernetFrame(scapyFrame):
    return sr(scapyFrame)


# def sendEthernetFrame(scapyEthernetFrame):
#    return sendp(scapyEthernetFrame)

def identRequestAll():
    Ident = Ether(src=managementServerMAC, dst=profinetIOMulticastMAC) / ProfinetIO(frameID=0xFEFE) / ProfinetDCP(
        service_id=0x05, service_type=0x00,
        option=0xFF, sub_option=0xFF,
        dcp_data_length=0x04)
    #Ident.show()
    return sendEthernetFrame(Ident)
