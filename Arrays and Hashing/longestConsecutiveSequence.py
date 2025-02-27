class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        #count sequences 
        #create a set an iterate through and check for left 
        #by checkiung left node you will know if its he start of a sequence
        #also check for right nodes (1+) 

    
        #create a set of numners
        numberSet = set(nums)

        longestSeq = 0

        for aNum in nums:
            #chekc left to see if its a start of the sequence
            leftNode = aNum - 1
            # if there is no left node then its a start for a sequence 
            if leftNode not in numberSet:
                length = 0
                while (aNum + length) in numberSet: #check the current number 
                    length += 1 #keep increasing length by one
                longestSeq = max(longestSeq, length)    #update the max length if larger value found 

        #return the int value
        return longestSeq