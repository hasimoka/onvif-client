from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
from wsdiscovery import QName


# Discover it (along with any other service out there)
wsd = WSDiscovery()
wsd.start()
services = wsd.searchServices(types=[QName("http://www.onvif.org/ver10/network/wsdl", "NetworkVideoTransmitter")])
for service in services:
    print(service.getEPR() + ":" + service.getXAddrs()[0])
wsd.stop()
