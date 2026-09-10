class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_rev_s = ""

        for char in s:
            if char.isalnum():
                cleaned_rev_s += char.lower()    

        return cleaned_rev_s == cleaned_rev_s[::-1]        
        