class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars_s = {}
        chars_t = {}

        for i in s:
            if i in chars_s:
                chars_s[i] += 1
            else:
                chars_s[i] = 1
        for i in t:
            if i in chars_t:
                chars_t[i] += 1
            else:
                chars_t[i] = 1

        return chars_s == chars_t