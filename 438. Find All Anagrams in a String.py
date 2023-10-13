class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq_p = [0] * 26
        window = [0] * 26
        ans = []

        if len(s) < len(p):
            return {}

        for i in range(len(p)):
            freq_p[ ord(p[i]) - ord('a') ] +=1 # record p
            # record first p number of character in s
            window[ ord(s[i]) - ord('a') ] +=1 
    
        # examine first set of string in s
        if freq_p == window:
            ans.append(0)

        for i in range(len(p), len(s)):
            window[ ord(s[i- len(p)]) - ord('a')] -= 1
            window[ ord(s[i]) - ord('a')] += 1

            if freq_p == window:
                ans.append(i - len(p) + 1)

        return ans
