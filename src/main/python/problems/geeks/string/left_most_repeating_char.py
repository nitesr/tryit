# Leftmost Repeating Character
# We are given a string s, we need to find out index of leftmost characters 
#   that is present in given string more than once.
#
# If there is no character which is repeating , then we need to print -1.
# For Example: Let us consider a string: 
#   str="abbcc", 
#   then our answer will be 1 
#   because character 'b' is the leftmost character which is 
#       repeating in given string str.

def left_most_repeating_char_two_loops(str1: str) -> str:
    if len(str1) == 0 or len(str1) == 1:
        return ""
    
    char_idx = [0]*256

    for c in str1:
       char_idx[ord(c)] += 1
    
    for c in str1:
        if char_idx[ord(c)] > 1:
            return c
    
    return ""

def left_most_repeating_char(str1: str) -> str:
    if len(str1) == 0 or len(str1) == 1:
        return ""
    
    char_idx = [-1]*256

    result = -1
    for i in range(len(str1)-1, -1, -1):
       if char_idx[ord(str1[i])] == -1:
           char_idx[ord(str1[i])] = i
       else:
           result = i

    return str1[result] if result != -1 else ""

import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"s1": "GeekforGeeks", "expected": "G", "description": "example1"},
        {"s1": "GeeksQuiz", "expected": "e", "description": "example2"},
        {"s1": "abcddcb", "expected": "b", "description": "first character"},
        {"s1": "bbcddca", "expected": "b", "description": "last character"},

        # Edge cases
        {"s1": "a", "expected": "", "description": "only one character"},
        {"s1": "", "expected": "", "description": "empty string"},
        {"s1": "&^BJG%%GJBA", "expected": "B", "description": "non alpha string"},
        {"s1": "aaabbbbccccdddd", "expected": "a", "description": "all repeating characters"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = left_most_repeating_char(test_case['s1'])
            self.assertEqual(test_case['expected'], actual, f"s1={test_case['s1']}")

if __name__ == '__main__':
    unittest.main()