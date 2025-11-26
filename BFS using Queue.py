from collections import deque

def bfs(graph, start):
    visited = set()                 # nodes already visited
    queue = deque([start])          # queue for BFS

    visited.add(start)

    while queue:
        node = queue.popleft()      # remove front element
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)   # push neighbor into queue
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BFS Traversal:")
    bfs(graph, 'A')
