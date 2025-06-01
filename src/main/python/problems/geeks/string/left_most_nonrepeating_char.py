# Given a string, find its first the index Leftmost  non-repeating character 
# For example, 
#   if the input string is “GeeksforGeeks”, 
#   then the output should be ‘f’ and 
# 
#   if the input string is “GeeksQuiz”, 
#   then the output should be ‘G’. 

def left_most_nonrepeating_char(str1: str) -> str:
    if len(str1) == 0:
        return ""

    if len(str1) == 1:
        return str1[0]
    
    char_idx = [0]*256

    for c in str1:
       char_idx[ord(c)] += 1
    
    for c in str1:
        if char_idx[ord(c)] == 1:
            return c
    
    return ""



import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"s1": "GeekforGeeks", "expected": "f", "description": "example1"},
        {"s1": "GeeksQuiz", "expected": "G", "description": "example2"},
        {"s1": "abcddcb", "expected": "a", "description": "first character"},
        {"s1": "bbcddca", "expected": "a", "description": "last character"},

        # Edge cases
        {"s1": "a", "expected": "a", "description": "only one character"},
        {"s1": "", "expected": "", "description": "empty string"},
        {"s1": "&^BJG%%GJB&", "expected": "^", "description": "non alpha string"},
        {"s1": "aaabbbbccccdddd", "expected": "", "description": "all repeating characters"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = left_most_nonrepeating_char(test_case['s1'])
            self.assertEqual(test_case['expected'], actual, f"s1={test_case['s1']}")

if __name__ == '__main__':
    unittest.main()


