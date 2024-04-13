import json

import grpc
from . frr_northbound_pb2 import GetCapabilitiesRequest, GetRequest, JSON
from . frr_northbound_pb2_grpc import NorthboundStub

class FRRouter:
    def __init__(self, address_port):
        self._address_port = address_port
        self.channel = None

    @property
    def address_port(self):
        return self._address_port

    def __del__(self):
        if self.channel is not None:
            self.channel.close()

    def __get_stub(self):
        channel = self.__get_channel()
        return NorthboundStub(channel)

    def __get_channel(self):
        if self.channel is None:
            self.channel = grpc.insecure_channel(self.address_port)
        return self.channel

    @classmethod
    def _process_interface_state_data(cls, i_data):
        interface_info = {}
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

    def get_interface_state(self):
        request = GetRequest()
        request.path.append("/frr-interface:lib")
        request.type=GetRequest.ALL
        request.encoding=JSON
        stub = self.__get_stub()
        response = stub.Get(request)
        data = []
        for r in response:
            if r.data and r.data.data:
                i_data = json.loads(r.data.data)
                data.append(FRRouter._process_interface_state_data(i_data))
        return data

    def get_capabilities(self):
        stub = self.__get_stub()
        request = GetCapabilitiesRequest()
        response = stub.GetCapabilities(request)
        return response