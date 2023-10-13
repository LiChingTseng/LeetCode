class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' Two pointers
        go inwards towards the middle
        '''
        # isalnum() returns True if all the characters are alphanumeric, 
        #   meaning alphabet letter (a-z) and numbers (0-9).

        # Define the two pointers on each end
        i, j = 0, len(s) - 1

        while i<j:
            # increase the left-end point if current character is non-alphanumeric
            while i<j and not s[i].isalnum():
                i+=1

            # decrease the righy-end point if current character is non-alohanumeric
            while i<j and not s[j].isalnum():
                j-=1

            # compare both pointers should point to equivalent character or else breaak early
            if s[i].lower() != s[j].lower():
                return False
        
            # increase the pointer to work on next character
            i+=1
            j-=1
        
        return True
