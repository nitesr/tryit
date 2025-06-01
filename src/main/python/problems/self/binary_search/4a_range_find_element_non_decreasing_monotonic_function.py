"""
Given a range and a monotonic non-decreasing function, 
    find the elements that have the same return value as the target.

Input: int range, monotonic non-decreasing function f, and target value
Output: values from int value where f(x) == target

"""
from typing import List, Tuple, Callable, Dict

def binary_search(min_max: Tuple[int, int], montonic_func: Callable[[int], int], target: int) -> List[int]:
    if not montonic_func:
        return []
      
    if min_max[-1] < min_max[0]:
        return []
    
    if target < montonic_func(min_max[0]) or target > montonic_func(min_max[-1]):
        return []
    
    left, right = min_max[0], min_max[-1]
    while left <= right:
        mid = left + (right - left) // 2

        mid_value = montonic_func(mid)
        if target <= mid_value:
            right = mid - 1
        else:
            left = mid + 1
    
    
    
    min_range = left if target == montonic_func(left) else min_max[0] - 1

    left, right = min_max[0], min_max[-1]
    while left <= right:
        mid = left + (right - left) // 2

        mid_value = montonic_func(mid)
        if target >= mid_value:
            left = mid + 1
        else:
            right = mid - 1
    
    max_range = right if target == montonic_func(right) else min_max[-1] + 1

    if min_range in range(min_max[0], min_max[-1] + 1) \
        and max_range in range(min_max[0], min_max[-1] + 1):
        return [v for v in range(min_range, max_range + 1)]
    
    return []

import unittest

class MonotonicFunctionFactory:
    def __init__(self, min_max: Tuple[int, int], start_value: int = 0):
        self.min_max = min_max
        self.start_value = start_value

    def create_increase_on_evens(self):
        def increase_on_evens(num: int) -> int:
            if num in range(self.min_max[0], self.min_max[-1]+1):
                return (num - self.min_max[0]) // 2 + self.start_value

            raise ValueError(f"{num} out of range!")

        return increase_on_evens
    
    def create_increase_on_even_squares(self):
        def increase_on_even_squares(num: int) -> int:
            if num in range(self.min_max[0], self.min_max[-1]+1):
                val = (num - self.min_max[0]) // 2 + self.start_value
                return val * val

            raise ValueError(f"{num} out of range!")

        return increase_on_even_squares
    
    def create_constant_function(self, const: int):
        def constant_function(num: int) -> int:
            if num in range(self.min_max[0], self.min_max[-1]+1):
                return const

            raise ValueError(f"{num} out of range!")

        return constant_function
    

    def create_custom_sequence(self, map_seq: Dict[int, int], min_max: Tuple[int, int]):
        min_val, max_val = min_max
        def custom_sequence(num: int) -> int:
            if num >= min_val and num <= max_val:
                return map_seq[num]
            
            raise ValueError(f"{num} out of range!")
        
        return custom_sequence


class Testcase(unittest.TestCase):
    FUNC_FACTORY = MonotonicFunctionFactory((0, 10), 0)
    TEST_CASES = [
        # Basic cases
        {"minmax": (0, 10), "func": FUNC_FACTORY.create_increase_on_evens(), "target": 3, "expected": [6, 7], "description": "exists in middle"}
        ,{"minmax": (0, 10), "func": FUNC_FACTORY.create_increase_on_evens(), "target": 2, "expected": [4, 5], "description": "exists in left half"}
        ,{"minmax": (0, 10), "func": FUNC_FACTORY.create_increase_on_evens(), "target": 4, "expected": [8, 9], "description": "exists in right half"}
        
        # Edge cases
        ,{"minmax": (0, -1), "func": FUNC_FACTORY.create_custom_sequence({}, (0, -1)), "target": 3, "expected": [], "description": "empty range"}
        ,{"minmax": (3, 3), "func": FUNC_FACTORY.create_custom_sequence({3: 10}, (3, 3)), "target": 10, "expected": [3], "description": "uno range"}
        ,{"minmax": (3, 3), "func": FUNC_FACTORY.create_custom_sequence({3: 10}, (3, 3)), "target": 11, "expected": [], "description": "uno range, right outer"}
        ,{"minmax": (3, 3), "func": FUNC_FACTORY.create_custom_sequence({3: 10}, (3, 3)), "target": 9, "expected": [], "description": "uno range, left outer"}
        ,{"minmax": (0, 10), "func": FUNC_FACTORY.create_constant_function(2), "target": 3, "expected": [], "description": "all of range mapped to same value"}
        ,{"minmax": (0, 10), "func": FUNC_FACTORY.create_constant_function(2), "target": 2, "expected": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "description": "all of range mapped to same value"}
        
       
        # Boundary cases
        ,{"minmax": (1, 5), "func": FUNC_FACTORY.create_custom_sequence({1: 2, 2: 2, 3: 3, 4: 4, 5: 5}, (1, 5)), "target": 2, "expected": [1, 2], "description": "first element"}
        ,{"minmax": (1, 5), "func": FUNC_FACTORY.create_custom_sequence({1: 2, 2: 2, 3: 3, 4: 4, 5: 5}, (1, 5)), "target": 5, "expected": [5], "description": "last element"}
        ,{"minmax": (1, 5), "func": FUNC_FACTORY.create_custom_sequence({1: 2, 2: 2, 3: 3, 4: 4, 5: 5}, (1, 5)), "target": 3, "expected": [3], "description": "next to last"}
        ,{"minmax": (1, 5), "func": FUNC_FACTORY.create_custom_sequence({1: 2, 2: 2, 3: 3, 4: 4, 5: 5}, (1, 5)), "target": 4, "expected": [4], "description": "previous to first"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            try:
                actual = binary_search(test_case['minmax'], test_case['func'], test_case['target'])
                self.assertEqual(test_case['expected'], actual, f"{test_case['description']}")
            except ValueError as e:
                print(test_case['description'], e)
                raise e

if __name__ == '__main__':
    unittest.main()