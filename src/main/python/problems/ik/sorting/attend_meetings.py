# coding:: utf-8
#
# Attend Meetings
#  Given a list of meeting intervals where each interval consists of a start and an end time, 
#   check if a person can attend all the given meetings such that only one meeting can be attended at a time.
#
#  A new meeting can start at the same time the previous one ended.
#
# Example 1:
#   Input: intervals = [ [1, 5], [5, 8], [10, 15] ], Output = 1
#   Output: 2
#   Explanation: As the above intervals are non-overlapping intervals, 
#       it means a person can attend all these meetings.
#
# Example 2:
#   Input: intervals = [ [1, 5], [4, 8] ], Output = 0
#   Output: 2
#   Explanation: Time 4 - 5 is overlapping in the first and second intervals.
# 
# Constraints:
#   1 <= number of intervals <= 10^5
#   0 <= start time < end time <= 10^9

import unittest
from typing import List

def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # Solution:
    #   Sort the meetings with start time and as we go through meeting according to start time
    #       check previous meeting ended, if not return 0
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    
    # Edge cases:
    if intervals is None or len(intervals) == 0:
        return 1
    
    sol = 1
    sorted_intervals = sorted(intervals, key = lambda m: m[0])
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            sol = 0
            break

    return sol

class Testcase(unittest.TestCase):
    def test_example1(self):
        intervals = [ [1, 5], [5, 8], [10, 15] ]
        actual = can_attend_all_meetings(intervals)
        expected = 1
        self.assertEqual(expected, actual, "Example1") 

    def test_example2(self):
        intervals = [ [1, 5], [4, 8] ]
        actual = can_attend_all_meetings(intervals)
        expected = 0
        self.assertEqual(expected, actual, "Example2") 

    def test_no_meetings(self):
        intervals = [ ]
        actual = can_attend_all_meetings(intervals)
        expected = 1
        self.assertEqual(expected, actual, "no_meetings") 

    def test_one_meetings(self):
        intervals = [ [1, 10]]
        actual = can_attend_all_meetings(intervals)
        expected = 1
        self.assertEqual(expected, actual, "one_meeting") 
    

    def test_example1_unsorted(self):
        intervals = [ [1, 5], [10, 15], [5, 8] ]
        actual = can_attend_all_meetings(intervals)
        expected = 1
        self.assertEqual(expected, actual, "example1_unsorted") 

if __name__ == '__main__':
    unittest.main()