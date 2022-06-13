class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(str(bin(n)))
        # print(n)
        return int(c["1"])