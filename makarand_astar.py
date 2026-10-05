"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Script         : makarand_astar.py (Reference Implementation)
Title          : A* Search Algorithm - 5-Node Graph Pathfinding
========================================================================================
"""

import heapq

graph = {
    'S': {'A': 2, 'B': 4},
    'A': {'S': 2, 'B': 1, 'C': 3},
    'B': {'S': 4, 'A': 1, 'G': 5},
    'C': {'A': 3, 'G': 2},
    'G': {'B': 5, 'C': 2}
}

heuristic = {
    'S': 6,
    'A': 4,
    'B': 2,
    'C': 1,
    'G': 0
}

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g_cost[goal]

        for neighbour, cost in graph[current].items():
            new_g_cost = g_cost[current] + cost
            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost
                f_cost = new_g_cost + heuristic[neighbour]
                parent[neighbour] = current
                heapq.heappush(open_list, (f_cost, neighbour))

    return None, float('inf')

start = 'S'
goal = 'G'

path, cost = a_star(graph, start, goal, heuristic)
if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")