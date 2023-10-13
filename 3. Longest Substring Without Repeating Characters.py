class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # total number of letters, digits, symbols and spaces
        # charIndex record the indices of characters pointed by right pointer
        charIndex = [-1] * 128 
        left = 0
        maxlength = 0

        for right in range(len(s)):
            # check if the character pointed by left is same as that by right pointer
            if charIndex[ ord(s[right])] >= left:
                left = charIndex[ ord(s[right])] + 1 
                # move left pointer to the next index of the charatcter that 
                #   right pointer had pointed

            charIndex[ ord(s[right])] = right
            maxlength = max(maxlength, right-left+1)

        return maxlength

