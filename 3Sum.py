#Leetcode 15
#3 Sum
#Python 3
#Time Complexity: O(n^2)
#
#
#Set 3 pointers to iterate through the list
#
# 
# __p_i____ p_left______________________________________p_right_
#|________|________|___________________________________|________|
# 
#
# Check the sum of 3 numbers, 
# if == 0: append to result
# if  < 0: move p_left 
# if  > 0: move p_right
#
# Also, check if the element are the same after shifting the pointer
#
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #Sort the input list from small to large
        nums.sort()

        result = []
        
        #Case check: List element count smaller than 3
        if(len(nums)<3):
            return result
        #Case check: List elements are all negative
        if(nums[-1] < 0):
            return result
        #Case check: List elements are all positive
        if(nums[0] > 0):
            return result
        
        #Initialize pointers
        for pointer_i in range(len(nums)-2):

            pointer_left = pointer_i+1
            pointer_right = len(nums)-1
            if(pointer_i > 0 and nums[pointer_i] == nums[pointer_i-1]):
                continue
            #If nums[pointer_i] is positive, then the sum will always be greater than 0
            if(nums[pointer_i] > 0):
                break

            while pointer_left < pointer_right:
                _sum = nums[pointer_i] + nums[pointer_left] + nums[pointer_right]
                if(_sum == 0):
                    result.append([nums[pointer_i], nums[pointer_left], nums[pointer_right]])
                    pointer_left+=1
                    pointer_right-=1
                    #Check same elements
                    while pointer_left < pointer_right and nums[pointer_left] == nums[pointer_left-1]:
                        pointer_left += 1
                    while pointer_left < pointer_right and nums[pointer_right] == nums[pointer_right+1]:
                        pointer_right-=1
                elif(_sum < 0):
                    pointer_left+=1
                elif(_sum > 0):
                    pointer_right-=1
        return result
