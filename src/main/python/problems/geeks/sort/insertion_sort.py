#
# Insertion sort is a simple sorting algorithm that works similar to 
#   the way you sort playing cards in your hands. 
# 
# The array is virtually split into a sorted and an unsorted part.
#   Values from the unsorted part are picked and placed at the correct 
#   position in the sorted part.

def insert_sort(arr):
    # for each iteration (i = 1 to n-1) we will move the
    #   element i, into its right postion (0, i-1)
    # We will do this by swapping until the element is higher
    # than the one in arr part (0, i-1)

    lo = 0
    while lo < len(arr)-1:
        hi = lo+1
        while hi > 0:
            if arr[hi] < arr[hi-1]:
                arr[hi], arr[hi-1] = arr[hi-1], arr[hi]
            hi -= 1
        lo += 1 
    return arr

import unittest
import random
class Testcase(unittest.TestCase):
    def test_one(self):
        actual = insert_sort([1])
        expected = [1]
        self.assertListEqual(expected, actual, "one") 

    def test_two_sorted(self):
        actual = insert_sort([1, 2])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_sorted") 

    def test_two_reversed(self):
        actual = insert_sort([2, 1])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_reversed") 

    def test_three_sorted(self):
        actual = insert_sort([1, 2, 3])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_sorted") 

    def test_three_reversed(self):
        actual = insert_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_reversed") 

    def test_all_duplicates(self):
        actual = insert_sort([3, 3, 3, 3, 3, 3, 3, 3])
        expected = [3, 3, 3, 3, 3, 3, 3, 3]
        self.assertListEqual(expected, actual, "all_duplicates") 

    def test_random(self):
        for i in range(10):
            length = random.randint(1, 100)
            arr = [random.randint(1, 10) for _ in range(length)]
            expected = sorted(arr)
            actual = insert_sort(arr)
            self.assertListEqual(expected, actual, f"random_{i}") 


if __name__ == '__main__':
    unittest.main()