class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana = {}
        for w in strs:
            s = "".join(sorted(w))
            if s not in ana:
                ana[s]=[]
            ana[s].append(w)
        return list(ana.values())
