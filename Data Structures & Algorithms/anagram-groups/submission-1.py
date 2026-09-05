from collections import defaultdict
class Solution:
    def getKey(self, word: str) -> str:
        res = [0] * 26

        for char in word:
            res[ord(char) - ord("a")] += 1
        
        return str(res)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = defaultdict(list)

        for word in strs:
            out[self.getKey(word)].append(word)
        

        return list(out.values())
        