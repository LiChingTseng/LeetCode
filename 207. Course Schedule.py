class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        ## Whether it is possible to finish all the given courses without any cyclic dependencies.
        
        # create an empty adjancency list to represent the directed graph
        # each node in the graph represents a course and the edges represent the prerequisites
        adj =[[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1
    
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            current = queue.popleft()
            ans.append(current)
        
            for next_course in adj[current]:
                indegree[next_course]-=1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                
        return len(ans) == numCourses

        # create an array called indegree of size n
        # keep track of the number of incoming edges to each course

        
