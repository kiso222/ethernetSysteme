import time

import ethernetFrameReceiver
import ethernetFrameSender
from Device import getPositionOfDeviceInListbyNameOfStation
from constants import *

# testTargetMAC = '08:00:06:6b:f5:b8'
testTargetName = 'et200s-nr3'
# testTargetMAC = '00:0e:8c:cb:56:83'  # et200s-nr3
# testTargetIP = '172.16.1.213'

#testTargetName = 'et200s-nr2'
#testTargetMAC = '00:0e:8c:cb:56:5f'  # et200s-nr3
#testTargetIP = '172.16.1.212'
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

# while (True):
#    time.sleep(1)
time.sleep(10)
print('Init finished')

# time.sleep(0)
for item in allDevices:
    print(str(item.nameOfStation))
    print(str(item.objectUUID))
    print(str(item.interfaceUUID))
    print(str(item.ip))
    print(str(item.macAdress))

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

####################################################
#               Aufgabe 3                          #
#                  Teil 1                          #
####################################################

targetDeviceNumber = getPositionOfDeviceInListbyNameOfStation(list=allDevices, nameOfStation=testTargetName)
ethernetFrameSender.readRequestIandMFilterData(allDevices[targetDeviceNumber])
time.sleep(5)

ethernetFrameSender.readRequestIandM0Data(allDevices[targetDeviceNumber])

time.sleep(5)

for item in allDevices:
    print('Name of Station: {}'.format(str(item.nameOfStation)))
    print('Vendor ID: {}'.format(str(item.vendorID)))
    print('Serial Number: {}'.format(str(item.serialNumber)))
    print('')

ethernetFrameSender.connectRequest(allDevices[targetDeviceNumber])

time.sleep(5)
#while (True):
#    time.sleep(1)
