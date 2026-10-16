import os
import unittest

from openc3.request import Request


class TestRequest(unittest.TestCase):
    def setUp(self):
        os.environ["ENV"] = "dev"

    def test_run(self):
        request = Request()
        request.run()
        self.assertEqual(request.total, 100)
        self.assertEqual(request.user_ids, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
