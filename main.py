from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP, DCP_IDENTIFY_REQUEST_FRAME_ID, DCP_SERVICE_ID_IDENTIFY, DCP_REQUEST
from scapy.layers.l2 import Ether

import EthernetFrame
import ProfinetIOFrame
import ethernetFrameReceiver
import ethernetFrameSender
import ProfinetIODCPFrame
from constants import *

testTargetMAC = '08:00:06:6b:f5:b8'

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
# ethernetFrameReceiver.receiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver = ethernetFrameReceiver.asyncReceiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver.start()

####################################################
#               Aufgabe 2                          #
#                  Teil 1                          #
####################################################
# ethernetFrameSender.identRequestAll()
# ethernetFrameSender.sendEthernetFrame(Ident)

####################################################
#               Aufgabe 2                          #
#                  Teil 2                          #
####################################################

# ethernetFrameSender.writeRequestNameOfStation(testTargetMAC, 'DasistEinWirklichLangerNameFuerEineMaschine123')
# time.sleep(1)
# ethernetFrameSender.readRequestNameOfStation(testTargetMAC)

time.sleep(5)
