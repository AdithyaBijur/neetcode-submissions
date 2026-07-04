class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = []

        s = 0
        for i in nums:
            s += i
            prefix.append(s)
        
        if len(prefix) < 2:
            return False
        if len(prefix) == 2:
            return prefix[-1] % k == 0
        
        for i in range(2, len(prefix)):
            for j in range(i-2,-1,-1):
                if (prefix[i] - prefix[j]) % k == 0:
                    # print(prefix, i, j)
                    return True
        
        return False