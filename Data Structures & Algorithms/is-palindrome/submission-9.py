import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        for i in range(int(len(s)/2)):
            if s[i].lower() != s[int(len(s)) - i - 1].lower():
                return False

        return True

        