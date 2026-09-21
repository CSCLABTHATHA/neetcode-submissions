class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        leng = len(s)
        right =  leng -1
        while right > left:
            while left < leng and not s[left].isalnum():
                left += 1

            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left > leng or right < 0:
                return True

            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1


        return True
