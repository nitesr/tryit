import unittest
from typing import List

def search(target, numbers):
    sorted_numbers = [(numbers[i], i) for i in range(len(numbers))]
    sorted_numbers.sort()

    lo = 0
    hi = len(sorted_numbers)
    while lo < hi:
        m = (lo+hi)//2
        if sorted_numbers[m][0] < target:
            lo = m+1
        else:
            hi = m
    
    if hi < len(sorted_numbers) and sorted_numbers[hi][0] == target:
        return hi
    else:
        return -(hi+1)



class Testcase(unittest.TestCase):
    def test_found_in(self):
        numbers = [5, 0, -1, 1, 3, 3, 2]
        target = 2
        actual = search(target, numbers)
        expected = 3
        self.assertEqual(expected, actual, "found_in") 

    def test_found_first(self):
        numbers = [5, 0, -1, 3, 2]
        target = -1
        actual = search(target, numbers)
        expected = 0
        self.assertEqual(expected, actual, "found_first")

    def test_found_last(self):
        numbers = [5, 0, -1, 3, 2]
        target = 5
        actual = search(target, numbers)
        expected = 4
        self.assertEqual(expected, actual, "found_last") 

    def test_not_found_in(self):
        numbers = [5, 0, -1, 3, 2]
        target = 4
        actual = search(target, numbers)
        expected = -(4+1)
        self.assertEqual(expected, actual, "not_found_in") 

    def test_not_found_last(self):
        numbers = [5, 0, -1, 3, 2]
        target = 6
        actual = search(target, numbers)
        expected = -(5+1)
        self.assertEqual(expected, actual, "not_found_after") 

    def test_not_found_first(self):
        numbers = [5, 0, -1, 3, 2]
        target = -2
        actual = search(target, numbers)
        expected = -(0+1)
        self.assertEqual(expected, actual, "not_found_before") 


if __name__ == '__main__':
    unittest.main()