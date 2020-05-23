from scapy.contrib.pnio import ProfinetIO
from scapy.main import load_contrib

load_contrib("pnio")

class ProfinetIOFrame:
    def __init__(self, frameID):
        self.frameID = frameID

    def getScapyProfinetIOFrame(self):
        scapyProfinetIOFrame = ProfinetIO(frameID=self.frameID)
        scapyProfinetIOFrame.show()
        return scapyProfinetIOFrame