class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = i

        for i in range(len(numbers)):
            if target - numbers[i] in d:
                return [i + 1, d[target - numbers[i]]+1]
