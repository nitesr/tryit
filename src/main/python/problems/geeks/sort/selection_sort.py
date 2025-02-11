#
# The selection sort algorithm sorts an array by 
#   repeatedly finding the minimum element (considering ascending order) 
#   from unsorted part and putting it at the beginning. 
# 
# The algorithm maintains two subarrays in a given array.
#   1) The subarray which is already sorted.
#   2) Remaining subarray which is unsorted. In every iteration of selection sort, 
#       the minimum element (considering ascending order) from the unsorted subarray 
#       is picked and moved to the sorted subarray. 
#

def select_sort(arr):
    # for each iteration (i = 0 to n-1) we find the left most element
    #   and move it to the location. 
    # we will do a linear search for find the element.

    lo = 0
    while lo < len(arr)-1:
        hi = lo+1
        min_idx = lo
        while hi < len(arr):
            if arr[hi] < arr[min_idx]:
                min_idx = hi
            hi += 1
        arr[min_idx], arr[lo] = arr[lo], arr[min_idx]
        lo += 1 
    return arr

import unittest
import random
class Testcase(unittest.TestCase):
    def test_one(self):
        actual = select_sort([1])
        expected = [1]
        self.assertListEqual(expected, actual, "one") 

    def test_two_sorted(self):
        actual = select_sort([1, 2])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_sorted") 

    def test_two_reversed(self):
        actual = select_sort([2, 1])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_reversed") 

    def test_three_sorted(self):
        actual = select_sort([1, 2, 3])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_sorted") 

    def test_three_reversed(self):
        actual = select_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_reversed") 

    def test_all_duplicates(self):
        actual = select_sort([3, 3, 3, 3, 3, 3, 3, 3])
        expected = [3, 3, 3, 3, 3, 3, 3, 3]
        self.assertListEqual(expected, actual, "all_duplicates") 

    def test_random(self):
        for i in range(10):
            length = random.randint(1, 100)
            arr = [random.randint(1, 10) for _ in range(length)]
            expected = sorted(arr)
            actual = select_sort(arr)
            self.assertListEqual(expected, actual, f"random_{i}") 


if __name__ == '__main__':
    unittest.main()