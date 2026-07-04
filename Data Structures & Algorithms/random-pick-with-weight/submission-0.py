import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        s = 0
        for i in w:
            s += i
            self.prefix.append(s)
        self.total = s

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, rand)

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()