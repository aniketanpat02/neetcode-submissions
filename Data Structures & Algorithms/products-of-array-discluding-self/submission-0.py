import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sufix_array = copy.deepcopy(nums)
        final_array = copy.deepcopy(nums)
        prefix_array = []

        for i in range(len(nums)):
            j=len(nums)-1-i
            if i == 0 :
                prefix_array.append(nums[i])
            else:
                prefix_array.append((prefix_array[i-1])*nums[i])
                sufix_array[j] = nums[j]*(sufix_array[j+1])

        for i in range(len(nums)):
            if i == 0:
                final_array[i] = sufix_array[i+1]
            elif i == len(nums) - 1:
                final_array[i] = prefix_array[i-1]
            else:
                final_array[i] = prefix_array[i-1] * sufix_array[i+1]

        return final_array
            