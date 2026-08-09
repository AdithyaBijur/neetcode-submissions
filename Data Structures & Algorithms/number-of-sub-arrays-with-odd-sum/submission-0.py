class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = [0] * len(arr)
        even = [0] * len(arr)

        if arr[0] % 2 == 0:
            even[0] = 1
        else:
            odd[0] = 1 

        for i in range(1,len(arr)):
            if arr[i] % 2 == 0:
                odd[i] += odd[i-1]
                even[i] += even[i-1] + 1
            else:
                odd[i] = even[i-1] + 1
                even[i] = odd[i-1]

        print(odd, even)
        return sum(odd)
