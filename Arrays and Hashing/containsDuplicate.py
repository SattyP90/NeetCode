class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #create a set to store the values that have been seen
        seen = set()
        for i in nums: #iterate through the list 
            if i in seen: #check if i has been seeen
                return True # if so then return true and exit the loop
            else:
                seen.add(i)#or else add the new item into see hashset
        
        return False #if nothing is found return false


