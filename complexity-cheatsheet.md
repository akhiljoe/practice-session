# Data Structures & Algorithms — Time and Space Complexity Cheatsheet

> All complexities expressed in **Big O notation**.
> $n$ = number of elements · $V$ = vertices · $E$ = edges · $h$ = tree height · $k$ = key range or digit count.

---

## Table of Contents

1. [Data Structures](#1-data-structures)
2. [Sorting Algorithms](#2-sorting-algorithms)
3. [Search Algorithms](#3-search-algorithms)
4. [Graph Algorithms](#4-graph-algorithms)
5. [Tree Traversals](#5-tree-traversals)
6. [String Algorithms](#6-string-algorithms)
7. [Dynamic Programming Patterns](#7-dynamic-programming-patterns)
8. [Quick Reference — Complexity Classes](#8-quick-reference--complexity-classes)

---

## 1. Data Structures

---

### Arrays

> Fixed-size contiguous memory block. Index-based $O(1)$ access is the primary advantage.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(1)$       | $O(1)$     |
| Search    | $O(n)$       | $O(n)$     |
| Insertion | $O(n)$       | $O(n)$     |
| Deletion  | $O(n)$       | $O(n)$     |

**Space Complexity:** $O(n)$

---

### Singly Linked List

> Sequential nodes, each holding a value and a pointer to the next node. No random access.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(n)$       | $O(n)$     |
| Search    | $O(n)$       | $O(n)$     |
| Insertion | $O(1)$       | $O(1)$     |
| Deletion  | $O(1)$       | $O(1)$     |

> Insertion/Deletion is $O(1)$ **given a pointer to the node**; finding that node is $O(n)$.

**Space Complexity:** $O(n)$

---

### Doubly Linked List

> Each node holds pointers to both the next and previous nodes, enabling bidirectional traversal.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(n)$       | $O(n)$     |
| Search    | $O(n)$       | $O(n)$     |
| Insertion | $O(1)$       | $O(1)$     |
| Deletion  | $O(1)$       | $O(1)$     |

**Space Complexity:** $O(n)$

---

### Circular Linked List

> Last node links back to the head. Variants: singly or doubly circular. Traversal can loop indefinitely without a sentinel.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(n)$       | $O(n)$     |
| Search    | $O(n)$       | $O(n)$     |
| Insertion | $O(1)$       | $O(1)$     |
| Deletion  | $O(1)$       | $O(1)$     |

**Space Complexity:** $O(n)$

---

### Stack

> LIFO structure. Typically implemented with an array or linked list. All core operations act on the top.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(n)$       | $O(n)$     |
| Search    | $O(n)$       | $O(n)$     |
| Push      | $O(1)$       | $O(1)$     |
| Pop       | $O(1)$       | $O(1)$     |

**Space Complexity:** $O(n)$

---

### Queue / Deque

> **Queue:** FIFO — enqueue at rear, dequeue from front.
> **Deque (double-ended queue):** supports $O(1)$ insertion and deletion at both ends.
> Both are typically implemented with a circular array or doubly linked list.

| Operation           | Average Case | Worst Case |
|---------------------|:------------:|:----------:|
| Access              | $O(n)$       | $O(n)$     |
| Search              | $O(n)$       | $O(n)$     |
| Enqueue / Push Front/Back | $O(1)$ | $O(1)$     |
| Dequeue / Pop Front/Back  | $O(1)$ | $O(1)$     |

**Space Complexity:** $O(n)$

---

### Hash Table

> Maps keys to values via a hash function. Performance degrades with collisions (chaining or open addressing).

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(1)$       | $O(n)$     |
| Search    | $O(1)$       | $O(n)$     |
| Insertion | $O(1)$       | $O(n)$     |
| Deletion  | $O(1)$       | $O(n)$     |

> Worst case $O(n)$ arises from hash collisions causing all keys to hash to the same bucket.

**Space Complexity:** $O(n)$

---

### Binary Search Tree (BST)

> Left subtree values < node < right subtree values. Performance depends heavily on balance.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Access    | $O(\log n)$  | $O(n)$     |
| Search    | $O(\log n)$  | $O(n)$     |
| Insertion | $O(\log n)$  | $O(n)$     |
| Deletion  | $O(\log n)$  | $O(n)$     |

> Worst case $O(n)$ occurs on a degenerate tree (e.g., sorted insertion → linked list shape).

**Space Complexity:** $O(n)$

---

### AVL Tree

> Self-balancing BST. Maintains a balance factor of $\{-1, 0, 1\}$ at every node via rotations, guaranteeing $O(\log n)$ height.

| Operation | Average Case | Worst Case  |
|-----------|:------------:|:-----------:|
| Access    | $O(\log n)$  | $O(\log n)$ |
| Search    | $O(\log n)$  | $O(\log n)$ |
| Insertion | $O(\log n)$  | $O(\log n)$ |
| Deletion  | $O(\log n)$  | $O(\log n)$ |

**Space Complexity:** $O(n)$

---

### Red-Black Tree

> Self-balancing BST with color-based invariants. Fewer rotations than AVL on insertion-heavy workloads. Used in `std::map` (C++), `TreeMap` (Java).

| Operation | Average Case | Worst Case  |
|-----------|:------------:|:-----------:|
| Access    | $O(\log n)$  | $O(\log n)$ |
| Search    | $O(\log n)$  | $O(\log n)$ |
| Insertion | $O(\log n)$  | $O(\log n)$ |
| Deletion  | $O(\log n)$  | $O(\log n)$ |

**Space Complexity:** $O(n)$

---

### B-Tree (order $m$)

> Generalized BST allowing nodes to hold up to $m-1$ keys. Optimized for disk I/O; used in databases and file systems.

| Operation | Average Case | Worst Case  |
|-----------|:------------:|:-----------:|
| Access    | $O(\log n)$  | $O(\log n)$ |
| Search    | $O(\log n)$  | $O(\log n)$ |
| Insertion | $O(\log n)$  | $O(\log n)$ |
| Deletion  | $O(\log n)$  | $O(\log n)$ |

**Space Complexity:** $O(n)$

---

### Heap (Binary — Min/Max)

> Complete binary tree satisfying the heap property. Stored in an array. Does **not** support efficient arbitrary-key search.

| Operation          | Average Case | Worst Case  |
|--------------------|:------------:|:-----------:|
| Access (peek)      | $O(1)$       | $O(1)$      |
| Search             | $O(n)$       | $O(n)$      |
| Insertion          | $O(1)$\*     | $O(\log n)$ |
| Deletion (extract) | $O(\log n)$  | $O(\log n)$ |
| Heapify (build)    | $O(n)$       | $O(n)$      |

> \* Amortized $O(1)$ insert; worst-case is $O(\log n)$ when a full sift-up traverses the entire height.

**Space Complexity:** $O(n)$

---

### Trie (Prefix Tree)

> Tree where each node represents a character. All descendants share a common prefix. Commonly used for autocomplete and prefix search. $L$ = length of the key.

| Operation | Average Case | Worst Case |
|-----------|:------------:|:----------:|
| Search    | $O(L)$       | $O(L)$     |
| Insertion | $O(L)$       | $O(L)$     |
| Deletion  | $O(L)$       | $O(L)$     |
| Prefix Check | $O(L)$    | $O(L)$     |

**Space Complexity:** $O(n \cdot L)$ — where $n$ = number of keys, $L$ = average key length. Much higher constant than a hash table due to per-character node overhead.

---

### Disjoint Set / Union-Find (DSU)

> Tracks a partition of elements into disjoint sets. Supports near-constant-time union and find with **path compression + union by rank**. $\alpha(n)$ = inverse Ackermann function (effectively constant for all practical $n$).

| Operation    | Amortized (with optimizations) |
|--------------|:------------------------------:|
| Find         | $O(\alpha(n))$                 |
| Union        | $O(\alpha(n))$                 |
| Connected?   | $O(\alpha(n))$                 |

> Without path compression/union by rank: Find and Union are $O(\log n)$; naive is $O(n)$.

**Space Complexity:** $O(n)$

---

### Segment Tree

> Binary tree over an array that enables efficient range queries and point/range updates. $n$ = array size.

| Operation           | Time Complexity |
|---------------------|:---------------:|
| Build               | $O(n)$          |
| Range Query         | $O(\log n)$     |
| Point Update        | $O(\log n)$     |
| Range Update (lazy) | $O(\log n)$     |

**Space Complexity:** $O(n)$ (tree stored in array of size $\approx 4n$)

---

### Fenwick Tree (Binary Indexed Tree — BIT)

> Array-based structure supporting prefix sum queries and point updates. Simpler and more cache-friendly than a Segment Tree but supports fewer query types.

| Operation      | Time Complexity |
|----------------|:---------------:|
| Build          | $O(n \log n)$   |
| Prefix Query   | $O(\log n)$     |
| Point Update   | $O(\log n)$     |

**Space Complexity:** $O(n)$

> Use a **Segment Tree** when you need range updates or more complex queries. Use a **Fenwick Tree** when only prefix sums and point updates are needed — it has lower constant factors and is easier to implement.

---

### Graph — Adjacency List

> Each vertex stores a list of its neighbours. Space-efficient for sparse graphs.

| Operation          | Average Case         | Worst Case   |
|--------------------|:--------------------:|:------------:|
| Add Vertex         | $O(1)$               | $O(1)$       |
| Add Edge           | $O(1)$               | $O(1)$       |
| Remove Vertex      | $O(V + E)$           | $O(V + E)$   |
| Remove Edge        | $O(E)$               | $O(E)$       |
| Query Edge (u → v) | $O(\text{deg}(u))$   | $O(V)$       |

**Space Complexity:** $O(V + E)$

---

### Graph — Adjacency Matrix

> $V \times V$ boolean/weight matrix. $O(1)$ edge lookup at the cost of $O(V^2)$ space regardless of edge count.

| Operation          | Average Case | Worst Case   |
|--------------------|:------------:|:------------:|
| Add Vertex         | $O(V^2)$     | $O(V^2)$     |
| Add Edge           | $O(1)$       | $O(1)$       |
| Remove Vertex      | $O(V^2)$     | $O(V^2)$     |
| Remove Edge        | $O(1)$       | $O(1)$       |
| Query Edge (u → v) | $O(1)$       | $O(1)$       |

**Space Complexity:** $O(V^2)$

---

## 2. Sorting Algorithms

| Algorithm      | Best Case      | Average Case    | Worst Case      | Space (Avg)    | Space (Worst)  | Stable? |
|----------------|:--------------:|:---------------:|:---------------:|:--------------:|:--------------:|:-------:|
| Bubble Sort    | $O(n)$         | $O(n^2)$        | $O(n^2)$        | $O(1)$         | $O(1)$         | ✅      |
| Selection Sort | $O(n^2)$       | $O(n^2)$        | $O(n^2)$        | $O(1)$         | $O(1)$         | ❌      |
| Insertion Sort | $O(n)$         | $O(n^2)$        | $O(n^2)$        | $O(1)$         | $O(1)$         | ✅      |
| Merge Sort     | $O(n \log n)$  | $O(n \log n)$   | $O(n \log n)$   | $O(n)$         | $O(n)$         | ✅      |
| Quick Sort     | $O(n \log n)$  | $O(n \log n)$   | $O(n^2)$        | $O(\log n)$    | $O(n)$         | ❌      |
| Heap Sort      | $O(n \log n)$  | $O(n \log n)$   | $O(n \log n)$   | $O(1)$         | $O(1)$         | ❌      |
| Radix Sort     | $O(nk)$        | $O(nk)$         | $O(nk)$         | $O(n + k)$     | $O(n + k)$     | ✅      |
| Counting Sort  | $O(n + k)$     | $O(n + k)$      | $O(n + k)$      | $O(k)$         | $O(k)$         | ✅      |
| Tim Sort       | $O(n)$         | $O(n \log n)$   | $O(n \log n)$   | $O(n)$         | $O(n)$         | ✅      |

> **Notes:**
> - $k$ in Radix Sort = number of digits; $k$ in Counting Sort = range of input values.
> - Quick Sort worst case ($O(n^2)$) occurs with a poorly chosen pivot (e.g., always min/max on a sorted input). Randomized pivot mitigates this. Worst-case stack space is $O(n)$ due to unbalanced recursion.
> - Merge Sort's $O(n)$ space is due to the auxiliary merge buffer.
> - Heap Sort is in-place but not cache-friendly; slower in practice than Quick Sort despite identical asymptotic guarantees.
> - Tim Sort (Python's `sorted()`, Java's `Arrays.sort` for objects) is a hybrid Merge + Insertion Sort optimized for real-world data.

---

## 3. Search Algorithms

| Algorithm        | Best Case    | Average Case | Worst Case   | Space      | Requirement             |
|------------------|:------------:|:------------:|:------------:|:----------:|-------------------------|
| Linear Search    | $O(1)$       | $O(n)$       | $O(n)$       | $O(1)$     | None                    |
| Binary Search    | $O(1)$       | $O(\log n)$  | $O(\log n)$  | $O(1)$     | Sorted array            |
| Binary Search (recursive) | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | Sorted array + call stack |
| Jump Search      | $O(1)$       | $O(\sqrt{n})$| $O(\sqrt{n})$| $O(1)$     | Sorted array            |
| Interpolation Search | $O(1)$   | $O(\log \log n)$ | $O(n)$  | $O(1)$     | Sorted + uniformly distributed |
| Exponential Search | $O(1)$     | $O(\log n)$  | $O(\log n)$  | $O(1)$     | Sorted array            |

> **Notes:**
> - Binary Search is the standard; know both iterative ($O(1)$ space) and recursive ($O(\log n)$ stack space) forms.
> - Interpolation Search degrades to $O(n)$ on skewed distributions — rarely used in practice.
> - Exponential Search is useful when the array size is unknown (e.g., unbounded/infinite arrays).

---

## 4. Graph Algorithms

### Traversal & Basic

| Algorithm          | Time Complexity | Space Complexity | Use Case                                                 |
|--------------------|:---------------:|:----------------:|----------------------------------------------------------|
| BFS                | $O(V + E)$      | $O(V)$           | Shortest path (unweighted), level-order, connected components |
| DFS                | $O(V + E)$      | $O(V)$           | Cycle detection, topological sort, connected components  |

> With adjacency matrix: both BFS and DFS become $O(V^2)$.

---

### Shortest Path

| Algorithm      | Time Complexity              | Space Complexity | Notes                                                             |
|----------------|:----------------------------:|:----------------:|-------------------------------------------------------------------|
| BFS            | $O(V + E)$                   | $O(V)$           | Unweighted graphs only                                            |
| Dijkstra's     | $O((V + E) \log V)$          | $O(V)$           | Non-negative edge weights only · binary min-heap implementation   |
| Dijkstra's (Fibonacci heap) | $O(E + V \log V)$ | $O(V)$  | Theoretically optimal; complex to implement                       |
| Bellman-Ford   | $O(VE)$                      | $O(V)$           | Handles negative edge weights · detects negative weight cycles    |
| Floyd-Warshall | $O(V^3)$                     | $O(V^2)$         | All-pairs shortest path (APSP) · works with negative weights (no negative cycles) |
| A\*            | $O(E)$ (best) / $O(b^d)$ (worst) | $O(V)$      | Heuristic-guided · optimal when heuristic is admissible           |

> - **Bellman-Ford:** runs $V-1$ relaxation passes; the $V$-th pass detects negative weight cycles.
> - **Floyd-Warshall:** DP on all vertex pairs; use when $V \leq 500$ and all-pairs paths are needed.
> - **A\*:** $b$ = branching factor, $d$ = depth of optimal solution. Performance is heuristic-dependent.

---

### Minimum Spanning Tree

| Algorithm   | Time Complexity          | Space Complexity | Notes                                                            |
|-------------|:------------------------:|:----------------:|------------------------------------------------------------------|
| Kruskal's   | $O(E \log E)$            | $O(V)$           | Sort edges + Union-Find · better for sparse graphs               |
| Prim's (min-heap) | $O((V + E) \log V)$ | $O(V)$          | Greedy expansion · better for dense graphs                       |
| Prim's (array)    | $O(V^2)$            | $O(V)$          | Simpler implementation; preferred when $E \approx V^2$           |

> Kruskal's $O(E \log E)$ is dominated by sorting; Union-Find operations are near-constant with path compression + union by rank.

---

### Topological Sort

| Algorithm         | Time Complexity | Space Complexity | Notes                                              |
|-------------------|:---------------:|:----------------:|----------------------------------------------------|
| Kahn's (BFS)      | $O(V + E)$      | $O(V)$           | Iterative · detects cycles if not all nodes processed |
| DFS-based         | $O(V + E)$      | $O(V)$           | Recursive · post-order push to stack               |

---

### Strongly Connected Components (SCC)

| Algorithm    | Time Complexity | Space Complexity | Notes                                        |
|--------------|:---------------:|:----------------:|----------------------------------------------|
| Tarjan's     | $O(V + E)$      | $O(V)$           | Single DFS pass · uses low-link values       |
| Kosaraju's   | $O(V + E)$      | $O(V)$           | Two DFS passes · simpler to understand       |

---

## 5. Tree Traversals

> All traversals below are for a binary tree with $n$ nodes.
> Recursive implementations use $O(h)$ call stack space; $h = O(\log n)$ for balanced trees, $O(n)$ for degenerate trees.

| Traversal            | Time Complexity | Space (Recursive) | Space (Iterative) |
|----------------------|:---------------:|:-----------------:|:-----------------:|
| Inorder (L → N → R)  | $O(n)$          | $O(h)$            | $O(h)$            |
| Preorder (N → L → R) | $O(n)$          | $O(h)$            | $O(h)$            |
| Postorder (L → R → N)| $O(n)$          | $O(h)$            | $O(h)$            |
| Level-order (BFS)    | $O(n)$          | $O(w)$\*          | $O(w)$\*          |

> \* $w$ = maximum width of the tree. For a complete binary tree, $w = O(n)$ at the last level.

**Common tree operations:**

| Operation                       | Balanced BST    | Degenerate BST |
|---------------------------------|:---------------:|:--------------:|
| Height / Depth                  | $O(\log n)$     | $O(n)$         |
| Diameter                        | $O(n)$          | $O(n)$         |
| Lowest Common Ancestor (LCA)    | $O(\log n)$ / $O(n)$ | $O(n)$    |
| Path Sum (root to leaf)         | $O(n)$          | $O(n)$         |
| Count nodes / leaves            | $O(n)$          | $O(n)$         |

---

## 6. String Algorithms

| Algorithm       | Preprocessing  | Search         | Space      | Use Case                               |
|-----------------|:--------------:|:--------------:|:----------:|----------------------------------------|
| Naive Search    | —              | $O(nm)$        | $O(1)$     | Simple brute-force substring search    |
| KMP             | $O(m)$         | $O(n)$         | $O(m)$     | Linear-time pattern matching · no re-scan |
| Z-Algorithm     | $O(n + m)$     | $O(n + m)$     | $O(n + m)$ | Prefix matching · equivalent power to KMP |
| Rabin-Karp      | $O(m)$         | $O(n)$ avg / $O(nm)$ worst | $O(1)$ | Rolling hash · useful for multi-pattern search |
| Boyer-Moore     | $O(m + \sigma)$| $O(n/m)$ best / $O(nm)$ worst | $O(m + \sigma)$ | Fast in practice on natural language text |

> $n$ = text length · $m$ = pattern length · $\sigma$ = alphabet size.
> - **KMP** is the standard for guaranteed $O(n)$ single-pattern search; know the failure function construction.
> - **Rabin-Karp** shines when searching for multiple patterns simultaneously.
> - **Z-Algorithm** is equivalent to KMP in power but often simpler to implement cleanly.

**Common string DP problems:**

| Problem                              | Time Complexity  | Space          |
|--------------------------------------|:----------------:|:--------------:|
| Longest Common Subsequence (LCS)     | $O(nm)$          | $O(nm)$ / $O(\min(n,m))$ with rolling array |
| Edit Distance (Levenshtein)          | $O(nm)$          | $O(nm)$ / $O(\min(n,m))$ |
| Longest Common Substring             | $O(nm)$          | $O(nm)$        |
| Palindrome Partitioning              | $O(n^2)$         | $O(n^2)$       |
| Longest Palindromic Subsequence      | $O(n^2)$         | $O(n^2)$       |

---

## 7. Dynamic Programming Patterns

| Problem / Pattern                   | Time Complexity     | Space Complexity     |
|-------------------------------------|:-------------------:|:--------------------:|
| Fibonacci (memoized)                | $O(n)$              | $O(n)$               |
| Fibonacci (bottom-up optimized)     | $O(n)$              | $O(1)$               |
| 0/1 Knapsack                        | $O(n \cdot W)$      | $O(n \cdot W)$ / $O(W)$ |
| Unbounded Knapsack                  | $O(n \cdot W)$      | $O(W)$               |
| Coin Change (min coins)             | $O(n \cdot amount)$ | $O(amount)$          |
| Coin Change (count ways)            | $O(n \cdot amount)$ | $O(amount)$          |
| Longest Increasing Subsequence (LIS) | $O(n^2)$ / $O(n \log n)$\* | $O(n)$    |
| Longest Common Subsequence (LCS)    | $O(nm)$             | $O(\min(n,m))$       |
| Edit Distance                       | $O(nm)$             | $O(\min(n,m))$       |
| Matrix Chain Multiplication         | $O(n^3)$            | $O(n^2)$             |
| Subset Sum                          | $O(n \cdot S)$      | $O(S)$               |
| Partition Equal Subset Sum          | $O(n \cdot S/2)$    | $O(S/2)$             |
| Rod Cutting                         | $O(n^2)$            | $O(n)$               |
| Word Break                          | $O(n^2)$            | $O(n)$               |
| Unique Paths (grid)                 | $O(mn)$             | $O(n)$               |
| Min Path Sum (grid)                 | $O(mn)$             | $O(n)$               |
| Egg Drop Problem                    | $O(n \cdot k^2)$ / $O(n \cdot k \log k)$ | $O(nk)$ |

> $n$ = number of items · $W$ = knapsack capacity · $S$ = target sum · $m, n$ = grid or string dimensions.
> \* LIS in $O(n \log n)$ uses a patience sort / binary search approach (not standard DP).

---

## 8. Quick Reference — Complexity Classes

| Notation           | Name         | Example                                      |
|--------------------|:------------:|----------------------------------------------|
| $O(1)$             | Constant     | Array index access, hash table lookup        |
| $O(\alpha(n))$     | Inverse Ackermann | Union-Find with optimizations           |
| $O(\log \log n)$   | Log-log      | Interpolation search (uniform distribution)  |
| $O(\log n)$        | Logarithmic  | Binary search, balanced BST operations       |
| $O(\sqrt{n})$      | Square root  | Jump search, trial division primality        |
| $O(n)$             | Linear       | Linear search, BFS/DFS, single-pass DP       |
| $O(n \log n)$      | Linearithmic | Merge sort, heap sort, Dijkstra              |
| $O(n^2)$           | Quadratic    | Bubble sort, naive LCS, simple graph DP      |
| $O(n^3)$           | Cubic        | Floyd-Warshall, matrix chain multiplication  |
| $O(n \cdot W)$     | Pseudo-polynomial | Knapsack DP                             |
| $O(2^n)$           | Exponential  | Naive subset enumeration, bitmask DP         |
| $O(n!)$            | Factorial    | Naive TSP, generating all permutations       |

---

*Last updated: 2026. Based on classical algorithm analysis. All complexities assume comparison-based models unless stated otherwise.*
