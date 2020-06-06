class Device:
    def __init__(self, macAdress: str, nameOfStation: str, ip: str, netmask: str, gateway: str):
        self.macAdress = macAdress
        self.nameOfStation = nameOfStation
        self.ip = ip
        self.netmask = netmask
        self.gateway = gateway

    def getMacAdress(self):
        return self.macAdress

    def __eq__(self, other):
        if not isinstance(other, Device):
            return NotImplemented
        return self.macAdress == other.macAdress


def listContainsDevice(list: list, device: Device):
    for item in list:
        if item.__eq__(other=device):
            return True
    return False


def getPositionOfDeviceInList(list: list, device: Device):
      if listContainsDevice(list, Device):
        for i in range(len(list)):
            if list[i].__eq__(other=device):
                print(i)
                return i
        else:
            return -1

def getPositionOfDeviceInListbyNameOfStation(list: list, nameOfStation:str):
    for i in range(len(list)):
        if list[i].nameOfStation == nameOfStation:
            return i
