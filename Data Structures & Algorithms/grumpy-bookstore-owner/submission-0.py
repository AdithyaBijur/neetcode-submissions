class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        product = []

        if minutes > len(customers):
            return sum(customers)

        for i in range(len(customers)):
            if grumpy[i] == 1:
                product.append(-1 * customers[i])
            else:
                product.append(customers[i])

        
        s = sum(product[:minutes])

        minn = s
        minnStart = 0
        for j in range(minutes,len(customers)):
            if product[j - minutes] < 0:
                s -= product[j - minutes]
            if product[j] < 0:
                s += product[j]
            minn = min(minn, s)
            if s == minn:
                minnStart = j - minutes + 1

        
       
        print(product, minn, minnStart)

        for i in range(minnStart, minnStart + minutes):
            if product[i] < 0:
                product[i] *= -1
        
        ans = 0

        print(product, minn, minnStart)

        for p in product:
            if p > 0:
                ans += p

        return ans
        
        
        