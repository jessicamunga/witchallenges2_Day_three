import unittest

from Day_three2 import missing_number

class test_Day_three2(unittest.TestCase):
    def test_missing(self):
        self.assertEqual(missing_number([1,3,6,7,8,9]),[2,4,5])

        
if __name__ == '__main__':
    unittest.main()
            

        
