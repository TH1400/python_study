import unittest

def hh(x):
    return x+1

class Test1(unittest.TestCase):
    def test_1(self):
        print('This is test1')
        self.assertEqual(hh(2), 3)

    def test_2(self):
        print('----这是test2----')

    def setUp(self) -> None:
        print('用例前执行')

    @classmethod
    def setUpClass(cls) -> None:
        print('全部前执行')