import pprint
import time
import random
import uuid

from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP, DCP_IDENTIFY_REQUEST_FRAME_ID, DCP_SERVICE_ID_IDENTIFY, DCP_REQUEST
from scapy.layers.l2 import Ether

import EthernetFrame
import ProfinetIOFrame
import ethernetFrameReceiver
import ethernetFrameSender
import ProfinetIODCPFrame
from Device import getPositionOfDeviceInListbyNameOfStation
from ProfinetIORPCFrame import ProfinetIORPCFrame
from constants import *

testTargetMAC = '08:00:06:6b:f5:b8'
testTargetName = 'et200s-nr3'

# print(managementServerNICName)

# Name of Station lesen/schreiben
# IP Adresse lesen/schreiben

####################################################
#               Aufgabe 1                          #
####################################################
# test = EthernetFrame.EthernetFrame(
#   sendingNetworkInterface['HWaddr'], 'ffffffffffff', '0x800', 'Hello Ethernet World', sendingNetworkInterface['name'])
# pprint.pprint(test.getEthernetFrame())
# send.sendEthernetFrame(test)


####################################################
#               Aufgabe 2                          #
####################################################
asyncResceiver = ethernetFrameReceiver.asyncReceiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver.start()

####################################################
#               Aufgabe 2                          #
#                  Teil 1                          #
####################################################
ethernetFrameSender.identRequestAll()

#while (True):
#    time.sleep(1)
time.sleep(10)
print('Init finished')
# random.shuffle(allDevices)

time.sleep(0)
for item in allDevices:
    print(str(item.nameOfStation))
    print(str(item.objectUUID))
    print(str(item.interfaceUUID))


# pprint.pprint(allDevices)
####################################################
#               Aufgabe 2                          #
#                  Teil 2                          #
####################################################

# ethernetFrameSender.readRequestNameOfStation(testTargetMAC)


# ethernetFrameSender.writeRequestNameOfStation(testTargetMAC, 'FelixWarHier')
# ethernetFrameSender.readRequestNameOfStation(testTargetMAC)

# ethernetFrameSender.readRequestIPAdress(testTargetMAC)
# ethernetFrameSender.writeRequestIPAdress(testTargetMAC, '10.27.6.23', '255.255.255.0', '10.27.6.1')
# ethernetFrameSender.readRequestIPAdress(testTargetMAC)

# time.sleep(5)


# ethernetFrameSender.readRequestIPAdress(
#    allDevices[getPositionOfDeviceInListbyNameOfStation(nameOfStation=testTargetName, list=allDevices)].macAdress)
# time.sleep(5)

# test = ProfinetIORPCFrame()

# test.getScapyProfinetIORPCFrame()
