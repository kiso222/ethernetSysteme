from scapy.contrib.pnio import ProfinetIO
from scapy.contrib.pnio_dcp import ProfinetDCP, DCPNameOfStationBlock, DCP_SERVICE_ID_IDENTIFY, \
    DCP_IDENTIFY_REQUEST_FRAME_ID, DCP_REQUEST
from scapy.main import load_contrib

import EthernetFrame
import DCPBlock

load_contrib("pnio_dcp")


class ProfinetIODCPFrame:
    def __init__(self, frameID, serviceID, serviceType, ethernetFrame: EthernetFrame):
        self.ethernetFrame = ethernetFrame
        self.frameID = frameID
        self.serviceID = serviceID
        self.serviceType = serviceType
        # self.responseDelay = responseDelay
        # self.block = block

    def getScapyProfinetIODCPFrame(self):
        scapyProfinetIOFrame = self.ethernetFrame.getScapyFrame() / ProfinetIO(
            frameID=DCP_IDENTIFY_REQUEST_FRAME_ID) / ProfinetDCP(service_id=DCP_SERVICE_ID_IDENTIFY,
                                                                 service_type=DCP_REQUEST, option=255, sub_option=255,
                                                                 dcp_data_length=4)

        scapyProfinetIOFrame.show()
        return scapyProfinetIOFrame
