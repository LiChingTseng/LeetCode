class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # total number of letters, digits, symbols and spaces
        # charIndex record the indices of characters
        charIndex = [-1] * 128 
        left = 0
        maxlength = 0

        for right in range(len(s)):
            # check if the character has occurred
            if charIndex[ ord(s[right])] >= left:
                left = charIndex[ ord(s[right])] + 1

            charIndex[ ord(s[right])] = right
            maxlength = max(maxlength, right-left+1)

        return maxlength

