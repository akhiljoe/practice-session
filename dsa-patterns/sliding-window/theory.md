# Sliding Window — Theory

> A technique for processing contiguous subarrays or substrings by maintaining a moving window instead of recomputing from scratch each time.

---

## The Core Idea

Imagine you have a row of houses and you need to find the 3 most expensive consecutive houses. The naive way is to price every group of 3 — but you'd be recounting houses you already counted.

The smarter way: price the first 3 houses, then as you move right, just **subtract the house you left behind and add the new one**. You never restart from zero.

That is the sliding window technique. You maintain a window — a contiguous segment of your array — and slide it forward, updating a running state rather than recomputing it. This typically reduces time complexity from $O(n \cdot k)$ to $O(n)$.

---

## Visualising the Window

```
Array:  [ 2,  1,  5,  1,  3,  2 ]
           ↑        ↑
          left     right
          └── window ──┘
```

The `left` pointer is the start of the window, `right` is the end. The window always represents the subarray between them. As you move right, you decide whether to:

- **Expand** — move `right` forward to include more elements
- **Shrink** — move `left` forward to drop elements from the front

---

## Three Problem Types

---

### Type 1 — Fixed-Size Window

**What it is:** The window size `k` is given. You slide a window of exactly that size across the entire array.

**The idea:** Build the initial window over the first `k` elements. Then for each subsequent step, drop the leftmost element and absorb the next rightmost one. At each position, record whatever you need (max sum, min average, etc.).

**Real example:** *"Find the maximum sum of any 3 consecutive elements in the array."*

For `[2, 1, 5, 1, 3, 2]` with `k = 3`:
- Window 1: `[2, 1, 5]` → sum = 8
- Window 2: drop 2, add 1 → `[1, 5, 1]` → sum = 7
- Window 3: drop 1, add 3 → `[5, 1, 3]` → sum = 9 ✅
- Window 4: drop 5, add 2 → `[1, 3, 2]` → sum = 6

Answer: **9**

> The key operation is: `new_sum = old_sum - element_leaving_left + element_entering_right`

---

### Type 2 — Variable-Size Window

**What it is:** No fixed size. You need to find the **longest** (or shortest) subarray/substring that satisfies a condition.

**The idea:** Expand the window by moving `right` forward. Whenever the condition is violated, shrink from the left until the condition holds again. Track the maximum window size seen while the condition was valid.

**Real example:** *"Find the longest subarray where the sum is ≤ 6."*

For `[2, 1, 5, 1, 3, 2]` with `k = 6`:

| Step | Window | Sum | Valid? | Max Length |
|------|--------|-----|--------|------------|
| Add 2 | `[2]` | 2 | ✅ | 1 |
| Add 1 | `[2,1]` | 3 | ✅ | 2 |
| Add 5 | `[2,1,5]` | 8 | ❌ — shrink |  |
| Drop 2 | `[1,5]` | 6 | ✅ | 2 |
| Add 1 | `[1,5,1]` | 7 | ❌ — shrink |  |
| Drop 1 | `[5,1]` | 6 | ✅ | 2 |
| Add 3 | `[5,1,3]` | 9 | ❌ — shrink |  |
| Drop 5 | `[1,3]` | 4 | ✅ | 2 |
| Add 2 | `[1,3,2]` | 6 | ✅ | **3** ✅ |

Answer: **3** (the subarray `[1, 3, 2]`)

> **Why is this still $O(n)$?** Each element is added by `right` exactly once and removed by `left` at most once. So the total number of operations across the entire run is at most $2n$.

---

### Type 3 — Count Subarrays with Exact Condition

**What it is:** You don't want the longest window — you want to **count** how many subarrays satisfy an exact condition (e.g., sum equals exactly `k`).

**The problem with direct approach:** When the condition is "exactly k", the window can neither freely expand nor shrink — elements could be added or removed and still satisfy the condition, making it hard to maintain a clean window boundary.

**The trick — complement counting:**

> Count(exactly k) = Count(at most k) − Count(at most k−1)

You solve two easier "at most" problems and subtract. The "at most" version works cleanly with a sliding window because the window can always shrink when the condition is violated.

**Why this works:**

Think of it this way. Every subarray that sums to *at most k* is either:
- Summing to *exactly k*, or
- Summing to *at most k−1*

So subarrays summing to *exactly k* = the difference between the two groups.

**Real example:** *"Count subarrays with exactly 2 ones in `[1, 0, 1, 0, 1]`."*

- Count(at most 2 ones): 12
- Count(at most 1 one): 9
- Answer: 12 − 9 = **3** ✅

The three subarrays are: `[1,0,1]`, `[0,1,0,1]`, `[1,0,1]` (starting at index 2).

---

## When to Recognise This Pattern

You are likely dealing with a sliding window problem when:

- The problem involves a **subarray** or **substring**
- You need to find something that is **longest**, **shortest**, **maximum**, **minimum**, or a **count**
- The problem has a **constraint** on that subarray (sum ≤ k, at most k distinct chars, etc.)
- The input is an **array or string** (not a tree or graph)

| Problem phrasing | Likely type |
|---|---|
| "fixed window of size k" | Fixed-size window |
| "longest subarray where..." | Variable-size window |
| "count subarrays with exactly..." | Complement counting |
| "minimum window containing..." | Variable-size window (shrink for minimum) |

---

## Common Mistakes

**Forgetting to shrink.** In variable windows, if you only expand, you will overcount invalid windows. Always shrink from the left when the condition breaks.

**Using the wrong condition for shrinking.** Shrink *until* the condition is restored, not just once. A `while` loop, not an `if` statement.

**Counting subarrays directly for exact conditions.** Direct sliding window does not cleanly handle "exactly k" — always reach for the complement trick.

**Applying this to non-contiguous problems.** Sliding window only works when the answer must be a contiguous segment. If the problem involves subsequences (not subarrays), think DP instead.

---

## Summary

| Type | Window Size | Goal | Key Operation |
|---|---|---|---|
| Fixed | Exactly `k` | Compute over each window | Drop left, add right |
| Variable | Grows and shrinks | Find longest/shortest valid window | Expand right, shrink left |
| Count (exact) | Grows and shrinks | Count subarrays | atMost(k) − atMost(k−1) |

---

*Part of `patterns/sliding-window/`*
