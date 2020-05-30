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

    # Request.show()

    return sendEthernetFrame(Request)


def writeRequestNameOfStation(dstMacAdress, newName: str):
    option = 0x02
    sub_option = 0x02
    dcp_block_length = 2 + len(newName)
    paddingByte = 0
    block_qualifier_length = 2

    if len(newName) % 2:
        paddingByte = 1

    # debug1 = len(newName)
    # debug2 = len(str(option))
    # debug3 = len(str(sub_option))
    # debug4 = len(str(dcp_block_length))

    dcp_data_length = len(newName) + len(str(option)) + len(str(sub_option)) + len(
        str(dcp_block_length)) + block_qualifier_length + paddingByte

    Request = Ether(src=managementServerMAC, dst=dstMacAdress) / ProfinetIO(frameID=0xFEFD) / ProfinetDCP(
        service_id=0x04, service_type=0x00, option=option, sub_option=sub_option, dcp_data_length=dcp_data_length,
        dcp_block_length=dcp_block_length,
        name_of_station=newName, reserved=0)

    # Request.show()
    return sendEthernetFrame(Request)


def readRequestIPAdress(dstMacAdress):
    option = 0x01
    sub_option = 0x02
    dcp_data_length = len(str(option)) + len(str(sub_option))

    Request = Ether(src=managementServerMAC, dst=profinetIOMulticastMAC) / ProfinetIO(frameID=0xFEFD) / ProfinetDCP(
        service_id=0x03, service_type=0x00, option=option, sub_option=sub_option, dcp_data_length=dcp_data_length,
        reserved=0)

    # Request.show()

    return sendEthernetFrame(Request)
