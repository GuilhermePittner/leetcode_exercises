class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        rst = []

        for id_x, x in enumerate(nums):
            
            for id_y, y in enumerate(nums):
               
                #print(f'segue x {x} e segue y {y}')
                
                if x + y == target:

                    if id_x != id_y:
                        rst.append(id_x)
                        rst.append(id_y)
                        return rst


"""
rst = []
        sum = 0

        for idc, x in enumerate(nums):
            
            if sum == 0:
                sum += x
                rst.append(idc)
            
            else:
                sum += x
                rst.append(idc)

                if sum == target:
                    print('chegamos!!')
                    return rst

                elif sum > target:
                    sum -= x
                    rst.pop()
"""

