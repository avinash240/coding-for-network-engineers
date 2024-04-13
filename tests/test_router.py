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
            print(router._process_interface_state_data(i_data))
