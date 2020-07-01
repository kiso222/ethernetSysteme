import socket
from binascii import hexlify
from copy import deepcopy
from pprint import pprint

import uuid

from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP, DCPDeviceRoleBlock, DCPDeviceIDBlock
from scapy.contrib.pnio_rpc import RPC_INTERFACE_UUID
from scapy.layers.inet import UDP
from scapy.layers.l2 import Ether, Dot1Q
from scapy.main import load_contrib
from scapy.packet import Raw
from scapy.sendrecv import sniff, AsyncSniffer
from scapy.utils import hexdump
from scapy2dict import to_dict

from Device import Device, listContainsDevice, getPositionOfDeviceInList, getPositionOfDeviceInListbyMacAdress
from constants import managementServerMAC, allDevices

load_contrib("pnio_rcp")


def receiveEthernetFrame(interface):
    # sniff(iface=interface, prn=lambda x: x.show(), filter="ether src 00:0c:29:e2:35:30")
    sniff(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    # sniff(iface = interface, prn=lambda x: x.show())


def asyncReceiveEthernetFrame(interface):
    # return AsyncSniffer(iface=interface, prn=lambda x: print('Da ist was reingekommen und zwar:' + str(x.show())))
    return AsyncSniffer(iface=interface, prn=lambda x: incomingFrameHandler(x))


def incomingFrameHandler(frame):
    # frame.show()
    try:
        if frame[Ether].dst == managementServerMAC:
            print('Da ist etwas reingekommen.')
            # frame.show()
            if UDP in frame:
                if frame[UDP].dport == 34964:
                    print('PNIO-CM reingekommen')
                    hexString = bytes(frame).hex()
                    hexString = [hexString[i:i + 2] for i in range(0, len(hexString), 2)]
                    device = allDevices[
                        getPositionOfDeviceInListbyMacAdress(list=allDevices, macAdress=frame[Ether].src)]
                    if ''.join(hexString[142:144]) == '8009':
                        print('Read Response eingegangen')
                        if hexString[176:178] == ['f8', '40']:
                            print('I&M0 FilterData')
                            numberOfSlots = int(''.join(hexString[218:220]))
                            #print("Number of Slots: {}".format(numberOfSlots))
                            for i in range(numberOfSlots):
                                startByte = 220 + i * 14
                                endByte = startByte + 14 + 1
                                temp = hexString[startByte:endByte]
                                slotNumber = int(''.join(temp[0:2]))
                                numberOfSublots = int(''.join(temp[6:8]))
                                # subSlotNumber = int(''.join(temp[9:11]))
                            temp2 = []
                            for j in range(numberOfSlots):
                                temp2.append([])
                                for k in range(numberOfSublots):
                                    temp2[j].append(k + 1)
                            device.slots = deepcopy(temp2)

                            device.IandM0Slot = int(''.join(hexString[416:418]))
                            device.IandM0SubSlot = int(''.join(hexString[424:426]))
                    if hexString[176:178] == ['af', 'f0']:
                        print('I&M0 Data')
                        device.vendorID = ''.join(hexString[212:214])
                        device.serialNumber = ''.join(hexString[234:250])

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
                    vendorID = hex(frame[DCPDeviceIDBlock].vendor_id)[2:].zfill(4)
                    deviceID = hex(frame[DCPDeviceIDBlock].device_id)[2:].zfill(4)
                    instance = hex(0x0001)[2:].zfill(4)

                    uuidPart4 = '0x' + str(instance) + str(deviceID) + str(vendorID)
                    uuidPart4 = int(uuidPart4, 16)
                    objectUUID = uuid.UUID(fields=(0xDEA00000, 0x6C97, 0x11D1, 0x82, 0x71, uuidPart4))
                    InterfaceUUID = RPC_INTERFACE_UUID['UUID_IO_DeviceInterface']
                    newDevice = Device(macAdress=macAdress, ip=ip, nameOfStation=nameOfStation, netmask=netmask,
                                       gateway=gateway, interfaceUUID=InterfaceUUID,
                                       objectUUID=objectUUID)
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
