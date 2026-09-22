class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        str_dict = {}
        for abet in s:
            if not str_dict.get(abet):
                str_dict[abet] = 1
            else: 
                str_dict[abet] = str_dict[abet] + 1

        for sbet in t: 
            if sbet not in str_dict.keys():
                return False
            str_dict[sbet] = str_dict[sbet] - 1

            if str_dict[sbet] < 0:
                return False

        return True

        


