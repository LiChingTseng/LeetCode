class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        """collections.counter
        counter is a dictionary subclass for counting hashable objects
        elements are stored as dictionary keys and their counts are stored as dictionary values
        counts are allowed to be any integer value including zero or negative counts
        """

        ans = collections.Counter()
        
        for domain in cpdomains:
            count, domain = domain.split() # space between count and domain
            ans[domain] += int(count) # domain is key, storing count of domain

            # check subdomains in domain
            for i in range(len(domain)):
                if domain[i] == '.':
                    ans[domain[i+1: ]] += int(count) # create new key 
        
        return ["%d %s" % (ans[k], k) for k in ans] 
        # %d and %s are placeholders for an integer and a number
        #   ans[k] replace %d, k repalce %s
        #   % operator is used to replace the placeholders in the string with the values from the tuple. 
