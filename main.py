from scapy.all import *
from scapy.layers.l2 import Ether

import EthernetFrame
from getNetworkInterfaces import *
import netifaces
import pprint
import receive
import send

from scapy.all import *

sendingNetworkInterface = getUsableNetworkInterface(getNetworkInterfaces())


# test = EthernetFrame.EthernetFrame(
#   sendingNetworkInterface['HWaddr'], 'ffffffffffff', '0x800', 'Hello Ethernet World', sendingNetworkInterface['name'])

# pprint.pprint(test.getEthernetFrame())

# send.sendEthernetFrame(test)

test = Ether(
    src=sendingNetworkInterface['HWaddr'], dst='ff:ff:ff:ff:ff:ff', type=0x800)
sendp(test)
test.show()
# print(str(firstEther))
