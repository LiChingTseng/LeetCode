class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Categorize by Sorted string

        # creat a dictionary in list format that always assigns deafult values
        #    when any key that does not exist in the defaultdict is added or accessed
        ans = collections.defaultdict(list) 

        for s in strs:
            ans[tuple(sorted(s))].append(s)
            # take advanage of sorted() to create unique index for anagrams

        return ans.values()
