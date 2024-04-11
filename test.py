import sys
import os
import json
import argparse
import csv

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
    response = stub.Get(request)
    return response

def get_channel(host):
    return grpc.insecure_channel(host)

def process_interface_state(i_state):
    import pprint
    interface_info = {}
    for r in i_state:
        if r.data and r.data.data:
            i_data = json.loads(r.data.data)
            pprint.pprint(i_data)
            if 'frr-interface:lib' in i_data and 'interface' in i_data['frr-interface:lib']:
                for i in i_data['frr-interface:lib']['interface']:
                    if 'name' in i:
                        d = dict(name=i['name'])
                        if 'state' in i:
                            for k in ['phy-address']:
                                d[k]= i['state'].get(k)

                        for ipv in ['ipv4-addrs', 'ipv6-addrs']:
                            if ipv in i:
                                ip_list = ["{}/{}".format(x['ip'], x['prefix-length']) for x in i[ipv]]
                                d[ipv] = ip_list.join(",")
                            else:
                                d[ipv] = 'n/a'
                        interface_info[i['name']] = d
    return interface_info


def write_csv(fname, i_map):
    with open(fname, 'w') as fh:
        mwriter = csv.writer(fh, dialect='excel')
        mwriter.writerow(['router-address-grpc',
                          'interface name',
                          'phy-address',
                          'ipv4-addrs',
                          'ipv6-addrs'])
        for router_add_port, i_info in i_map.items():
            for iname, istate in i_info.items():
                mwriter.writerow([router_add_port,
                                  iname,
                                  istate['phy-address'],
                                  istate['ipv4-addrs'],
                                  istate['ipv6-addrs']])

class SplitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, [x.strip() for x in values.split(',')])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='interface-map',
                    description='generates csv of frr router interfaces',
                )
    parser.add_argument('-r', '--router-addresses',type=str, action=SplitArgs, required=True, help="comma seperated list of address:grpc-port")
    parser.add_argument('-o','--output-csv', type=str, required=True, help="output csv filename")
    args = parser.parse_args()
    #
    router_i_map = {}
    #
    for router in args.router_addresses:
        channel = get_channel(router)
        interface_state = get_interface_state(channel)
        router_i_map[router] = process_interface_state(interface_state)
        channel.close()
    write_csv(args.output_csv, router_i_map)