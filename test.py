import grpc
import frr_northbound_pb2
import frr_northbound_pb2_grpc

channel = grpc.insecure_channel('172.20.20.3:50051')
stub = frr_northbound_pb2_grpc.NorthboundStub(channel)
response = stub.GetCapabilities(frr_northbound_pb2.GetCapabilitiesRequest())

print(response)
