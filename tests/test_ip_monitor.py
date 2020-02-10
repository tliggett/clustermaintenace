import unittest
import urllib.request

from ipmonitor.ipmonitor import get_public_ip


class IpMonitorTest(unittest.TestCase):

    def test_public_ip(self):
        self.assertEqual(
            get_public_ip(),
            urllib.request.urlopen('https://api.ipify.org').read().decode('utf-8')
        )

