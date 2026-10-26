from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            cur = [0] * 26

            for char in s:
                cur[ord(char) - ord("a")] += 1
            
            groups[str(cur)].append(s)
        
        return [ls for key, ls in groups.items()]

        