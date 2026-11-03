from collections import deque
# Mapping location names to indices for matrix representation
locations = ['A', 'B', 'C', 'D']
location_index = {}
for i in range(len(locations)):
    location_index[locations[i]] = i
# Graph represented as adjacency matrix
adj_matrix = [    # A  B  C  D
                  [ 0, 1, 1, 0],  # A
                  [ 1, 0, 0, 1],  # B
                  [ 1, 0, 0, 1],  # C
                  [ 0, 1, 1, 0]   # D
            ]
def dfs_matrix(start):
    visited = [False] * len(locations)
    result = []

    def dfs(node):
        visited[node] = True
        result.append(locations[node])
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    dfs(location_index[start])
    return result

# Graph represented as adjacency list
adj_list = {'A': ['B', 'C'],'B': ['A', 'D'],'C': ['A', 'D'],'D': ['B', 'C'] }

def bfs_list(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result
start_location = 'A'
dfs_result = dfs_matrix(start_location)
print("DFS Traversal (using adjacency matrix):", dfs_result)
bfs_result = bfs_list(start_location)
print("BFS Traversal (using adjacency list):", bfs_result)
 