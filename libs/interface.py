import csv

class Mapper(object):
    def __init__(self) -> None:
        self.router_map = {}

    def add_router(self, router):
        self.router_map[router.address_port] = router

    def export_csv(self, fname):
        with open(fname, 'w') as fh:
            mwriter = csv.writer(fh, dialect='excel')
            mwriter.writerow(['router-address-grpc',
                            'interface name',
                            'phy-address',
                            'ipv4-addrs',
                            'ipv6-addrs'])
            for router_add_port, router in self.router_map.items():
                i_info_list = router.get_interface_state()
                for i_info in i_info_list:
                    for iname, istate in i_info.items():
                        mwriter.writerow([router_add_port,
                                        iname,
                                        istate['phy-address'],
                                        istate['ipv4-addrs'],
                                        istate['ipv6-addrs']])