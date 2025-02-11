#
# The Merge Sort algorithm is a sorting algorithm that is based on 
#   the Divide and Conquer paradigm. 
# 
# In this algorithm, the array is initially divided into two equal halves 
#   and then they are combined in a sorted manner.

def merge_sort(arr):
    # we divide the array into two halves
    #   sort each half recursively and merge the two halves.

    def _merge(lo, mid, hi):
        left_arr = arr[lo:mid+1]
        right_arr = arr[mid+1:hi+1]

        i = lo
        left, right = 0, 0
        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left] <= right_arr[right]:
                arr[i] = left_arr[left]
                left += 1
            else:
                arr[i] = right_arr[right]
                right += 1
            i += 1
        
        while left < len(left_arr):
            arr[i] = left_arr[left]
            left += 1
            i += 1
        
        while right < len(right_arr):
            arr[i] = right_arr[right]
            right += 1
            i += 1

    def _merge_sort(lo, hi):
        if lo < hi:
            mid = lo + (hi - lo) // 2
            _merge_sort(lo, mid)
            _merge_sort(mid+1, hi)
            _merge(lo, mid, hi)
    
    _merge_sort(0, len(arr)-1)
    return arr


import unittest
import random
class Testcase(unittest.TestCase):
    def test_one(self):
        actual = merge_sort([1])
        expected = [1]
        self.assertListEqual(expected, actual, "one") 

    def test_two_sorted(self):
        actual = merge_sort([1, 2])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_sorted") 

    def test_two_reversed(self):
        actual = merge_sort([2, 1])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_reversed") 

    def test_three_sorted(self):
        actual = merge_sort([1, 2, 3])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_sorted") 

    def test_three_reversed(self):
        actual = merge_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_reversed") 

    def test_all_duplicates(self):
        actual = merge_sort([3, 3, 3, 3, 3, 3, 3, 3])
        expected = [3, 3, 3, 3, 3, 3, 3, 3]
        self.assertListEqual(expected, actual, "all_duplicates") 

    def test_random(self):
        for i in range(10):
            length = random.randint(1, 100)
            arr = [random.randint(1, 10) for _ in range(length)]
            expected = sorted(arr)
            actual = merge_sort(arr)
            self.assertListEqual(expected, actual, f"random_{i}") 


if __name__ == '__main__':
    unittest.main()