class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i], (target - position[i]) / speed[i]))

        cars.sort()
        
        stack = []

        for i in range(len(cars)):
            while stack and stack[-1][2] <= cars[i][2]:
                stack.pop()
            stack.append(cars[i])
        return len(stack)
        