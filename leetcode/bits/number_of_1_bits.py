class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        bin_str = bin(n)[2:]
        for c in bin_str:
            if c == '1':
                ones += 1
        return ones
    
if __name__ == '__main__':
    s = Solution()
    assert s.hammingWeight(11) == 3
    assert s.hammingWeight(128) == 1
    assert s.hammingWeight(2147483645) == 30