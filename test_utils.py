import unittest
from utils import tokenizer

class Test_tokenizer(unittest.TestCase):

    test_list = "This is a Sentence"

    num, lower, enum = tokenizer(test_list, True)

    def test_num(self):
        self.assertEqual(self.num, len(self.test_list.split()))
    
    def test_lower(self):
        self.assertEqual(self.lower, ["this", "is", "a", "sentence"])

    def test_diff_enum(self):
        new_num, new_lower, new_enum = tokenizer("Top, Pop, Mop, Mop", True)
        self.assertEqual(new_enum[0] != new_enum[1],True)
        self.assertEqual(new_enum[2] == new_enum[3], True)


if __name__ == '__main__':
    unittest.main()