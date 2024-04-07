import sys
import os
lib_path = os.path.join(os.path.dirname(__file__), 'lib')
sys.path.append(lib_path)

import grpc
import frr_northbound_pb2
import frr_northbound_pb2_grpc

def get_capabilities(channel):
    stub = frr_northbound_pb2_grpc.NorthboundStub(channel)
    request = frr_northbound_pb2.GetCapabilitiesRequest()
    response = stub.GetCapabilities(request)
    return response

def get_channel(host):
    return grpc.insecure_channel(host)

if __name__ == "__main__":
    channel = get_channel("172.20.20.3:50051")
    capabilies = get_capabilities(channel)
    print(capabilies)
