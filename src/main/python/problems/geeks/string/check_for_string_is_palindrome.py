# Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string. 
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

# Example 1: 
#   Input : malayalam
#   Output : Yes
#
# Example 2:
#   Input : geeks
#   Output : No
def is_palindrome(str1: str) -> bool:
   lo = 0 
   hi = len(str1)-1
   result = True
   while lo < hi:
       if str1[lo] != str1[hi]:
           result = False
           break
       lo += 1
       hi -= 1
   else:
      result = True
   return result

import unittest
class Testcase(unittest.TestCase):
    def test_example1(self):
        actual = is_palindrome("malayalam")
        expected = True
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        actual = is_palindrome("geeks")
        expected = False
        self.assertEqual(expected, actual, "example2")

    def test_one(self):
        actual = is_palindrome("a")
        expected = True
        self.assertEqual(expected, actual, "one")

    def test_two_yes(self):
        actual = is_palindrome("aa")
        expected = True
        self.assertEqual(expected, actual, "two_yes")

    def test_two_no(self):
        actual = is_palindrome("ab")
        expected = False
        self.assertEqual(expected, actual, "two_no")

    def test_aabbcc(self):
        actual = is_palindrome("aabbcc")
        expected = False
        self.assertEqual(expected, actual, "aabbcc")

    def test_aabbccccbbaa(self):
        actual = is_palindrome("aabbccccbbaa")
        expected = True
        self.assertEqual(expected, actual, "aabbccccbbaa")

if __name__ == '__main__':
    unittest.main()