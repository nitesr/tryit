# Check if string is rotated
#
# Example 1:
#   Input: s1 = "ABDC", s2 = "DCAB"
#   Output: True 
#   Explanation:  s1[2:]+s1[0:2] == s2
def is_rotated_with_aux_space(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    new_str = str1 + str1
    return new_str.find(str2) >= 0

def is_rotated(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    if len(str1) == 0 and len(str2) == 0:
        return True

    matched = False
    for j in range(0, len(str2)):
        if str2[j] == str1[0]:
            j_s = j+1
            for i in range(1, len(str1)):
                if str2[j_s % len(str2)] != str1[i]:
                    matched = False
                    break
                j_s += 1
            else:
                matched = True
                break
    return matched

import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"s1": "abcde", "s2": "cdeab", "expected": True, "description": "Basic rotation match"},
        {"s1": "abcde", "s2": "eabcd", "expected": True, "description": "One-step rotation match"},
        {"s1": "abcde", "s2": "abced", "expected": False, "description": "Basic non-matching strings (permutation, not rotation)"},
        
        # Edge cases
        {"s1": "", "s2": "", "expected": True, "description": "Empty strings are considered rotations of each other"},
        {"s1": "a", "s2": "a", "expected": True, "description": "Single character strings, same character"},
        {"s1": "a", "s2": "b", "expected": False, "description": "Single character strings, different characters"},
        {"s1": "ab", "s2": "a", "expected": False, "description": "Different length strings"},
        
        # Case sensitivity
        {"s1": "Hello", "s2": "lloHe", "expected": True, "description": "Case-sensitive rotation match"},
        {"s1": "Hello", "s2": "LLOHE", "expected": False, "description": "Case-sensitive rotation mismatch"},
        
        # Strings with repeated characters
        {"s1": "aaaa", "s2": "aaaa", "expected": True, "description": "All same characters, any rotation gives same string"},
        {"s1": "aaba", "s2": "baaa", "expected": True, "description": "Mostly repeated characters with rotation"},
        {"s1": "aaba", "s2": "abaa", "expected": True, "description": "Another rotation with repeated characters"},
        
        # Strings with special characters
        {"s1": "a*b$c", "s2": "$c*a*b", "expected": False, "description": "Special characters, non-rotation"},
        {"s1": "a*b$c", "s2": "$ca*b", "expected": True, "description": "Special characters, valid rotation"},
        
        # Full rotations (rotating by length of string)
        {"s1": "hello", "s2": "hello", "expected": True, "description": "Full rotation (same as original)"},
        
        # Long strings
        {"s1": "abcdefghijklmnopqrstuvwxyz", "s2": "nopqrstuvwxyzabcdefghijklm", "expected": True, "description": "Long string rotation"},
        {"s1": "abcdefghijklmnopqrstuvwxyz", "s2": "abcdefghijklmnopqrstuvwxzy", "expected": False, "description": "Long string, not a rotation"},
        
        # Palindromes
        {"s1": "racecar", "s2": "acecarr", "expected": True, "description": "Palindrome rotation"},
        {"s1": "racecar", "s2": "racecar", "expected": True, "description": "Palindrome with no rotation"},
        
        # Unicode characters
        {"s1": "Привет", "s2": "иветПр", "expected": True, "description": "Unicode character rotation"},
        {"s1": "こんにちは", "s2": "にちはこん", "expected": True, "description": "Japanese character rotation"},
        
        # Tricky cases
        {"s1": "waterbottle", "s2": "erbottlewat", "expected": True, "description": "Classic rotation example"},
        {"s1": "waterbottle", "s2": "bottlewater", "expected": True, "description": "Almost rotatable, with one character difference"},
        
        # Spaces and whitespace
        {"s1": "hello world", "s2": "worldhello ", "expected": True, "description": "Space position matters (incorrect rotation)"},
        {"s1": "hello world", "s2": "world hello", "expected": False, "description": "Space position matters (incorrect rotation)"},
        {"s1": "hello world", "s2": "llo worldhe", "expected": True, "description": "Space position preserved in rotation"}
    ]

    def test_example1(self):
        s = 'ABDC'
        t = 'DCAB'
        actual = is_rotated(s, t)
        expected = True
        self.assertEqual(expected, actual, f"{s} == {t}")

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = is_rotated(test_case['s1'], test_case['s2'])
            self.assertEqual(test_case['expected'], actual, f"s={test_case['s1']} t={test_case['s2']}")

if __name__ == '__main__':
    unittest.main()