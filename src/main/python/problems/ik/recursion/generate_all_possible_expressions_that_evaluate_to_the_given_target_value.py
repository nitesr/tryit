# coding:: utf-8
#
# Generate All Possible Expressions That Evaluate To The Given Target Value
#   Given a string s that consists of digits ("0".."9") and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.
#       When building expressions, you have to insert one of the following operators 
#           between each pair of consecutive characters in s: join or * or +. 
#           For example, by inserting different operators between the two characters of string "12" 
#               we can get either 12 (1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").
#       Other operators such as - or ÷ are NOT supported.
#       Expressions that evaluate to the target but only utilize a part of s do not count: 
#           entires has to be consumed.
#       Precedence of the operators is conventional: join has the highest precedence, 
#           * – medium and + has the lowest precedence. 
#           For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.
#   You have to return ALL expressions that can be built from string s and evaluate to the target.
#
# Example 1:
#   Input: s = "202", target = 4
#   Output: ["2+0+2", "2+02", "2*02"]
#   Same three strings in any other order are also a correct output.
#
# Notes:
#   Order of strings in the output does not matter.
#   If there are no expressions that evaluate to target, return an empty list.
#   Returned strings must not contain spaces or any characters other than "0",..., "9", "*", "+".
#   All returned strings must start and end with a digit.
#
#  Constraints:
#   1 <= length of the string <= 13
#   1 <= target <= 10^13

import unittest
import random

from typing import List
def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Solution:
    #   recursively add possible options as we traverse through the string
    #       possible options: join, +, *
    #   base condition: if ptr == len(s), evaluate the expression and add if equals target
    #
    #   Time Complexity: O(n * 3^n)
    #   Space Complexity: O(n)
    #
    # Edge case
    if s is None or len(s) == 0:
        return []
    
    def evaluate(expression):
        stack = [expression[0]]
        for term in expression[1:]:
            if stack[-1] == '*':
                stack.pop()
                other_num = stack.pop()
                stack.append(int(term) * int(other_num))
            else:
                stack.append(term)
    
        while len(stack) > 1:
           num = stack.pop()
           stack.pop()
           other_num = stack.pop()
           stack.append(int(num) + int(other_num))
          
        return int(stack[-1])
    
    expressions = []
    def gen_exp_helper(ptr, expression):
        if ptr == len(s):
            val = evaluate(expression)
            if val == target:
                expressions.append(''.join(expression))
            return
        
        expression[-1] = f"{expression[-1]}{s[ptr]}"
        gen_exp_helper(ptr+1, expression)
        expression[-1] = expression[-1][:-1]
        
        expression.append('+')
        expression.append(s[ptr])
        gen_exp_helper(ptr+1, expression)
        expression.pop()
        expression.pop()
        
        expression.append('*')
        expression.append(s[ptr])
        gen_exp_helper(ptr+1, expression)
        expression.pop()
        expression.pop()
    
    gen_exp_helper(1, [s[0]])
    return expressions

class Testcase(unittest.TestCase):
    def test_example1(self):
        s = "202"
        target = 4
        actual = generate_all_expressions(s, target)
        expected =  ["2+02", "2+0+2", "2*02"]
        self.assertEqual(len(expected), len(actual), "Example1-len")
        self.assertListEqual(expected, actual, "Example1")

    def test_one(self):
        s = "1"
        target = 1
        actual = generate_all_expressions(s, target)
        expected = ["1"]
        self.assertListEqual(expected, actual, "one") 
        
if __name__ == '__main__':
    unittest.main()