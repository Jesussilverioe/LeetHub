class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mydic = {i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            mydic[course].append(pre)
                
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if mydic[course] == []:
                return True
            
            visited.add(course)
            for cour in mydic[course]:
                if not dfs(cour): return False
            visited.remove(course)
            mydic[course] = []
            return True
        
        for courses in range(numCourses):
            if not dfs(courses): return False
        return True
        