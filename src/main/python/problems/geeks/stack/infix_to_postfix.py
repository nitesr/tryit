# Given an infix expression in the form of string s. 
#   Convert this infix expression to a postfix expression.

# Infix expression: 
#   The expression of the form a op b. 
#   When an operator is in between every pair of operands.
# Postfix expression: 
#   The expression of the form a b op. 
#   When an operator is followed for every pair of operands.
#
# Note: The order of precedence is: 
#   ^ -> * /  -> + -
#   Ignore the right associativity of ^.
#
# Examples :
#
#   Input: s = "a+b*(c^d-e)^(f+g*h)-i"
#   Output: abcd^e-fgh*+^*+i-
#   Explanation: After converting the infix expression into postfix expression, 
#       the resultant expression will be abcd^e-fgh*+^*+i-
#
#
#   Input: s = "A*(B+C)/D"
#   Output: ABC+*D/
#   Explanation: After converting the infix expression into postfix expression,     
#       the resultant expression will be ABC+*D/
#
#   Input: s = "(a+b)*(c+d)"
#   Output: ab+cd+*

class InfixToPostfix:
    EXP_PRECEDENCE = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}

    def __init__(self):
        pass
    
    def compare_exp(self, exp1, exp2):
        return self.EXP_PRECEDENCE[exp1] - self.EXP_PRECEDENCE[exp2]
    
    
        
    def _convert(self, s, start):
        exp_stack = []
        var_stack = []

        def _process(next_exp):
            if len(exp_stack) == 0:
                    return
            # print(exp_stack, var_stack)
            while len(exp_stack) > 0 \
                and self.compare_exp(exp_stack[-1], next_exp) >= 0:
                var_rt = var_stack.pop()
                var_lt = var_stack.pop()
                exp = exp_stack.pop()
                var_stack.append(var_lt+var_rt+exp)
            # print(var_stack)
        
        i = start
        while i < len(s) and s[i] != ')':
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] == '(':
                i, result = self._convert(s, i+1)
                var_stack.append(result)
            elif s[i] in self.EXP_PRECEDENCE:
                _process(s[i])
                exp_stack.append(s[i])
            else:
                var_stack.append(s[i])
                
            i += 1
            
        _process('+')
        return i, var_stack.pop()
            
        
    #Function to convert an infix expression to a postfix expression.
    def convert(self, s):
        if len(s) == 0:
            return ""
            
        return self._convert(s, 0)[1]

import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        {'s': 'a+b', 'expected': 'ab+', 'description': 'test_one_operator'},
        {'s': 'a+b-c', 'expected': 'ab+c-', 'description': 'test_two_equal_operators'},
        {'s': 'a+b*c', 'expected': 'abc*+', 'description': 'test_two_unequal_operators'},
        {'s': 'a*(b+c)', 'expected': 'abc+*', 'description': 'test_two_unequal_operators_with_parantheses'},
        {'s': 'a+b*(c^d-e)^(f+g*h)-i', 'expected': 'abcd^e-fgh*+^*+i-', 'description': 'example 1'},
        {'s': 'A*(B+C)/D', 'expected': 'ABC+*D/', 'description': 'example 2'},
        {'s': '(a+b)*(c+d)', 'expected': 'ab+cd+*', 'description': 'example 3'},
        {'s': 'a', 'expected': 'a', 'description': 'variable only'},
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual =  InfixToPostfix().convert(test_case['s'])
            self.assertEqual(test_case['expected'], actual, f"s={test_case['s']}")

if __name__ == '__main__':
    unittest.main()