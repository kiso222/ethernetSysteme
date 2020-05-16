from get_nic import getnic
import pprint


def getNetworkInterfaces():
    return getnic.ipaddr(getnic.interfaces())


def getUsableNetworkInterface(interfaces):
    usableNetworkInterface: dict
    for interface in interfaces:
        if interface == 'lo':
            continue
        if interfaces[interface].get('HWaddr'):
            print("MAC Adresse gefunden: " +
                  interfaces[interface].get('HWaddr'))
            if interfaces[interface].get('state') == 'UP':
                print('Interface ist up')
                usableNetworkInterface = interfaces[interface]
                usableNetworkInterface['name'] = interface
                break
    if usableNetworkInterface:
        pprint.pprint('Interface gefunden:')
        pprint.pprint(usableNetworkInterface)
        #usableNetworkInterface['HWaddr'] = usableNetworkInterface['HWaddr'].replace(
        #    ':', '')
        #print('Konvertiere MAC Adresse zu:')
        #pprint.pprint(usableNetworkInterface)
        return usableNetworkInterface
    else:
        print('Kein nutzbares Interface gefunden!')
        return
