# Given an array (arr)  and partition index (pi), partition the array such that
#   arr[:p] <= arr[p] < arr[p:] where arr[p] == arr[pi]
#
# Example 1:
#   Input: arr = [10, 5, 9, 8, 7, 1 ], pi= 3
#   Output: 3 as [5, 7, 1, 8] <= 8 < [10, 9]

def hoarse_partition(arr, pi):
    # the algorithm needs two pointers on both ends, 
    #   each tracking the explored partitions <= and > pivot element
    #   i.e.  <= pivot | unexplored | > pivot
    # let say the paritions are tracked by lo and hi
    
    arr[0], arr[pi] = arr[pi], arr[0]
    lo, hi = 1, len(arr)-1

    while lo <= hi:
        if arr[lo] <= arr[0]:
            lo += 1
        elif arr[hi] > arr[0]:
            hi -= 1
        elif arr[lo] > arr[0] :
            arr[lo], arr[hi] = arr[hi], arr[lo]
            hi -= 1
        elif arr[hi] <= arr[0]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1

    arr[0], arr[hi] = arr[hi], arr[0]
    return hi

import unittest
import random

class Testcase(unittest.TestCase):
    def test_example1(self):
        actual = hoarse_partition([10, 5, 9, 8, 7, 1], 3)
        expected = 3
        self.assertEqual(expected, actual, "example1")

    def test_example1_last(self):
        actual = hoarse_partition([10, 5, 9, 8, 7, 1], 0)
        expected = 5
        self.assertEqual(expected, actual, "example1_last")

    def test_example1_first(self):
        actual = hoarse_partition([10, 5, 9, 8, 7, 1], 5)
        expected = 0
        self.assertEqual(expected, actual, "example1_first")

    def test_example1_last_before(self):
        actual = hoarse_partition([10, 5, 9, 8, 7, 1], 2)
        expected = 4
        self.assertEqual(expected, actual, "example1_last_before")

    def test_example1_second(self):
        actual = hoarse_partition([10, 5, 9, 8, 7, 1], 1)
        expected = 1
        self.assertEqual(expected, actual, "example1_second")
    
    def test_sorted_duplicates(self):
        actual = hoarse_partition([1, 2, 3, 4, 5, 5, 5, 6, 7, 8], 6)
        expected = 6
        self.assertEqual(expected, actual, "sorted_duplicates")

    def test_one(self):
        actual = hoarse_partition([1], 0)
        expected = 0
        self.assertEqual(expected, actual, "one")
    
    def test_random(self):
        for _ in range(10):
            length = random.randint(1, 100)
            pi = random.randint(0, length-1)
            arr = [random.randint(0, 20) for _ in range(length)]
            expected = self._naive_partition(arr, pi)
            actual = hoarse_partition(arr, pi)
            self.assertEqual(expected, actual)
    
    def _naive_partition(self, arr, pi) -> int:
        p = -1
        for i in range(0, len(arr)):
            if arr[i] <= arr[pi]:
                p += 1
        return p

if __name__ == '__main__':
    unittest.main()