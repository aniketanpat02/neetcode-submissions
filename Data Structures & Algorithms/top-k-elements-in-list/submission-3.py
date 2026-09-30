class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        if len(set(nums)) == k: 
            return list(set(nums))

        for i in nums:
            if not dictt.get(i):
                dictt[i] = 0
            dictt[i] += 1

        sorted_dict = dict(sorted(dictt.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]
