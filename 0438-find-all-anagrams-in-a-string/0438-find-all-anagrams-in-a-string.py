class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k = len(p)
        # a = sorted(p)
        ind = []
        if len(s)<k:
            return []
        # curr = s[:k]
        # for i in range(len(s)-k+1):
        #     if a == sorted(curr):
        #         ind.append(i)
        #     curr = s[i+1:i+1+k]
        # return ind

        p_count=[0]*26
        window=[0]*26

        for ch in p:
            p_count[ord(ch)-ord('a')]+=1

        for i in range(len(s)):
            window[ord(s[i])-ord('a')]+=1
            if i>=k:
                window[ord(s[i-k])-ord('a')]-=1
            if window == p_count:
                ind.append(i-k+1)
        return ind