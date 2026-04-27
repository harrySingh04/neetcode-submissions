class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # AAABABB , k = 2

        # A
        l = 0
        n = len(s)

        count = {}

        res = 0
        maxF = 0

        # AABABBA, k = 1, count = {A: 1}, r = 0, l = 0

        for r in range(n):

            count[s[r]] = count.get(s[r],0) + 1
            maxF = max(maxF, count[s[r]])


            while (r - l + 1) -  maxF > k:
                count[s[l]] = count[s[l]] - 1
                l += 1

            res = max(r - l + 1, res)
            
            
        
        return res




        