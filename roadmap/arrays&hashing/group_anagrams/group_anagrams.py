class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        return_list = []

        for i in range(len(strs)):
            anagram = {}
            for char in strs[i]:
                if char in anagram:
                    anagram[char] += 1
                else:
                    anagram[char] = 1

            if anagram in anagram_list:
                # Here I know the anagram is inside the return_list
                return_list[anagram_list.index(anagram)].append(strs[i])
            else:
                anagram_list.append(anagram)
                return_list.append([strs[i]])

        return return_list

