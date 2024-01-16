class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        str_x = str(x)
        diss = ''

        for char in str_x[::-1]:
            diss+=char

        if str(x) == str(diss):
            return True

        """
        for item in str(x):
            diss+=item

        if int(x) == int(diss):
            return True
        
        return False
        """
        