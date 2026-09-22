from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sotrs = "".join(sorted(s))
            res[sotrs].append(s)

        return list(res.values())