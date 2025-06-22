"""
Given an unsigned integer N. The task is to convert gray to binary code

Gray code has a property that two successive numbers differ in only one bit 
    because of this property gray code does the cycling through various states 
    with minimal effort and is used in K-maps, error correction, communication, etc.

Example:
    Input: 28
    Output: 23
    Explanation: 28 (11100) should be converted to 23 (10111) .
"""

def gray_code_to_bin(num):
    """
    solution: 
        gray code = 28 (11100) 
        let position each bit by G5, G4, G3, G2, G1, G0

        bin = 23 (10111)
        let position of each bit B5, B4, B3, B2, B1, B0

        B5 = G5
        B4 = G4 ^ G5
        ...
        B0 = G0 ^ G1 ^ G2 ^ G3 ^ G4 ^ G5

        we work from left to right applying XOR each time
        notes: XOR with 0 always retain the bits (x ^ 0 = x)
    """
    bnum = num
    while num > 0:
        num >>= 1 # left to right
        bnum ^= num 
    
    return bnum

if __name__ == '__main__':
    x = 28; # 11100

    # Output is 23 (10111)
    print(gray_code_to_bin(x));


