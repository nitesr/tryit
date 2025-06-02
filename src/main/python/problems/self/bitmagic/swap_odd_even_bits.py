"""
Given an unsigned integer N. The task is to swap all odd bits with adjacent even bits.

Example:
    Input: 23
    Output: 43
    Explanation: 23 (00010111) should be converted to 43 (00101011).
"""

def swap_odd_even_bits(num):
    odd_mask = int(0b10101010101010101010101010101010)
    even_mask =  int(0b01010101010101010101010101010101)

    even_bits = num & even_mask
    odd_bits = num & odd_mask

    even_bits <<= 1
    odd_bits >>= 1

    return even_bits | odd_bits

if __name__ == '__main__':
    x = 23; # 00010111

    # Output is 43 (00101011)
    print(swap_odd_even_bits(x));


