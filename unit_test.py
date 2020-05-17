import unittest
from CountandSay import Solution


class ImplementstrStrTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.n = 1
        self.assertEqual(temp.countAndSay(1), 1)


if __name__ == "__main__":
    unittest.main()
