# 🧠 practice-session

> A structured, self-paced DSA practice repository for software engineering interviews — built to go from problem-aware to problem-confident.

---

## 📌 About This Repository

This repo is my personal interview preparation workspace. It contains solutions, notes, patterns, and complexity analysis for DSA problems.

The focus is on **understanding patterns**, not memorizing solutions — so every problem includes a breakdown of the thought process, not just the answer.

---

## 🗂️ Repository Structure

```
practice-session/
│
├── data-structures/
│   ├── arrays/
│   ├── linked-lists/
│   ├── stacks-and-queues/
│   ├── hash-tables/
│   ├── trees/
│   │   ├── binary-search-tree/
│   │   ├── avl-tree/
│   │   └── heap/
│   │   └── trie/
│   │   └── red-black-tree/
│   └── graphs/
│   │   └── adjacency-list/
│   │   └── adjacency-matrix/
│   └── disjoint-set/
│
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── dynamic-programming/
│   ├── greedy/
│   ├── backtracking/
│   ├── divide-and-conquer/
│   └── graph-algorithms/
│   └── string-algorithms/
│   └── mathematical/
│
├── patterns/
│   ├── array-string-patterns/
│   │   ├── count-array-frequencies/
│   │   ├── subset-permutation-generation/
│   │   └── matching-parsing-stack/
│   │
│   ├── backtracking/
│   │   ├── permutations-combinations/
│   │   ├── subset-generation/
│   │   └── constraint-satisfaction/
│   │
│   ├── bfs-dfs-templates/
│   │   ├── bfs-level-order/
│   │   ├── dfs-recursive/
│   │   └── dfs-iterative/
│   │
│   ├── binary-search-variants/
│   │   ├── search-on-answer/
│   │   ├── rotated-sorted-array/
│   │   └── binary-search-on-result/
│   │
│   ├── bit-manipulation/
│   │   ├── xor-tricks/
│   │   ├── bitmask-subsets/
│   │   └── bit-checks/
│   │
│   ├── dynamic-programming-patterns/
│   │   ├── 1d-dp/
│   │   ├── 2d-dp-matrix/
│   │   ├── knapsack-variants/
│   │   ├── edit-distance-lcs/
│   │   ├── memoization/
│   │   └── tabulation/
│   │
│   ├── fast-slow-pointers/
│   │   ├── cycle-detection/
│   │   └── middle-of-linked-list/
│   │
│   ├── graph-algorithms/
│   │   ├── shortest-path/
│   │   │   ├── dijkstra/
│   │   │   ├── bellman-ford/
│   │   │   └── a-star/
│   │   ├── topological-sort/
│   │   │   ├── kahns-algorithm/
│   │   │   └── dfs-topo/
│   │   ├── cycle-detection/
│   │   ├── connected-components/
│   │   ├── minimum-spanning-tree/
│   │   │   ├── kruskal/
│   │   │   └── prim/
│   │   ├── union-find-dsu/
│   │   ├── grid-graph-problems/
│   │   ├── strongly-connected-components/
│   │   │   ├── tarjan/
│   │   │   └── kosaraju/
│   │   ├── graph-coloring-bipartite/
│   │   └── eulerian-hamiltonian-paths/
│   │
│   ├── greedy-algorithms/
│   │   ├── interval-scheduling/
│   │   └── local-global-optimum/
│   │
│   ├── hashing-maps/
│   │   ├── frequency-count/
│   │   ├── two-sum-variants/
│   │   └── duplicate-detection/
│   │
│   ├── heap-priority-queue/
│   │   ├── top-k-elements/
│   │   ├── kth-largest-smallest/
│   │   ├── merge-k-sorted/
│   │   └── quick-select/
│   │
│   ├── linked-list-patterns/
│   │   ├── reversal/
│   │   ├── middle-intersection/
│   │   └── in-place-manipulation/
│   │
│   ├── merge-intervals/
│   │   ├── overlapping-intervals/
│   │   └── insert-interval/
│   │
│   ├── monotonic-stack/
│   │   ├── next-greater-element/
│   │   ├── next-smaller-element/
│   │   └── largest-rectangle/
│   │
│   ├── prefix-suffix-sum/
│   │   ├── range-queries-static/
│   │   ├── subarray-sum-equals-k/
│   │   └── 2d-prefix-sum/
│   │
│   ├── range-queries-advanced/
│   │   ├── segment-tree/
│   │   └── fenwick-tree-bit/
│   │
│   ├── recursion-patterns/
│   │   ├── divide-and-conquer/
│   │   ├── recursion-to-iterative/
│   │   └── tree-nested-problems/
│   │
│   ├── sliding-window/
│   │   ├── fixed-size-window/
│   │   └── variable-size-window/
│   │
│   ├── string-patterns/
│   │   ├── kmp-algorithm/
│   │   ├── z-algorithm/
│   │   ├── rabin-karp/
│   │   ├── longest-common-subsequence/
│   │   ├── edit-distance/
│   │   ├── palindrome-problems/
│   │   └── regex-matching/
│   │
│   ├── tree-patterns/
│   │   ├── traversals/
│   │   │   ├── inorder-preorder-postorder/
│   │   │   └── level-order-bfs/
│   │   ├── lowest-common-ancestor/
│   │   ├── diameter-balance-checks/
│   │   ├── binary-lifting/
│   │   ├── tree-dp/
│   │   ├── sum-of-distances-rerooting/
│   │   ├── subtree-queries-hld/
│   │   └── path-queries-prefix-sums/
│   │
│   ├── trie/
│   │   ├── prefix-search/
│   │   ├── word-dictionary/
│   │   └── autocomplete/
│   │
│   └── two-pointers/
│       ├── opposite-ends/
│       ├── same-direction/
│       └── three-sum-variants/
│
├── problem-sets/
│   ├── easy/
│   ├── medium/
│   └── hard/
│
├── complexity-cheatsheet.md
└── README.md
```

---

## 📚 Topics Covered

### 🔷 Data Structures

| Data Structure            | Implementation | Notes |
|---------------------------|:--------------:|:-----:|
| Array                     | ✅             | ✅    |
| Singly Linked List        | ✅             | ✅    |
| Doubly Linked List        | ✅             | ✅    |
| Stack                     | ✅             | ✅    |
| Queue / Deque             | ✅             | ✅    |
| Hash Map / Hash Set       | ✅             | ✅    |
| Binary Search Tree        | ✅             | ✅    |
| AVL Tree                  | ⬜             | ⬜    |
| Heap (Min/Max)            | ✅             | ✅    |
| Trie                      | ⬜             | ⬜    |
| Graph (Adjacency List)    | ✅             | ✅    |
| Graph (Adjacency Matrix)  | ⬜             | ⬜    |
| Disjoint Set (Union-Find) | ⬜             | ⬜    |

> Legend: ✅ Done &nbsp;|&nbsp; 🔄 In Progress &nbsp;|&nbsp; ⬜ Pending

---

### 🔷 Problem-Solving Patterns

All patterns tracked in this repo, mapped to the `patterns/` directory:

| #  | Pattern                    | Key Techniques / Example Problems                                          |
|----|----------------------------|----------------------------------------------------------------------------|
| 1  | Sliding Window             | Fixed & variable window · Max sum subarray · Longest substring without repeat |
| 2  | Two Pointers               | Opposite ends · Same direction · Pair sum · Container with most water     |
| 3  | Fast & Slow Pointers       | Cycle detection · Middle of linked list                                    |
| 4  | Merge Intervals            | Overlapping intervals · Insert interval · Meeting rooms                   |
| 5  | Linked List Patterns       | In-place reversal · Reverse sublist · K-group reversal · Intersection     |
| 6  | Tree BFS                   | Level-order traversal · Zigzag traversal                                   |
| 7  | Tree DFS                   | Path sum · Diameter · LCA · Balance checks · Tree DP                      |
| 8  | Backtracking               | Permutations · Combinations · Subsets · Constraint satisfaction           |
| 9  | Binary Search Variants     | Search rotated array · Search on answer · Find peak element               |
| 10 | Graph Algorithms           | BFS/DFS templates · Shortest path · Topological sort · SCC · MST · DSU   |
| 11 | Heap / Priority Queue      | Top-K elements · Kth largest/smallest · Merge K sorted · Quick-select     |
| 12 | Dynamic Programming        | 1D/2D DP · Knapsack variants · Edit distance · LCS · Memoization          |
| 13 | Monotonic Stack            | Next greater element · Next smaller element · Largest rectangle           |
| 14 | Prefix / Suffix Sum        | Range queries (static) · Subarray sum equals K · 2D prefix sum            |
| 15 | Hashing & Maps             | Frequency count · Two-sum variants · Duplicate detection                  |
| 16 | Trie                       | Prefix search · Word dictionary · Autocomplete                            |
| 17 | Greedy Algorithms          | Interval scheduling · Local-to-global optimum                             |
| 18 | Bit Manipulation           | XOR tricks · Bitmask subsets · Bit checks                                 |
| 19 | Array & String Patterns    | Frequency count · Subset/permutation generation · Matching/parsing        |
| 20 | Recursion Patterns         | Divide and conquer · Recursion-to-iterative · Tree/nested problems        |
| 21 | Range Queries (Advanced)   | Segment tree · Fenwick tree (BIT)                                         |
| 22 | String Patterns            | KMP · Z-algorithm · Rabin-Karp · Palindromes · Edit distance · Regex      |

---

## ⏱️ Time & Space Complexity Reference

A full cheatsheet covering all major data structures and sorting/graph algorithms is available here:

📄 [`complexity-cheatsheet.md`](./complexity-cheatsheet.md)

Quick reference:

| Structure / Algorithm | Avg Access  | Avg Search  | Avg Insert  | Avg Delete  |
|-----------------------|:-----------:|:-----------:|:-----------:|:-----------:|
| Array                 | O(1)        | O(n)        | O(n)        | O(n)        |
| Hash Table            | O(1)        | O(1)        | O(1)        | O(1)        |
| BST (balanced)        | O(log n)    | O(log n)    | O(log n)    | O(log n)    |
| Heap                  | O(1) peek   | O(n)        | O(log n)    | O(log n)    |
| Graph (BFS/DFS)       | —           | O(V+E)      | O(1)        | O(V+E)      |

---

## 🗺️ Pattern → Algorithm Mapping (by Input Type)

### Array / String Inputs

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Sorted input                          | Binary Search, Two Pointers, Prefix Sums    |
| Optimization problem                  | Sliding Window, DP, Greedy                  |
| Duplicates / frequencies              | HashMap, HashSet, Count Array               |
| Substrings / subarrays                | Sliding Window + Two Pointers               |
| Frequent min/max                      | Monotonic Queue / Deque / Heap              |
| Generating subsets / permutations     | Backtracking                                |
| Matching / parsing                    | Stack                                       |

### Graph Inputs

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Unweighted shortest path              | BFS                                         |
| Weighted shortest path                | Dijkstra, Bellman-Ford, A*                  |
| Connected components / cycles         | DFS, Union-Find                             |
| Topological order                     | Kahn's Algorithm, DFS + visited             |
| Minimum spanning tree                 | Kruskal, Prim                               |
| Grid / matrix traversal               | BFS / DFS on grid                           |
| Strongly connected components         | Tarjan, Kosaraju                            |

### Tree Inputs

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Tree traversal                        | Inorder, Preorder, Postorder, Level-order   |
| Diameter / balance checks             | Postorder + height                          |
| Lowest Common Ancestor                | DFS or Parent Map, Binary Lifting           |
| Subtree queries                       | Segment Trees, HLD                          |
| Distance between nodes                | LCA / BFS / DFS                             |
| Tree DP                               | Post-order + memoization                    |

### Linked List Inputs

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Cycle detection                       | Slow / Fast Pointers                        |
| Reversals                             | prev, curr, next pointers                   |
| Middle / intersection                 | Two Pointers                                |

### Dynamic Programming

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Optimal choice / overlapping subproblems | Memoization / Tabulation               |
| Knapsack / subset selection           | 1D / 2D DP                                  |
| Edit distance / LCS                   | DP Matrix                                   |

### Range Queries

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Static range queries (no updates)     | Prefix Sums                                 |
| Dynamic range queries (with updates)  | Segment Tree, Fenwick Tree                  |

### String-Specific Problems

| Scenario                              | Pattern / Algorithm                         |
|---------------------------------------|---------------------------------------------|
| Fast substring search                 | KMP, Z-Algorithm, Rabin-Karp                |
| Common subsequence / alignment        | LCS, Edit Distance                          |
| Pattern with wildcards / rules        | Regex Matching, Backtracking                |
| Palindromic substrings                | Expand Around Center, DP                    |

---

## 🧠 Pattern Selection Heuristics

| Clue in Problem                                | Think                                   |
|------------------------------------------------|-----------------------------------------|
| Sorted array / string                          | Binary Search or Two Pointers           |
| Subarray / substring                           | Sliding Window                          |
| Nested relationships, undo/redo                | Stack or Queue                          |
| Optimal substructure + overlapping subproblems | Dynamic Programming                     |
| Local optimum = global optimum                 | Greedy                                  |
| Ordering with dependencies                     | Topological Sort (DAG)                  |
| Merging groups / connectivity                  | Union-Find (DSU)                        |
| Efficient min/max, Top-K                       | Heap / Priority Queue                   |
| Prefix string problems                         | Trie                                    |
| Bit operations, subsets via bits               | Bit Manipulation / Bitmasks             |
| Risk of stack overflow in recursion            | Convert to Iterative with Stack         |
| Small input (n ≤ 15)                           | Backtracking / Bitmask DP               |
| O(n²) → O(n) optimization needed               | Hashing / HashMap                       |
| Relationships / networks / reachability        | Graphs (BFS/DFS)                        |
| Next greater / smaller element                 | Monotonic Stack                         |

---

## 🔧 Languages Used

Solutions are primarily written in **Python 3**, chosen for:

- Concise syntax that keeps focus on the algorithm, not boilerplate
- Rich standard library (`heapq`, `collections`, `bisect`, `itertools`)
- Widest support on competitive/interview platforms (LeetCode, HackerRank)

Where relevant, pseudocode or alternative implementations in other languages may be included.

---

## 📎 Resources

| Resource                             | Type         | Notes                      |
|--------------------------------------|--------------|----------------------------|
| [LeetCode](https://leetcode.com)     | Problem Bank | Primary practice platform  |

---

## 📈 Progress Tracker

| Difficulty  | Solved  | Target  |
|-------------|:-------:|:-------:|
| Easy        | 15      | 50      |
| Medium      | 10      | 80      |
| Hard        | 0       | 20      |
| **Total**   | **0**   | **150** |

---

## 📝 License

This repository is for personal learning and interview preparation. All problem statements referenced belong to their respective platforms (LeetCode, HackerRank, etc.). Solutions and notes are original work.

---

<p align="center">
  <i>Consistency beats intensity. Solve one problem well every day.</i>
</p>
