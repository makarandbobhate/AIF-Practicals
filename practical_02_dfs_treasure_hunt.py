"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Practical No.  : 02
Title          : Depth First Search (DFS) - Treasure Hunt Game with Backtracking
========================================================================================
Problem Statement:
A player explores a complex dungeon/cave network to locate hidden treasure.
The player explores each corridor completely down to its deepest chamber before
backtracking to explore untried alternate passages. DFS is implemented with
explicit path tracking and backtrack logging.
"""

from typing import Dict, List, Set, Optional, Tuple

class TreasureHuntDungeon:
    """Graph model representing dungeon chambers and connecting passageways."""

    def __init__(self) -> None:
        self.passageways: Dict[str, List[str]] = {}

    def add_passage(self, room1: str, room2: str) -> None:
        """Add bidirectional passageway between two chambers."""
        if room1 not in self.passageways:
            self.passageways[room1] = []
        if room2 not in self.passageways:
            self.passageways[room2] = []
        self.passageways[room1].append(room2)
        self.passageways[room2].append(room1)

    def find_treasure_dfs(
        self, start_room: str, treasure_room: str
    ) -> Tuple[Optional[List[str]], List[str]]:
        """
        Executes recursive Depth First Search (DFS) to locate the treasure.
        
        Returns:
            - path: Reconstructed list of chambers from start to treasure.
            - trace_log: Detailed step-by-step exploration and backtracking log.
        """
        visited: Set[str] = set()
        trace_log: List[str] = []
        path: List[str] = []

        def dfs_recursive(current: str) -> bool:
            visited.add(current)
            path.append(current)
            trace_log.append(f"EXPLORE  -> Chamber: '{current}' (Current Stack Depth: {len(path)})")

            # Goal Test
            if current == treasure_room:
                trace_log.append(f"SUCCESS  -> Treasure Chamber '{current}' discovered!")
                return True

            for neighbor in self.passageways.get(current, []):
                if neighbor not in visited:
                    if dfs_recursive(neighbor):
                        return True
                    else:
                        trace_log.append(
                            f"BACKTRACK<- Dead end at '{neighbor}'. Backtracking to '{current}'"
                        )

            # Backtrack if all branches from current room are exhausted
            path.pop()
            return False

        found = dfs_recursive(start_room)
        return (path if found else None), trace_log


def main() -> None:
    dungeon = TreasureHuntDungeon()

    # Chamber network layout with branches and dead-ends
    passages = [
        ("Dungeon_Entrance", "Hall_of_Whispers"),
        ("Dungeon_Entrance", "Sunken_Grotto"),
        ("Hall_of_Whispers", "Crypt_of_Shadows"),
        ("Crypt_of_Shadows", "Skeleton_Pit"),      # Dead end
        ("Hall_of_Whispers", "Armory"),
        ("Armory", "Cursed_Vault"),                # Dead end
        ("Sunken_Grotto", "Crystal_Cavern"),
        ("Crystal_Cavern", "Underground_Lake"),
        ("Underground_Lake", "Treasure_Chamber"),  # Target Goal
        ("Crystal_Cavern", "Collapsed_Tunnel")     # Dead end
    ]

    for r1, r2 in passages:
        dungeon.add_passage(r1, r2)

    start = "Dungeon_Entrance"
    goal = "Treasure_Chamber"

    print("==================================================================")
    print("      TREASURE HUNT GAME - DUNGEON PATHFINDER (DFS)              ")
    print("==================================================================")
    print(f"Origin (Dungeon Gate): {start}")
    print(f"Target (Treasure)    : {goal}\n")

    path, logs = dungeon.find_treasure_dfs(start, goal)

    print("--- DFS Exploration & Backtracking Trace ---")
    for log in logs:
        print(log)

    print("\n--- Final Exploration Summary ---")
    if path:
        print("Treasure successfully located!")
        print(f"Total Traversal Depth: {len(path)} chambers")
        print(f"Discovered Path      : {' -> '.join(path)}")
    else:
        print("No route found leading to the treasure chamber.")
    print("==================================================================")


if __name__ == "__main__":
    main()
