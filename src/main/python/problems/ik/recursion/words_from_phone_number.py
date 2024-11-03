# coding:: utf-8
#
# Words From Phone Number
#   Given a seven-digit phone number, 
#       return all the character combinations that can be generated according to old phone keypad
#   Return the combinations in the lexicographical order.
#   Return an array of the generated string combinations in the lexicographical order. 
#       If nothing can be generated, return a list with an empty string "".
#   Digits 0 and 1 map to nothing. Other digits map to either three or four different characters each.
#
# Example 1:
#   Input: s = "1234567"
#   Output: [ "adgjmp", "adgjmq", "adgjmr", "adgjms", "adgjnp", ... "cfilns", "cfilop", "cfiloq", "cfilor", "cfilos"]
#   Explanation: 
#       First string "adgjmp" in the first line comes from the first characters 
#       mapped to digits 2, 3, 4, 5, 6 and 7 respectively. Since digit 1 maps to nothing, 
#       nothing is appended before 'a'. Similarly, the fifth string "adgjnp" generated from 
#       first characters of 2, 3, 4, 5 second character of 6 and first character of 7. 
#       All combinations generated in such a way must be returned in the lexicographical order.
#
# Example 2:
#   Input: s = "1010101"
#   Output: [""]
#
#  Constraints:
#   Input string is 7 characters long; each character is a digit.
#
import unittest
import random

from typing import List
def get_words_from_phone_number(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Solution:
    #   hold mapping of character for each digit
    #   recursively try choosing each character for the digit to generate possible combination
    #   base condition: once u finish up all the digits in the s add the combination.
    #
    #   Time Complexity: O(n * 4^n)
    #   Space Compelxity: O(n) - call stack, O(n) - auxilary, O(n * 4^n) - output
    #
    # Edge cases:
    if s is None:
        return []
    
    if len(s) == 0:
        return [""]
    
    key_pad = {\
        '0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl'\
        , '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    combinations = []
    def helper(ptr, combination):
        if ptr == len(s):
            combinations.append(''.join(combination))
            return
        
        if len(key_pad[s[ptr]]) == 0:
            helper(ptr+1, combination)

        for ch in key_pad[s[ptr]]:
            combination.append(ch)
            helper(ptr+1, combination)
            combination.pop()

    helper(0, [])
    return combinations

class Testcase(unittest.TestCase):
    def test_example1(self):
        s = "1234567"
        actual = get_words_from_phone_number(s)
        self.assertEqual(1*3*3*3*3*3*4, len(actual), "Example1")

    def test_example2(self):
        s = "1010101"
        actual = get_words_from_phone_number(s)
        expected = [""]
        self.assertListEqual(expected, actual, "Example2") 

    def test_zero(self):
        s = ""
        actual = get_words_from_phone_number(s)
        expected = [""]
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        s = "1"
        actual = get_words_from_phone_number(s)
        expected = [""]
        self.assertListEqual(expected, actual, "one") 
    
    def test_each_char(self):
        pad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i in range(2, 10):
            actual = get_words_from_phone_number(f'{i}')
            expected = [f'{x}' for x in pad[i]]
            self.assertListEqual(expected, actual, f"each_char_{i}")
            self.assertEqual(len(pad[i]), len(actual), f"each_char_count_{i}") 

if __name__ == '__main__':
    unittest.main()