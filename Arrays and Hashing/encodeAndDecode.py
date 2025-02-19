class Solution:

    def encode(self, strs: List[str]) -> str:
        
        ecode = "" #empty string
        for string in strs: #for each string in the list
            ecode += str(len(string)) + "£" + string #add the length of the string and character £ and the string itself 
        return ecode    #return the encoded string






    def decode(self, s: str) -> List[str]:
        #create an empty list and i var to keep track of the index
        result = []
        i = 0

        while i < len(s):#while i is less than the length of the string
            j = i#look for the special character £ after the int value
            while s[j] != "£":
                j += 1 #increment j go to the next character
            
            length = int(s[i:j]) #when the special character is foiund the while loop will break and the length will be between i and j

            result.append(s[j + 1 : j+1 +length])#append the string to the result list

            i = j+1+length #increement i to the start of the next string
        
        return result#return the next result
    
