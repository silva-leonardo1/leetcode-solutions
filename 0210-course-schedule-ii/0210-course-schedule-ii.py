class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        order = []

        for course, requisite in prerequisites:
            graph[requisite].append(course)
            degree[course] += 1

        if min(degree) > 0 and numCourses > 0:
            return []
        
        queue = deque(
            course for course in range(numCourses)
            if degree[course] == 0
        )
        
        while queue:
            current_node = queue.popleft()
            order.append(current_node)
            for neighbour in graph[current_node]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    queue.append(neighbour)
        return order if len(order) == numCourses else []