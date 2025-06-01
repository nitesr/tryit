# Reverse words in a given string
# Let the input string be “i like this program very much”. 
#   The function should change the string to “much very program this like i”
#
# Examples: 
#   Input: s = “geeks quiz practice code” 
#   Output: s = “code practice quiz geeks” 

def reverse_words(str1: str) -> str:
    str1_lst = list(str1)

    def _reverse(lst, start, end):
        lo, hi = start, end
        while lo < hi:
            lst[lo], lst[hi] = lst[hi], lst[lo]
            lo += 1
            hi -= 1
    
    prev_space = -1
    for i in range(len(str1_lst)):
        if str1_lst[i] == ' ':
            _reverse(str1_lst, prev_space+1, i-1)
            prev_space = i
    
    _reverse(str1_lst, prev_space+1, len(str1_lst)-1)
    str1_lst.reverse()
    return ''.join(str1_lst)

    

import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"s1": "geeks quiz practice code", "expected": "code practice quiz geeks", "description": "example1"},
        {"s1": "GeeksQuiz", "expected": "GeeksQuiz", "description": "example2"},

        # Edge cases
        {"s1": "a", "expected": "a", "description": "only one character"},
        {"s1": "", "expected": "", "description": "empty string"},
        {"s1": "seekg rof", "expected": "rof seekg", "description": "two words"},
        {"s1": "aa aa aaa bbb", "expected": "bbb aaa aa aa", "description": "all repeating characters"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = reverse_words(test_case['s1'])
            self.assertEqual(test_case['expected'], actual, f"s1={test_case['s1']}")

if __name__ == '__main__':
    unittest.main()