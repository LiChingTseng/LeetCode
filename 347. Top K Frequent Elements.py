class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # count the occurances of each element in the list
        cnums = collections.Counter(nums)
        #  print(cnums)

        # cnums.most_common() : cnums sorted in descending order of count
        return [_[0] for _ in cnums.most_common()][:k]
        
