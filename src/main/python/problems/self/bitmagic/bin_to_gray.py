"""
Given an unsigned integer N. The task is to convert binary to gray code

Gray code has a property that two successive numbers differ in only one bit 
    because of this property gray code does the cycling through various states 
    with minimal effort and is used in K-maps, error correction, communication, etc.

Example:
    Input: 23
    Output: 28
    Explanation: 23 (00010111) should be converted to 28 (11100).
"""

def bin_to_gray_code(num):
    return num ^ (num >> 1)

if __name__ == '__main__':
    x = 23; # 10111

    # Output is 28 (11100)
    print(bin_to_gray_code(x));


