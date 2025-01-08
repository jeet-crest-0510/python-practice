import unittest
import re

def validate_input(data):
    pat = r'^[a-zA-Z]{4,6}[!@#$%]\d{4}'
    if re.search(pat, data):
        return True
    return False 

class Test(unittest.TestCase):
    def test_one(self):
        data = "Jeet#1234"
        result = validate_input(data)
        self.assertEqual(result, True)
        
    def test_two(self):
        data = "Je#12"
        result = validate_input(data)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main() 