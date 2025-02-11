#
# We are given two sorted arrays. We need to merge these two arrays 
#   such that the initial numbers (after complete sorting) are in the first array 
#   and the remaining numbers are in the second array. Extra space is allowed in O(1).
#
#
def merge_sorted_subarrays(arr, lo, mid, hi):
    left_arr, right_arr = arr[lo:mid+1], arr[mid+1:hi+1]

    left, right = 0, 0
    i = lo
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
        i += 1
        left += 1

    while right < len(right_arr):
        arr[i] = right_arr[right]
        right += 1
        i += 1

    return arr

import random
import unittest
class Testcase(unittest.TestCase):
    
    def test_one_after_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = merge_sorted_subarrays(arr1+arr2, 0, len(arr1)-1, len(arr1)+len(arr2)-1)
        expected = arr1 + arr2
        self.assertListEqual(expected, actual, "one_after_other") 

    def test_one_before_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = merge_sorted_subarrays(arr2+arr1, 0, len(arr2)-1, len(arr1)+len(arr2)-1)
        expected = arr1 + arr2
        self.assertListEqual(expected, actual, "one_before_other") 

    def test_random(self):
        for i in range(10):
            len1 = random.randint(0, 100)
            len2 = random.randint(0, 100)
            arr1 = [random.randint(0, 20) for _ in range(len1)]
            arr2 = [random.randint(0, 20) for _ in range(len2)]
            arr1.sort()
            arr2.sort()


            actual = merge_sorted_subarrays(arr1+arr2, 0, len(arr1)-1, len(arr1)+len(arr2)-1)
            expected = list(sorted(arr1+arr2))
            self.assertListEqual(expected, actual, "random") 


if __name__ == '__main__':
    unittest.main()