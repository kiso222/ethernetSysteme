from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP, DCPNameOfStationBlock
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
    # Ident.show()
    return sendEthernetFrame(Ident)


def readRequestNameOfStation(dstMacAdress):
    Request = Ether(src=managementServerMAC, dst=dstMacAdress) / ProfinetIO(frameID=0xFEFD) / ProfinetDCP(
        service_id=0x03, service_type=0x00, option=0x02, sub_option=0x02, dcp_data_length=0x02)
    # dcp_block_length=10)  # / DCPNameOfStationBlock(option=0x02, sub_option=0x02,
    # name_of_station = '')

    Request.show()

    return sendEthernetFrame(Request)


def writeRequestNameOfStation(dstMacAdress):
    Request = Ether(src=managementServerMAC, dst=dstMacAdress) / ProfinetIO(frameID=0xFEFD) / ProfinetDCP(
        service_id=0x04, service_type=0x00, option=0x02, sub_option=0x02, dcp_data_length=16, dcp_block_length=0xC,
        name_of_station='terminator', reserved=0)
    #Request = Ether(src=managementServerMAC, dst=dstMacAdress) / ProfinetIO(frameID=0xFEFD) / ProfinetDCP(
    #    service_id=0x04, service_type=0x00, dcp_data_length=0xC, ) / DCPNameOfStationBlock(
    #    option=0x02, sub_option=0x02, dcp_block_length=0xC,
    #    name_of_station='terminator')
    # ProfinetDCP(
    # service_id=0x04, service_type=0x00, option=0x02, sub_option=0x02, dcp_data_length=0x2, dcp_block_length=12,
    # name_of_station='1')

    Request.show()
    return sendEthernetFrame(Request)
