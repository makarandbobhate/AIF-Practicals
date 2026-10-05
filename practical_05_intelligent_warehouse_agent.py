"""
========================================================================================
MIT ADT University, Pune
School of AI (SO AI) | Division 5
Subject: Artificial Intelligence Fundamentals (AI Fundamentals)
----------------------------------------------------------------------------------------
Candidate Name : Makarand Pankaj Bobhate
Roll Number    : 09
GitHub Profile : https://github.com/makarandbobhate
Practical No.  : 05
Title          : Intelligent Agent Architecture - Autonomous Warehouse Mobile Robot
========================================================================================
Problem Statement:
An intelligent agent controls an autonomous mobile robot (AMR) in a fulfillment warehouse.
The agent must navigate from the Storage Bay (Start) to the Packing Station (Goal).

Agent Architecture (PEAS):
  - Performance Measure: Minimum steps/energy, zero collisions, timely delivery.
  - Environment        : 2D warehouse grid with static racks and dynamic unforeseen obstacles.
  - Actuators          : Drive motors (UP, DOWN, LEFT, RIGHT), package lifter.
  - Sensors            : Grid localization (current coordinates), forward proximity sensors.
  - Agent Function     : Goal-based deliberative agent with dynamic re-planning via A* Search.
"""

import heapq
from typing import List, Tuple, Dict, Set, Optional

# Grid cell definitions
OPEN = 0
RACK_OBSTACLE = 1
DYNAMIC_OBSTACLE = 2

class WarehouseEnvironment:
    """Simulates the physical warehouse floor and obstacle occurrences."""

    def __init__(self, rows: int, cols: int, static_racks: Set[Tuple[int, int]]) -> None:
        self.rows = rows
        self.cols = cols
        self.static_racks = static_racks
        self.dynamic_obstacles: Set[Tuple[int, int]] = set()

    def add_dynamic_obstacle(self, pos: Tuple[int, int]) -> None:
        self.dynamic_obstacles.add(pos)

    def is_blocked(self, pos: Tuple[int, int]) -> bool:
        r, c = pos
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return True
        return (pos in self.static_racks) or (pos in self.dynamic_obstacles)


class AutonomousWarehouseAgent:
    """
    Goal-Based Intelligent Agent.
    Maintains an internal world model and deliberates using A* heuristic search.
    """

    def __init__(
        self,
        start_pos: Tuple[int, int],
        goal_pos: Tuple[int, int],
        floor_shape: Tuple[int, int],
        known_obstacles: Set[Tuple[int, int]],
    ) -> None:
        # Internal World Model
        self.current_pos = start_pos
        self.goal_pos = goal_pos
        self.rows, self.cols = floor_shape
        self.known_obstacles = set(known_obstacles)

        # Agent operational states
        self.mission_complete = False
        self.steps_taken = 0
        self.planned_path: List[Tuple[int, int]] = []

    def manhattan_distance(self, pos: Tuple[int, int]) -> int:
        return abs(pos[0] - self.goal_pos[0]) + abs(pos[1] - self.goal_pos[1])

    def deliberate_search(self) -> Optional[List[Tuple[int, int]]]:
        """Deliberative component: A* Search over the internal world model."""
        start = self.current_pos
        goal = self.goal_pos

        open_set: List[Tuple[int, int, Tuple[int, int]]] = []
        heapq.heappush(open_set, (self.manhattan_distance(start), 0, start))

        g_scores: Dict[Tuple[int, int], int] = {start: 0}
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
        closed_set: Set[Tuple[int, int]] = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while open_set:
            f, current_g, current = heapq.heappop(open_set)

            if current in closed_set:
                continue
            closed_set.add(current)

            # Goal Test
            if current == goal:
                path: List[Tuple[int, int]] = []
                curr: Tuple[int, int] = current
                while curr in came_from:
                    path.append(curr)
                    curr = came_from[curr]
                path.append(start)
                path.reverse()
                return path

            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                neighbor = (nr, nc)

                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if neighbor not in self.known_obstacles:
                        tentative_g = current_g + 1
                        if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                            g_scores[neighbor] = tentative_g
                            f_score = tentative_g + self.manhattan_distance(neighbor)
                            came_from[neighbor] = current
                            heapq.heappush(open_set, (f_score, tentative_g, neighbor))

        return None

    def perceive_and_act(self, env: WarehouseEnvironment) -> str:
        """
        Sense-Plan-Act cycle:
        1. Sense environment (obstacle check along next waypoint)
        2. Update internal belief/model if unexpected obstruction is detected
        3. Deliberate / Re-plan if plan is invalidated
        4. Actuate motors to advance
        """
        if self.current_pos == self.goal_pos:
            self.mission_complete = True
            return "GOAL REACHED: Cargo successfully delivered to Packing Station."

        # If no plan exists or current plan was fully traversed, deliberate now
        if not self.planned_path or len(self.planned_path) <= 1:
            self.planned_path = self.deliberate_search()
            if not self.planned_path:
                return "FAIL: No viable path exists to the destination."

        next_step = self.planned_path[1]

        # SENSOR: Check obstruction ahead
        if env.is_blocked(next_step):
            self.known_obstacles.add(next_step)
            new_path = self.deliberate_search()
            if not new_path or len(new_path) < 2:
                return f"ALERT: Obstacle at {next_step}. Re-planning failed (No alternative path)!"
            self.planned_path = new_path
            next_step = self.planned_path[1]
            status_msg = f"[OBSTACLE DETECTED at {next_step}] -> Re-planning path!"
        else:
            status_msg = ""

        # ACTUATOR: Execute movement
        self.current_pos = next_step
        self.planned_path.pop(0)
        self.steps_taken += 1

        action_report = f"Agent moved to {self.current_pos} (Step #{self.steps_taken})"
        return f"{status_msg}\n  {action_report}" if status_msg else action_report


def print_warehouse_state(
    agent_pos: Tuple[int, int], goal_pos: Tuple[int, int], env: WarehouseEnvironment
) -> None:
    print("   " + " ".join(f"{c:2d}" for c in range(env.cols)))
    for r in range(env.rows):
        row_str = []
        for c in range(env.cols):
            cell = (r, c)
            if cell == agent_pos:
                row_str.append(" A")  # Agent
            elif cell == goal_pos:
                row_str.append(" G")  # Goal (Packing)
            elif cell in env.dynamic_obstacles:
                row_str.append(" X")  # Dynamic blockage
            elif cell in env.static_racks:
                row_str.append(" #")  # Static rack
            else:
                row_str.append(" .")
        print(f"{r:2d} " + " ".join(row_str))
    print("Legend: [A] Robot Agent | [G] Packing Goal | [#] Storage Rack | [X] Unexpected Obstacle\n")


def main() -> None:
    rows, cols = 8, 8
    start_storage = (0, 0)
    goal_packing = (7, 7)

    # Static warehouse storage racks
    static_racks = {
        (1, 1), (1, 2), (1, 3), (1, 5), (1, 6),
        (3, 1), (3, 2), (3, 4), (3, 5),
        (5, 2), (5, 3), (5, 5), (5, 6)
    }

    env = WarehouseEnvironment(rows, cols, static_racks)
    agent = AutonomousWarehouseAgent(start_storage, goal_packing, (rows, cols), static_racks)

    print("==================================================================")
    print(" INTELLIGENT AGENT SYSTEM: AUTONOMOUS WAREHOUSE ROBOT (AIF LAB)   ")
    print("==================================================================")
    print("PEAS Formal Specification:")
    print(" - Performance Measure: Minimum moves, zero collisions, task completion")
    print(" - Environment        : 8x8 grid warehouse with aisles and static racks")
    print(" - Actuators          : Drive motors, payload lifter")
    print(" - Sensors            : Coordinate odometry, forward obstacle sensor\n")

    print(f"Origin Position (Storage Bay)      : {start_storage}")
    print(f"Goal Destination (Packing Station) : {goal_packing}\n")
    print("Initial Warehouse Layout:")
    print_warehouse_state(agent.current_pos, goal_packing, env)

    # Simulation cycle
    cycle = 0
    while not agent.mission_complete and cycle < 30:
        cycle += 1

        # Dynamic disturbance event: At cycle 4, fallen cargo blocks (3, 3)
        if cycle == 4:
            print("\n>>> [ENVIRONMENT EVENT] Sudden obstacle appeared at (3, 3)! <<<\n")
            env.add_dynamic_obstacle((3, 3))

        result = agent.perceive_and_act(env)
        print(f"[Cycle {cycle:2d}] {result}")

    print("\n--- Final Mission Summary ---")
    print_warehouse_state(agent.current_pos, goal_packing, env)
    print(f"Total Traversal Steps Executed: {agent.steps_taken}")
    print(f"Mission Status                 : {'SUCCESS' if agent.mission_complete else 'INCOMPLETE'}")
    print("==================================================================")


if __name__ == "__main__":
    main()
