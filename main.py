from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP, DCP_IDENTIFY_REQUEST_FRAME_ID, DCP_SERVICE_ID_IDENTIFY, DCP_REQUEST
from scapy.layers.l2 import Ether

import EthernetFrame
import ProfinetIOFrame
import ethernetFrameReceiver
import ethernetFrameSender
import ProfinetIODCPFrame
from constants import *

# https://github.com/littlezz/scapy2dict

# test = EthernetFrame.EthernetFrame(
#   sendingNetworkInterface['HWaddr'], 'ffffffffffff', '0x800', 'Hello Ethernet World', sendingNetworkInterface['name'])

# pprint.pprint(test.getEthernetFrame())

# send.sendEthernetFrame(test)

# test = Ether(
#     src=sendingNetworkInterface['HWaddr'], dst='ff:ff:ff:ff:ff:ff')
# sendp(test)
# test.show()
# print(str(firstEther))

DCPTestEthernetFrame = EthernetFrame.EthernetFrame(
    managementServerMAC, profinetIOMulticastMAC, profinetEtherType)

profinetDCPTestFrame = ProfinetIODCPFrame.ProfinetIODCPFrame(frameID=0xFEFE, serviceID=0x03, serviceType=0x00,
                                                             ethernetFrame=DCPTestEthernetFrame)
profinetDCPTestFrame.getScapyProfinetIODCPFrame()
# DCPprofinetIOFrame = ProfinetIOFrame.ProfinetIOFrame(frameID=0xFEFE)

# test = EthernetFrame.EthernetFrame(
#    managementServerMAC, clientMAC, 0x9000, 'Hello Ethernet World', sendingNetworkInterface['name'])
# combined = DCPethernetFrame.getScapyFrame() / DCPprofinetIOFrame.getScapyProfinetIOFrame()

# ethernetFrameSender.sendEthernetFrame(combined)
# scapyFrame = test.getScapyFrame()
#ethernetFrameSender.sendEthernetFrame(scapyFrame)

# ethernetFrameSender.sendAndReceiveEthernetFrame(scapyFrame)

# ethernetFrameReceiver.receiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver = ethernetFrameReceiver.asyncReceiveEthernetFrame(sendingNetworkInterface['name'])
asyncResceiver.start()

#hardcodet IdentRequest-All
ethernetFrameSender.sendEthernetFrame(Ether(dst="01:0e:cf:00:00:00") /
        ProfinetIO(frameID=0xFEFE) /
        ProfinetDCP(service_id=0x05,
            service_type=0x00, option=0xFF, sub_option=0xFF,
            dcp_data_length=0x04))
#testProfinetDCP = ProfinetIODCPFrame.ProfinetIODCPFrame()

time.sleep(5)