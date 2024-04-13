import unittest
import os
import json
from libs.frr.router import FRRouter

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.base_test_dir = os.path.join(os.path.dirname(__file__), 'testdata')
        return super().setUp()

    def test_process_interface_state(self):
        router = FRRouter("fakeaddress:port")
        test_file = os.path.join(self.base_test_dir, 'interface-data.json')
        with open(test_file, 'r') as fh:
            i_data = json.load(fh)
            processed_data = router._process_interface_state_data(i_data)
            expected_interfaces = ['eth0', 'eth1', 'eth2', 'eth3', 'eth4', 'lo']
            for eth in expected_interfaces:
                self.assertIn(eth, processed_data)
            self.assertEqual(processed_data['eth0']['phy-addrs'], "02:42:ac:14:14:03")
            self.assertEqual(processed_data['eth1']['phy-addrs'], "00:00:00:00:00:00")
            self.assertEqual(processed_data['eth1']['ipv4-addrs'], "172.16.1.10/30")
            self.assertEqual(processed_data['eth1']['ipv6-addrs'], "2001:db8:1:40::d/60")

