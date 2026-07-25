class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1
        
        lst = [(i, j) for i, j in freq_map.items()]
        lst1 = sorted(lst, key=lambda x: x[1], reverse=True)  # sort by freq
        
        k_most = lst1[:k]
        res = [n for n, m in k_most]
        return res