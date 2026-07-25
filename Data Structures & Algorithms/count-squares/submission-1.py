class CountSquares:

    def __init__(self):
        self.ptsCount = collections.defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        ans = 0
        x,y  = point[0], point[1]

        keys = self.ptsCount.keys()
        k = []
        for i in keys:
            k.append(i)
        for pt in k:
            dx,dy = pt[0],pt[1]
            if abs(x - dx) == abs(y - dy) and abs(x - dx) != 0:
                ans += self.ptsCount[(x,dy)] * self.ptsCount[(dx,y)] * self.ptsCount[(dx,dy)]
        
        return ans
            

        
