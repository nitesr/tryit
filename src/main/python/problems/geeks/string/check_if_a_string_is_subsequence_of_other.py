# In this problem, we are given two strings s1 and s2 of different sizes. 
#   Our task is to find out that string s2 is a subsequence of string s1 or not.
#
# Note: A subsequence is a sequence that can be derived from another sequence by 
#   deleting some elements without changing the order of the remaining elements. 
#
# For example , subsequences of string "abc" are a, b, c, ab, ac, bc and abc.
def is_subsequence(str1: str, str2: str) -> bool:
    if len(str1) == 0 or len(str2) == 0:
        return True
    
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            j += 1
    
    return i == len(str1)

import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"s": "abc", "t": "ahbgdc", "expected": True, "description": "Basic subsequence match"},
        {"s": "axc", "t": "ahbgdc", "expected": False, "description": "Basic non-match"},
        
        # Edge cases
        {"s": "", "t": "ahbgdc", "expected": True, "description": "Empty subsequence is always true"},
        {"s": "abc", "t": "", "expected": True, "description": "Non-empty subsequence with empty main string"},
        {"s": "", "t": "", "expected": True, "description": "Both strings empty"},
        
        # Case sensitivity
        {"s": "ABC", "t": "ahbgdc", "expected": False, "description": "Case sensitive mismatch"},
        {"s": "abc", "t": "AHBGDC", "expected": False, "description": "Another case sensitive mismatch"},
        
        # Repeated characters
        {"s": "abb", "t": "ahbgdbbc", "expected": True, "description": "Repeated characters in sequence"},
        {"s": "abbc", "t": "ahbgdb", "expected": False, "description": "Not enough repeated characters in main string"},
        
        # Sequences with special characters
        {"s": "a*c", "t": "ab*cd", "expected": True, "description": "Special characters in sequence"},
        {"s": "@#$", "t": "abc@de#f$g", "expected": True, "description": "Special characters only"},
        
        # Long strings
        {"s": "abcdefg", "t": "a1b2c3d4e5f6g7", "expected": True, "description": "Long sequence with interspersed characters"},
        {"s": "abcdefghijklm", "t": "nopqrstuvwxyz", "expected": False, "description": "No matching characters"},
        
        # Tricky cases
        {"s": "ace", "t": "abcde", "expected": True, "description": "Skip middle characters"},
        {"s": "aec", "t": "abcde", "expected": False, "description": "Out of order characters"},
        {"s": "leetcode", "t": "lyezetcyod", "expected": False, "description": "Missing characters"},
        
        # Boundary cases
        {"s": "a", "t": "a", "expected": True, "description": "Single character match"},
        {"s": "a", "t": "b", "expected": False, "description": "Single character mismatch"},
        {"s": "aaaa", "t": "aaaaa", "expected": True, "description": "Repeated same character"},
        {"s": "aaaaa", "t": "aaaa", "expected": True, "description": "Subsequence longer than main string"}
    ]

    def test_example1(self):
        actual = is_subsequence("empathy", "apathy")
        expected = False
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        actual = is_subsequence("empathy", "empty")
        expected = True
        self.assertEqual(expected, actual, "example2")
    
    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = is_subsequence(test_case['s'], test_case['t'])
            self.assertEqual(test_case['expected'], actual, f"s={test_case['s']} t={test_case['t']}")

if __name__ == '__main__':
    unittest.main()