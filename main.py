import EthernetFrame
import ethernetFrameReceiver
import ethernetFrameSender
from getNetworkInterfaces import *

sendingNetworkInterface = getUsableNetworkInterface(getNetworkInterfaces())

# test = EthernetFrame.EthernetFrame(
#   sendingNetworkInterface['HWaddr'], 'ffffffffffff', '0x800', 'Hello Ethernet World', sendingNetworkInterface['name'])

# pprint.pprint(test.getEthernetFrame())

# send.sendEthernetFrame(test)

# test = Ether(
#     src=sendingNetworkInterface['HWaddr'], dst='ff:ff:ff:ff:ff:ff')
# sendp(test)
# test.show()
# print(str(firstEther))


test = EthernetFrame.EthernetFrame(
    sendingNetworkInterface['HWaddr'], 'ff:ff:ff:ff:ff:ff', 0x9000, 'Hello Ethernet World', sendingNetworkInterface['name'])

scapyFrame = test.getScapyFrame()
ethernetFrameSender.sendethernetframe(scapyFrame)

ethernetFrameReceiver.receiveEthernetFrame()