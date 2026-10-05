"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Script         : makarand_bfs.py (Reference Implementation)
Title          : Breadth First Search (BFS) - 4-Level Filesystem Hierarchy Traversal
========================================================================================
"""

# Graph input: Filesystem directory hierarchy across 4 levels:
# Level 0: Root
# Level 1: Home, System
# Level 2: User, Shared, Drivers
# Level 3: Documents, Downloads, Network
# Level 4: Resume.pdf
graph = {
    'Root'       : ['Home', 'System'],
    'Home'       : ['User', 'Shared'],
    'System'     : ['Drivers'],
    'User'       : ['Documents', 'Downloads'],
    'Shared'     : ['Network'],
    'Drivers'    : [],
    'Documents'  : ['Resume.pdf'],
    'Downloads'  : [],
    'Network'    : [],
    'Resume.pdf' : []
}

# Initializing the queue and visited set
queue = []
visited = set()

# Starting point is 'Root'
start = 'Root'
queue.append(start)
visited.add(start)

print("BFS TRAVERSAL:")

# Continue the BFS as long as there are nodes in the queue
while queue:
    # Removing the node from the front of the queue
    node = queue.pop(0)
    
    # Printing the currently visited node
    print(node, end=" ")
    
    # Check all neighbors of the current node
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
print()