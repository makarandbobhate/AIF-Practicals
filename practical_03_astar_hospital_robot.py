"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Practical No.  : 03
Title          : A* Search Algorithm - Hospital Medicine Delivery Robot
========================================================================================
Problem Statement:
An autonomous medical courier robot must navigate a hospital floor grid from the
Pharmacy (Start) to an Intensive Care Ward (Goal). The floor contains blocked
corridors and restricted rooms. A* Search using the Manhattan Distance heuristic
finds the optimal, collision-free route.
"""

import heapq
from typing import List, Tuple, Dict, Optional, Set

# Cell representation constants
EMPTY = 0
BLOCKED = 1

class HospitalFloorMap:
    """Represents the hospital floor grid and pathfinding logic."""

    def __init__(
        self, grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]
    ) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = start
        self.goal = goal

    def manhattan_distance(self, cell: Tuple[int, int]) -> int:
        """Heuristic h(n) = |x1 - x2| + |y1 - y2|"""
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])

    def get_neighbors(self, cell: Tuple[int, int]) -> List[Tuple[int, int]]:
        """4-directional movement: North, South, West, East."""
        r, c = cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors: List[Tuple[int, int]] = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != BLOCKED:
                    neighbors.append((nr, nc))
        return neighbors

    def a_star_search(self) -> Tuple[Optional[List[Tuple[int, int]]], int, int]:
        """
        Executes A* Search algorithm using Manhattan distance heuristic.
        
        Returns:
            - optimal_path: Coordinates from start to goal.
            - total_cost: Exact g(goal) path cost.
            - nodes_evaluated: Total count of expanded nodes.
        """
        # Priority Queue holds: (f_score, g_score, cell)
        open_set: List[Tuple[int, int, Tuple[int, int]]] = []
        heapq.heappush(open_set, (self.manhattan_distance(self.start), 0, self.start))

        g_scores: Dict[Tuple[int, int], int] = {self.start: 0}
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
        closed_set: Set[Tuple[int, int]] = set()

        nodes_evaluated = 0

        while open_set:
            f, current_g, current = heapq.heappop(open_set)

            if current in closed_set:
                continue

            closed_set.add(current)
            nodes_evaluated += 1

            # Goal Test
            if current == self.goal:
                path: List[Tuple[int, int]] = []
                curr: Tuple[int, int] = current
                while curr in came_from:
                    path.append(curr)
                    curr = came_from[curr]
                path.append(self.start)
                path.reverse()
                return path, current_g, nodes_evaluated

            for neighbor in self.get_neighbors(current):
                tentative_g = current_g + 1  # Uniform step cost = 1

                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + self.manhattan_distance(neighbor)
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))

        return None, -1, nodes_evaluated

    def render_map(self, path: Optional[List[Tuple[int, int]]] = None) -> None:
        """Visual representation of the hospital floor layout."""
        path_set = set(path) if path else set()
        print("    " + " ".join(f"{c:2d}" for c in range(self.cols)))
        print("   +" + "--" * self.cols + "-+")
        for r in range(self.rows):
            row_symbols = []
            for c in range(self.cols):
                cell = (r, c)
                if cell == self.start:
                    row_symbols.append(" P")  # Pharmacy (Start)
                elif cell == self.goal:
                    row_symbols.append(" W")  # Ward (Goal)
                elif cell in path_set:
                    row_symbols.append(" *")  # Navigated Path
                elif self.grid[r][c] == BLOCKED:
                    row_symbols.append(" ■")  # Blocked Barrier
                else:
                    row_symbols.append(" .")  # Open corridor
            print(f"{r:2d} | " + " ".join(row_symbols) + " |")
        print("   +" + "--" * self.cols + "-+")
        print("Legend: [P] Pharmacy Start | [W] Ward Goal | [*] Robot Path | [■] Blocked Wall | [.] Corridor\n")


def main() -> None:
    # 0 = Open corridor, 1 = Blocked / Restricted partition
    hospital_grid = [
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0, 0]
    ]

    start_pharmacy = (0, 0)
    goal_ward = (6, 7)

    hospital = HospitalFloorMap(hospital_grid, start_pharmacy, goal_ward)

    print("==================================================================")
    print(" HOSPITAL MEDICINE DELIVERY ROBOT (A* SEARCH WITH MANHATTAN)      ")
    print("==================================================================")
    print(f"Origin (Pharmacy)          : {start_pharmacy}")
    print(f"Destination (Patient Ward) : {goal_ward}\n")

    print("Initial Floor Plan:")
    hospital.render_map()

    path, cost, evaluated = hospital.a_star_search()

    if path:
        print("Optimized Navigation Route Found:")
        hospital.render_map(path)
        print(f"Optimal Total Path Steps: {cost} moves")
        print(f"Total Nodes Evaluated   : {evaluated}")
        print("Detailed Step-by-Step Waypoints:")
        for idx, step in enumerate(path):
            h_val = hospital.manhattan_distance(step)
            print(f"  Step {idx:2d} -> Grid Coordinate {step} (Heuristic to Goal: {h_val})")
    else:
        print("Error: No viable pathway exists between Pharmacy and Patient Ward.")
    print("==================================================================")


if __name__ == "__main__":
    main()
