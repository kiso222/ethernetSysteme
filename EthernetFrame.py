from scapy.layers.l2 import Ether


class EthernetFrame:
    def __init__(self, src, dst, type, payload, interface):
        # if (len(src) == len(dst) == 6):
        self.src = src
        self.dst = dst
        # if (len(type) == 2):
        self.type = type
        self.payload = payload
        self.interface = interface

    def getEthernetFrame(self):
        ethernetFrameDictionary = {}
        ethernetFrameDictionary['src'] = self.src
        ethernetFrameDictionary['dst'] = self.dst
        ethernetFrameDictionary['type'] = self.type
        ethernetFrameDictionary['payload'] = self.payload
        ethernetFrameDictionary['interface'] = self.interface
        return ethernetFrameDictionary

    def getScapyFrame(self):
        scapyEthernetFrame = Ether(src=self.src, dst=self.dst, type=self.type)
        scapyEthernetFrame.show()
        return scapyEthernetFrame
