from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictNum = Counter(nums)# Counter will create a tuples with (eleement, freqs)

        tuplesWithFreq = dictNum.most_common(k)#only get the top values depending on int K
        
        out = [num for num, freq in tuplesWithFreq]# loop through the tuples and only get elements 

        return out# return output
        