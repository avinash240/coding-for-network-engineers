import sys
import os
import json
import argparse
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

def get_interface_state(channel):
    request = frr_northbound_pb2.GetRequest()
    request.path.append("/frr-interface:lib")
    request.type=frr_northbound_pb2.GetRequest.ALL
    request.encoding=frr_northbound_pb2.JSON
    stub = frr_northbound_pb2_grpc.NorthboundStub(channel)
    return stub.Get(request)

def get_channel(host):
    return grpc.insecure_channel(host)

class SplitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, [x.strip() for x in values.split(',')])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='interface-map',
                    description='generates csv of frr router interfaces',
                )
    parser.add_argument('-r', '--router-addresses', action=SplitArgs, required=True, help="comma seperated list of address:grpc-port")
    parser.add_argument('-o','--output-csv', type=argparse.FileType('w'), required=True, help="output csv filename")
    args = parser.parse_args()
    for router in args.router_addresses:
        #channel = get_channel("172.20.20.3:50051")
        channel = get_channel(router)
        capabilies = get_capabilities(channel)
        print(capabilies)
        interface_state = get_interface_state(channel)
        for r in interface_state:
            print(r.data.data)
