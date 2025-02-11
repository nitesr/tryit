#
# The Merge Sort algorithm is a sorting algorithm that is based on 
#   the Divide and Conquer paradigm. 
# 
# In this algorithm, the array is initially divided into two equal halves 
#   and then they are combined in a sorted manner.

import random

def lomuto_partition(arr, lo, hi, pvt_idx):
    arr[lo], arr[pvt_idx] = arr[pvt_idx], arr[lo]

    p, i = lo, lo
    for i in range(lo+1, hi+1):
        if arr[i] <= arr[lo]:
            arr[p+1], arr[i] = arr[i], arr[p+1]
            p += 1
    arr[p], arr[lo] = arr[lo], arr[p]
    return p

def hoarse_partition(arr, lo, hi, pvt_idx):
    arr[lo], arr[pvt_idx] = arr[pvt_idx], arr[lo]
    i, j = lo+1, hi
    while i <= j:
        if arr[i] <= arr[lo]:
            i += 1
        elif arr[j] > arr[lo]:
            j -= 1
        elif arr[i] > arr[lo]:
            arr[i], arr[j] = arr[j], arr[i]
            j -=1 
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

def find_pivot_index(arr, lo, hi):
    return random.randint(lo, hi)

def quick_sort(arr, partition_algo = 'hoarse'):
    # quick sort is a divide and conquer algorithm similar to divide and conquer
    #   where majority work is one for division by finding the pariting
    #       the array into two parts where left part is <= pivot elment
    #       and right part is >= pivot element.
    #   and the each part undergoes the same logic recursively

    # Psuedo code:
    #   quicksort:
    #       pvt_idx = find_pivot_element()
    #       partition = patition(arr, pvt_idx)
    #       quicksort(arr[:parition])
    #       quicksort(arr[partition+1:])
    def _patition_arr(lo, hi, pvt_idx):
        if partition_algo == 'hoarse':
            return hoarse_partition(arr, lo, hi, pvt_idx)
        return lomuto_partition(arr, lo, hi, pvt_idx)

    def _quick_sort(lo, hi):
        if lo < hi:
            pvt_idx = find_pivot_index(arr, lo, hi)
            partition_idx = _patition_arr(lo, hi, pvt_idx)
            _quick_sort(lo, partition_idx-1)
            _quick_sort(partition_idx+1, hi)

    _quick_sort(0, len(arr)-1)
    return arr

import unittest
import random
class Testcase(unittest.TestCase):
    def test_one_lomuto(self):
        actual = quick_sort([1], partition_algo="lomuto")
        expected = [1]
        self.assertListEqual(expected, actual, "one_lomuto") 

    def test_two_sorted_lomuto(self):
        actual = quick_sort([1, 2], partition_algo="lomuto")
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_sorted_lomuto") 

    def test_two_reversed_lomuto(self):
        actual = quick_sort([2, 1], partition_algo="lomuto")
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_reversed_lomuto") 

    def test_three_sorted_lomuto(self):
        actual = quick_sort([1, 2, 3], partition_algo="lomuto")
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_sorted_lomuto") 

    def test_three_reversed_lomuto(self):
        actual = quick_sort([3, 2, 1], partition_algo="lomuto")
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_reversed_lomuto") 

    def test_all_duplicates_lomuto(self):
        actual = quick_sort([3, 3, 3, 3, 3, 3, 3, 3], partition_algo="lomuto")
        expected = [3, 3, 3, 3, 3, 3, 3, 3]
        self.assertListEqual(expected, actual, "all_duplicates_lomuto") 

    def test_random_lomuto(self):
        for i in range(10):
            length = random.randint(1, 100)
            arr = [random.randint(1, 10) for _ in range(length)]
            expected = sorted(arr)
            actual = quick_sort(arr, partition_algo="lomuto")
            self.assertListEqual(expected, actual, f"random_{i}_lomuto") 

    def test_one_hoarse(self):
        actual = quick_sort([1])
        expected = [1]
        self.assertListEqual(expected, actual, "one_horase") 

    def test_two_sorted_hoarse(self):
        actual = quick_sort([1, 2])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_sorted_hoarse") 

    def test_two_reversed_hoarse(self):
        actual = quick_sort([2, 1])
        expected = [1, 2]
        self.assertListEqual(expected, actual, "two_reversed_hoarse") 

    def test_three_sorted_hoarse(self):
        actual = quick_sort([1, 2, 3])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_sorted_hoarse") 

    def test_three_reversed_hoarse(self):
        actual = quick_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "three_reversed_hoarse") 

    def test_all_duplicates_hoarse(self):
        actual = quick_sort([3, 3, 3, 3, 3, 3, 3, 3])
        expected = [3, 3, 3, 3, 3, 3, 3, 3]
        self.assertListEqual(expected, actual, "all_duplicates_hoarse") 

    def test_random_hoarse(self):
        for i in range(10):
            length = random.randint(1, 100)
            arr = [random.randint(1, 10) for _ in range(length)]
            expected = sorted(arr)
            actual = quick_sort(arr)
            self.assertListEqual(expected, actual, f"random_{i}_hoarse") 


if __name__ == '__main__':
    unittest.main()