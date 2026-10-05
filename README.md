<div align="center">

# 🧠 Artificial Intelligence Fundamentals (AIF)
### Practical Implementations & Real-World Problem Solving

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](#)
[![Institution](https://img.shields.io/badge/Institution-MIT_ADT_University-orange.svg)](#)
[![Department](https://img.shields.io/badge/Department-School_of_AI-blueviolet.svg)](#)
[![Lab Status](https://img.shields.io/badge/Practicals-Complete_%26_Verified-brightgreen.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

A curated laboratory repository featuring production-grade Python implementations of classical and modern Artificial Intelligence search algorithms, heuristic evaluation, performance benchmarking, and autonomous goal-based intelligent agents.

---

</div>

## 🎓 Academic & Student Profile

| Field | Details |
| :--- | :--- |
| **Candidate Name** | **Makarand Pankaj Bobhate** |
| **Roll Number** | **09** |
| **Class / Department** | **School of AI (SO AI)** |
| **Division** | **Division 5** |
| **Institution** | **MIT ADT University, Pune** |
| **Subject** | **Artificial Intelligence Fundamentals (AI Fundamentals)** |
| **GitHub Profile** | [@makarandbobhate](https://github.com/makarandbobhate) |

---

## 🎯 Key AI Competencies Covered

1. **Uninformed Search Strategies (Blind Search):**
   - **Breadth-First Search (BFS):** FIFO queue-based exploration, guarantees shortest path on unweighted graphs, level-by-level evaluation.
   - **Depth-First Search (DFS):** LIFO stack/recursion-based deep traversal, space-efficient backtracking, reachability in search spaces with dead ends.

2. **Informed (Heuristic) Search:**
   - **A\* Search Algorithm:** Combines path-so-far cost $g(n)$ with admissible heuristic estimate $h(n)$ using Manhattan Distance $h(n) = |x_1 - x_2| + |y_1 - y_2|$ to guarantee optimal pathfinding with minimized node expansions.

3. **Algorithm Benchmarking & Comparative Analysis:**
   - Quantitative evaluation of BFS, DFS, and A\* on an identical road network topology measuring:
     - Path optimality (distance cost)
     - Search space complexity (nodes explored)
     - Wall-clock compute latency (execution time in microseconds)

4. **Intelligent Agent Architecture (PEAS Framework):**
   - Design of a **Goal-Based Deliberative Agent** operating in a dynamic grid environment with:
     - **P**erformance measure, **E**nvironment, **A**ctuators, and **S**ensors.
     - Perception-Action cycle, internal world model updating, and real-time obstacle evasion with dynamic A\* re-planning.

---

## 📂 Laboratory Practicals Index

| No. | Core Question | Applied Scenario / Real-World Problem | Key Concept | Source File |
| :---: | :--- | :--- | :--- | :---: |
| **01** | Graph Traversal using BFS | **Smart City Emergency Evacuation:** Finds the nearest evacuation shelter from a disaster zone level-by-level. | BFS, Queue, Shortest Path | [practical_01_bfs_evacuation.py](./practical_01_bfs_evacuation.py) |
| **02** | Pathfinding using DFS | **Treasure Hunt Game:** Explores dungeon chambers to maximum depth before backtracking out of dead ends. | DFS, Backtracking, Recursion | [practical_02_dfs_treasure_hunt.py](./practical_02_dfs_treasure_hunt.py) |
| **03** | A\* with Manhattan Distance | **Hospital Medicine Delivery Robot:** Navigates floor corridors to deliver medicine to an ICU ward avoiding partitions. | A\* Search, Priority Queue, Heuristics | [practical_03_astar_hospital_robot.py](./practical_03_astar_hospital_robot.py) |
| **04** | Compare BFS, DFS, & A\* | **Smart City Road Navigation:** Benchmarks route optimality, search space, and latency on an identical graph. | Algorithm Benchmarking, Performance Profiling | [practical_04_compare_search_algorithms.py](./practical_04_compare_search_algorithms.py) |
| **05** | Intelligent Goal-Based Agent | **Autonomous Warehouse Robot:** Mobile agent with dynamic sensor feedback and real-time path re-planning. | PEAS, Sense-Plan-Act, Deliberative Agent | [practical_05_intelligent_warehouse_agent.py](./practical_05_intelligent_warehouse_agent.py) |

### 📑 Foundational Reference Implementations
- [makarand_bfs.py](./makarand_bfs.py) — Core 4-level filesystem directory traversal using BFS.
- [makarand_dfs.py](./makarand_dfs.py) — Adjacency list social graph traversal using recursive DFS.
- [makarand_astar.py](./makarand_astar.py) — 5-node weighted graph pathfinding using basic A\* search.

---

## 🌳 Repository Directory Structure

```text
AIF-Practicals/
├── .gitignore                                  # Git ignore rules for Python & build artifacts
├── README.md                                   # Comprehensive lab documentation & index
├── practical_01_bfs_evacuation.py              # Practical 1: BFS Smart City Evacuation
├── practical_02_dfs_treasure_hunt.py           # Practical 2: DFS Treasure Hunt with Backtracking
├── practical_03_astar_hospital_robot.py        # Practical 3: A* Search Hospital Robot Navigation
├── practical_04_compare_search_algorithms.py   # Practical 4: Comparative Benchmark (BFS vs DFS vs A*)
├── practical_05_intelligent_warehouse_agent.py  # Practical 5: Goal-Based Autonomous Warehouse Agent
├── makarand_bfs.py                             # Reference BFS script
├── makarand_dfs.py                             # Reference DFS script
└── makarand_astar.py                           # Reference A* script
```

---

## 🚀 Setup & Execution Guide

### Prerequisites
- Python 3.8 or higher installed on your system.
- Standard Library only (All practicals use built-in Python modules: `heapq`, `collections`, `time`, `typing`). No external `pip` dependencies required!

### 1. Clone the Repository
```bash
git clone https://github.com/makarandbobhate/AIF-Practicals.git
cd AIF-Practicals
```

### 2. (Optional) Create Virtual Environment
```bash
# Windows (PowerShell / Command Prompt)
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Run the Practicals

#### ▶ Run Practical 1 (BFS - Smart City Evacuation)
```bash
python practical_01_bfs_evacuation.py
```

#### ▶ Run Practical 2 (DFS - Dungeon Treasure Hunt)
```bash
python practical_02_dfs_treasure_hunt.py
```

#### ▶ Run Practical 3 (A\* - Hospital Medicine Robot)
```bash
python practical_03_astar_hospital_robot.py
```

#### ▶ Run Practical 4 (Algorithm Benchmark: BFS vs DFS vs A\*)
```bash
python practical_04_compare_search_algorithms.py
```

#### ▶ Run Practical 5 (Intelligent Warehouse Agent with Re-planning)
```bash
python practical_05_intelligent_warehouse_agent.py
```

---

## 📊 Sample Benchmark Results (Practical 4)

Benchmarked on an identical 8-node smart city road network:

| Algorithm | Discovered Route | Path Cost (km) | Nodes Explored | Optimality Verdict |
| :--- | :--- | :---: | :---: | :--- |
| **BFS** | Tech_Park $\rightarrow$ Cyber_Hub $\rightarrow$ City_Square $\rightarrow$ Terminal_Airport | 12.30 km | 7 | Guarantees minimum hops, not minimum distance. |
| **DFS** | Tech_Park $\rightarrow$ Cyber_Hub $\rightarrow$ North_Ring $\rightarrow$ City_Square $\rightarrow$ Terminal_Airport | 15.70 km | 8 | Sub-optimal, explores arbitrarily deep paths. |
| **A\*** | Tech_Park $\rightarrow$ Metro_Central $\rightarrow$ South_Plaza $\rightarrow$ East_Gate $\rightarrow$ Terminal_Airport | **14.00 km** | **5** | **Optimal distance with minimal search space.** |

---

## 👤 Author & Academic Citation
**Makarand Pankaj Bobhate**  
Roll No: 09 | Division: 5  
School of Artificial Intelligence (SO AI), MIT ADT University, Pune  
GitHub: [@makarandbobhate](https://github.com/makarandbobhate)

---
*Developed for the academic coursework of Artificial Intelligence Fundamentals (Python).*
