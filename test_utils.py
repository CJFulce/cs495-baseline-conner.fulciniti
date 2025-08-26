import unittest
from utils import first_unique_char

class test_utils(unittest.TestCase):
    
    def test_first_unique_char(self):
        self.assertEqual(first_unique_char("aabbccddeffgg"), 8)
        self.assertEqual(first_unique_char("racecar"), 3)
        self.assertEqual(first_unique_char("GGGGGGGGGGGGGGGGGGGGGGGGG"), "No unique character found within string.")


if __name__ == "__main__": 
    unittest.main()