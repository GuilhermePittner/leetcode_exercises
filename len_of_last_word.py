class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        lst_words = s.strip()        
        lst_words = lst_words.split(' ')

        #print(len(lst_words[-1]))

        return len(lst_words[-1])
        