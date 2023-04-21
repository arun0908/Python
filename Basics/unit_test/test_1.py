"""Unit test case module to test the functionality of test_concept file"""

import unittest
from ..test_concept import method_1


class Test(unittest.TestCase):
    """Class containing unit test case nethods for test_concept module"""

    def test_method_1(self):
        """unit test case for method_1"""
        param = 10
        result = method_1(param)
        self.assertEqual(result, 15)


unittest.main()
