from typing import List

import ws_discovery_pb2
import ws_discovery_pb2_grpc
from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
from wsdiscovery import QName


class WsDiscoveryService(ws_discovery_pb2_grpc.WsDiscoveryService):
    def GetNvtList(self, request: ws_discovery_pb2.GetNvtListRequest, context):
        service_address_list = []

        wsd = WSDiscovery()
        try:
            wsd.start()
            services = wsd.searchServices(types=[QName("http://www.onvif.org/ver10/network/wsdl", "NetworkVideoTransmitter")])
            service_address_list = [service.getEPR() + ":" + service.getXAddrs()[0] for service in services]
        finally:
            wsd.stop()

        return ws_discovery_pb2.GetNvtListResponse(nvt_address=service_address_list)

# # Discover it (along with any other service out there)
# wsd = WSDiscovery()
# wsd.start()
# services = wsd.searchServices(types=[QName("http://www.onvif.org/ver10/network/wsdl", "NetworkVideoTransmitter")])
# for service in services:
#     print(service.getEPR() + ":" + service.getXAddrs()[0])
# wsd.stop()
