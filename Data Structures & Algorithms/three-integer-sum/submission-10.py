class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums=sorted(nums)
        for i in range(len(nums)):
            left = 0
            right = len(nums) -1
            while left < right:
                if left == i:
                    left +=1
                    continue
                if right == i:
                    right -=1
                    continue
                if left == right:
                    left +=1
                    right -=1
                    continue
                if nums[left] + nums[right] + nums[i] == 0:
                    l = list(sorted([nums[left],nums[right],nums[i]]))
                    if l not in final:
                            final.append(l)
                    left +=1
                    right -=1
                if nums[left] + nums[right] > -(nums[i]):
                    right-=1
                if nums[left] + nums[right] < -(nums[i]):
                    left+=1
        return final