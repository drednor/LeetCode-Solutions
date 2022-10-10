class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        if palindrome == len(palindrome) * palindrome[0] and len(palindrome)>1 and palindrome[0]=="a":
            i = len(palindrome) -1
            palindrome = palindrome[:i] + "b" + palindrome[i+1:]
            return palindrome
            
        for i in range(len(palindrome)):
            if palindrome[i] == "a":
                continue
            else:
                temp = palindrome.replace(palindrome[i],"a",1)
                if temp == len(palindrome) * palindrome[0] and len(palindrome)>1:
                    i = len(palindrome) -1
                    palindrome = palindrome[:i] + "b" + palindrome[i+1:]
                    return palindrome
                else:
                    palindrome = palindrome.replace(palindrome[i],"a",1)
                    return palindrome
                    
                #return palindrome
        return ""