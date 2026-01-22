class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for key in s:
            if key in s_dict:
                s_dict[key] += 1
            else:
                s_dict[key] = 1

        for key in t:
            if key in s_dict:
                s_dict[key] -= 1
            else:
                return False

        for key in s:
            if s_dict.get(key) == 0:
                s_dict.pop(key)

        if len(s_dict) == 0:
            return True
        return False

