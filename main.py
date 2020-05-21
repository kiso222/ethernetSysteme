import EthernetFrame
import ethernetFrameReceiver
import ethernetFrameSender
from getNetworkInterfaces import *

managementServerMAC = getUsableNetworkInterface(getNetworkInterfaces())['HWaddr']
clientMAC = '00:0c:29:e2:35:30'
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
    managementServerMAC, clientMAC, 0x9000, 'Hello Ethernet World', sendingNetworkInterface['name'])

scapyFrame = test.getScapyFrame()
ethernetFrameSender.sendEthernetFrame(scapyFrame)

#ethernetFrameSender.sendAndReceiveEthernetFrame(scapyFrame)

#ethernetFrameReceiver.receiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver = ethernetFrameReceiver.asyncReceiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver.start()

time.sleep(20)