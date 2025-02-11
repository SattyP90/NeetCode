class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)#create a dictionary to store the anagrams has to be default dict as we dont need to initialise for every new key.


        for s in strs:#list through the list of strings
            
            count = [0] * 26 #create a "key" where the index of each character will be increased 

            for c in s: 
                count[ord(c) - ord('a')] =+ 1 #find the correct index for character and add 1 to it 

            anagrams[tuple(count)].append(s)#add the string to the list of anagrams with the same key



        return anagrams.values()#return the values of the dictionary which is a list of lists of anagrams


                
        
        
            
