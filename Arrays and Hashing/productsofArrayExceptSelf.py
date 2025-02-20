class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        
        output = [1] * (len(nums)) # create an oiutput array with same lenght of nums list

        #create a prefix variable where default val is 1
        pre = 1 

        for i in range(len(nums)): # loop through (left to right)
            output[i] = pre # set first as 1 then keep multiplying with the next items 
            pre *= nums[i]
        #at the end youll have a list of all the suffix products 

        post = 1

        for i in range (len(nums) - 1, - 1, -1): # loop backwards 
            output[i] *= post #  multiply post with all prefixes in list
            post *= nums[i]
        
        return output# return the list 
