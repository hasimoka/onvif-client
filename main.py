from concurrent import futures

import grpc
from ws_discovery import WsDiscoveryService

import ws_discovery_pb2_grpc


class Server():
    _port = '[::]:50051'

    def __init__(self):
        self._server = None
        self._ws_discovery_service = WsDiscoveryService()
    
    def start(self):
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
        ws_discovery_pb2_grpc.add_WsDiscoveryServiceServicer_to_server(
            self._ws_discovery_service, self._server
        )

        self._server.add_insecure_port(self._port)
        self._server.start()
        self._server.wait_for_termination()

    def stop(self):
        self._server.stop(0)


if __name__ == "__main__":
    server = Server()

    try:
        server.start()
    except KeyboardInterrupt:
        # Ctrl-c を検出
        server.stop()
