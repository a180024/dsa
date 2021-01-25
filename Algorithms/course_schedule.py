import collections

# BFS
#  class Solution:
#  def canFinish(self, numCourses, prerequisites):
#  graph = collections.defaultdict(list)
#  indegree = collections.defaultdict(list)
#  queue = collections.deque([])

#  for i, j in prerequisites:
#  graph[j].append(i)
#  indegree[i].append(j)

#  for k in range(numCourses):
#  if len(indegree[k]) == 0:
#  queue.append(k)

#  while queue:
#  course = queue.popleft()
#  indegree.pop(course)
#  for node in graph[course]:
#  indegree[node].remove(course)
#  if len(indegree[node]) == 0:
#  queue.append(node)

#  return not indegree


# DFS
class Solution:
    def topologicalSort(self, i, graph, visited, recStack):
        visited[i] = True
        recStack[i] = True
        for node in graph[i]:
            if recStack[node]:
                return False
            if not visited[node]:
                if not self.topologicalSort(node, graph, visited, recStack):
                    return False
        recStack[i] = False
        return True

    def canFinish(self, numCourses, prerequisites):
        visited, recStack = [False] * numCourses, [False] * numCourses
        graph = collections.defaultdict(list)
        for src, dest in prerequisites:
            graph[src].append(dest)
        for i in range(numCourses):
            if not visited[i]:
                if not self.topologicalSort(i, graph, visited, recStack):
                    return False
        return True


sol = Solution()
sol.canFinish(2, [[1, 0]])
