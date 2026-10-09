class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num1 = list(sorted(set(nums)))
        count = 1
        temp_count = 1
        if not num1:
            return 0

        for i in range(len(num1)-1):
            if not num1[i+1]-num1[i]==1:
                if temp_count > count:
                    count = temp_count
                temp_count=1
            else: 
                temp_count +=1
        if temp_count > count:
            count = temp_count

        return count if count else 0



        