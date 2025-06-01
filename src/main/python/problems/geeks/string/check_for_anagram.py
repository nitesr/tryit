# Given two strings. The task is to check whether given strings 
#   are anagrams of each other or not. 
# An anagram of a string is another string that contains 
#   the same characters, only the order of characters can be different. 
# 
# For example, “abcd” and “dabc” are an anagram of each other.

# Examples:
#   Input: str1 = “listen”  str2 = “silent”
#   Output: “Anagram”
#   Explanation: All characters of “listen” and “silent” are the same.

def is_anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    char_idx = [0]*256
    for i in range(len(str1)):
        char_idx[ord(str1[i])] += 1
        char_idx[ord(str2[i])] -= 1
    
    return all([x == 0 for x in char_idx])


import unittest
import random
class Testcase(unittest.TestCase):
    def test_example(self):
        actual = is_anagram("listen", "silent")
        expected = True
        self.assertEqual(expected, actual, "example")

    def test_empty(self):
        actual = is_anagram("", "")
        expected = True
        self.assertEqual(expected, actual, "empty")

    def test_nonalpha(self):
        actual = is_anagram("#$C^$%", "^$%$#C")
        expected = True
        self.assertEqual(expected, actual, "nonalpha")

    def test_one(self):
        actual = is_anagram("a", "a")
        expected = True
        self.assertEqual(expected, actual, "one")

    def test_onechar_diff(self):
        actual = is_anagram("aid", "aim")
        expected = False
        self.assertEqual(expected, actual, "onechar_diff")

    def test_len_diff(self):
        actual = is_anagram("aidjhjhk", "aim")
        expected = False
        self.assertEqual(expected, actual, "len_diff")

    def test_random(self):
        for i in range(10):
            str1 = self.gen_random_string(20)
            str2 = self.gen_random_string(20)
            
            actual = is_anagram(str1, str2)
            expected = self.sort_and_compare(str1, str2)
            self.assertEqual(expected, actual, f"random_{i}")
    
    def test_random_anagram(self):
        for i in range(10):
            str1 = self.gen_random_string(20)
            str2 = self.shuffle_string(str1)
            
            actual = is_anagram(str1, str2)
            expected = True
            self.assertEqual(expected, actual, f"random_anagram_{i}")
   
    def gen_random_string(self, length):
        str1 = ''
        for i in range(length):
            str1 += chr(random.randint(0, 255))
        return str1
    
    def shuffle_string(self, str1):
        idxs = [i for i in range(len(str1))]
        random.shuffle(idxs)
        shuffled_str = ''
        for i in idxs:
            shuffled_str += str1[i]
        return shuffled_str

    def sort_and_compare(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        return list(sorted(list(str1))) == list(sorted(list(str2)))
        
if __name__ == '__main__':
    unittest.main()