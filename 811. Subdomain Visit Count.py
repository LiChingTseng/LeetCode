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
            count, domain = domain.split()
            ans[domain] += int(count)

            for i in range(len(domain)):
                if domain[i] == '.':
                    ans[domain[i+1: ]] += int(count)
        
        return ["%d %s" % (ans[k], k) for k in ans]
