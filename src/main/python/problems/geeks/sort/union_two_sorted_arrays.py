#
# In this problem, we are given two sorted arrays and we need to find the union of both arrays,
#   i.e. we need to merge both arrays such that 
#   the elements which are present in both arrays should present only once in our answer.
#
def union_two_sorted_arrays(arr1, arr2):
    # hold two pointers one for each array
    #   move the lower element pointer while collecting the element
    #   in case the elements are equal move the pointer until its not equal
    #
    
    arr = []
    left, right = 0, 0
    while left < len(arr1) and right < len(arr2):
        if arr1[left] <= arr2[right]:
            if len(arr) == 0 or arr[-1] != arr1[left]:
                arr.append(arr1[left])
            left += 1
        else:
            if len(arr) == 0 or arr[-1] != arr2[right]:
                arr.append(arr2[right])
            right += 1

    while left < len(arr1):
        if len(arr) == 0 or arr[-1] != arr1[left]:
            arr.append(arr1[left])
        left += 1

    while right < len(arr2):
        if len(arr) == 0 or arr[-1] != arr2[right]:
            arr.append(arr2[right])
        right += 1

    return arr

import random
import unittest
class Testcase(unittest.TestCase):
    def test_two_empty(self):
        arr1, arr2 = [], []
        actual = union_two_sorted_arrays(arr1, arr2)
        expected = []
        self.assertListEqual(expected, actual, "two_empty") 

    def test_one_empty(self):
        arr1, arr2 = [1, 2, 4], []
        actual = union_two_sorted_arrays(arr1, arr2)
        expected = [1, 2, 4]
        self.assertListEqual(expected, actual, "one_empty") 

    def test_other_empty(self):
        arr1, arr2 = [1, 2, 4], []
        actual = union_two_sorted_arrays(arr2, arr1)
        expected = [1, 2, 4]
        self.assertListEqual(expected, actual, "other_empty") 

    def test_one_after_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = union_two_sorted_arrays(arr1, arr2)
        expected = [1, 2, 4, 6, 7, 8]
        self.assertListEqual(expected, actual, "one_after_other") 

    def test_one_before_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = union_two_sorted_arrays(arr2, arr1)
        expected = [1, 2, 4, 6, 7, 8]
        self.assertListEqual(expected, actual, "one_before_other") 

    def test_random(self):
        for i in range(10):
            len1 = random.randint(0, 100)
            len2 = random.randint(0, 100)
            arr1 = [random.randint(0, 10) for _ in range(len1)]
            arr2 = [random.randint(0, 10) for _ in range(len2)]
            arr1.sort()
            arr2.sort()

            actual = union_two_sorted_arrays(arr1, arr2)
            expected = list(sorted(arr1+arr2))
            expected = [e for i, e in enumerate(expected) if i == 0 or expected[i-1] != expected[i]]
            self.assertListEqual(expected, actual, "random")


if __name__ == '__main__':
    unittest.main()