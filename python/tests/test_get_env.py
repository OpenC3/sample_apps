import os
import unittest

from openc3.get_env import GetEnv


class TestGetEnv(unittest.TestCase):
    def setUp(self):
        os.environ["ENV"] = "dev"

    def test_run(self):
        get_env = GetEnv()
        get_env.run()
        self.assertEqual(get_env.stdout, "Development environment")
        os.environ["ENV"] = "prod"
        get_env.run()
        self.assertEqual(get_env.stdout, "Production environment")
