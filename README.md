# LeetCode Solutions in Python 3

Algorithm and Data Structures solutions implemented in **Python 3** with type annotations, organized by core problem-solving pattern.

---

## Solutions by Algorithmic Pattern

### 1. Graphs, BFS, Topological Sort & Shortest Path (Dijkstra)
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0200 | Number of Islands | Grid BFS / Connected Components | [Python](./0200-number-of-islands/) |
| 0207 | Course Schedule | Cycle Detection / Kahn's Topological Sort (BFS) | [Python](./0207-course-schedule/) |
| 0210 | Course Schedule II | Topological Sort (Indegree Queue) | [Python](./0210-course-schedule-ii/) |
| 0743 | Network Delay Time | Dijkstra's Shortest Path (`heapq` Priority Queue) | [Python](./0743-network-delay-time/) |
| 0994 | Rotting Oranges | Multi-Source BFS | [Python](./0994-rotting-oranges/) |

### 2. Binary Trees & Binary Search Trees (BST)
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0098 | Validate Binary Search Tree | DFS Range Validation / Inorder Traversal | [Python](./0098-validate-binary-search-tree/) |
| 0102 | Binary Tree Level Order Traversal | Breadth-First Search (`collections.deque`) | [Python](./0102-binary-tree-level-order-traversal/) |
| 0103 | Binary Tree Zigzag Level Order Traversal | Level-Order BFS with Alternating Direction | [Python](./0103-binary-tree-zigzag-level-order-traversal/) |
| 0104 | Maximum Depth of Binary Tree | Recursive DFS | [Python](./0104-maximum-depth-of-binary-tree/) |
| 0144 | Binary Tree Preorder Traversal | DFS Traversal | [Python](./0144-binary-tree-preorder-traversal/) |
| 0199 | Binary Tree Right Side View | Level-Order BFS (Rightmost Node) | [Python](./0199-binary-tree-right-side-view/) |
| 0230 | Kth Smallest Element in a BST | Inorder BST Traversal | [Python](./0230-kth-smallest-element-in-a-bst/) |

### 3. Monotonic Stack
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0496 | Next Greater Element I | Monotonic Decreasing Stack + Hash Map | [Python](./0496-next-greater-element-i/) |
| 0503 | Next Greater Element II | Circular Array + Monotonic Stack | [Python](./0503-next-greater-element-ii/) |
| 0739 | Daily Temperatures | Monotonic Decreasing Stack (Index Tracking) | [Python](./0739-daily-temperatures/) |
| 0901 | Online Stock Span | Stateful Monotonic Stack | [Python](./0901-online-stock-span/) |

### 4. Sliding Window & Two Pointers
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0003 | Longest Substring Without Repeating Characters | Variable-Size Sliding Window + Set/Map | [Python](./0003-longest-substring-without-repeating-characters/) |
| 0015 | 3Sum | Sorting + Two Pointers with Duplicate Skipping | [Python](./0015-3sum/) |
| 0016 | 3Sum Closest | Sorting + Two Pointers | [Python](./0016-3sum-closest/) |
| 0567 | Permutation in String | Fixed-Size Sliding Window + Frequency Counter | [Python](./0567-permutation-in-string/) |

### 5. Heaps, Hashing & Prefix Sums
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0215 | Kth Largest Element in an Array | Min-Heap (`heapq`) | [Python](./0215-kth-largest-element-in-an-array/) |
| 0238 | Product of Array Except Self | Prefix & Suffix Running Products ($O(1)$ Extra Space) | [Python](./0238-product-of-array-except-self/) |
| 0347 | Top K Frequent Elements | Frequency Hash Map + Bucket Sort / Heap | [Python](./0347-top-k-frequent-elements/) |
| 0560 | Subarray Sum Equals K | Prefix Sum + Hash Map Frequency Count | [Python](./0560-subarray-sum-equals-k/) |
| 2150 | Find All Lonely Numbers in the Array | Hash Map Frequency Lookup | [Python](./2150-find-all-lonely-numbers-in-the-array/) |

### 6. Intervals, Matrices, Greedy & Simulation
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0048 | Rotate Image | In-Place Matrix Transpose + Row Reversal | [Python](./0048-rotate-image/) |
| 0056 | Merge Intervals | Sorting by Start Time + Interval Merging | [Python](./0056-merge-intervals/) |
| 0057 | Insert Interval | Linear Interval Merge | [Python](./0057-insert-interval/) |
| 0334 | Increasing Triplet Subsequence | Greedy Two-Threshold Tracking ($O(n)$ Time, $O(1)$ Space) | [Python](./0334-increasing-triplet-subsequence/) |
| 2257 | Count Unguarded Cells in the Grid | Directional Grid Simulation | [Python](./2257-count-unguarded-cells-in-the-grid/) |

### 7. Linked Lists, Strings & Math
| # | Problem | Pattern / Technique | Solution |
| :--- | :--- | :--- | :--- |
| 0007 | Reverse Integer | 32-bit Signed Integer Overflow Check | [Python](./0007-reverse-integer/) |
| 0008 | String to Integer (atoi) | Deterministic String Parsing & Clamping | [Python](./0008-string-to-integer-atoi/) |
| 0012 | Integer to Roman | Greedy Value-Symbol Mapping | [Python](./0012-integer-to-roman/) |
| 0141 | Linked List Cycle | Floyd's Tortoise and Hare (Fast & Slow Pointers) | [Python](./0141-linked-list-cycle/) |
| 0206 | Reverse Linked List | Iterative Pointer Reversal | [Python](./0206-reverse-linked-list/) |

<!---LeetCode Topics Start-->
# LeetCode Topics
## String
| Problem Name | Difficulty |
| ------- | ------- |
| [2914-minimum-number-of-changes-to-make-binary-string-beautiful](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/2914-minimum-number-of-changes-to-make-binary-string-beautiful/) | Medium |
| [3163-string-compression-iii](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/3163-string-compression-iii/) | Medium |
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [0033-search-in-rotated-sorted-array](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/0033-search-in-rotated-sorted-array/) | Medium |
| [0128-longest-consecutive-sequence](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/0128-longest-consecutive-sequence/) | Medium |
| [2352-equal-row-and-column-pairs](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/2352-equal-row-and-column-pairs/) | Medium |
| [3046-split-the-array](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/3046-split-the-array/) | Easy |
## Hash Table
| Problem Name | Difficulty |
| ------- | ------- |
| [0128-longest-consecutive-sequence](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/0128-longest-consecutive-sequence/) | Medium |
| [2352-equal-row-and-column-pairs](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/2352-equal-row-and-column-pairs/) | Medium |
| [3046-split-the-array](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/3046-split-the-array/) | Easy |
## Counting
| Problem Name | Difficulty |
| ------- | ------- |
| [3046-split-the-array](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/3046-split-the-array/) | Easy |
## Matrix
| Problem Name | Difficulty |
| ------- | ------- |
| [2352-equal-row-and-column-pairs](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/2352-equal-row-and-column-pairs/) | Medium |
## Simulation
| Problem Name | Difficulty |
| ------- | ------- |
| [2352-equal-row-and-column-pairs](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/2352-equal-row-and-column-pairs/) | Medium |
| [3360-stone-removal-game](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/3360-stone-removal-game/) | Easy |
## Union-Find
| Problem Name | Difficulty |
| ------- | ------- |
| [0128-longest-consecutive-sequence](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/0128-longest-consecutive-sequence/) | Medium |
## Backtracking
| Problem Name | Difficulty |
| ------- | ------- |
| [0077-combinations](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/0077-combinations/) | Medium |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [3360-stone-removal-game](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/3360-stone-removal-game/) | Easy |
## Binary Search
| Problem Name | Difficulty |
| ------- | ------- |
| [0033-search-in-rotated-sorted-array](https://github.com/silva-leonardo1/leetcode-solutions/tree/main/0033-search-in-rotated-sorted-array/) | Medium |
<!---LeetCode Topics End-->