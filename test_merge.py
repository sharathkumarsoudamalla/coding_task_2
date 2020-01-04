import unittest
from merge import merge_interval

class MergeTest(unittest.TestCase):
    def test_merge(self):
        # test if the overlapping intervals are merged by the merge_interval Function
        self.assertEqual(merge_interval([[25,30],[2,19],[14,23],[4,8]]), [[2,23],[25,30]])


