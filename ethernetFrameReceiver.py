import socket
from pprint import pprint

from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP
from scapy.layers.l2 import Ether, Dot1Q
from scapy.sendrecv import sniff, AsyncSniffer
from scapy2dict import to_dict

from Device import Device, listContainsDevice, getPositionOfDeviceInList
from constants import managementServerMAC, allDevices


def receiveEthernetFrame(interface):
    # sniff(iface=interface, prn=lambda x: x.show(), filter="ether src 00:0c:29:e2:35:30")
    sniff(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    # sniff(iface = interface, prn=lambda x: x.show())


def asyncReceiveEthernetFrame(interface):
    # return AsyncSniffer(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    return AsyncSniffer(iface=interface, prn=lambda x: incomingFrameHandler(x))


def incomingFrameHandler(frame):
    if frame[Ether].dst == managementServerMAC:
        print('Da ist etwas reingekommen.')
        frame.show()
        try:
            if frame[Dot1Q].type == 0x8892:
                if frame[ProfinetIO].frameID == 0xFEFF and frame[ProfinetDCP].service_id == 0x05 and frame[
                    ProfinetDCP].service_type == 0x01:
                    print('Identify Response eingegangen')

                    dict = frameToDict(frame)

                    # print(dict)
                    macAdress = dict['Ethernet']['src']
                    nameOfStation = (dict['DCPNameOfStationBlock']['name_of_station']).decode('utf-8')
                    ip = dict['DCPIPBlock']['ip']
                    netmask = dict['DCPIPBlock']["netmask"]
                    gateway = dict['DCPIPBlock']['gateway']

                    newDevice = Device(macAdress=macAdress, ip=ip, nameOfStation=nameOfStation, netmask=netmask,
                                       gateway=gateway)
                    if listContainsDevice(device=newDevice, list=allDevices):
                        index = getPositionOfDeviceInList(device=newDevice, list=allDevices)
                        del allDevices[index]
                        allDevices.append(newDevice)
                    else:
                        allDevices.append(newDevice)

                ########################################################
                # ToDo: implement update functions for ip adress and nameofstation
                # ######################################################
        except IndexError:
            pass


def frameToDict(frame):
    data = to_dict(frame)
    # pprint(data)
    return data
