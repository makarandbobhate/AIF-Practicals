"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Script         : makarand_dfs.py (Reference Implementation)
Title          : Depth First Search (DFS) - Social Graph Traversal
========================================================================================
"""

def DFS(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            DFS(graph, neighbour, visited)

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice'],
    'David': ['Bob'],
    'Eve': ['Bob']
}

visited = set()
start_vertex = 'Alice'

print("DFS Traversal:")
DFS(graph, start_vertex, visited)
print()
