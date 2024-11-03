# coding: utf-8
#
# K Most Frequent Words
#   Given a number and a list of words, return the given number of most frequent words.
#   Notes:
#       Every word consists of only lowercase English letters.
#       Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
#
# Example 1:
#   Input: 
#       words = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
#       k = 4
#   Output: ["car", "driver", "taxi", "bus"]
#
#
# Constraints:
#   1 <= number of words <= 10^5
#   1 <= size of each word <= 10
#   1 <= the given number <= the number of unique words

import unittest
from heapq import heappushpop, heappop, heapify
from typing import List

def klogn_sol(k, word_freqs):
    word_heap = [(-item[1], item[0]) for item in word_freqs.items()]
    heapify(word_heap)

    pop_len = min(len(word_heap), k)
    sol = [ heappop(word_heap)[1] for i in range(pop_len)]
    return sol

def nlogk_sol(k, word_freqs):
    class WordTuple(tuple):
        def __lt__(self, other: tuple) -> bool:
            if self[1] != other[1]:
                return self[1] < other[1]
            else:
                return self[0] >= other[0]
    
    word_tuples = [WordTuple(item) for item in word_freqs.items()]
    top_k = min(len(word_tuples), k)
    k_word_heap = word_tuples[:top_k]
    heapify(k_word_heap)
    for w in word_tuples[top_k:]:
        if k_word_heap[0] < w:
            heappushpop(k_word_heap, w)

    sol =  [ heappop(k_word_heap)[0] for i in range(top_k)]
    sol.reverse()
    return sol

def k_most_frequent(k, words):
    """
    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    # Solution:
    #    use a heap to get top k frequent words, 
    #       the priority should be on both frequency and string comparision
    #   iterate through words and create a tuple of (count, word)
    #
    #   Time complexity: O(n + kmlog(n)), where m is string length
    #   Space complexity: O(nm)
    #
    # Edge cases:
    if words is None or len(words) == 0:
        return []

    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return nlogk_sol(k, count_dict)


class Testcase(unittest.TestCase):
    def test_example1(self):
        words = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
        k = 4
        actual = k_most_frequent(k, words)
        expected = ["car", "driver", "taxi", "bus"]
        self.assertListEqual(expected, actual, "Example1")
    
    def test_less_than_k(self):
        words = ["car", "bus", "taxi"]
        k = 4
        actual = k_most_frequent(k, words)
        expected = ["bus", "car", "taxi"]
        self.assertListEqual(expected, actual, "less_than_k")
    
    def test_same_frequency(self):
        words = ["car", "zebra", "carlike", "cars", "taxi", "taxis"]
        k = 4
        actual = k_most_frequent(k, words)
        expected = ["car", "carlike", "cars", "taxi"]
        self.assertListEqual(expected, actual, "same_frequency")
    


if __name__ == '__main__':
    unittest.main()