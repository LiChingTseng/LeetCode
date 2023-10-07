class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        ans = []

        # store the index of nums list
        
        for i in range(n):

            # step 1. remove all the nums smaller than num[i], and must append the latest one
            while len(dq) > 0 and nums[dq[-1]] < nums[i] :
                dq.pop()
            dq.append(i)

            # step 2. ensure the scope of sliding window
            if i - dq[0] >= k:
                dq.popleft()
            
            if i >= k-1:  # start appeding maximum num in each sliding window
                ans.append(nums[dq[0]]) 
                
        return ans
