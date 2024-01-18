class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        number = ''
        for x in digits:
            number += str(x)
        
        number = int(number)
        number += 1

        str_number = str(number)

        lst_rst = []
        for y in str_number:
            lst_rst.append(int(y))

        return lst_rst
    
        """  
        n_switch = digits[-1]

        if n_switch == 9:
            print('bla')
        else:
            n_switch += 1
            digits[-1] = n_switch

        return digits
        """