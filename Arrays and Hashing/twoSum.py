class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} #val : index ,this is a hashmap

        #iterate through the lsit once and if no sum is found add the item to hash map 
        #and look for the difference in the hashmap and return the indexes
        for i, n in enumerate(nums):
            diff = target - n #calculate the difference using the target 

            if diff in prevMap: # look for the number you need in the 
                return [prevMap[diff], i] # if the number is already in the map then rreturn the corresponding value (which is an index) adn the original index of current number in the list
            prevMap[n] = i # if the number isnt found add it to the map with n as key and i as the value 
        return sasd
    