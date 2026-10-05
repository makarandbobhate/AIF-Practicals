"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Practical No.  : 01
Title          : Breadth First Search (BFS) - Smart City Emergency Evacuation
========================================================================================
Problem Statement:
During a natural disaster, an emergency response system must identify the nearest
evacuation center by exploring all connected roads level-by-level. Breadth First
Search (BFS) guarantees finding the shortest unweighted route (minimum road hops).
"""

from collections import deque
from typing import Dict, List, Set, Tuple, Optional

class SmartCityEvacuationNetwork:
    """Graph representation of city road intersections and evacuation shelters."""

    def __init__(self) -> None:
        self.adj_list: Dict[str, List[str]] = {}
        self.evacuation_centers: Set[str] = set()

    def add_road(self, u: str, v: str) -> None:
        """Add bidirectional road connection between intersections u and v."""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def mark_evacuation_center(self, center: str) -> None:
        """Designate an intersection/node as an emergency evacuation shelter."""
        self.evacuation_centers.add(center)

    def find_nearest_evacuation_route(
        self, start_node: str
    ) -> Tuple[Optional[List[str]], Optional[str], List[Tuple[str, int]]]:
        """
        Executes Breadth First Search (BFS) level-by-level from start_node.
        
        Returns:
            - shortest_path: Ordered list of nodes from start to nearest shelter.
            - target_center: Name of the evacuation center reached.
            - traversal_order: List of (node, depth_level) visited during exploration.
        """
        if start_node not in self.adj_list:
            return None, None, []

        # Trivial case: Start location is already an evacuation shelter
        if start_node in self.evacuation_centers:
            return [start_node], start_node, [(start_node, 0)]

        # Queue stores: (current_node, depth_level)
        queue = deque([(start_node, 0)])
        visited: Set[str] = {start_node}
        parent: Dict[str, Optional[str]] = {start_node: None}
        traversal_order: List[Tuple[str, int]] = []
        found_center: Optional[str] = None

        while queue:
            current, level = queue.popleft()
            traversal_order.append((current, level))

            # Goal Test
            if current in self.evacuation_centers:
                found_center = current
                break

            # Explore neighbors level-by-level
            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append((neighbor, level + 1))

        if not found_center:
            return None, None, traversal_order

        # Reconstruct optimal path via parent pointers
        path: List[str] = []
        curr: Optional[str] = found_center
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

        return path, found_center, traversal_order


def main() -> None:
    city = SmartCityEvacuationNetwork()

    # Network topology: Intersections & connecting roads
    roads = [
        ("Sector_4_Residential", "Junction_A"),
        ("Sector_4_Residential", "Junction_B"),
        ("Junction_A", "Central_Avenue"),
        ("Junction_B", "Market_Square"),
        ("Junction_B", "River_Bridge"),
        ("Central_Avenue", "Stadium_Shelter"),     # Shelter 1
        ("Market_Square", "High_School_Gym"),      # Shelter 2
        ("River_Bridge", "South_Camp"),            # Shelter 3
        ("Central_Avenue", "North_Expressway"),
        ("North_Expressway", "Airport_Hangar")     # Shelter 4
    ]

    for u, v in roads:
        city.add_road(u, v)

    shelters = ["Stadium_Shelter", "High_School_Gym", "South_Camp", "Airport_Hangar"]
    for s in shelters:
        city.mark_evacuation_center(s)

    danger_zone = "Sector_4_Residential"
    print("==================================================================")
    print("  SMART CITY EMERGENCY EVACUATION SYSTEM (BFS ROUTE FINDER)       ")
    print("==================================================================")
    print(f"Origin (Hazard Area): {danger_zone}")
    print(f"Designated Shelters : {shelters}\n")

    path, center, traversal = city.find_nearest_evacuation_route(danger_zone)

    print("--- BFS Traversal Sequence (Level-by-Level Exploration) ---")
    for node, level in traversal:
        tag = " [GOAL REACHED]" if node == center else ""
        print(f"Level {level}: Explored node '{node}'{tag}")

    print("\n--- Evacuation Result ---")
    if path and center:
        print(f"Nearest Evacuation Center Found: {center}")
        print(f"Total Road Hops (Distance)     : {len(path) - 1}")
        print(f"Safest Evacuation Route        : {' -> '.join(path)}")
    else:
        print("No reachable evacuation center found!")
    print("==================================================================")


if __name__ == "__main__":
    main()
