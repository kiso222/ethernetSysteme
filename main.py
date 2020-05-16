from scapy.all import *
from scapy.layers.l2 import Ether

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
