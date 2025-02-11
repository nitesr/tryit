# Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
#   If the array is already sorted, then the inversion count is 0, 
#   but if the array is sorted in reverse order, the inversion count is the maximum. 

# Given an array a[]. The task is to find the inversion count of a[].
#   Where two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

# Example1: 
#   Input: arr[] = {8, 4, 2, 1}
#   Output: 6
#   Explanation: Given array has six inversions: (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

# Example 2:
#   Input: arr[] = {1, 20, 6, 4, 5}
#   Output: 5
#   Explanation: Given array has five inversions: (20, 6), (20, 4), (20, 5), (6, 4), (6, 5). 

def count_inversions(arr):
    # in the approach of divide and conquer, where left and right parts are sorted
    #   num of elements which right element passes in left array should result in a inversion
    # we recursively sort & merge the array and count the inversions.
    #
    #   divide into two halves
    #   x = 0
    #   x += countAndSort(left halve)
    #   x += countAndSort(right halve)
    #   x += mergeAndCount(left, right)
    #   return x
    def _merge_and_count(lo, mid, hi):
        left_arr = arr[lo:mid+1]
        right_arr = arr[mid+1:hi+1]

        inv = 0
        left, right = 0, 0
        i = lo
        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left] <= right_arr[right]:
                arr[i] = left_arr[left]
                left += 1
            else:
                arr[i] = right_arr[right]
                inv += len(left_arr) - left
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

        return inv
 
    def _count_inversions(lo, hi) -> int:
        if lo >= hi:
            return 0
        
        mid = lo + (hi - lo) // 2
        inv = _count_inversions(lo, mid)
        inv += _count_inversions(mid+1, hi)
        inv += _merge_and_count(lo, mid, hi)
        return inv


    return _count_inversions(0, len(arr)-1)

import random
import unittest
class Testcase(unittest.TestCase):
    def test_example1(self):
        arr = [8, 4, 2, 1]
        actual = count_inversions(arr)
        expected = 6
        self.assertEqual(expected, actual, "example1")

    def test_example1(self):
        arr = [1, 20, 6, 4, 5]
        actual = count_inversions(arr)
        expected = 5
        self.assertEqual(expected, actual, "example2")

    def test_sorted(self):
        arr = [1, 2, 4, 8]
        actual = count_inversions(arr)
        expected = 0
        self.assertEqual(expected, actual, "sorted")


    def test_duplicates(self):
        arr = [1, 2, 2, 2, 0]
        actual = count_inversions(arr)
        expected = 4
        self.assertEqual(expected, actual, "duplicates")

    def test_one(self):
        arr = [1]
        actual = count_inversions(arr)
        expected = 0
        self.assertEqual(expected, actual, "one")

    def test_random(self):
        for _ in range(10):
            length = random.randint(0, 100)
            arr = [random.randint(0, 20) for _ in range(length)]
            expected = self._count_inversions_naive(arr)
            actual = count_inversions(arr)
            self.assertEqual(expected, actual, f"random - {arr}")

    def _count_inversions_naive(self, arr) -> int:
        count = 0
        for i in range(1, len(arr)):
            for j in range(0, i):
                if arr[i] < arr[j]:
                    count += 1
        return count

if __name__ == '__main__':
    unittest.main()