import unittest

from harness import util
from harness.util import Global


class TestUserSpecToList(unittest.TestCase):
    def setUp(self):
        self._orig = Global.subtest_list
        Global.subtest_list = [i + 1 for i in range(16)]

    def tearDown(self):
        Global.subtest_list = self._orig

    def test_single_subtest(self):
        self.assertTrue(util.user_spec_to_list('3'))
        self.assertEqual(Global.subtest_list, [3])

    def test_range_subtests(self):
        self.assertTrue(util.user_spec_to_list('2-4'))
        self.assertEqual(Global.subtest_list, [2, 3, 4])

    def test_reject_out_of_bounds_range(self):
        self.assertFalse(util.user_spec_to_list('15-17'))
        self.assertEqual(Global.subtest_list, [i + 1 for i in range(16)])

    def test_reject_invalid_range_order(self):
        self.assertFalse(util.user_spec_to_list('4-2'))
        self.assertEqual(Global.subtest_list, [i + 1 for i in range(16)])


if __name__ == '__main__':
    unittest.main()
