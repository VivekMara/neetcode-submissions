class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prereqs:
            graph[b].append(a)

        state = [0] * numCourses   # 0=unvisited, 1=visiting, 2=done
        order = []

        def dfs(course):
            if state[course] == 1: return False   # cycle
            if state[course] == 2: return True    # already processed

            state[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            state[course] = 2
            order.append(course)                  # record when done
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return order[::-1]                        # reverse finish order