class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}
        for word in strs:
            st = "".join(sorted(word))
            if st not in anagram:
                anagram[st]=[]
            anagram[st].append(word)
        return list(anagram.values())