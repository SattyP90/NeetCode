class Solution:
    def isValid(self, s: str) -> bool:


        #pop and push ?
        #add open brackets to a stack 
        #until a close bracket is found 
        #then start check process
        #check the pops of the stack
        #if they match the list then return true
        #else return false 
        #this wont work ^^^ open brackets need to be closed before opening another one 



        stack = []
        #hashmap of all the brackets with closing and opening
        brackets = {")":"(" , "]":"[" ,"}":"{"}

        for b in s: 
            #checking if the brackets before closing brackets are infact valid (the same)
            if b in brackets: #checking if its a closing bracket
                #check is stack is empty (cant be empty if theres a closing bracket because there needs to be open bracket before it)
                #and check if the last val is the corresponding bracket for that closing bracket
                if stack and stack[-1] == brackets[b]:#stack -1 is that last added val to stack
                    stack.pop()#remove from that stack if vals a matching
                else: #if previous check fail that means the list is invalid 
                    return False
            else:#if nothing is in the stack then just append the b item.
                stack.append(b)

        #if the stack is empty that everything matches so return true
        #else return false (meaning not everything matched and theres items still in the list)

        return True if not stack else False