import unittest
from tafqeet import Tafqeet, Currency


class TestTafqeet(unittest.TestCase):
    def test_tafqeet(self):
        num = 956342
        result = Tafqeet.tafqeet(num)
        self.assertEqual(result, "تسعمائة وستة وخمسون ألفًا وثلاثمائة واثنان وأربعون")

    def test_tafqeet_EGP(self):
        num = 956342
        result = Tafqeet.tafqeet_EGP(num)
        self.assertEqual(result, "تسعمائة وستة وخمسون ألفًا وثلاثمائة واثنان وأربعون جنيها مصريا فقط لا غير")

    def test_tafqeet_EGP_with_pt(self):
        num = 956342.432
        result = Tafqeet.tafqeet_EGP(num)
        self.assertEqual(result, "تسعمائة وستة وخمسون ألفًا وثلاثمائة واثنان وأربعون جنيها وأربعمائة واثنان وثلاثون قرشا مصريا فقط لا غير")


if __name__ == '__main__':
    unittest.main()
