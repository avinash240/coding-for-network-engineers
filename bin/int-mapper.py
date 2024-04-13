import sys
import os
import argparse

lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(lib_path)

#
from libs.frr.router import FRRouter
from libs.interface import Mapper

class SplitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, [x.strip() for x in values.split(',')])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='interface-map',
                    description='generates csv of frr router interfaces',
                )
    parser.add_argument('-r', '--router-address-ports',type=str, action=SplitArgs, required=True, help="comma seperated list of address:grpc-port")
    parser.add_argument('-o','--output-csv', type=str, required=True, help="output csv filename")
    args = parser.parse_args()
    #
    router_i_map = Mapper()
    for address_port in args.router_address_ports:
        router_i_map.add_router(FRRouter(address_port))
    router_i_map.export_csv(args.output_csv)