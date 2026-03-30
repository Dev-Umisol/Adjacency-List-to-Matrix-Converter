# 📁 Adjacency List to Matrix Converter

> A Python function that converts a graph from adjacency list representation to an adjacency matrix, built to understand the two core ways graphs are stored in memory.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Learning](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

This project was built directly after implementing Dijkstra's algorithm to deepen the understanding of how graphs are represented in memory. An adjacency list stores only existing edges as a dictionary of neighbor lists, compact but harder to query. An adjacency matrix stores all possible edges in a 2D grid, easier to query but uses more memory. This converter bridges the two, taking a dictionary and producing the equivalent matrix. Built to understand the trade-offs between graph representations and practice nested list construction.

---

## 🧠 What I Learned

- **Two graph representations and their trade-offs** — Adjacency lists are memory efficient for sparse graphs since they only store existing edges, while adjacency matrices use O(n²) space but allow O(1) edge lookup, understanding when to use each is a key computer science concept
- **Building a 2D matrix with nested list comprehensions** — Using `[[0 for col in range(n)] for row in range(n)]` to initialize an n×n grid of zeros in a single line, rather than nested for loops
- **Dictionary iteration with `.items()`** — Iterating over `k, v` pairs to access each node and its neighbor list, then marking `adj_matrix[k][neighbor] = 1` for every connection
- **Edge cases with isolated nodes** — Passing `{0: [], 1: [], 2: []}` confirms the function correctly produces an all zero matrix when no edges exist, without crashing or skipping nodes
- **Connecting this to Dijkstra's** — Recognizing that the adjacency matrix from this converter is the same format used as input to the shortest path algorithm, showing how these two projects fit together

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core language |

---

## 💡 How It Works

The function takes a dictionary where each key is a node and each value is a list of its neighbors. It builds an `n × n` matrix of zeros, then marks a `1` at `[row][col]` for every edge that exists.

```
Input (adjacency list):
{ 0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2] }

Output (adjacency matrix):
[0, 0, 1, 0]   ← node 0 connects to node 2
[0, 0, 1, 1]   ← node 1 connects to nodes 2 and 3
[1, 1, 0, 1]   ← node 2 connects to nodes 0, 1, and 3
[0, 1, 1, 0]   ← node 3 connects to nodes 1 and 2
```

**Example output:**
```python
adjacency_list_to_matrix({0: [1], 1: [0]})
# [0, 1]
# [1, 0]

adjacency_list_to_matrix({0: [], 1: [], 2: []})
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]
```

---

## 🚀 Future Improvements

- [ ] Add a reverse converter — `adjacency_matrix_to_list()` — to complete the two-way bridge
- [ ] Support weighted edges by storing the weight value instead of `1`
- [ ] Add a graph visualizer using `matplotlib` to render both representations side by side
- [ ] Connect directly to the Dijkstra's shortest path function to form a complete graph toolkit

---

## 📂 Project Structure

```
adjacency-converter/
│
├── AdjacencyListToMatrixConverter.py    # Converter function and example usage
└── README.md
```

---

*Part of my Python learning journey 🐍 — building a deeper understanding of graph theory and data representation*
