from getNetworkInterfaces import getUsableNetworkInterface, getNetworkInterfaces

managementServerMAC = getUsableNetworkInterface(getNetworkInterfaces())['HWaddr']
clientMAC = '00:0c:29:e2:35:30'
broadcastMAC = 'ff:ff:ff:ff:ff:ff'
profinetIOMulticastMAC = '01:0E:CF:00:00:00'

profinetEtherType = 0x8892

sendingNetworkInterface = getUsableNetworkInterface(getNetworkInterfaces())

