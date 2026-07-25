class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            curr_map = {}
            for ch in s:
                curr_map[ch] = curr_map.get(ch, 0) + 1
            
            # convert dict to a hashable key
            key = tuple(sorted(curr_map.items()))
            
            groups.setdefault(key, []).append(s)
        
        return list(groups.values())