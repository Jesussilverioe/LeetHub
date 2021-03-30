class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjpre = {i:[] for i in range(numCourses)}
        for pre,val in prerequisites:
            adjpre[pre].append(val)
            
        visited = set()
        cycle = set()
        ans = []
        
        def bfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for cour in adjpre[course]:
                if not bfs(cour):
                    return False
            visited.add(course)
            cycle.remove(course)
            ans.append(course)
            return True
        
        for cour in range(numCourses):
            if not bfs(cour):
                return []
        return ans