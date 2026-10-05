<div align="center">

# 🧠 Artificial Intelligence Fundamentals
### Practical Laboratory Portfolio & Implementation Log

[![Language](https://img.shields.io/badge/Language-Python%203.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Curriculum](https://img.shields.io/badge/Curriculum-MIT--ADT%20SOAI-FF6F00?style=for-the-badge)](https://mituniversity.ac.in/)
[![Class](https://img.shields.io/badge/Division-Div%205%20%7C%20Roll%2009-7928CA?style=for-the-badge)](https://github.com/makarandbobhate)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)](https://github.com/makarandbobhate/AIF-Practicals)

<p align="center">
  A structured, modular laboratory repository illustrating fundamental-to-advanced paradigms of <b>Artificial Intelligence & Search Techniques</b> in modern Python, focusing on real-world systems modeling, clean code architecture, and autonomous intelligent agents.
</p>

</div>

---

## 📌 Student & Academic Profile

| Attribute | Details |
| :--- | :--- |
| **Candidate Name** | **Makarand Pankaj Bobhate** |
| **Roll Number** | `09` |
| **Institution** | **MIT ADT University** |
| **Department / Class** | School of AI (SO AI) |
| **Division** | Division 5 |
| **Course Module** | Artificial Intelligence Fundamentals (AI Fundamentals) |
| **Programming Language** | Python 3.x |

---

## 🎯 Curriculum Objectives & Competencies

This laboratory suite targets mastery over foundational artificial intelligence principles:
* **Uninformed State-Space Search:** Systematic graph exploration without heuristics using FIFO queue-based Breadth-First Search (BFS) and LIFO/recursive Depth-First Search (DFS) with backtracking.
* **Heuristic Optimization (A\*):** Informed search strategy combining path cost $g(n)$ with admissible Manhattan distance $h(n)$ to guarantee optimal shortest-path discovery.
* **Empirical Algorithm Benchmarking:** Quantitative evaluation of search strategies on identical road networks comparing path cost, search space expansion, and execution latency.
* **Deliberative Intelligent Agents (PEAS):** Designing autonomous mobile agents with dynamic environment sensing, internal world model updating, and real-time path re-planning.

---

## 📑 Lab Practicals Index

| Practical | Core AI Paradigm | Problem Statement & Specification | Code Source |
| :---: | :--- | :--- | :---: |
| **01** | **Breadth-First Search** | **Smart City Emergency Evacuation:** Identify nearest evacuation shelter during natural disasters by exploring road intersections level-by-level. | [`practical_01_bfs_evacuation.py`](./practical_01_bfs_evacuation.py) |
| **02** | **Depth-First Search** | **Treasure Hunt Game:** Navigate dungeon chambers completely down each branch before backtracking from dead ends to reach the goal. | [`practical_02_dfs_treasure_hunt.py`](./practical_02_dfs_treasure_hunt.py) |
| **03** | **Heuristic A\* Search** | **Hospital Medicine Delivery Robot:** Route an automated courier across an $8 \times 7$ hospital grid from Pharmacy to ICU using Manhattan heuristic. | [`practical_03_astar_hospital_robot.py`](./practical_03_astar_hospital_robot.py) |
| **04** | **Comparative Benchmarking** | **Smart City Road Navigation:** Multi-metric benchmark evaluating BFS, DFS, and A\* on path cost, nodes explored, and execution latency ($\mu s$). | [`practical_04_compare_search_algorithms.py`](./practical_04_compare_search_algorithms.py) |
| **05** | **Goal-Based Intelligent Agent** | **Autonomous Warehouse Robot:** Mobile agent adhering to PEAS framework, navigating storage-to-packing while autonomously evading dynamic obstacles. | [`practical_05_intelligent_warehouse_agent.py`](./practical_05_intelligent_warehouse_agent.py) |

---

## 🛠️ Build & Execution Instructions

All practical files are self-contained and require only standard Python 3.8+ (no third-party dependencies required).

### Prerequisites
* **Runtime:** Python 3.8 or higher (`python --version`)
* **Terminal:** PowerShell, Command Prompt, or Bash

### Execution Command

```bash
# General syntax
python "practical_<N>_<name>.py"

# Example: Run Practical 1
python practical_01_bfs_evacuation.py

# Run all practicals sequentially
python practical_01_bfs_evacuation.py && python practical_02_dfs_treasure_hunt.py && python practical_03_astar_hospital_robot.py && python practical_04_compare_search_algorithms.py && python practical_05_intelligent_warehouse_agent.py
```

---

## 📁 Repository Directory Structure

```text
AIF-Practicals/
├── .gitignore                                  # Ignores Python bytecode (__pycache__), virtualenvs, and IDE configs
├── README.md                                   # Comprehensive documentation and practical directory
├── practical_01_bfs_evacuation.py              # Practical 1: BFS Smart City Evacuation System
├── practical_02_dfs_treasure_hunt.py           # Practical 2: DFS Dungeon Treasure Hunt with Backtracking
├── practical_03_astar_hospital_robot.py        # Practical 3: A* Search Hospital AGV Medicine Delivery
├── practical_04_compare_search_algorithms.py   # Practical 4: Comparative Benchmarking (BFS vs DFS vs A*)
├── practical_05_intelligent_warehouse_agent.py  # Practical 5: Goal-Based Autonomous Warehouse AMR (PEAS)
├── makarand_bfs.py                             # Reference Script: 4-Level Filesystem BFS Traversal
├── makarand_dfs.py                             # Reference Script: Recursive Social Network DFS
└── makarand_astar.py                           # Reference Script: Basic 5-Node Graph Heuristic A*
```

---

<div align="center">

Developed & maintained by **[Makarand Bobhate](https://github.com/makarandbobhate)**<br>
<sub>Released for academic reference and software engineering practice.</sub>

</div>
