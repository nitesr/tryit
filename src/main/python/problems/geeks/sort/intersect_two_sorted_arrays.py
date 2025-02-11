#
# Given two sorted arrays, find their intersection.
#
# Example 1:
#   Input:
#       arr1[] = {1, 3, 4, 5, 7}
#       arr2[] = {2, 3, 5, 6}
#   Output: [3, 5]

def intersect_two_sorted_arrays_linear(arr1, arr2):
    # Move the left and right pointers until find a matching element
    #   on finding matching element move both pointers
    #
    arr = []
    left, right = 0, 0
    while left < len(arr1) and right < len(arr2):
        if arr1[left] < arr2[right]:
            left += 1
        elif arr2[right] < arr1[left]:
            right += 1
        else:
            if len(arr) == 0 or arr[-1] != arr1[left]:
                arr.append(arr1[left])
            left += 1
            right += 1
    
    return arr

def intersect_two_sorted_arrays_log(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2  = arr2, arr1
    
    def _search(ele, arr, start_index):
        lo = start_index
        hi = len(arr)-1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= ele:
                lo = mid + 1
            else:
                hi = mid - 1

        return (hi >= 0 and arr[hi] == ele, lo)

    start_index = 0
    arr = []
    for e in arr1:
        (found, start_index) = _search(e, arr2, start_index)
        if found:
            if len(arr) == 0 or arr[-1] != e:
                arr.append(e)
        elif start_index >= len(arr2):
            break

    return arr

def intersect_two_sorted_arrays(arr1, arr2):
    # return intersect_two_sorted_arrays_linear(arr1, arr2)
    return intersect_two_sorted_arrays_log(arr1, arr2)



import random
import unittest
class Testcase(unittest.TestCase):
    def test_two_empty(self):
        arr1, arr2 = [], []
        actual = intersect_two_sorted_arrays(arr1, arr2)
        expected = []
        self.assertListEqual(expected, actual, "two_empty") 

    def test_one_empty(self):
        arr1, arr2 = [1, 2, 4], []
        actual = intersect_two_sorted_arrays(arr1, arr2)
        expected = []
        self.assertListEqual(expected, actual, "one_empty") 

    def test_other_empty(self):
        arr1, arr2 = [1, 2, 4], []
        actual = intersect_two_sorted_arrays(arr2, arr1)
        expected = []
        self.assertListEqual(expected, actual, "other_empty") 

    def test_duplicates(self):
        arr1, arr2 = [1, 2, 2, 4, 4], [1, 2, 4, 4, 4]
        actual = intersect_two_sorted_arrays(arr2, arr1)
        expected = [1, 2, 4]
        self.assertListEqual(expected, actual, "duplicates") 

    def test_one_after_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = intersect_two_sorted_arrays(arr1, arr2)
        expected = []
        self.assertListEqual(expected, actual, "one_after_other") 

    def test_one_before_other(self):
        arr1, arr2 = [1, 2, 4], [6, 6, 7, 8]
        actual = intersect_two_sorted_arrays(arr2, arr1)
        expected = []
        self.assertListEqual(expected, actual, "one_before_other") 

    def test_random(self):
        for i in range(10):
            len1 = random.randint(0, 100)
            len2 = random.randint(0, 100)
            arr1 = [random.randint(0, 20) for _ in range(len1)]
            arr2 = [random.randint(0, 20) for _ in range(len2)]
            arr1.sort()
            arr2.sort()

            actual = intersect_two_sorted_arrays(arr1, arr2)
            expected = list(set(arr1) & set(arr2))
            self.assertListEqual(expected, actual, "random")


if __name__ == '__main__':
    unittest.main()