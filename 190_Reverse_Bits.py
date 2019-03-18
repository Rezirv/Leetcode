class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rer = bin(n)[2:][::-1]
        while len(rer) < 32:
            rer += '0'
        return int(rer, 2)
