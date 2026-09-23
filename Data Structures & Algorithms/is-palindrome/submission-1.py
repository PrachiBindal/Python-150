class Solution:
    def check(self, c:str) -> bool:
        x=ord(c)
        if 64<x<91 or 96<x<123 or 47<x<58:
            return False
        return True
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<=j:
            while i<=j and self.check(s[i]):
                i+=1
            while i<=j and self.check(s[j]):
                j-=1
            if i<=j and s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
        