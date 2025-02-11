#
# Bubble Sort is the simplest sorting algorithm that works by 
#   repeatedly swapping the adjacent elements if they are in the wrong order. 
#
# This algorithm is not suitable for large data sets as its average 
#   and worst-case time complexity is quite high.
#

def bubble_sort(arr):
    # for each iteration the heavy element bubbles donw
    #   or we can make easy element bubble up
    #   by repeatedly swapping next element which is higher (to bubble down) 
    #   or lower (to bubble up).

    hi = len(arr)-1

    while hi > 0:
        lo = 0
        while lo < hi:
            if arr[lo] > arr[lo+1]:
                arr[lo], arr[lo+1] = arr[lo+1], arr[lo]
            lo += 1
        hi -=1 
    return arr


import unittest
import random
class Testcase(unittest.TestCase):
    def test_one(self):
        actual = bubble_sort([1])
        expected = [1]
        self.assertListEqual(expected, actual, "one") 

    def test_two_sorted(self):
        actual = bubble_sort([1, 2])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_sorted") 

    def test_two_reversed(self):
        actual = bubble_sort([2, 1])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_reversed") 

    def test_three_sorted(self):
        actual = bubble_sort([1, 2, 3])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_sorted") 

    def test_three_reversed(self):
        actual = bubble_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_reversed") 

    def test_all_duplicates(self):
        actual = bubble_sort([3, 3, 3, 3, 3, 3, 3, 3])
        expected = [3, 3, 3, 3, 3, 3, 3, 3]
        self.assertListEqual(expected, actual, "all_duplicates") 

    def test_random(self):
        for i in range(10):
            length = random.randint(1, 100)
            arr = [random.randint(1, 10) for _ in range(length)]
            expected = sorted(arr)
            actual = bubble_sort(arr)
            self.assertListEqual(expected, actual, f"random_{i}") 


if __name__ == '__main__':
    unittest.main()