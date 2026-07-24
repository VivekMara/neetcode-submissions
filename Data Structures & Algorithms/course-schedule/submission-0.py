from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        UNVISITED, VISITING, DONE = 0, 1, 2
        state = [UNVISITED] * numCourses

        def has_cycle(course):
            if state[course] == VISITING:
                return True
            if state[course] == DONE:
                return False

            state[course] = VISITING
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            state[course] = DONE
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True