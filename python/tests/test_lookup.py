
import os
import unittest
from openc3.lookup import Lookup

class TestGetEnv(unittest.TestCase):
    def test_run(self):
        lookup = Lookup()
        lookup.run('RED_HIGH', [-80.0, -70.0, 60.0, 80.0])
        self.assertEqual(lookup.stdout, 80.0)
        lookup.run('YELLOW_HIGH', [-80.0, -70.0, 60.0, 80.0])
        self.assertEqual(lookup.stdout, 60.0)
        lookup.run('YELLOW_LOW', [-80.0, -70.0, 60.0, 80.0])
        self.assertEqual(lookup.stdout, -70.0)
        lookup.run('RED_LOW', [-80.0, -70.0, 60.0, 80.0])
        self.assertEqual(lookup.stdout, -80.0)
