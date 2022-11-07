import grpc
import ws_discovery_pb2
import ws_discovery_pb2_grpc


if __name__ == "__main__":
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ws_discovery_pb2_grpc.WsDiscoveryServiceStub(channel)

        response = stub.GetNvtList(ws_discovery_pb2.GetNvtListRequest())

        print(response)
