class Solution:
    def reverseBits(self, n: int) -> int:
        t = int('{:032b}'.format(n)[::-1], 2)
        return t