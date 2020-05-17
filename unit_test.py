import unittest
from CountandSay import Solution


class ImplementstrStrTest(unittest.TestCase):
    def test_basic_function1(self):
        temp = Solution()
        self.n = 1
        self.assertEqual(temp.countAndSay(self.n), "1")

    def test_basic_function2(self):
        temp = Solution()
        self.n = 2
        self.assertEqual(temp.countAndSay(self.n), "11")

    def test_basic_function3(self):
        temp = Solution()
        self.n = 3
        self.assertEqual(temp.countAndSay(self.n), "21")

    def test_basic_function4(self):
        temp = Solution()
        self.n = 4
        self.assertEqual(temp.countAndSay(self.n), "1211")

    def test_basic_function5(self):
        temp = Solution()
        self.n = 5
        self.assertEqual(temp.countAndSay(self.n), "111221")


if __name__ == "__main__":
    unittest.main()
