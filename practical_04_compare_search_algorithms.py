"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Practical No.  : 04
Title          : Comparative Study: BFS vs DFS vs A* on Smart City Road Network
========================================================================================
Problem Statement:
A smart city navigation software evaluates search algorithms for route planning.
This program compares Breadth First Search (BFS), Depth First Search (DFS), and
A* Search on the exact same road network graph. It benchmarks:
  1. Discovered Navigation Path
  2. Total Path Cost / Travel Distance (km)
  3. Total Search Space Explored (Nodes Evaluated)
  4. Execution Time (microseconds)
"""

import time
import heapq
from collections import deque
from typing import Dict, List, Tuple, Optional, Set

class SmartCityGraph:
    """Road network graph with 2D spatial coordinates for heuristic evaluation."""

    def __init__(self) -> None:
        self.coordinates: Dict[str, Tuple[int, int]] = {}
        self.adj_list: Dict[str, List[Tuple[str, float]]] = {}

    def add_intersection(self, name: str, x: int, y: int) -> None:
        self.coordinates[name] = (x, y)
        if name not in self.adj_list:
            self.adj_list[name] = []

    def add_road(self, u: str, v: str, cost: float) -> None:
        """Bidirectional road with distance/travel cost."""
        self.adj_list[u].append((v, cost))
        self.adj_list[v].append((u, cost))

    def manhattan_heuristic(self, node: str, goal: str) -> float:
        x1, y1 = self.coordinates[node]
        x2, y2 = self.coordinates[goal]
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate_path_cost(self, path: List[str]) -> float:
        """Calculate cumulative edge costs along a path."""
        total = 0.0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for neighbor, cost in self.adj_list[u]:
                if neighbor == v:
                    total += cost
                    break
        return total

    # 1. Breadth First Search (BFS)
    def run_bfs(self, start: str, goal: str) -> Tuple[Optional[List[str]], float, int, float]:
        t0 = time.perf_counter()
        queue = deque([start])
        visited: Set[str] = {start}
        parent: Dict[str, Optional[str]] = {start: None}
        nodes_explored = 0
        found = False

        while queue:
            curr = queue.popleft()
            nodes_explored += 1
            if curr == goal:
                found = True
                break

            for neighbor, _ in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    queue.append(neighbor)

        t_elapsed = (time.perf_counter() - t0) * 1e6  # microseconds

        if not found:
            return None, 0.0, nodes_explored, t_elapsed

        path: List[str] = []
        curr_node: Optional[str] = goal
        while curr_node is not None:
            path.append(curr_node)
            curr_node = parent[curr_node]
        path.reverse()
        return path, self.calculate_path_cost(path), nodes_explored, t_elapsed

    # 2. Depth First Search (DFS)
    def run_dfs(self, start: str, goal: str) -> Tuple[Optional[List[str]], float, int, float]:
        t0 = time.perf_counter()
        stack = [start]
        visited: Set[str] = set()
        parent: Dict[str, Optional[str]] = {start: None}
        nodes_explored = 0
        found = False

        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            nodes_explored += 1

            if curr == goal:
                found = True
                break

            for neighbor, _ in reversed(self.adj_list.get(curr, [])):
                if neighbor not in visited:
                    parent[neighbor] = curr
                    stack.append(neighbor)

        t_elapsed = (time.perf_counter() - t0) * 1e6  # microseconds

        if not found:
            return None, 0.0, nodes_explored, t_elapsed

        path: List[str] = []
        curr_node: Optional[str] = goal
        while curr_node is not None:
            path.append(curr_node)
            curr_node = parent[curr_node]
        path.reverse()
        return path, self.calculate_path_cost(path), nodes_explored, t_elapsed

    # 3. A* Search Algorithm
    def run_astar(self, start: str, goal: str) -> Tuple[Optional[List[str]], float, int, float]:
        t0 = time.perf_counter()
        open_set: List[Tuple[float, float, str]] = []
        heapq.heappush(open_set, (self.manhattan_heuristic(start, goal), 0.0, start))

        g_scores: Dict[str, float] = {start: 0.0}
        parent: Dict[str, Optional[str]] = {start: None}
        closed_set: Set[str] = set()
        nodes_explored = 0
        found = False

        while open_set:
            f, current_g, curr = heapq.heappop(open_set)

            if curr in closed_set:
                continue
            closed_set.add(curr)
            nodes_explored += 1

            if curr == goal:
                found = True
                break

            for neighbor, edge_cost in self.adj_list.get(curr, []):
                tentative_g = current_g + edge_cost
                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + self.manhattan_heuristic(neighbor, goal)
                    parent[neighbor] = curr
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))

        t_elapsed = (time.perf_counter() - t0) * 1e6  # microseconds

        if not found:
            return None, 0.0, nodes_explored, t_elapsed

        path: List[str] = []
        curr_node: Optional[str] = goal
        while curr_node is not None:
            path.append(curr_node)
            curr_node = parent[curr_node]
        path.reverse()
        return path, g_scores[goal], nodes_explored, t_elapsed


def main() -> None:
    city = SmartCityGraph()

    # Intersections with (X, Y) spatial coordinates
    intersections = {
        "Tech_Park": (0, 0),
        "Cyber_Hub": (2, 3),
        "Metro_Central": (4, 1),
        "City_Square": (5, 5),
        "East_Gate": (8, 2),
        "North_Ring": (3, 7),
        "South_Plaza": (7, 0),
        "Terminal_Airport": (10, 6)
    }

    for name, (x, y) in intersections.items():
        city.add_intersection(name, x, y)

    # Road network edges with travel distance (km)
    roads = [
        ("Tech_Park", "Cyber_Hub", 3.6),
        ("Tech_Park", "Metro_Central", 4.1),
        ("Cyber_Hub", "North_Ring", 4.2),
        ("Cyber_Hub", "City_Square", 3.6),
        ("Metro_Central", "East_Gate", 4.1),
        ("Metro_Central", "South_Plaza", 3.2),
        ("North_Ring", "City_Square", 2.8),
        ("City_Square", "Terminal_Airport", 5.1),
        ("East_Gate", "Terminal_Airport", 4.5),
        ("South_Plaza", "East_Gate", 2.2),
        ("City_Square", "East_Gate", 4.3)
    ]

    for u, v, w in roads:
        city.add_road(u, v, w)

    start_node = "Tech_Park"
    goal_node = "Terminal_Airport"

    print("==========================================================================================")
    print("      COMPARATIVE BENCHMARK: BFS vs DFS vs A* ON SMART CITY ROAD NETWORK                 ")
    print("==========================================================================================")
    print(f"Origin Junction : {start_node} (Coords: {intersections[start_node]})")
    print(f"Destination     : {goal_node} (Coords: {intersections[goal_node]})\n")

    bfs_path, bfs_cost, bfs_exp, bfs_time = city.run_bfs(start_node, goal_node)
    dfs_path, dfs_cost, dfs_exp, dfs_time = city.run_dfs(start_node, goal_node)
    ast_path, ast_cost, ast_exp, ast_time = city.run_astar(start_node, goal_node)

    results = [
        ("BFS (Breadth First)", bfs_path, bfs_cost, bfs_exp, bfs_time),
        ("DFS (Depth First)",   dfs_path, dfs_cost, dfs_exp, dfs_time),
        ("A* (Heuristic Search)", ast_path, ast_cost, ast_exp, ast_time),
    ]

    print(f"{'Algorithm':<22} | {'Path Cost (km)':<14} | {'Nodes Explored':<14} | {'Exec Time (μs)':<14}")
    print("-" * 72)
    for name, path, cost, exp, t_val in results:
        cost_str = f"{cost:.2f}" if path else "N/A"
        print(f"{name:<22} | {cost_str:<14} | {exp:<14} | {t_val:<14.2f}")

    print("\n--- Discovered Navigation Routes ---")
    for name, path, cost, _, _ in results:
        print(f"\n[{name}]")
        if path:
            print(f"  Path      : {' -> '.join(path)}")
            print(f"  Total Cost: {cost:.2f} km | Number of Hops: {len(path) - 1}")
        else:
            print("  No route found.")

    print("\n--- Theoretical & Practical Insights ---")
    print("1. BFS : Explores level-by-level; guarantees shortest hops in unweighted graphs but ignores road weights.")
    print("2. DFS : Traverses deep into single paths; results in non-optimal, arbitrary routes with high variance.")
    print("3. A*  : Combines path cost g(n) with heuristic h(n); guarantees mathematically optimal shortest distance.")
    print("==========================================================================================")


if __name__ == "__main__":
    main()
