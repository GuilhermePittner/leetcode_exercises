class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        #closest = 9999
        closest = float('inf') #gpt hint

        for x in nums:

            if abs(x) < abs(closest):
                closest = x
                print(f'mais próximo: {closest}')

            elif abs(x) == abs(closest):

                if x > closest:
                    closest = x

        return closest


"""
elif abs(x) == closest:
closest = x
print(f'closest: {closest}')
"""