class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # a dictionary-like object that has a default value for any new keys you
        sDict = collections.defaultdict(int) # int is the default type
        tDict = collections.defaultdict(int)
        for i in t:
            tDict[i] += 1
        print(tDict)

        count = 0
        left, right = 0, 0
        ans = ""
        r = float('inf')
        
        for right in range(len(s)):
            sDict[s[right]] += 1

            if tDict.get(s[right], -1) == sDict[s[right]]:
                count += 1

            while count == len(tDict) and left <= right:
                if right-left+1 < r:
                    r = right - left + 1
                    ans = s[left:right+1]
                if sDict[s[left]] == tDict.get(s[left], -1):
                    count -= 1
                sDict[s[left]] -= 1
                left += 1

        return ans




        
