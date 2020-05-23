import EthernetFrame
import ProfinetIOFrame
import ethernetFrameReceiver
import ethernetFrameSender
from getNetworkInterfaces import *
#https://github.com/littlezz/scapy2dict
managementServerMAC = getUsableNetworkInterface(getNetworkInterfaces())['HWaddr']
clientMAC = '00:0c:29:e2:35:30'
broadcastMAC = 'ff:ff:ff:ff:ff:ff'
profinetIOMulticastMAC = '01:0E:CF:00:00:00'
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

DCPethernetFrame = EthernetFrame.EthernetFrame(
    managementServerMAC, profinetIOMulticastMAC, 0x8892, 'Hello Ethernet World', sendingNetworkInterface['name'])

DCPprofinetIOFrame = ProfinetIOFrame.ProfinetIOFrame(frameID=0xFEFE)

#test = EthernetFrame.EthernetFrame(
#    managementServerMAC, clientMAC, 0x9000, 'Hello Ethernet World', sendingNetworkInterface['name'])
combined = DCPethernetFrame.getScapyFrame() / DCPprofinetIOFrame.getScapyProfinetIOFrame()

ethernetFrameSender.sendEthernetFrame(combined)
#scapyFrame = test.getScapyFrame()
#ethernetFrameSender.sendEthernetFrame(scapyFrame)

#ethernetFrameSender.sendAndReceiveEthernetFrame(scapyFrame)

#ethernetFrameReceiver.receiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver = ethernetFrameReceiver.asyncReceiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver.start()

time.sleep(5)