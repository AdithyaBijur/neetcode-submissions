class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def isValid(toCheck):
            ans = []
            for i in range(0, len(toCheck)):
                if toCheck[i] > target[i]:
                    return []
                elif toCheck[i] == target[i]:
                    ans.append(i)
            print(ans)
            return ans
        
        resSet = set()
        for t in triplets:
            
            res = isValid(t)
            for i in res:
                resSet.add(i)
            if len(resSet) == 3:
                return True
        
        return False



        