#
# We are given two sorted arrays. We need to merge these two arrays 
#   such that the initial numbers (after complete sorting) are in the first array 
#   and the remaining numbers are in the second array. Extra space is allowed in O(1).
#
#
def merge_two_sorted_arrays(arr1, arr2):
    arr = []
    left, right = 0, 0
    while left < len(arr1) and right < len(arr2):
        if arr1[left] <= arr2[right]:
            arr.append(arr1[left])
            left += 1
        else:
            arr.append(arr2[right])
            right += 1

    while left < len(arr1):
        arr.append(arr1[left])
        left += 1

    while right < len(arr2):
        arr.append(arr2[right])
        right += 1

    return arr

import random
import unittest
class Testcase(unittest.TestCase):
    def test_two_empty(self):
        arr1, arr2 = [], []
        actual = merge_two_sorted_arrays(arr1, arr2)
        expected = []
        self.assertListEqual(expected, actual, "two_empty") 

    def test_one_empty(self):
        arr1, arr2 = [1, 2, 4], []
        actual = merge_two_sorted_arrays(arr1, arr2)
        expected = [1, 2, 4]
        self.assertListEqual(expected, actual, "one_empty") 

    def test_other_empty(self):
        arr1, arr2 = [1, 2, 4], []
        actual = merge_two_sorted_arrays(arr2, arr1)
        expected = [1, 2, 4]
        self.assertListEqual(expected, actual, "other_empty") 

    def test_one_after_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = merge_two_sorted_arrays(arr1, arr2)
        expected = arr1 + arr2
        self.assertListEqual(expected, actual, "one_after_other") 

    def test_one_before_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = merge_two_sorted_arrays(arr2, arr1)
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

            actual = merge_two_sorted_arrays(arr1, arr2)
            expected = list(sorted(arr1+arr2))
            self.assertListEqual(expected, actual, "random") 


if __name__ == '__main__':
    unittest.main()