# coding:: utf-8
#
# Dutch National Flag
#   Given some balls of three colors arranged in a line, 
#   rearrange them such that all the red balls go first, then green and then blue ones.
#   Do rearrange the balls in place. 
#  
#   This is an important problem in search algorithms theory proposed by Dutch computer scientist 
#       Edsger Dijkstra. Dutch national flag has three colors 
#       (albeit different from ones used in this problem).
#
# Example 1:
#   Input: balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
#   Output: ["R", "R", "G", "G", "G", "G", "B", "B"]
#   Explanation: There are a total of 2 red, 4 green and 2 blue balls. 
#       In this order they appear in the correct output.
#
# Constraints:
#   1 <= balls.length <= 10^5
#   
#   R B R B
#   R R B B
#   R G G G G     B
#   R G G G G R B B
#   R R G G G G B B
#
# Notes:
#   Do this in ONE pass over the array, NOT TWO passes
#   Solution is only allowed to use constant extra memory
#   A solution that simply counts colors and overwrites the array is not the one we are looking for.

import unittest
import random
from typing import List

def dutch_flag_sort(balls: List[str]) -> List[str]:
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    
    # Solution: Inspired from the partition technique in quick sort
    #   we can keep two pointers for red and blue and keep swapping the 
    #      balls on both ends till we look at all elements.
    # Time complexity: O(n)
    # Space complexity: O(1)

    # edge cases
    if balls is None or len(balls) < 2:
        return balls

    red_end = 0
    blue_prestart = len(balls) - 1
    
    i = red_end
    while i <= blue_prestart:
        while balls[i] == 'R' and red_end <= i:
            balls[red_end], balls[i] = balls[i], balls[red_end]
            red_end += 1
        
        while balls[i] == 'B' and blue_prestart >= i:
            balls[blue_prestart], balls[i] = balls[i], balls[blue_prestart]
            blue_prestart -= 1
        
        if balls[i] == 'G' or red_end > i:
            i += 1

    return balls

class Testcase(unittest.TestCase):
    def test_example1(self):
        balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
        actual = dutch_flag_sort(balls)
        expected = ["R", "R", "G", "G", "G", "G", "B", "B"]
        self.assertListEqual(expected, actual, "Example1")

    def test_all_reds_2(self):
        balls = ["R", "R"]
        actual = dutch_flag_sort(balls)
        expected = ["R", "R"]
        self.assertListEqual(expected, actual, "all_reds_2")

    def test_all_reds_3(self):
        balls = ["R", "R", "R"]
        actual = dutch_flag_sort(balls)
        expected = ["R", "R", "R"]
        self.assertListEqual(expected, actual, "all_reds_3")

    def test_all_blues_2(self):
        balls = ["B", "B"]
        actual = dutch_flag_sort(balls)
        expected = ["B", "B"]
        self.assertListEqual(expected, actual, "all_blues_2")

    def test_all_blues_3(self):
        balls = ["B", "B", "B"]
        actual = dutch_flag_sort(balls)
        expected = ["B", "B", "B"]
        self.assertListEqual(expected, actual, "all_blues_3")

    def test_all_greens_3(self):
        balls = ["G", "G", "G"]
        actual = dutch_flag_sort(balls)
        expected = ["G", "G", "G"]
        self.assertListEqual(expected, actual, "all_greens_3")

    def test_all_greens_2(self):
        balls = ["G", "G"]
        actual = dutch_flag_sort(balls)
        expected = ["G", "G"]
        self.assertListEqual(expected, actual, "all_greens_2")

    def test_only_green_red(self):
        balls = ["G", "R", "G", "R", "G", "R"]
        
        for i in range(10):
            random.shuffle(balls)
            actual = dutch_flag_sort(balls)
            expected = ["R", "R", "R", "G", "G", "G"]
            self.assertListEqual(expected, actual, f"only_green_red_{i}")

    def test_only_green_blue(self):
        balls = ["G", "B", "G", "B", "G", "B"]
        
        for i in range(10):
            random.shuffle(balls)
            actual = dutch_flag_sort(balls)
            expected = ["G", "G", "G", "B", "B", "B"]
            self.assertListEqual(expected, actual, f"only_green_blue_{i}")
    
    def test_only_red_blue(self):
        balls = ["R", "B", "R", "B", "R", "B"]
        
        for i in range(10):
            random.shuffle(balls)
            actual = dutch_flag_sort(balls)
            expected = ["R", "R", "R", "B", "B", "B"]
            self.assertListEqual(expected, actual, f"only_red_blue_{i}")   
    
    def test_one_rgb(self):
        balls = ["R", "G", "B"]
        
        for i in range(10):
            random.shuffle(balls)
            actual = dutch_flag_sort(balls)
            expected = ["R", "G", "B"]
            self.assertListEqual(expected, actual, f"one_rgb_{i}") 
    
    def test_rgb(self):
        balls = ["R", "G", "R", "B", "R", "G", "B", "B", "R", "G"]
        
        for i in range(10):
            random.shuffle(balls)
            actual = dutch_flag_sort(balls)
            expected = ["R", "R", "R", "R", "G", "G", "G", "B", "B", "B"]
            self.assertListEqual(expected, actual, f"rgb_{i}")   

if __name__ == '__main__':
    unittest.main()