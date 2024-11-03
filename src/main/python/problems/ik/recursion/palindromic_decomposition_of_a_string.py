# coding:: utf-8
#
# Palindromic Decomposition Of A String
#   Find all palindromic decompositions of a given string s.
#   A palindromic decomposition of string is a decomposition of the string into substrings, 
#       such that all those substrings are valid palindromes.
#
#   Any string is its own substring.
#   Output should include ALL possible palindromic decompositions of the given string.
#   Order of decompositions in the output does not matter.
#   To separate substrings in the decomposed string, use | as a separator.
#   Order of characters in a decomposition must remain the same as in the given string. For example, for s = "ab", return ["a|b"] and not ["b|a"].
#   Strings in the output must not contain whitespace. For example, ["a |b"] or ["a| b"] is incorrect.
#
# Example 1:
#   Input: s = "abracadabra"
#   Output: ["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
#
#
#  Constraints:
#   1 <= length of the string <= 20
#   String consists of lowercase English letters

import unittest
import random

from typing import List

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Solution:
    #   recursively try the separating after each character provided the string from last separater
    #       is a palindrome e.g aba -> a | (a is a palindrome - valid), 
    #       a | ba | (ba is not a palindrome - not valid)
    #
    #   base condition: on reaching end of the string
    #   constraints: palindrome check before placing the separater
    #
    #   Time Complexity: O(n * 2^n) - adding separator after each character recursively, n is palindrome check
    #   Space Compelxity: O(n) - call stack, O(n) - working set,  O(2^n) - output
    #
    # Edge cases:
    if s is None:
        return []
    
    if len(s) == 0:
        return []
    
    palindromes = []
    def is_palindrome(s_start, s_end):
        while s_start < s_end:
            if s[s_start] != s[s_end]:
                return False
            s_start += 1
            s_end -= 1
        return True

    def helper(ptr, palindrome):
        if ptr == len(s):
            palindromes.append('|'.join(palindrome))
            return
        
        for i in range(ptr, len(s)):
            if is_palindrome(ptr, i):
                palindrome.append(s[ptr:i+1])
                helper(i+1, palindrome)
                palindrome.pop()
    helper(0, [])
    return palindromes

class Testcase(unittest.TestCase):
    def test_example1(self):
        s = "abracadabra"
        actual = generate_palindromic_decompositions(s)
        expected =  ["a|b|r|a|c|a|d|a|b|r|a", "a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", ]
        self.assertEqual(len(expected), len(actual), 'Example1-len')
        self.assertListEqual(expected, actual, "Example1")

    def test_zero(self):
        s = ""
        actual = generate_palindromic_decompositions(s)
        expected = []
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        s = "a"
        actual = generate_palindromic_decompositions(s)
        expected = ["a"]
        self.assertListEqual(expected, actual, "one") 
    

    def test_same_char(self):
        s = "aaa"
        actual = generate_palindromic_decompositions(s)
        expected = ["a|a|a", "a|aa", "aa|a", "aaa"]
        self.assertListEqual(expected, actual, "same_char") 

    def test_uniq_char(self):
        s = "abc"
        actual = generate_palindromic_decompositions(s)
        expected = ["a|b|c"]
        self.assertListEqual(expected, actual, "uniq_char") 

    def test_palindrome_odd(self):
        s = "abcba"
        actual = generate_palindromic_decompositions(s)
        expected = ["a|b|c|b|a", "a|bcb|a", "abcba"]
        self.assertListEqual(expected, actual, "palindrome_odd") 

    def test_palindrome_even(self):
        s = "abba"
        actual = generate_palindromic_decompositions(s)
        expected = ["a|b|b|a", "abba"]
        self.assertListEqual(expected, actual, "palindrome_even") 
if __name__ == '__main__':
    unittest.main()